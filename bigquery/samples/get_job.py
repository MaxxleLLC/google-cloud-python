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


def get_job():

    # [START bigquery_get_job]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    sql = """
        SELECT corpus
        FROM `bigquery-public-data.samples.shakespeare`
        GROUP BY corpus;
    """
    location = "us"
    job = client.query(sql, location=location)
    job_id = job.job_id

    job = client.get_job(job_id, location=location)  # Make an API request.
    print("Details for job {} running in {}:".format(job_id, location))

    print(
        "Type: {}, State: {}, Created: {}".format(job.job_type, job.state, job.created)
    )
    # [END bigquery_get_job]
