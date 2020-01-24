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


def query_results_as_dataframe():

    # [START bigquery_query_results_dataframe]
    from google.cloud import bigquery

    import pandas

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Run a SQL script.
    sql = """
            SELECT name, SUM(number) as count
            FROM `bigquery-public-data.usa_names.usa_1910_current`
            GROUP BY name
            ORDER BY count DESC
            LIMIT 10
        """

    df = client.query(sql).to_dataframe()

    assert isinstance(df, pandas.DataFrame)
    print(
        "There are {} rows and {} columns in dataframe.".format(len(list(df)), len(df))
    )
    # [END bigquery_query_results_dataframe]
