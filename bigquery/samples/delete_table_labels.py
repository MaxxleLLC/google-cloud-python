# Copyright 2020 Google LLC
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


def delete_table_labels(table_id):

    # [START bigquery_delete_label_table]

    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    table = client.get_table(table_id)  # Make an API request.

    # To delete a label from a dataset, set its value to None.
    table.labels["color"] = None

    table = client.update_table(table, ["labels"])  # Make an API request.
    print("Labels deleted from {}".format(table_id))
    # [END bigquery_delete_label_table]
    return table
