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

from .. import create_view
from .. import update_view
from .. import get_view
from .. import grant_view_access


def test_manage_views(capsys, table_id, random_table_id, random_dataset_id):
    create_view.create_view(table_id, random_table_id)
    out, err = capsys.readouterr()
    assert "Successfully created view at {}".format(random_table_id) in out

    update_view.update_view(random_table_id)
    out, err = capsys.readouterr()
    assert "The View query has been updated." in out

    get_view.get_view(random_table_id)
    out, err = capsys.readouterr()
    assert "View at" in out
    assert "View Query" in out

    grant_view_access.grant_view_access(table_id, random_dataset_id)
    out, err = capsys.readouterr()
    assert "Assign access controls to the dataset successfully." in out
    assert "Grant view access successfully" in out
