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


def extract_table_compressed(client, bucket, table_id):

    # [START bigquery_extract_table_compressed]
    from google.cloud import bigquery

    from test_utils.retry import RetryErrors
    from google.api_core.exceptions import InternalServerError
    from google.api_core.exceptions import ServiceUnavailable
    from google.api_core.exceptions import TooManyRequests

    retry_storage_errors = RetryErrors(
        (TooManyRequests, InternalServerError, ServiceUnavailable)
    )

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Import the Storage library.
    # from google.cloud import storage

    # TODO(developer): Construct a Storage client object.
    # storage_client = storage.Client()

    # TODO(developer): Set bucket to the Cloud Storage Bucket where to extract the table.
    # bucket_name = "your_bucket_name"
    # bucket = retry_storage_errors(storage_client.create_bucket)(bucket_name)

    # TODO(developer): Set table_id to the ID of the table to extract.
    # table_id = 'your-project.your_dataset.your_table'

    destination_uri = "gs://{}/{}".format(bucket.name, "shakespeare.csv.gz")
    table = client.get_table(table_id)  # API request.

    job_config = bigquery.job.ExtractJobConfig()
    job_config.compression = bigquery.Compression.GZIP
    extract_job = client.extract_table(
        table,
        destination_uri,
        location="US",  # Must match the source table location.
        job_config=job_config,
    )
    extract_job.result()  # Waits for job to complete.

    blob = retry_storage_errors(bucket.get_blob)("shakespeare.csv.gz")
    if blob.exists and blob.size > 0:
        print("Exported {} to {}".format(table_id, destination_uri))
    # [END bigquery_extract_table_compressed]
