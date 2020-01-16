import os

from .. import load_table_relax_column


def test_load_table_relax_column(capsys, random_table_id):

    samples_test_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(
        samples_test_dir, "..", "..", "tests", "data", "people.csv"
    )
    table = load_table_relax_column.load_table_relax_column(file_path, random_table_id)
    out, _ = capsys.readouterr()
    assert "3 fields in the schema are required." in out
    assert "Loaded 2 rows into {}:{}.".format(table.dataset_id, table.table_id) in out
    assert "2 fields in the schema are now required." in out

    assert len(table.schema) == 3
    assert table.schema[2].mode == "NULLABLE"
    assert table.num_rows > 0
