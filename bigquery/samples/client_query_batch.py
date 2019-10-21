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


def client_query_batch(client):

    # [START bigquery_query_batch]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    job_config = bigquery.QueryJobConfig()

    # Run at batch priority, which won't count toward concurrent rate limit.
    job_config.priority = bigquery.QueryPriority.BATCH
    sql = """
        SELECT corpus
        FROM `bigquery-public-data.samples.shakespeare`
        GROUP BY corpus;
    """

    # Start the query, passing in the extra configuration.
    query_job = client.query(
        sql, location="US", job_config=job_config
    )  # Make an API request.

    # Check on the progress by getting the job's updated state. Once the state
    # is `DONE`, the results are ready.
    query_job = client.get_job(query_job.job_id, location="US")  # Make an API request.

    print("Job {} is currently in state {}".format(query_job.job_id, query_job.state))
    # [END bigquery_query_batch]
    return query_job
