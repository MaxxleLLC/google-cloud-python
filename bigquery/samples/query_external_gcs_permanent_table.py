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


def query_external_gcs_permanent_table(table_id):

    # [START bigquery_query_external_gcs_perm]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set dataset_id to the ID of the dataset to create.
    # dataset_id = "{}.your_dataset".format(client.project)

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    table = bigquery.Table(
        table_id,
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("post_abbr", "STRING"),
        ],
    )

    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [
        "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    ]
    external_config.options.skip_leading_rows = 1  # optionally skip header row
    table.external_data_configuration = external_config

    # Create a permanent table linked to the GCS file
    table = client.create_table(table)  # Make an API request.
    # Example query to find states starting with 'W'
    sql = 'SELECT * FROM `{}.{}` WHERE name LIKE "W%"'.format(
        table.dataset_id, table.table_id
    )

    query_job = client.query(sql)  # Make an API request.

    w_states = list(query_job)  # Waits for query to finish
    print("There are {} states with names starting with W.".format(len(w_states)))

    # [END bigquery_query_external_gcs_perm]
