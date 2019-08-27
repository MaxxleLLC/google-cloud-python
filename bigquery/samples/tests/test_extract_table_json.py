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


from .. import extract_table_json


def test_extract_table_json(capsys, client, bucket, table_with_data_id):

    extract_table_json.extract_table_json(client, bucket, table_with_data_id)
    out, err = capsys.readouterr()
    assert (
        "Exported {} to gs://{}/shakespeare.json".format(
            table_with_data_id, bucket.name
        )
        in out
    )
