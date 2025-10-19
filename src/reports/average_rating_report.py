from typing import List, Tuple
from ..models import Product, BrandRating


def generate_average_rating_report(products: List[Product]) -> Tuple[List[str], List[BrandRating]]:
    brand_ratings = dict()

    for product in products:
        if product.brand not in brand_ratings:
            brand_ratings[product.brand] = []
        brand_ratings[product.brand].append(product.rating)

    report_data = []
    for brand, ratings in brand_ratings.items():
        average_rating = sum(ratings) / len(ratings) # Средний рейтинг для каждого бренда
        report_data.append(BrandRating(brand=brand, average_rating=round(average_rating, 2)))

    report_data.sort(key=lambda x: x.average_rating, reverse=True)

    headers = ["brand", "rating"]
    return headers, report_data