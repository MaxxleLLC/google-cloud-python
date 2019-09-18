Managing Jobs
~~~~~~~~~~~~~

Jobs describe actions performed on data in BigQuery tables:

- Load data into a table
- Run a query against data in one or more tables
- Extract data from a table
- Copy a table

Creating a Job
^^^^^^^^^^^^^^

Create a job with the
:func:`~google.cloud.bigquery.client.Client.create_job` method:

.. literalinclude:: ../../samples/create_job.py
    :language: python
    :dedent: 4
    :start-after: [START bigquery_create_job]
    :end-before: [END bigquery_create_job]

Getting a Job
^^^^^^^^^^^^^

Get a job with the
:func:`~google.cloud.bigquery.client.Client.get_job` method:

.. literalinclude:: ../../samples/get_job.py
    :language: python
    :dedent: 4
    :start-after: [START bigquery_get_job]
    :end-before: [END bigquery_get_job]

Canceling a Job
^^^^^^^^^^^^^^^

Cancel a job with the
:func:`~google.cloud.bigquery.client.Client.cancel_job` method:

.. literalinclude:: ../../samples/cancel_job.py
    :language: python
    :dedent: 4
    :start-after: [START bigquery_cancel_job]
    :end-before: [END bigquery_cancel_job]

Listing jobs
^^^^^^^^^^^^

List jobs for a project with the
:func:`~google.cloud.bigquery.client.Client.list_jobs` method:

.. literalinclude:: ../samples/client_list_jobs.py
   :language: python
   :dedent: 4
   :start-after: [START bigquery_list_jobs]
   :end-before: [END bigquery_list_jobs]
