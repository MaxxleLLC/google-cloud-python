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


def get_view(load_table_id, table_id):

    # [START bigquery_get_view]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to load the data.
    # load_table_id = "your-project.your_dataset.your_table_name"

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("post_abbr", "STRING"),
        ],
        skip_leading_rows=1,
    )
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

    load_job = client.load_table_from_uri(uri, load_table_id, job_config=job_config)
    load_job.result()
    table = client.get_table(load_table_id)
    view = bigquery.Table(table_id)
    sql_template = 'SELECT name, post_abbr FROM `{}.{}.{}` WHERE name LIKE "W%"'
    view.view_query = sql_template.format(
        view.project, table.dataset_id, table.table_id
    )
    view = client.create_table(view)  # Make an API request.

    print("View at {}".format(view.full_table_id))
    print("View Query:\n{}".format(view.view_query))
    # [END bigquery_get_view]
