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

from .. import load_table_from_file


def test_load_table_from_file(capsys, client, random_table_id):

    samples_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(samples_dir, "data", "people.csv")

    load_table_from_file.load_table_from_file(client, random_table_id, filepath)
    out, err = capsys.readouterr()
    assert "Loaded 2 rows into {}.".format(random_table_id) in out
