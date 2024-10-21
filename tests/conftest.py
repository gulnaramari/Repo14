import pytest
from src.main import Category, Product


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для "
        "удобства жизни",
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15",
                    "512GB, Gray space",
                    210000.0,
                    8),
            Product("Xiaomi Redmi Note 11",
                    "1024GB, Синий",
                    31000.0,
                    14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром,"
        " станет вашим другом и помощником",
        [Product('55" QLED 4K',
                 "Фоновая подсветка",
                 123000.0,
                 7)],
    )


@pytest.fixture
def first_category_null():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для "
        "удобства жизни",
        [],
    )