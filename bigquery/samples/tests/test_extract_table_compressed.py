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

from .. import extract_table_compressed


def test_extract_table_compressed(capsys, table_with_data_id):

    blob, bucket = extract_table_compressed.extract_table_compressed(table_with_data_id)
    out, _ = capsys.readouterr()
    assert "Exported {} ".format(table_with_data_id) in out
    assert blob.exists
    assert blob.size > 0

    blob.delete()
    bucket.delete()
