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


def create_view(client, source_table_id, view_id):

    # [START bigquery_create_view]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set source_table_id to the ID of the source table.
    # source_table_id = "your-project.your_dataset.your_table_name"

    # TODO(developer): Set view_id to the ID of the destination table.
    # view_id = "your-project.your_dataset.your_table_name"

    # This example shows how to create a shared view of a source table of
    # US States. The source table contains all 50 states, while the view will
    # contain only states with names starting with 'W'.
    view = bigquery.Table(view_id)
    sql_template = 'SELECT name, post_abbr FROM `{}` WHERE name LIKE "W%"'
    view.view_query = sql_template.format(source_table_id)
    view = client.create_table(view)

    print(
        "Successfully created the view at {}.{}.{}".format(
            view.project, view.dataset_id, view.table_id
        )
    )
    # [END bigquery_create_view]
