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


from .. import browse_table_data


def test_browse_table_data(capsys, client, table_w_data):

    browse_table_data.browse_table_data(client, table_w_data)
    out, err = capsys.readouterr()
    assert "The amount of rows in the table = " in out
    assert "First 10 rows of the table are loaded" in out
    assert "Fields number set to 2"
    assert "List of non-blank lines:"
    assert "Printed data contains 11 rows"
