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


from .. import create_job
from .. import get_job
from .. import cancel_job


def test_manage_job(capsys, client):

    job = create_job.create_job(client)
    out, err = capsys.readouterr()
    assert "Started job: {}".format(job.job_id) in out

    get_job.get_job(client, job.job_id, job.location)
    out, err = capsys.readouterr()
    assert "Details for job {} running in {}:".format(job.job_id, job.location) in out

    cancel_job.cancel_job(client, job.job_id, job.location)
    out, err = capsys.readouterr()
    assert "Job: {} - canceled".format(job.job_id) in out
