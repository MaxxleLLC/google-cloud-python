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


def create_table_nested_repeated_schema(client, table_id):

    # [START bigquery_nested_repeated_schema]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create
    # table_id = "your-project.your_dataset.your_table_name"

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
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)

    table = client.get_table(table_id)
    if table.schema == schema:
        print("Created table {}".format(table_id))

    # [END bigquery_nested_repeated_schema]
