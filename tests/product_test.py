import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Nutella","Hazelnut chocolate spread", "80177173", "Condiments", 23, 10, 12, 1.78, 2.99, False)

    def test_name(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        # Set up completed above for all tests
        # Act - do the thing want to test
        returned=self.product.name
        # Assert - did it do what you wanted?
        self.assertEqual("Nutella",returned)
        # Red - Green - Refactor - Commit

    def test_description(self):
        returned=self.product.description
        self.assertEqual("Hazelnut chocolate spread",returned)

    def test_part_number(self):
        returned=self.product.part_number
        self.assertEqual("80177173",returned)

    def test_category(self):
        returned=self.product.category
        self.assertEqual("Condiments",returned)

    def test_stock_qty(self):
        returned=self.product.stock_qty
        self.assertEqual(23,returned)

    def test_reorder_level(self):
        returned=self.product.reorder_level
        self.assertEqual(10,returned)

    def test_unit_multiple(self):
        returned=self.product.unit_multiple
        self.assertEqual(12,returned)

    def test_cost(self):
        returned=self.product.cost
        self.assertEqual(1.78,returned)

    def test_selling_price(self):
        returned=self.product.selling_price
        self.assertEqual(2.99,returned)

    def test_deleted(self):
        returned=self.product.deleted
        self.assertEqual(False,returned)