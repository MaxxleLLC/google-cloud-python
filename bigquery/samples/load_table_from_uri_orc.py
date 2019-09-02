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


def load_table_from_uri_orc(client, table_id):

    # [START bigquery_load_table_gcs_orc]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = 'your-project.your_dataset.your_table'

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.ORC
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.orc"

    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END bigquery_load_table_gcs_orc]
