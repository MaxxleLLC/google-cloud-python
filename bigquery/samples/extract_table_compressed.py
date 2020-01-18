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


def extract_table_compressed(table_id):

    # [START bigquery_extract_table_compressed]
    import time

    from google.cloud import bigquery
    from google.cloud import storage

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Construct a Storage client object.
    storage_client = storage.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    bucket_name = "extract_shakespeare_compress_{}".format(int(time.time() * 1000))
    bucket = storage_client.create_bucket(bucket_name)

    destination_uri = "gs://{}/{}".format(bucket_name, "shakespeare.csv.gz")

    job_config = bigquery.job.ExtractJobConfig(
        destination_format=bigquery.Compression.GZIP
    )
    extract_job = client.extract_table(
        table_id,
        destination_uri,
        job_config=job_config,
        # Must match the source table location.
        location="US",
    )  # Make an API request.
    extract_job.result()  # Waits for job to complete.

    table = client.get_table(table_id)
    print(
        "Exported {}.{}.{} to {}".format(
            table.project, table.dataset_id, table.table_id, destination_uri
        )
    )
    # [END bigquery_extract_table_compressed]

    blob = bucket.get_blob("shakespeare.csv.gz")
    return blob, bucket
