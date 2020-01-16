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


def update_table_cmek(table_id, old_kms_key_name, new_kms_key_name):

    # [START bigquery_update_table_cmek]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    # Set the encryption key to use for the destination.
    # TODO: Replace this key with a key you have created in KMS.
    # kms_key_name = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
    #     "cloud-samples-tests", "us", "test", "test"
    # )

    table = bigquery.Table(table_id)
    table.encryption_configuration = bigquery.EncryptionConfiguration(
        kms_key_name=old_kms_key_name
    )

    table = client.create_table(table)  # API request

    table.encryption_configuration = bigquery.EncryptionConfiguration(
        kms_key_name=new_kms_key_name
    )
    table = client.update_table(table, ["encryption_configuration"])  # API request

    if table.encryption_configuration.kms_key_name == new_kms_key_name:
        print("A table updated with encryption configuration key")

    # [END bigquery_update_table_cmek]
