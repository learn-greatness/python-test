import unittest
from src.inventory import find_available_products


class TestInventory(unittest.TestCase):
    def test_filters_by_category_and_stock(self):
        products = [
            {"id": 1, "name": "Ring", "category": "Rings", "stock": 5, "discontinued": False},
            {"id": 2, "name": "Necklace", "category": "Necklaces", "stock": 10, "discontinued": False},
            {"id": 3, "name": "Bracelet", "category": "Rings", "stock": 0, "discontinued": False},
        ]

        result = find_available_products(products, "Rings", 2)

        self.assertEqual([p["id"] for p in result], [1])

    def test_category_is_case_insensitive(self):
        products = [
            {"id": 1, "name": "Ring", "category": "Rings", "stock": 5, "discontinued": False}
        ]

        result = find_available_products(products, "rings", 1)

        self.assertEqual([p["id"] for p in result], [1])


if __name__ == "__main__":
    unittest.main()
