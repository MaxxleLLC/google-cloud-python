# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest

import mock

from ._testing import _make_credentials

from google.cloud.bigtable.batcher import MutationsBatcher
from google.cloud.bigtable.row import DirectRow


class TestMutationsBatcher(unittest.TestCase):
    from grpc import StatusCode

    TABLE_ID = "table-id"
    TABLE_NAME = "/tables/" + TABLE_ID

    # RPC Status Codes
    SUCCESS = StatusCode.OK.value[0]

    @staticmethod
    def _get_target_class():
        from google.cloud.bigtable.table import Table

        return Table

    def _make_table(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    @staticmethod
    def _get_target_client_class():
        from google.cloud.bigtable.client import Client

        return Client

    def _make_client(self, *args, **kwargs):
        return self._get_target_client_class()(*args, **kwargs)

    def test_constructor(self):
        credentials = _make_credentials()
        client = self._make_client(
            project="project-id", credentials=credentials, admin=True
        )

        instance = client.instance(instance_id="instance-id")
        table = self._make_table(self.TABLE_ID, instance)

        mutation_batcher = MutationsBatcher(table)
        self.assertEqual(table, mutation_batcher.table)

    def test_mutate_row(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table)

        rows = [
            DirectRow(row_key=b"row_key"),
            DirectRow(row_key=b"row_key_2"),
            DirectRow(row_key=b"row_key_3"),
            DirectRow(row_key=b"row_key_4"),
        ]

        mutation_batcher.mutate_rows(rows)
        mutation_batcher.finish_batch()

        self.assertEqual(len(mutation_batcher.batches), 1)

    def test_mutate_rows(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table)

        row = DirectRow(row_key=b"row_key")
        row.set_cell("cf1", b"c1", 1)
        row.set_cell("cf1", b"c2", 2)
        row.set_cell("cf1", b"c3", 3)
        row.set_cell("cf1", b"c4", 4)
        mutation_batcher.mutate(row, True)
        mutation_batcher.flush_batches()
        self.assertEqual(len(mutation_batcher.batches), 1)

    def test_flush_with_no_rows(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table)
        mutation_batcher.flush_batches()
        self.assertEqual(len(mutation_batcher.batches), 0)

    def test_add_row_with_max_flush_count(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table, flush_count=3)

        row_1 = DirectRow(row_key=b"row_key_1")
        row_2 = DirectRow(row_key=b"row_key_2")
        row_3 = DirectRow(row_key=b"row_key_3")

        mutation_batcher.mutate(row_1)
        mutation_batcher.mutate(row_2)
        mutation_batcher.mutate(row_3)

        self.assertEqual(len(mutation_batcher.batches), 1)

    @mock.patch("google.cloud.bigtable.batcher.MAX_MUTATIONS", new=3)
    def test_mutate_row_with_max_mutations_failure(self):
        from google.cloud.bigtable.batcher import MaxMutationsError

        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table)

        row = DirectRow(row_key=b"row_key")
        row.set_cell("cf1", b"c1", 1)
        row.set_cell("cf1", b"c2", 2)
        row.set_cell("cf1", b"c3", 3)
        row.set_cell("cf1", b"c4", 4)

        with self.assertRaises(MaxMutationsError):
            mutation_batcher.mutate(row)

    @mock.patch("google.cloud.bigtable.batcher.MAX_MUTATIONS", new=3)
    def test_mutate_row_with_max_mutations(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table)

        row = DirectRow(row_key=b"row_key")
        row.set_cell("cf1", b"c1", 1)
        row.set_cell("cf1", b"c2", 2)
        row.set_cell("cf1", b"c3", 3)

        mutation_batcher.mutate(row)
        mutation_batcher.finish_batch()

        self.assertEqual(len(mutation_batcher.batches), 1)

    def test_mutate_row_with_max_row_bytes(self):
        table = _Table(self.TABLE_NAME)
        mutation_batcher = MutationsBatcher(table=table, max_row_bytes=3 * 1024 * 1024)

        number_of_bytes = 1 * 1024 * 1024
        max_value = b"1" * number_of_bytes

        row = DirectRow(row_key=b"row_key")
        row.set_cell("cf1", b"c1", max_value)
        row.set_cell("cf1", b"c2", max_value)
        row.set_cell("cf1", b"c3", max_value)

        mutation_batcher.mutate(row)

        self.assertEqual(len(mutation_batcher.batches), 1)


class _Instance(object):
    def __init__(self, client=None):
        self._client = client


class _Table(object):
    def __init__(self, name, client=None):
        self.name = name
        self._instance = _Instance(client)
        self.mutation_calls = 0

    def flush_batches(self, rows):
        self.mutation_calls += 1
        return rows
