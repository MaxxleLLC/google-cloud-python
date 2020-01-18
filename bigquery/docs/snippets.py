# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Testable usage examples for Google BigQuery API wrapper
Each example function takes a ``client`` argument (which must be an instance
of :class:`google.cloud.bigquery.client.Client`) and uses it to perform a task
with the API.
To facilitate running the examples as system tests, each example is also passed
a ``to_delete`` list;  the function adds to the list any objects created which
need to be deleted during teardown.
"""

import os
import time

import pytest
import six

try:
    import fastparquet
except (ImportError, AttributeError):
    fastparquet = None
try:
    import pandas
except (ImportError, AttributeError):
    pandas = None
try:
    import pyarrow
except (ImportError, AttributeError):
    pyarrow = None

from google.api_core.exceptions import InternalServerError
from google.api_core.exceptions import ServiceUnavailable
from google.api_core.exceptions import TooManyRequests
from google.cloud import bigquery
from google.cloud import storage
from test_utils.retry import RetryErrors

ORIGINAL_FRIENDLY_NAME = "Original friendly name"
ORIGINAL_DESCRIPTION = "Original description"
LOCALLY_CHANGED_FRIENDLY_NAME = "Locally-changed friendly name"
LOCALLY_CHANGED_DESCRIPTION = "Locally-changed description"
UPDATED_FRIENDLY_NAME = "Updated friendly name"
UPDATED_DESCRIPTION = "Updated description"

SCHEMA = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]

ROWS = [
    ("Phred Phlyntstone", 32),
    ("Bharney Rhubble", 33),
    ("Wylma Phlyntstone", 29),
    ("Bhettye Rhubble", 27),
]

QUERY = (
    "SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` "
    'WHERE state = "TX"'
)


retry_429 = RetryErrors(TooManyRequests)
retry_storage_errors = RetryErrors(
    (TooManyRequests, InternalServerError, ServiceUnavailable)
)


@pytest.fixture(scope="module")
def client():
    return bigquery.Client()


@pytest.fixture
def to_delete(client):
    doomed = []
    yield doomed
    for item in doomed:
        if isinstance(item, (bigquery.Dataset, bigquery.DatasetReference)):
            retry_429(client.delete_dataset)(item, delete_contents=True)
        elif isinstance(item, storage.Bucket):
            retry_storage_errors(item.delete)()
        else:
            retry_429(item.delete)()


def _millis():
    return int(time.time() * 1000)


class _CloseOnDelete(object):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def delete(self):
        self._wrapped.close()


def test_create_client_default_credentials():
    """Create a BigQuery client with Application Default Credentials"""

    # [START bigquery_client_default_credentials]
    from google.cloud import bigquery

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    client = bigquery.Client()
    # [END bigquery_client_default_credentials]

    assert client is not None


def test_create_table_nested_repeated_schema(client, to_delete):
    dataset_id = "create_table_nested_repeated_{}".format(_millis())
    dataset_ref = client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)
    client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_nested_repeated_schema]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_ref = client.dataset('my_dataset')

    schema = [
        bigquery.SchemaField("id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("first_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("dob", "DATE", mode="NULLABLE"),
        bigquery.SchemaField(
            "addresses",
            "RECORD",
            mode="REPEATED",
            fields=[
                bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("address", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("city", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("state", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("zip", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("numberOfYears", "STRING", mode="NULLABLE"),
            ],
        ),
    ]
    table_ref = dataset_ref.table("my_table")
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)  # API request

    print("Created table {}".format(table.full_table_id))
    # [END bigquery_nested_repeated_schema]


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_manage_table_labels(client, to_delete):
    dataset_id = "label_table_dataset_{}".format(_millis())
    table_id = "label_table_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    table = bigquery.Table(dataset.table(table_id), schema=SCHEMA)
    table = client.create_table(table)

    # [START bigquery_label_table]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # table_ref = client.dataset('my_dataset').table('my_table')
    # table = client.get_table(table_ref)  # API request

    assert table.labels == {}
    labels = {"color": "green"}
    table.labels = labels

    table = client.update_table(table, ["labels"])  # API request

    assert table.labels == labels
    # [END bigquery_label_table]

    # [START bigquery_get_table_labels]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'
    # table_id = 'my_table'

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)  # API Request

    # View table labels
    print("Table ID: {}".format(table_id))
    print("Labels:")
    if table.labels:
        for label, value in table.labels.items():
            print("\t{}: {}".format(label, value))
    else:
        print("\tTable has no labels defined.")
    # [END bigquery_get_table_labels]
    assert table.labels == labels

    # [START bigquery_delete_label_table]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # table_ref = client.dataset('my_dataset').table('my_table')
    # table = client.get_table(table_ref)  # API request

    # This example table starts with one label
    assert table.labels == {"color": "green"}
    # To delete a label from a table, set its value to None
    table.labels["color"] = None

    table = client.update_table(table, ["labels"])  # API request

    assert table.labels == {}
    # [END bigquery_delete_label_table]


if __name__ == "__main__":
    pytest.main()
