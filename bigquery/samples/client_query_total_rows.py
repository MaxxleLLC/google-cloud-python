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


def client_query_total_rows():

    # [START bigquery_relax_column_query_append]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    query = (
        "SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` "
        'WHERE state = "TX" '
        "LIMIT 100"
    )
    query_job = client.query(
        query,
        # Must match the dataset(s) location referenced in the query.
        location="US",
    )  # Make an API request. - starts the query

    results = query_job.result()  # Wait for the query to complete.
    print("Got {} rows.".format(results.total_rows))
    # [END bigquery_query_total_rows]
