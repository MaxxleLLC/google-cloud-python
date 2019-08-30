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


@pytest.mark.skip(
    reason=(
        "update_table() is flaky "
        "https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5589"
    )
)
def test_manage_views(client, to_delete):
    project = client.project
    source_dataset_id = "source_dataset_{}".format(_millis())
    source_dataset_ref = client.dataset(source_dataset_id)
    source_dataset = bigquery.Dataset(source_dataset_ref)
    source_dataset = client.create_dataset(source_dataset)
    to_delete.append(source_dataset)

    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    job_config.skip_leading_rows = 1
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    source_table_id = "us_states"
    load_job = client.load_table_from_uri(
        uri, source_dataset.table(source_table_id), job_config=job_config
    )
    load_job.result()

    shared_dataset_id = "shared_dataset_{}".format(_millis())
    shared_dataset_ref = client.dataset(shared_dataset_id)
    shared_dataset = bigquery.Dataset(shared_dataset_ref)
    shared_dataset = client.create_dataset(shared_dataset)
    to_delete.append(shared_dataset)

    # [START bigquery_create_view]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # project = 'my-project'
    # source_dataset_id = 'my_source_dataset'
    # source_table_id = 'us_states'
    # shared_dataset_ref = client.dataset('my_shared_dataset')

    # This example shows how to create a shared view of a source table of
    # US States. The source table contains all 50 states, while the view will
    # contain only states with names starting with 'W'.
    view_ref = shared_dataset_ref.table("my_shared_view")
    view = bigquery.Table(view_ref)
    sql_template = 'SELECT name, post_abbr FROM `{}.{}.{}` WHERE name LIKE "W%"'
    view.view_query = sql_template.format(project, source_dataset_id, source_table_id)
    view = client.create_table(view)  # API request

    print("Successfully created view at {}".format(view.full_table_id))
    # [END bigquery_create_view]

    # [START bigquery_update_view_query]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # project = 'my-project'
    # source_dataset_id = 'my_source_dataset'
    # source_table_id = 'us_states'
    # shared_dataset_ref = client.dataset('my_shared_dataset')

    # This example shows how to update a shared view of a source table of
    # US States. The view's query will be updated to contain only states with
    # names starting with 'M'.
    view_ref = shared_dataset_ref.table("my_shared_view")
    view = bigquery.Table(view_ref)
    sql_template = 'SELECT name, post_abbr FROM `{}.{}.{}` WHERE name LIKE "M%"'
    view.view_query = sql_template.format(project, source_dataset_id, source_table_id)
    view = client.update_table(view, ["view_query"])  # API request
    # [END bigquery_update_view_query]

    # [START bigquery_get_view]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # shared_dataset_id = 'my_shared_dataset'

    view_ref = client.dataset(shared_dataset_id).table("my_shared_view")
    view = client.get_table(view_ref)  # API Request

    # Display view properties
    print("View at {}".format(view.full_table_id))
    print("View Query:\n{}".format(view.view_query))
    # [END bigquery_get_view]
    assert view.view_query is not None

    analyst_group_email = "example-analyst-group@google.com"
    # [START bigquery_grant_view_access]
    # from google.cloud import bigquery
    # client = bigquery.Client()

    # Assign access controls to the dataset containing the view
    # shared_dataset_id = 'my_shared_dataset'
    # analyst_group_email = 'data_analysts@example.com'
    shared_dataset = client.get_dataset(
        client.dataset(shared_dataset_id)
    )  # API request
    access_entries = shared_dataset.access_entries
    access_entries.append(
        bigquery.AccessEntry("READER", "groupByEmail", analyst_group_email)
    )
    shared_dataset.access_entries = access_entries
    shared_dataset = client.update_dataset(
        shared_dataset, ["access_entries"]
    )  # API request

    # Authorize the view to access the source dataset
    # project = 'my-project'
    # source_dataset_id = 'my_source_dataset'
    source_dataset = client.get_dataset(
        client.dataset(source_dataset_id)
    )  # API request
    view_reference = {
        "projectId": project,
        "datasetId": shared_dataset_id,
        "tableId": "my_shared_view",
    }
    access_entries = source_dataset.access_entries
    access_entries.append(bigquery.AccessEntry(None, "view", view_reference))
    source_dataset.access_entries = access_entries
    source_dataset = client.update_dataset(
        source_dataset, ["access_entries"]
    )  # API request
    # [END bigquery_grant_view_access]


