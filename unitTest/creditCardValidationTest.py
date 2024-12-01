import unittest
from creditcardvalidation import *

class CreditCardValidationTest(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test_validationCard_valid(self):
        result = validateCard(date(2020,2,2))
        self.assertEqual('Valid',result)

    def test_validation_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2020,2,2))

    def tearDown(self):
        print('teardown')

if __name__ == '__main__':
    unittest.main()