import pytest
import tempfile
import os
from src.file_reader import read_csv_files


def test_read_csv_files():
    files = []
    try:
        # Создаем первый временный файл
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,brand,price,rating\n')
            f.write('iphone 15,apple,999,4.9\n')
            files.append(f.name)

        # Создаем второй временный файл
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('name,brand,price,rating\n')
            f.write('galaxy s23,samsung,899,4.8\n')
            files.append(f.name)

        products = read_csv_files(files)
        assert len(products) == 2
        assert products[0].brand == 'apple'
        assert products[1].brand == 'samsung'

    finally:
        for file in files:
            os.unlink(file)


def test_read_csv_files_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent_file.csv'])