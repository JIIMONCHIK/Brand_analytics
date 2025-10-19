from dataclasses import dataclass


@dataclass
class Product:
    name: str
    brand: str
    price: float
    rating: float


@dataclass
class BrandRating:
    brand: str
    average_rating: float