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


def list_rows_as_dataframe(table_id):

    # [START bigquery_list_rows_dataframe]
    import pandas

    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    table = client.get_table(table_id)

    df = client.list_rows(table).to_dataframe()

    assert isinstance(df, pandas.DataFrame)
    print(
        "There are {} rows and {} columns in dataframe.".format(len(list(df)), len(df))
    )
    # [END bigquery_list_rows_dataframe]
