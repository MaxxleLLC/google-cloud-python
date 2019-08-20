Running Queries
~~~~~~~~~~~~~~~

Querying data
^^^^^^^^^^^^^

Run a query and wait for it to finish with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query]
   :end-before: [END bigquery_query]


Run a query
^^^^^^^^^^^

Run a dry run query with the 
:func:`~google.cloud.bigquery.client.Client.query` method:
.. literalinclude:: ../samples/client_query_dry_run.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_dry_run]
   :end-before: [END bigquery_query_dry_run]

Run a query at a batch priority with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_batch.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_batch]
   :end-before: [END bigquery_query_batch]

Run a query with Legacy SQL explicitly set with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_legacy_sql.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_legacy]
   :end-before: [END bigquery_query_legacy]
   
Run a query and just check for how many rows with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_total_rows.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_total_rows]
   :end-before: [END bigquery_query_total_rows]

Run a query to update a table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a column to the existing table with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_add_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_add_column_query_append]
   :end-before: [END bigquery_add_column_query_append]

See BigQuery documentation for more information on
`writing query results <https://cloud.google.com/bigquery/docs/writing-results>`_.

Write a query results to a destination table with the
:func:`~google.cloud.bigquery.client.Client.query` method:
.. literalinclude:: ../samples/client_query_destination_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_destination_table]
   :end-before: [END bigquery_query_destination_table]

Write a query results in the legacy SQL syntax to a destination table with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_destination_table_legacy.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_legacy_large_results]
   :end-before: [END bigquery_query_legacy_large_results]

Write a query results to a destination table, allowing fields relaxation with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_relax_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_relax_column_query_append]
   :end-before: [END bigquery_relax_column_query_append]

Write a specified encryption configuration to a destination table with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_destination_table_cmek.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_destination_table_cmek]
   :end-before: [END bigquery_query_destination_table_cmek]

Run a query using specified parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See BigQuery documentation for more information on
`parameterized queries <https://cloud.google.com/bigquery/docs/parameterized-queries>`_.

Run a query using a named query parameter
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_params_named]
   :end-before: [END bigquery_query_params_named]

Run a query using array query parameters with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_w_array_params.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_params_arrays]
   :end-before: [END bigquery_query_params_arrays]
