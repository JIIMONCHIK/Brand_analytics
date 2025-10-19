from src.models import Product
from src.reports.average_rating_report import generate_average_rating_report


def test_generate_average_rating_report():
    products = [
        Product('iphone 15', 'apple', 999, 4.9),
        Product('iphone 14', 'apple', 799, 4.7),
        Product('galaxy s23', 'samsung', 899, 4.8),
        Product('galaxy s22', 'samsung', 699, 4.6),
    ]

    headers, report_data = generate_average_rating_report(products)

    # Проверяем заголовки
    assert headers == ['brand', 'rating']

    # Проверяем данные
    assert len(report_data) == 2

    # Проверяем расчет среднего рейтинга
    apple_rating = next(item for item in report_data if item.brand == 'apple')
    samsung_rating = next(item for item in report_data if item.brand == 'samsung')

    assert apple_rating.average_rating == 4.8
    assert samsung_rating.average_rating == 4.7

    # Проверяем сортировку (по убыванию рейтинга)
    assert report_data[0].brand == 'apple'
    assert report_data[1].brand == 'samsung'