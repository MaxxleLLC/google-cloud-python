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

import datetime

from .. import update_table_expiration


def test_update_table_expiration(capsys, random_table_id):

    table, expiration = update_table_expiration.update_table_expiration(random_table_id)
    out, _ = capsys.readouterr()
    assert "Updated table {} with new expiration".format(table.table_id) in out

    # expiration is stored in milliseconds
    margin = datetime.timedelta(microseconds=1000)
    assert expiration - margin <= table.expires <= expiration + margin
