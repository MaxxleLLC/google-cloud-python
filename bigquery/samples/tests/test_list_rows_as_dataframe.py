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

import pytest

from .. import list_rows_as_dataframe


pandas = pytest.importorskip("pandas")


def test_list_rows_as_dataframe(capsys, table_with_data_id):
    list_rows_as_dataframe.list_rows_as_dataframe(table_with_data_id)
    out, _ = capsys.readouterr()
    assert "There are 4 rows and 164656 columns in dataframe." in out
