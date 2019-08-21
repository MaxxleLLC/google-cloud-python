Running Queries
~~~~~~~~~~~~~~~

Querying data
^^^^^^^^^^^^^

Run a query and wait for it to finish:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query]
   :end-before: [END bigquery_query]


Run a dry run query
^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../samples/client_query_dry_run.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_dry_run]
   :end-before: [END bigquery_query_dry_run]


Writing query results to a destination table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run a query with Legacy SQL explicitly set with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_legacy_sql.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_legacy]
   :end-before: [END bigquery_query_legacy]


See BigQuery documentation for more information on
`writing query results <https://cloud.google.com/bigquery/docs/writing-results>`_.

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_destination_table]
   :end-before: [END bigquery_query_destination_table]

Write a query results to a table, using the legacy SQL syntax with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_destination_table_legacy.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_legacy_large_results]
   :end-before: [END bigquery_query_legacy_large_results]

Write a query results to a table, allowing fields relaxation with the
:func:`~google.cloud.bigquery.client.Client.query` method:

.. literalinclude:: ../samples/client_query_relax_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_relax_column_query_append]
   :end-before: [END bigquery_relax_column_query_append]

Run a query using a named query parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See BigQuery documentation for more information on
`parameterized queries <https://cloud.google.com/bigquery/docs/parameterized-queries>`_.

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_query_params_named]
   :end-before: [END bigquery_query_params_named]
