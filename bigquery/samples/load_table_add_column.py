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


def load_table_add_column(client, table_id):

    # [START bigquery_add_column_load_append]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = 'your-project.your_dataset.your_table'

    import os

    samples_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(samples_dir, "tests", "data", "people.csv")

    old_schema = [bigquery.SchemaField("full_name", "STRING", mode="REQUIRED")]
    table = client.create_table(bigquery.Table(table_id, schema=old_schema))

    # Retrieves the destination table and checks the length of the schema
    print("Table {} contains {} column(s).".format(table_id, len(table.schema)))

    # Configures the load job to append the data to the destination table,
    # allowing field addition
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.schema_update_options = [
        bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
    ]
    # In this example, the existing table contains only the 'full_name' column.
    # 'REQUIRED' fields cannot be added to an existing schema, so the
    # additional column must be 'NULLABLE'.
    job_config.schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1

    with open(filepath, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            table,
            location="US",  # Must match the destination dataset location.
            job_config=job_config,
        )
    job.result()

    print("Loaded {} row(s) into {}.".format(job.output_rows, table_id))

    # Checks the updated length of the schema
    table = client.get_table(table)
    print("Table {} now contains {} column(s).".format(table_id, len(table.schema)))
    # [END bigquery_add_column_load_append]
