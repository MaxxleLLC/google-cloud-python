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


def client_query_relax_column(client, table_id):

    # [START bigquery_relax_column_query_append]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]

    table = client.create_table(bigquery.Table(table_id, schema=schema))

    # Retrieves the destination table and checks the number of required fields.
    original_required_fields = sum(field.mode == "REQUIRED" for field in table.schema)
    # In this example, the existing table has 2 required fields
    print("{} fields in the schema are required.".format(original_required_fields))

    # Configures the query to append the results to a destination table,
    # allowing field relaxation.
    job_config = bigquery.QueryJobConfig()
    job_config.schema_update_options = [
        bigquery.SchemaUpdateOption.ALLOW_FIELD_RELAXATION
    ]
    job_config.destination = table
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    query_job = client.query(
        # In this example, the existing table contains 'full_name' and 'age' as
        # required columns, but the query results will omit the second column.
        'SELECT "Beyonce" as full_name;',
        # Location must match that of the dataset(s) referenced in the query
        # and of the destination table.
        location="US",
        job_config=job_config,
    )
    query_job.result()

    # Checks the updated number of required fields
    table = client.get_table(table_id)
    current_required_fields = sum(field.mode == "REQUIRED" for field in table.schema)
    if (
        original_required_fields - current_required_fields > 0
        and table.schema[1].mode == "NULLABLE"
    ):
        print(
            "{} fields in the schema are now required.".format(current_required_fields)
        )
    # [END bigquery_relax_column_query_append]
