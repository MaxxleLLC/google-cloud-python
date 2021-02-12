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

import os

from .. import load_table_relax_column


def test_load_table_relax_column(capsys, random_table_id):

    samples_test_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(
        samples_test_dir, "..", "..", "tests", "data", "people.csv"
    )
    table = load_table_relax_column.load_table_relax_column(file_path, random_table_id)
    out, _ = capsys.readouterr()
    assert "3 fields in the schema are required." in out
    assert "Loaded 2 rows into {}:{}.".format(table.dataset_id, table.table_id) in out
    assert "2 fields in the schema are now required." in out

    assert len(table.schema) == 3
    assert table.schema[2].mode == "NULLABLE"
    assert table.num_rows > 0
