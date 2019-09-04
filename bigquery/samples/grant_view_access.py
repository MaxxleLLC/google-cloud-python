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


def grant_view_access(client, view_dataset_id, source_dataset_id, view_table_name):

    # [START bigquery_grant_view_access]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set view_dataset_id to the ID of the dataset containing view.
    # view_dataset_id = 'your-project.your_dataset'

    # TODO(developer): Set source_dataset_id to the ID of the dataset containing source.
    # source_dataset_id = 'your-project.your_dataset'

    # TODO(developer): Set view_table_name to the name of your view.
    # view_table_name = "your_view_name"

    # Assign access controls to the dataset containing the view
    view_dataset = client.get_dataset(view_dataset_id)
    analyst_group_email = "example-analyst-group@google.com"  # replace with your values
    access_entries = view_dataset.access_entries
    access_entries.append(
        bigquery.AccessEntry("READER", "groupByEmail", analyst_group_email)
    )
    view_dataset.access_entries = access_entries
    view_dataset = client.update_dataset(view_dataset, ["access_entries"])
    print("Dataset: {} access entries updated.".format(view_dataset_id))

    # Authorize the view to access the source dataset
    source_dataset = client.get_dataset(source_dataset_id)
    view_reference = {
        "projectId": view_dataset.project,
        "datasetId": view_dataset.dataset_id,
        "tableId": view_table_name,
    }
    access_entries = source_dataset.access_entries
    access_entries.append(bigquery.AccessEntry(None, "view", view_reference))
    source_dataset.access_entries = access_entries
    source_dataset = client.update_dataset(source_dataset, ["access_entries"])
    print("View: {} authorized to access {}".format(view_table_name, source_dataset_id))
    # [END bigquery_grant_view_access]
