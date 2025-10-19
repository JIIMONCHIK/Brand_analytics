import csv
from typing import List
from .models import Product


def read_csv_files(files: List[str]) -> List[Product]:
    products = []
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(
                        name=row['name'],
                        brand=row['brand'],
                        price=float(row['price']),
                        rating=float(row['rating'])
                    )
                    products.append(product)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        except KeyError:
            raise ValueError(f"Некорректный файл: {file_path}")
        except ValueError as e:
            raise ValueError(f"Ошибка преобразования данных в файле {file_path}: {e}")
    return products