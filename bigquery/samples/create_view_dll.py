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


def create_view_dll(table_id):

    # [START bigquery_update_view_query]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to load the data.
    # table_id = "your-project.your_dataset.your_table_name"

    sql = """
        CREATE VIEW `{}`
        OPTIONS(
            expiration_timestamp=TIMESTAMP_ADD(
                CURRENT_TIMESTAMP(), INTERVAL 48 HOUR),
            friendly_name="new_view",
            description="a view that expires in 2 days",
            labels=[("org_unit", "development")]
        )
        AS SELECT name, state, year, number
            FROM `bigquery-public-data.usa_names.usa_1910_current`
            WHERE state LIKE 'W%'
        """.format(
        table_id
    )

    job = client.query(sql)  # API request.
    job.result()  # Waits for the query to finish.

    print(
        "Created new view {}.{}.{}.".format(
            job.destination.project,
            job.destination.dataset_id,
            job.destination.table_id,
        )
    )
    # [END bigquery_ddl_create_view]
    return job
