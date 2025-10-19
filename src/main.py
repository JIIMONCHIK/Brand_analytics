import argparse
from tabulate import tabulate
from .file_reader import read_csv_files
from .reports.average_rating_report import generate_average_rating_report


def setup_argparse() -> argparse.ArgumentParser:
    choices = ['average-rating']
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов',
                                     epilog=f'Доступные типы отчетов: {', '.join(choices)}')
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV файлам с данными о продуктах'
    )
    parser.add_argument(
        '--report',
        choices=choices, # Типы отчетов
        required=True,
        help='Тип отчета для генерации'
    )
    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    try:
        products = read_csv_files(args.files)

        # Генерация отчета в зависимости от выбранного типа
        if args.report == 'average-rating':
            headers, report_data = generate_average_rating_report(products)

            table_data = [
                [i + 1, item.brand, item.average_rating]
                for i, item in enumerate(report_data)
            ]
            table_headers = ["", "brand", "rating"]
            print(tabulate(table_data, headers=table_headers, tablefmt='grid'))
    except Exception as e:
        print(f"Ошибка: {e}")
        return 1
    return 0


if __name__ == '__main__':
    exit(main())