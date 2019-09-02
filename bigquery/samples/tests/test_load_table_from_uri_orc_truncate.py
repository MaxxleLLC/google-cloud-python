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


import six
from google.cloud import bigquery

from .. import load_table_from_uri_orc_truncate


def test_load_table_from_uri_orc_truncate(capsys, client, random_table_id):

    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ]
    body = six.BytesIO(b"Washington,WA")
    client.load_table_from_file(body, random_table_id, job_config=job_config).result()
    previous_rows = client.get_table(random_table_id).num_rows
    assert previous_rows > 0

    load_table_from_uri_orc_truncate.load_table_from_uri_orc_truncate(
        client, random_table_id
    )
    out, err = capsys.readouterr()
    assert "Loaded 50 rows." in out
