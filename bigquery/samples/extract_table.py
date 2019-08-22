# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def extract_table(client, bucket, table_id):

    # [START bigquery_extract_table]
    from test_utils.retry import RetryErrors
    from google.api_core.exceptions import InternalServerError
    from google.api_core.exceptions import ServiceUnavailable
    from google.api_core.exceptions import TooManyRequests

    retry_storage_errors = RetryErrors(
        (TooManyRequests, InternalServerError, ServiceUnavailable)
    )

    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set bucket to the Cloud Storage Bucket where to extract the table.
    # from google.cloud import storage
    # storage_client = storage.Client()
    # bucket_name = "your_bucket_name"
    # bucket = retry_storage_errors(storage_client.create_bucket)(bucket_name)

    # TODO(developer): Set table_id to the ID of the table to extract.
    # table_id = 'your-project.your_dataset.your_table'

    destination_uri = "gs://{}/{}".format(bucket.name, "shakespeare.csv")
    table = client.get_table(table_id)

    extract_job = client.extract_table(
        table,
        destination_uri,
        # Location must match that of the source table.
        location="US",
    )
    extract_job.result()  # Waits for job to complete.

    blob = retry_storage_errors(bucket.get_blob)("shakespeare.csv")
    if blob.exists and blob.size > 0:
        print("Exported {} to {}".format(table_id, destination_uri))

    # [END bigquery_extract_table]
