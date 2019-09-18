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

from google.api_core import datetime_helpers
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


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_update_table_description(client, to_delete):
    """Update a table's description."""
    dataset_id = "update_table_description_dataset_{}".format(_millis())
    table_id = "update_table_description_table_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    table = bigquery.Table(dataset.table(table_id), schema=SCHEMA)
    table.description = "Original description."
    table = client.create_table(table)

    # [START bigquery_update_table_description]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # table_ref = client.dataset('my_dataset').table('my_table')
    # table = client.get_table(table_ref)  # API request

    assert table.description == "Original description."
    table.description = "Updated description."

    table = client.update_table(table, ["description"])  # API request

    assert table.description == "Updated description."
    # [END bigquery_update_table_description]


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_update_table_expiration(client, to_delete):
    """Update a table's expiration time."""
    dataset_id = "update_table_expiration_dataset_{}".format(_millis())
    table_id = "update_table_expiration_table_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    table = bigquery.Table(dataset.table(table_id), schema=SCHEMA)
    table = client.create_table(table)

    # [START bigquery_update_table_expiration]
    import datetime
    import pytz

    # from google.cloud import bigquery
    # client = bigquery.Client()
    # table_ref = client.dataset('my_dataset').table('my_table')
    # table = client.get_table(table_ref)  # API request

    assert table.expires is None

    # set table to expire 5 days from now
    expiration = datetime.datetime.now(pytz.utc) + datetime.timedelta(days=5)
    table.expires = expiration
    table = client.update_table(table, ["expires"])  # API request

    # expiration is stored in milliseconds
    margin = datetime.timedelta(microseconds=1000)
    assert expiration - margin <= table.expires <= expiration + margin
    # [END bigquery_update_table_expiration]


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_relax_column(client, to_delete):
    """Updates a schema field from required to nullable."""
    dataset_id = "relax_column_dataset_{}".format(_millis())
    table_id = "relax_column_table_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    dataset = client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_relax_column]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'
    # table_id = 'my_table'

    original_schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=original_schema)
    table = client.create_table(table)
    assert all(field.mode == "REQUIRED" for field in table.schema)

    # SchemaField properties cannot be edited after initialization.
    # To make changes, construct new SchemaField objects.
    relaxed_schema = [
        bigquery.SchemaField("full_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    table.schema = relaxed_schema
    table = client.update_table(table, ["schema"])

    assert all(field.mode == "NULLABLE" for field in table.schema)
    # [END bigquery_relax_column]


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_update_table_cmek(client, to_delete):
    """Patch a table's metadata."""
    dataset_id = "update_table_cmek_{}".format(_millis())
    table_id = "update_table_cmek_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    table = bigquery.Table(dataset.table(table_id))
    original_kms_key_name = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
        "cloud-samples-tests", "us-central1", "test", "test"
    )
    table.encryption_configuration = bigquery.EncryptionConfiguration(
        kms_key_name=original_kms_key_name
    )
    table = client.create_table(table)

    # [START bigquery_update_table_cmek]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    assert table.encryption_configuration.kms_key_name == original_kms_key_name

    # Set a new encryption key to use for the destination.
    # TODO: Replace this key with a key you have created in KMS.
    updated_kms_key_name = (
        "projects/cloud-samples-tests/locations/us-central1/"
        "keyRings/test/cryptoKeys/otherkey"
    )
    table.encryption_configuration = bigquery.EncryptionConfiguration(
        kms_key_name=updated_kms_key_name
    )

    table = client.update_table(table, ["encryption_configuration"])  # API request

    assert table.encryption_configuration.kms_key_name == updated_kms_key_name
    assert original_kms_key_name != updated_kms_key_name
    # [END bigquery_update_table_cmek]


def test_query_no_cache(client):
    # [START bigquery_query_no_cache]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = False
    sql = """
        SELECT corpus
        FROM `bigquery-public-data.samples.shakespeare`
        GROUP BY corpus;
    """
    query_job = client.query(
        sql,
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
        job_config=job_config,
    )  # API request

    # Print the results.
    for row in query_job:  # API request - fetches results
        print(row)
    # [END bigquery_query_no_cache]


def test_query_external_gcs_temporary_table(client):
    # [START bigquery_query_external_gcs_temp]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    # Configure the external data source and query job
    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [
        "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    ]
    external_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    external_config.options.skip_leading_rows = 1  # optionally skip header row
    table_id = "us_states"
    job_config = bigquery.QueryJobConfig()
    job_config.table_definitions = {table_id: external_config}

    # Example query to find states starting with 'W'
    sql = 'SELECT * FROM `{}` WHERE name LIKE "W%"'.format(table_id)

    query_job = client.query(sql, job_config=job_config)  # API request

    w_states = list(query_job)  # Waits for query to finish
    print("There are {} states with names starting with W.".format(len(w_states)))
    # [END bigquery_query_external_gcs_temp]
    assert len(w_states) == 4


def test_query_external_gcs_permanent_table(client, to_delete):
    dataset_id = "query_external_gcs_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_query_external_gcs_perm]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'

    # Configure the external data source
    dataset_ref = client.dataset(dataset_id)
    table_id = "us_states"
    schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    table = bigquery.Table(dataset_ref.table(table_id), schema=schema)
    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [
        "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    ]
    external_config.options.skip_leading_rows = 1  # optionally skip header row
    table.external_data_configuration = external_config

    # Create a permanent table linked to the GCS file
    table = client.create_table(table)  # API request

    # Example query to find states starting with 'W'
    sql = 'SELECT * FROM `{}.{}` WHERE name LIKE "W%"'.format(dataset_id, table_id)

    query_job = client.query(sql)  # API request

    w_states = list(query_job)  # Waits for query to finish
    print("There are {} states with names starting with W.".format(len(w_states)))
    # [END bigquery_query_external_gcs_perm]
    assert len(w_states) == 4


def test_query_external_sheets_temporary_table(client):
    # [START bigquery_query_external_sheets_temp]
    # [START bigquery_auth_drive_scope]
    import google.auth

    # from google.cloud import bigquery

    # Create credentials with Drive & BigQuery API scopes
    # Both APIs must be enabled for your project before running this code
    credentials, project = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/bigquery",
        ]
    )
    client = bigquery.Client(credentials=credentials, project=project)
    # [END bigquery_auth_drive_scope]

    # Configure the external data source and query job
    external_config = bigquery.ExternalConfig("GOOGLE_SHEETS")
    # Use a shareable link or grant viewing access to the email address you
    # used to authenticate with BigQuery (this example Sheet is public)
    sheet_url = (
        "https://docs.google.com/spreadsheets"
        "/d/1i_QCL-7HcSyUZmIbP9E6lO_T5u3HnpLe7dnpHaijg_E/edit?usp=sharing"
    )
    external_config.source_uris = [sheet_url]
    external_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    external_config.options.skip_leading_rows = 1  # optionally skip header row
    table_id = "us_states"
    job_config = bigquery.QueryJobConfig()
    job_config.table_definitions = {table_id: external_config}

    # Example query to find states starting with 'W'
    sql = 'SELECT * FROM `{}` WHERE name LIKE "W%"'.format(table_id)

    query_job = client.query(sql, job_config=job_config)  # API request

    w_states = list(query_job)  # Waits for query to finish
    print("There are {} states with names starting with W.".format(len(w_states)))
    # [END bigquery_query_external_sheets_temp]
    assert len(w_states) == 4


def test_query_external_sheets_permanent_table(client, to_delete):
    dataset_id = "query_external_sheets_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_query_external_sheets_perm]
    import google.auth

    # from google.cloud import bigquery
    # dataset_id = 'my_dataset'

    # Create credentials with Drive & BigQuery API scopes
    # Both APIs must be enabled for your project before running this code
    credentials, project = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/bigquery",
        ]
    )
    client = bigquery.Client(credentials=credentials, project=project)

    # Configure the external data source
    dataset_ref = client.dataset(dataset_id)
    table_id = "us_states"
    schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    table = bigquery.Table(dataset_ref.table(table_id), schema=schema)
    external_config = bigquery.ExternalConfig("GOOGLE_SHEETS")
    # Use a shareable link or grant viewing access to the email address you
    # used to authenticate with BigQuery (this example Sheet is public)
    sheet_url = (
        "https://docs.google.com/spreadsheets"
        "/d/1i_QCL-7HcSyUZmIbP9E6lO_T5u3HnpLe7dnpHaijg_E/edit?usp=sharing"
    )
    external_config.source_uris = [sheet_url]
    external_config.options.skip_leading_rows = 1  # optionally skip header row
    table.external_data_configuration = external_config

    # Create a permanent table linked to the Sheets file
    table = client.create_table(table)  # API request

    # Example query to find states starting with 'W'
    sql = 'SELECT * FROM `{}.{}` WHERE name LIKE "W%"'.format(dataset_id, table_id)

    query_job = client.query(sql)  # API request

    w_states = list(query_job)  # Waits for query to finish
    print("There are {} states with names starting with W.".format(len(w_states)))
    # [END bigquery_query_external_sheets_perm]
    assert len(w_states) == 4


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_query_results_as_dataframe(client):
    # [START bigquery_query_results_dataframe]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    sql = """
        SELECT name, SUM(number) as count
        FROM `bigquery-public-data.usa_names.usa_1910_current`
        GROUP BY name
        ORDER BY count DESC
        LIMIT 10
    """

    df = client.query(sql).to_dataframe()
    # [END bigquery_query_results_dataframe]
    assert isinstance(df, pandas.DataFrame)
    assert len(list(df)) == 2  # verify the number of columns
    assert len(df) == 10  # verify the number of rows


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_list_rows_as_dataframe(client):
    # [START bigquery_list_rows_dataframe]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    dataset_ref = client.dataset("samples", project="bigquery-public-data")
    table_ref = dataset_ref.table("shakespeare")
    table = client.get_table(table_ref)

    df = client.list_rows(table).to_dataframe()
    # [END bigquery_list_rows_dataframe]
    assert isinstance(df, pandas.DataFrame)
    assert len(list(df)) == len(table.schema)  # verify the number of columns
    assert len(df) == table.num_rows  # verify the number of rows


if __name__ == "__main__":
    pytest.main()
