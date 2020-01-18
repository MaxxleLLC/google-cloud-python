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


def grant_view_access(load_table_id, dataset_id):

    # [START bigquery_update_view_query]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to load the data.
    # load_table_id = "your-project.your_dataset.your_table_name"

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
    analyst_group_email = "example-analyst-group@google.com"

    # Assign access controls to the dataset
    shared_dataset = client.get_dataset(client.dataset(table.dataset_id))  # API request

    access_entries = shared_dataset.access_entries
    access_entries.append(
        bigquery.AccessEntry("READER", "groupByEmail", analyst_group_email)
    )
    shared_dataset.access_entries = access_entries
    shared_dataset = client.update_dataset(
        shared_dataset, ["access_entries"]
    )  # Make an API request.
    if shared_dataset.access_entries:
        print("Assign access controls to the dataset successfully.")

    # Authorize the view to access the source dataset

    # TODO(developer): Set dataset_id to the ID of the dataset to create.
    # dataset_id = "{}.your_dataset".format(client.project)
    source_dataset = client.create_dataset(dataset_id)  # Make an API request.

    view_reference = {
        "projectId": client.project,
        "datasetId": table.dataset_id,
        "tableId": table.table_id,
    }
    access_entries = source_dataset.access_entries
    access_entries.append(bigquery.AccessEntry(None, "view", view_reference))
    source_dataset.access_entries = access_entries
    source_dataset = client.update_dataset(
        source_dataset, ["access_entries"]
    )  # Make an API request.
    for access_entry in source_dataset.access_entries:
        if access_entry.entity_type == "view":
            print("Grant view access successfully.")
    # [END bigquery_grant_view_access]
