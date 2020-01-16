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


def update_table_description(table_id):

    # [START bigquery_update_table_description]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    table = bigquery.Table(
        table_id,
        schema=[
            bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
        ],
    )
    table = client.create_table(table)
    table.description = "Updated description."
    table = client.update_table(table, ["description"])  # Make an API request.

    full_table_id = "{}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    print(
        "Updated table '{}' with description '{}'.".format(
            full_table_id, table.description
        )
    )
    # [END bigquery_update_table_description]
