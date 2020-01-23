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


def update_view(table_id):

    # [START bigquery_update_view_query]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to load the data.
    # load_table_id = "your-project.your_dataset.your_table_name"

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    view = client.get_table(table_id)  # Make an API request.
    old_view_query = view.view_query

    sql_template = 'SELECT name, post_abbr FROM `{}.{}.{}` WHERE name LIKE "M%"'
    view.view_query = sql_template.format(view.project, view.dataset_id, view.table_id)
    view = client.update_table(view, ["view_query"])  # API request
    new_view_query = view.view_query

    if old_view_query != new_view_query:
        print("The View query has been updated.")
    # [END bigquery_update_view_query]