def test_load_table_from_uri_parquet(client, to_delete, capsys):
    dataset_id = "load_table_from_uri_parquet_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_load_table_gcs_parquet]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'

    dataset_ref = client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.PARQUET
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.parquet"

    load_job = client.load_table_from_uri(
        uri, dataset_ref.table("us_states"), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(dataset_ref.table("us_states"))
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END bigquery_load_table_gcs_parquet]

    out, _ = capsys.readouterr()
    assert "Loaded 50 rows." in out


def test_load_table_from_uri_orc(client, to_delete, capsys):
    dataset_id = "load_table_from_uri_orc_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    # [START bigquery_load_table_gcs_orc]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'

    dataset_ref = client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.ORC
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.orc"

    load_job = client.load_table_from_uri(
        uri, dataset_ref.table("us_states"), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(dataset_ref.table("us_states"))
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END bigquery_load_table_gcs_orc]

    out, _ = capsys.readouterr()
    assert "Loaded 50 rows." in out


def test_load_table_from_uri_truncate(client, to_delete, capsys):
    """Replaces table data with data from a GCS URI using various formats
    Each file format has its own tested load from URI sample. Because most of
    the code is common for autodetect, append, and truncate, this sample
    includes snippets for all supported formats but only calls a single load
    job.
    This code snippet is made up of shared code, then format-specific code,
    followed by more shared code. Note that only the last format in the
    format-specific code section will be tested in this test.
    """
    dataset_id = "load_table_from_uri_trunc_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    client.create_dataset(dataset)
    to_delete.append(dataset)

    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    table_ref = dataset.table("us_states")
    body = six.BytesIO(b"Washington,WA")
    client.load_table_from_file(body, table_ref, job_config=job_config).result()
    previous_rows = client.get_table(table_ref).num_rows
    assert previous_rows > 0

    # Shared code
    # [START bigquery_load_table_gcs_avro_truncate]
    # [START bigquery_load_table_gcs_csv_truncate]
    # [START bigquery_load_table_gcs_json_truncate]
    # [START bigquery_load_table_gcs_parquet_truncate]
    # [START bigquery_load_table_gcs_orc_truncate]
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # table_ref = client.dataset('my_dataset').table('existing_table')

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    # [END bigquery_load_table_gcs_avro_truncate]
    # [END bigquery_load_table_gcs_csv_truncate]
    # [END bigquery_load_table_gcs_json_truncate]
    # [END bigquery_load_table_gcs_parquet_truncate]
    # [END bigquery_load_table_gcs_orc_truncate]

    # Format-specific code
    # [START bigquery_load_table_gcs_avro_truncate]
    job_config.source_format = bigquery.SourceFormat.AVRO
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.avro"
    # [END bigquery_load_table_gcs_avro_truncate]

    # [START bigquery_load_table_gcs_csv_truncate]
    job_config.skip_leading_rows = 1
    # The source format defaults to CSV, so the line below is optional.
    job_config.source_format = bigquery.SourceFormat.CSV
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    # [END bigquery_load_table_gcs_csv_truncate]
    # unset csv-specific attribute
    del job_config._properties["load"]["skipLeadingRows"]

    # [START bigquery_load_table_gcs_json_truncate]
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.json"
    # [END bigquery_load_table_gcs_json_truncate]

    # [START bigquery_load_table_gcs_parquet_truncate]
    job_config.source_format = bigquery.SourceFormat.PARQUET
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.parquet"
    # [END bigquery_load_table_gcs_parquet_truncate]

    # [START bigquery_load_table_gcs_orc_truncate]
    job_config.source_format = bigquery.SourceFormat.ORC
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.orc"
    # [END bigquery_load_table_gcs_orc_truncate]

    # Shared code
    # [START bigquery_load_table_gcs_avro_truncate]
    # [START bigquery_load_table_gcs_csv_truncate]
    # [START bigquery_load_table_gcs_json_truncate]
    # [START bigquery_load_table_gcs_parquet_truncate]
    # [START bigquery_load_table_gcs_orc_truncate]
    load_job = client.load_table_from_uri(
        uri, table_ref, job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(table_ref)
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END bigquery_load_table_gcs_avro_truncate]
    # [END bigquery_load_table_gcs_csv_truncate]
    # [END bigquery_load_table_gcs_json_truncate]
    # [END bigquery_load_table_gcs_parquet_truncate]
    # [END bigquery_load_table_gcs_orc_truncate]

    out, _ = capsys.readouterr()
    assert "Loaded 50 rows." in out


