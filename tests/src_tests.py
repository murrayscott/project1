import unittest
from src.src import function_name

class TestSrc(unittest.TestCase):
    def test_description(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        # None
        # Act - do the thing want to test
        self.src.function(value)
        # Assert - did it do what you wanted?
        self.assertEqual(expected_value,actual_function_value)
        # Red - Green - Refactor - Commit