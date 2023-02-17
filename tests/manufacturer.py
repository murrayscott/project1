import unittest
from models.manufacturer import Manufacturer

class TestSrc(unittest.TestCase):
    def test_name(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        name = "Mothers Pride"
        # Act - do the thing want to test
        returned=self.models.manufacturer(name)
        # Assert - did it do what you wanted?
        self.assertEqual("Mothers Pride",returned)
        # Red - Green - Refactor - Commit