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


pandas = pytest.importorskip("pandas", reason="Requeres `pandas`")


def test_list_rows_as_dataframe(capsys, client, table_with_data_id):

    df = list_rows_as_dataframe.list_rows_as_dataframe(client, table_with_data_id)
    out, err = capsys.readouterr()
    assert (
        'Retrieved table {} rows as a "pandas.DataFrame"'.format(table_with_data_id)
        in out
    )
    assert isinstance(df, pandas.DataFrame)
