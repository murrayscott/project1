import unittest
from models.supplier import Supplier

class TestSrc(unittest.TestCase):
    def test_name(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        id = 1
        # Act - do the thing want to test
        returned=self.models.supplier(id)
        # Assert - did it do what you wanted?
        self.assertEqual(1,returned)
        # Red - Green - Refactor - Commit