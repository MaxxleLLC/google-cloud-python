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


def load_table_from_dataframe(client, table_id):

    # [START bigquery_load_table_dataframe]
    # TODO(developer): Import the client library.
    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = 'your-project.your_dataset.your_table'

    import pandas

    records = [
        {"title": u"The Meaning of Life", "release_year": 1983},
        {"title": u"Monty Python and the Holy Grail", "release_year": 1975},
        {"title": u"Life of Brian", "release_year": 1979},
        {"title": u"And Now for Something Completely Different", "release_year": 1971},
    ]
    # Optionally set explicit indices.
    # If indices are not specified, a column will be created for the default
    # indices created by pandas.
    index = [u"Q24980", u"Q25043", u"Q24953", u"Q16403"]
    dataframe = pandas.DataFrame(records, index=pandas.Index(index, name="wikidata_id"))

    job = client.load_table_from_dataframe(dataframe, table_id, location="US")
    job.result()

    table = client.get_table(table_id)
    print("Table {} contains {} row(s)".format(table_id, table.num_rows))
    column_names = [field.name for field in table.schema]
    print(sorted(column_names))
    # [END bigquery_load_table_dataframe]
