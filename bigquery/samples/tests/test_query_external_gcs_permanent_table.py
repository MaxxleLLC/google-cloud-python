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

from .. import query_external_gcs_permanent_table


def test_query_external_gcs_permanent_table(capsys, random_table_id):
    query_external_gcs_permanent_table.query_external_gcs_permanent_table(
        random_table_id
    )
    out, _ = capsys.readouterr()
    assert "There are 4 states with names starting with W." in out
