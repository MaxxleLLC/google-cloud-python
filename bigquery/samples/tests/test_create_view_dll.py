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

from .. import create_view_dll


def test_create_view_dll(capsys, random_table_id):
    job = create_view_dll.create_view_dll(random_table_id)
    out, _ = capsys.readouterr()
    assert "Created new view {}.".format(random_table_id) in out

    # Test that listing query result rows succeeds so that generic query
    # processing tools work with DDL statements.
    rows = list(job)
    assert len(rows) == 0
