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


def ddl_create_view(client, table_id):

    # [START bigquery_ddl_create_view]
    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create
    # table_id = "your-project.your_dataset.your_table_name"

    try:
        import pandas
    except (ImportError, AttributeError):
        pandas = None

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

    # Test that listing query result rows succeeds so that generic query
    # processing tools work with DDL statements.
    rows = list(job)
    if pandas is not None:
        df = job.to_dataframe()
        if len(df) == 0 and len(rows) == 0:
            print('Created new view "{}".'.format(table_id))
    elif len(rows) == 0:
        print('Created new view "{}".'.format(table_id))

    # [END bigquery_ddl_create_view]
