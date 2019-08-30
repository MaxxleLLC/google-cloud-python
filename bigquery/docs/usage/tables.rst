Managing Tables
~~~~~~~~~~~~~~~

Tables exist within datasets. See BigQuery documentation for more information
on `Tables <https://cloud.google.com/bigquery/docs/tables>`_.

Listing Tables
^^^^^^^^^^^^^^

List the tables belonging to a dataset with the
:func:`~google.cloud.bigquery.client.Client.list_tables` method:

.. literalinclude:: ../samples/list_tables.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_list_tables]
   :end-before: [END bigquery_list_tables]

Getting a Table
^^^^^^^^^^^^^^^

Get a table resource with the
:func:`~google.cloud.bigquery.client.Client.get_table` method:

.. literalinclude:: ../samples/get_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_get_table]
   :end-before: [END bigquery_get_table]

Determine if a table exists with the
:func:`~google.cloud.bigquery.client.Client.get_table` method:

.. literalinclude:: ../samples/table_exists.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_table_exists]
   :end-before: [END bigquery_table_exists]

Browse data rows in a table with the
:func:`~google.cloud.bigquery.client.Client.list_rows` method:

.. literalinclude:: ../samples/browse_table_data.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_browse_table]
   :end-before: [END bigquery_browse_table]

Creating a Table
^^^^^^^^^^^^^^^^

Create an empty table with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table]
   :end-before: [END bigquery_create_table]

Create a partitioned table with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_partitioned_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_create_table_partitioned]
   :end-before: [END bigquery_create_table_partitioned]

Create a table with the nested repeated schema with the
:func:`~google.cloud.bigquery.client.Client.create_table` method:

.. literalinclude:: ../samples/create_table_nested_repeated_schema.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_nested_repeated_schema]
   :end-before: [END bigquery_nested_repeated_schema]

Loading a Table
^^^^^^^^^^^^^^^

Load a partitioned table with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../samples/load_partitioned_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_partitioned]
   :end-before: [END bigquery_load_table_partitioned]

Load table data from a file with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_file` method:

.. literalinclude:: ../samples/load_table_from_file.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_from_file]
   :end-before: [END bigquery_load_from_file]

Load table data from a file and add a column with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_file` method:

.. literalinclude:: ../samples/load_table_add_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_add_column_load_append]
   :end-before: [END bigquery_add_column_load_append]

Load table data from a file, allowing fields relaxation with the
:func:`~google.cloud.bigquery.[-REPLACE_METHOD-]` method:

.. literalinclude:: ../samples/load_table_relax_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_relax_column_load_append]
   :end-before: [END bigquery_relax_column_load_append]

Load table from a GCS URI using csv format and auto-detected schema with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../samples/load_table_from_uri_csv_autodetect.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_csv_autodetect]
   :end-before: [END bigquery_load_table_gcs_csv_autodetect]

Load table from a GCS URI using json format and auto-detected schema with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../samples/load_table_from_uri_json_autodetect.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json_autodetect]
   :end-before: [END bigquery_load_table_gcs_json_autodetect]

Load a CSV file from Cloud Storage with the
:func:`~google.cloud.bigquery.client.Client.load_table_from_uri` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_csv]
   :end-before: [END bigquery_load_table_gcs_csv]

See also: `Loading CSV data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv>`_.

Load a JSON file from Cloud Storage:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_json]
   :end-before: [END bigquery_load_table_gcs_json]

See also: `Loading JSON data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json>`_.

Load a Parquet file from Cloud Storage:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_load_table_gcs_parquet]
   :end-before: [END bigquery_load_table_gcs_parquet]

See also: `Loading Parquet data from Cloud Storage
<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet>`_.

Updating a Table
^^^^^^^^^^^^^^^^

Update a property in a table's metadata with the
:func:`~google.cloud.bigquery.client.Client.update_table` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_update_table_description]
   :end-before: [END bigquery_update_table_description]

Insert rows into a table's data with the
:func:`~google.cloud.bigquery.client.Client.insert_rows` method:

.. literalinclude:: ../samples/table_insert_rows.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_table_insert_rows]
   :end-before: [END bigquery_table_insert_rows]

Add an empty column to the existing table with the
:func:`~google.cloud.bigquery.update_table` method:

.. literalinclude:: ../samples/add_empty_column.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_add_empty_column]
   :end-before: [END bigquery_add_empty_column]

Copying a Table
^^^^^^^^^^^^^^^

Copy a table with the
:func:`~google.cloud.bigquery.client.Client.copy_table` method:

.. literalinclude:: ../samples/copy_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_copy_table]
   :end-before: [END bigquery_copy_table]

Copy multiple tables with the
:func:`~google.cloud.bigquery.client.Client.copy_table` method:

 .. literalinclude:: ../samples/copy_table_multiple_source.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_copy_table_multiple_source]
   :end-before: [END bigquery_copy_table_multiple_source]

Copy table data to Google Cloud Storage with the
:func:`~google.cloud.bigquery.client.Client.extract_table` method:

.. literalinclude:: ../snippets.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_extract_table]
   :end-before: [END bigquery_extract_table]

Compress table data and copy to Google Cloud Storage with the
:func:`~google.cloud.bigquery.client.Client.extract_table` method:

.. literalinclude:: ../samples/extract_table_compressed.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_extract_table_compressed]
   :end-before: [START bigquery_extract_table_compressed]

Copy table data to Google Cloud Storage json-file with the
:func:`~google.cloud.bigquery.client.Client.extract_table` method:
.. literalinclude:: ../samples/extract_table_json.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_extract_table_json]
   :end-before: [END bigquery_extract_table_json]


Deleting a Table
^^^^^^^^^^^^^^^^

Delete a table with the
:func:`~google.cloud.bigquery.client.Client.delete_table` method:

.. literalinclude:: ../samples/delete_table.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_delete_table]
   :end-before: [END bigquery_delete_table]
