import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    def test_name(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        name = "Cheese"
        # Act - do the thing want to test
        returned=self.models.product(name)
        # Assert - did it do what you wanted?
        self.assertEqual("Cheese",returned)
        # Red - Green - Refactor - Commit