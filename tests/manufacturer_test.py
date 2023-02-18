import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Allied Bakeries","180 Glentanar Rd, Glasgow. G22 7XS", "Barry Brownbread", "0141 347 4222", "sales@alliedbakeries.co.uk", "www.alliedbakeries.co.uk", False)

    def test_name(self):
        # ------------  AAA  ---------------
        # Arrange - setup specific to this test
        # Set up completed above for all tests
        # Act - do the thing want to test
        returned=self.manufacturer.name
        # Assert - did it do what you wanted?
        self.assertEqual("Allied Bakeries",returned)
        # Red - Green - Refactor - Commit

    def test_address(self):
        returned=self.manufacturer.address
        self.assertEqual("180 Glentanar Rd, Glasgow. G22 7XS",returned)

    def test_contact(self):
        returned=self.manufacturer.contact
        self.assertEqual("Barry Brownbread",returned)

    def test_telephone(self):
        returned=self.manufacturer.telephone
        self.assertEqual("0141 347 4222",returned)

    def test_email(self):
        returned=self.manufacturer.email
        self.assertEqual("sales@alliedbakeries.co.uk",returned)

    def test_website(self):
        returned=self.manufacturer.website
        self.assertEqual("www.alliedbakeries.co.uk",returned)

    def test_deleted(self):
        returned=self.manufacturer.deleted
        self.assertEqual(False ,returned)