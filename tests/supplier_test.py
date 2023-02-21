import unittest
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.supplier=Supplier(1,2,False)

    def test_product_id(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        # Set up completed above for all tests
        # Act - do the thing want to test
        returned=self.supplier.product
        # Assert - did it do what you wanted?
        self.assertEqual(1,returned)
        # Red - Green - Refactor - Commit

    def test_manufacturer_id(self):
        returned=self.supplier.manufacturer
        self.assertEqual(2,returned)

    def test_manufacturer_id(self):
        returned=self.supplier.deleted
        self.assertEqual(False,returned)
