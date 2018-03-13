#!/usr/bin/env python3
"""
test_models.py - Tests for models.py
"""

from models import Product, User

import unittest
import datetime


class TestModels(unittest.TestCase):

    def test_product_model(self):
        now = datetime.datetime.now()
        product_zero = Product(id=0, name='Banana', quantity=5,
                               unit='pcs', price=5.00, currency='GBP', date=now)
        self.assertIsInstance(product_zero, Product)

        self.assertEqual(product_zero.product_id, 0)
        self.assertEqual(product_zero.name, 'Banana')
        self.assertEqual(product_zero.quantity, 5)
        self.assertEqual(product_zero.unit, 'pcs')
        self.assertEqual(product_zero.price, 5.00)
        self.assertEqual(product_zero.currency_code, 'GBP')
        self.assertEqual(product_zero.date_created, now)

        expected_repr = '<Product(product_id=0, name=Banana, quantity=5, unit=pcs, price=5.00, currency_code=GBP, date_created=' + str(now) + ')>'
        self.assertEqual(product_zero.__repr__(), expected_repr)
        expected_str = '5 pcs of Banana costs 5.00 GBP on ' + str(now)
        self.assertEqual(product_zero.__str__(), expected_str)

    def test_user_model(self):
        user_zero = User(id=0, name='Vikash', location='UK', currency='GBP')
        self.assertIsInstance(user_zero, User)

        self.assertEqual(user_zero.user_id, 0)
        self.assertEqual(user_zero.name, 'Vikash')
        self.assertEqual(user_zero.location, 'UK')
        self.assertEqual(user_zero.currency_code, 'GBP')
        self.assertEqual(user_zero.history, [])

        expected_repr = '<User(user_id=0, name=Vikash, location=UK, currency_code=GBP, history=[])>'
        self.assertEqual(user_zero.__repr__(), expected_repr)
        expected_str = 'User Vikash from UK checks prices in GBP such as []'
        self.assertEqual(user_zero.__str__(), expected_str)

        user_one = User(id=1, name='Vikash', location='California', currency='USD', history=[])
        self.assertTrue(user_zero != user_one)


if __name__ == '__main__':
    unittest.main()