def test_undelete_table(client, to_delete):
    dataset_id = "undelete_table_dataset_{}".format(_millis())
    table_id = "undelete_table_table_{}".format(_millis())
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    dataset.location = "US"
    dataset = client.create_dataset(dataset)
    to_delete.append(dataset)

    table = bigquery.Table(dataset.table(table_id), schema=SCHEMA)
    client.create_table(table)

    # [START bigquery_undelete_table]
    # TODO(developer): Uncomment the lines below and replace with your values.
    # import time
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # dataset_id = 'my_dataset'  # Replace with your dataset ID.
    # table_id = 'my_table'      # Replace with your table ID.

    table_ref = client.dataset(dataset_id).table(table_id)

    # TODO(developer): Choose an appropriate snapshot point as epoch
    # milliseconds. For this example, we choose the current time as we're about
    # to delete the table immediately afterwards.
    snapshot_epoch = int(time.time() * 1000)
    # [END bigquery_undelete_table]

    # Due to very short lifecycle of the table, ensure we're not picking a time
    # prior to the table creation due to time drift between backend and client.
    table = client.get_table(table_ref)
    created_epoch = datetime_helpers.to_microseconds(table.created)
    if created_epoch > snapshot_epoch:
        snapshot_epoch = created_epoch

    # [START bigquery_undelete_table]

    # "Accidentally" delete the table.
    client.delete_table(table_ref)  # API request

    # Construct the restore-from table ID using a snapshot decorator.
    snapshot_table_id = "{}@{}".format(table_id, snapshot_epoch)
    source_table_ref = client.dataset(dataset_id).table(snapshot_table_id)

    # Choose a new table ID for the recovered table data.
    recovered_table_id = "{}_recovered".format(table_id)
    dest_table_ref = client.dataset(dataset_id).table(recovered_table_id)

    # Construct and run a copy job.
    job = client.copy_table(
        source_table_ref,
        dest_table_ref,
        # Location must match that of the source and destination tables.
        location="US",
    )  # API request

    job.result()  # Waits for job to complete.

    print(
        "Copied data from deleted table {} to {}".format(table_id, recovered_table_id)
    )
    # [END bigquery_undelete_table]


def test_manage_job(client):
    sql = """
        SELECT corpus
        FROM `bigquery-public-data.samples.shakespeare`
        GROUP BY corpus;
    """
    location = "us"
    job = client.query(sql, location=location)
    job_id = job.job_id

    # [START bigquery_cancel_job]
    # TODO(developer): Uncomment the lines below and replace with your values.
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # job_id = 'bq-job-123x456-123y123z123c'  # replace with your job ID
    # location = 'us'                         # replace with your location

    job = client.cancel_job(job_id, location=location)
    # [END bigquery_cancel_job]

    # [START bigquery_get_job]
    # TODO(developer): Uncomment the lines below and replace with your values.
    # from google.cloud import bigquery
    # client = bigquery.Client()
    # job_id = 'bq-job-123x456-123y123z123c'  # replace with your job ID
    # location = 'us'                         # replace with your location

    job = client.get_job(job_id, location=location)  # API request

    # Print selected job properties
    print("Details for job {} running in {}:".format(job_id, location))
    print(
        "\tType: {}\n\tState: {}\n\tCreated: {}".format(
            job.job_type, job.state, job.created
        )
    )
    # [END bigquery_get_job]


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
