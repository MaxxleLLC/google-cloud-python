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


from google.cloud import bigquery

from .. import create_view
from .. import get_view
from .. import grant_view_access
from .. import update_view_query


def test_view_samples(capsys, client, random_dataset_id, dataset_id):

    dest_dataset = client.get_dataset(dataset_id)
    view_table_name = "shared_view"
    view_id = "{}.{}.{}".format(
        dest_dataset.project, dest_dataset.dataset_id, view_table_name
    )

    source_dataset = client.create_dataset(random_dataset_id)
    source_table = source_dataset.table("source_table")
    source_table = client.create_table(source_table)
    source_table_id = "{}.source_table".format(random_dataset_id)

    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    job_config.skip_leading_rows = 1
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    load_job = client.load_table_from_uri(uri, source_table, job_config=job_config)
    load_job.result()

    create_view.create_view(client, source_table_id, view_id)
    out, err = capsys.readouterr()
    assert "Successfully created the view at {}".format(view_id) in out

    update_view_query.update_view_query(client, source_table_id, view_id)
    out, err = capsys.readouterr()
    assert "Successfully updated the view at {}".format(view_id) in out

    get_view.get_view(client, view_id)
    out, err = capsys.readouterr()
    assert "View at {}".format(view_id) in out
    assert (
        'SELECT name, post_abbr FROM `{}` WHERE name LIKE "M%"'.format(source_table_id)
        in out
    )

    grant_view_access.grant_view_access(
        client, dataset_id, random_dataset_id, view_table_name
    )
    out, err = capsys.readouterr()
    assert "Dataset: {} access entries updated.".format(dataset_id) in out
    assert (
        "View: {} authorized to access {}".format(view_table_name, random_dataset_id)
        in out
    )
