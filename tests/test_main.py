import tempfile
import os
from unittest.mock import patch
from src.main import main
import pytest


def test_main_successful_execution():
    """Тест успешного выполнения скрипта"""
    # Создаем временный файл
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write('name,brand,price,rating\n')
        f.write('iphone 15,apple,999,4.9\n')
        f.write('galaxy s23,samsung,899,4.8\n')
        temp_file = f.name

    try:
        test_args = ["main.py", "--files", temp_file, "--report", "average-rating"]
        with patch('sys.argv', test_args): # Подменяем sys.argv на наши аргументы
            result = main()
            assert result == 0

    finally:
        os.unlink(temp_file)


def test_main_missing_arguments():
    """Тест обработки отсутствующих аргументов"""
    # Когда отсутствуют обязательные аргументы, argparse вызывает SystemExit(2)
    test_args = ["main.py"]  # Нет --files и --report
    with patch('sys.argv', test_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code != 0


def test_main_file_not_found():
    """Тест обработки несуществующего файла"""
    test_args = ["main.py", "--files", "asdf.csv", "--report", "average-rating"]
    with patch('sys.argv', test_args):
        result = main()
        assert result != 0  # Должен вернуть код ошибки


def test_main_invalid_report_type():
    """Тест обработки неверного типа отчета"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write('name,brand,price,rating\n')
        f.write('iphone 15,apple,999,4.9\n')
        temp_file = f.name
    try:
        # Передаем неверный тип отчета
        test_args = ["main.py", "--files", temp_file, "--report", "invalid-report"]
        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code != 0

    finally:
        os.unlink(temp_file)


def test_main_invalid_csv_format():
    """Тест обработки CSV файла с неверным форматом"""
    # Создаем временный файл с неправильными колонками
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write('wrong,column,names\n')
        f.write('value1,value2,value3\n')
        temp_file = f.name

    try:
        test_args = ["main.py", "--files", temp_file, "--report", "average-rating"]
        with patch('sys.argv', test_args):
            result = main()
            assert result != 0  # Должен вернуть код ошибки

    finally:
        os.unlink(temp_file)
