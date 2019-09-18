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


def get_view(client, view_id):

    # [START bigquery_get_view]
    # TODO(developer): Import the client library.
    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set view_id to the ID of the destination table.
    # view_id = "your-project.your_dataset.your_table_name"

    view = client.get_table(view_id)

    # Display view properties
    print("View at {}.{}.{}".format(view.project, view.dataset_id, view.table_id))
    print("View Query:\n{}".format(view.view_query))
    # [END bigquery_get_view]
