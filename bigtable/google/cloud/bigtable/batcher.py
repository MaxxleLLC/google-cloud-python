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

"""User friendly container for Google Cloud Bigtable MutationBatcher."""


FLUSH_COUNT = 1000
MAX_MUTATIONS = 100000
MAX_ROW_BYTES = 5242880  # 5MB


class MaxMutationsError(ValueError):
    """The number of mutations for bulk request is too big."""


class MutationsBatcher(object):
    """ A MutationsBatcher is used in batch cases where the number of mutations
    is large or unknown. It will store DirectRows in memory until one of the
    size limits is reached, or an explicit call to finish_batch() is performed.
     When a flush event occurs, the DirectRows in memory will be sent to Cloud
    Bigtable. Batching mutations is more efficient than sending individual
    request.

    This class is not suited for usage in systems where each mutation
    needs to guaranteed to be sent, since calling mutate may only result in an
    in-memory change. In a case of a system crash, any DirectRows remaining in
    memory will not necessarily be sent to the service, even after the
    completion of the mutate() method.

    :type table: class
    :param table: class:`~google.cloud.bigtable.table.Table`.

    :type flush_count: int
    :param flush_count: (Optional) Max number of rows to flush. If it
    reaches the max number of rows it calls finish_batch() to mutate the
    current row batch. Default is FLUSH_COUNT (1000 rows).

    :type max_row_bytes: int
    :param max_row_bytes: (Optional) Max number of row mutations size to
    flush. If it reaches the max number of row mutations size it calls
    finish_batch() to mutate the current row batch. Default is MAX_ROW_BYTES
    (5 MB).
    """

    def __init__(self, table, flush_count=FLUSH_COUNT, max_row_bytes=MAX_ROW_BYTES):
        self.rows = []
        self.total_mutation_count = 0
        self.total_size = 0
        self.table = table
        self.flush_count = flush_count
        self.max_row_bytes = max_row_bytes
        self.batches = []

    def mutate(self, row, is_last=False):
        """ Add a row to the current batch. If the current batch meets one of
        the size limits, automatic new branch create and row append in the new
        batch

        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_batcher_mutate]
            :end-before: [END bigtable_batcher_mutate]

        :type row: class
        :param row: class:`~google.cloud.bigtable.row.DirectRow`.

        :raises: One of the following:
                 * :exc:`~.table._BigtableRetryableError` if any
                   row returned a transient error.
                 * :exc:`RuntimeError` if the number of responses doesn't
                   match the number of rows that were retried
                 * :exc:`.batcher.MaxMutationsError` if any row exceeds max
                   mutations count.
        """
        mutation_count = len(row._get_mutations())
        if mutation_count > MAX_MUTATIONS:
            raise MaxMutationsError(
                "The row key {} exceeds the number of mutations {}.".format(
                    row.row_key, mutation_count
                )
            )

        if (self.total_mutation_count + mutation_count) >= MAX_MUTATIONS:
            self.finish_batch()

        self.rows.append(row)
        self.total_mutation_count += mutation_count
        self.total_size += row.get_mutations_size()

        if (
            self.total_size >= self.max_row_bytes
            or len(self.rows) >= self.flush_count
            or is_last
        ):
            self.finish_batch()

    def mutate_rows(self, rows):
        """Make batch(es) from rows. batch is collection of rows.  mutate rows
        have multiple batch(es)

        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_batcher_mutate_rows]
            :end-before: [END bigtable_batcher_mutate_rows]

        :type rows: list:[`~google.cloud.bigtable.row.DirectRow`]
        :param rows: list:[`~google.cloud.bigtable.row.DirectRow`].

        :raises: One of the following:
                 * :exc:`~.table._BigtableRetryableError` if any
                   row returned a transient error.
                 * :exc:`RuntimeError` if the number of responses doesn't
                   match the number of rows that were retried
                 * :exc:`.batcher.MaxMutationsError` if any row exceeds max
                   mutations count.
        """
        for row in rows:
            is_last = rows[-1] is row
            self.mutate(row, is_last)

    def finish_batch(self):
        """Create a batch and add to the collection if there is rows exists
        in class. It can used for externally create batch
        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_batcher_flush]
            :end-before: [END bigtable_batcher_flush]

        """
        if len(self.rows) != 0:
            self.batches.append(self.rows)
            self.total_mutation_count = 0
            self.total_size = 0
            self.rows = []

    def flush_batches(self):
        """Sends batch(es) to Google Cloud Bigtable.
        The batch(es) is sent synchronously.

        :return: combined list of response status of every row in batches
        """
        return self.table.flush_batches(self.batches)
