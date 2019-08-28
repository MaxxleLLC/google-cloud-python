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

try:
    import fastparquet
except (ImportError, AttributeError):
    fastparquet = None
try:
    import pandas
except (ImportError, AttributeError):
    pandas = None
try:
    import pyarrow
except (ImportError, AttributeError):
    pyarrow = None

from .. import load_table_from_dataframe


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
@pytest.mark.parametrize("parquet_engine", ["pyarrow", "fastparquet"])
def test_load_table_from_dataframe(capsys, client, random_table_id, parquet_engine):

    if parquet_engine == "pyarrow" and pyarrow is None:
        pytest.skip("Requires `pyarrow`")
    if parquet_engine == "fastparquet" and fastparquet is None:
        pytest.skip("Requires `fastparquet`")

    pandas.set_option("io.parquet.engine", parquet_engine)

    load_table_from_dataframe.load_table_from_dataframe(client, random_table_id)
    out, err = capsys.readouterr()
    assert "Table {} contains 4 row(s)".format(random_table_id) in out
    assert "['release_year', 'title', 'wikidata_id']" in out
