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


def create_partitioned_table(table_id):

    # [START bigquery_create_table_partitioned]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    table = bigquery.Table(
        table_id,
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("post_abbr", "STRING"),
            bigquery.SchemaField("date", "DATE"),
        ],
    )
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="date",  # name of column to use for partitioning
        expiration_ms=7776000000,
    )  # 90 days

    table = client.create_table(table)
    print(
        "Created table {}, partitioned on column {}".format(
            table.table_id, table.time_partitioning.field
        )
    )
    # [END bigquery_create_table_partitioned]
    return table
