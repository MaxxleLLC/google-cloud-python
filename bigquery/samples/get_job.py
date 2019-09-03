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


def get_job(client, job_id, location):

    # [START bigquery_get_job]
    # TODO(developer): Import the client library.
    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set job_id to the ID of the job to cancel.
    # job_id = 'bq-job-123x456-123y123z123c'

    # TODO(developer): Set location to the location where job runs.
    # location = "your_location"

    job = client.get_job(job_id, location=location)

    print("Details for job {} running in {}:".format(job_id, location))
    print(
        "\tType: {}\n\tState: {}\n\tCreated: {}".format(
            job.job_type, job.state, job.created
        )
    )
    # [END bigquery_get_job]
