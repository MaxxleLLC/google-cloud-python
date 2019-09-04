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


from .. import delete_table_labels
from .. import get_table_labels
from .. import label_table


def test_table_label_samples(capsys, client, table_id):

    table = label_table.label_table(client, table_id)
    out, err = capsys.readouterr()
    assert "Labels added to {}".format(table_id) in out
    assert table.labels.get("color") == "green"

    get_table_labels.get_table_labels(client, table_id)
    out, err = capsys.readouterr()
    assert "Labels:\n\tcolor: green" in out

    table = delete_table_labels.delete_table_labels(client, table_id)
    out, err = capsys.readouterr()
    assert "Labels deleted from {}".format(table_id) in out
    assert table.labels.get("color") is None
