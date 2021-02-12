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

from .. import create_partitioned_table


def test_create_partitioned_table(capsys, random_table_id):
    table = create_partitioned_table.create_partitioned_table(random_table_id)
    out, _ = capsys.readouterr()
    assert "Created table {}, partitioned on column date".format(table.table_id)
    assert table.time_partitioning.type_ == "DAY"
    assert table.time_partitioning.field == "date"
    assert table.time_partitioning.expiration_ms == 7776000000
