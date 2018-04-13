#!/usr/bin/env python3
"""
test_models.py - Tests for models.py
"""

from models import Product, User

import unittest
import datetime


class TestModels(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_model(self):
        now = datetime.datetime.now()
        product_zero = Product(name='Banana', quantity=5,
                               unit=Product.BUNCH, price=5.00, location='UK', currency='GBP', date=now)
        self.assertIsInstance(product_zero, Product)

        self.assertEqual(product_zero.name, 'Banana')
        self.assertEqual(product_zero.quantity, 5)
        self.assertEqual(product_zero.unit, Product.BUNCH)
        self.assertEqual(product_zero.price, 5.00)
        self.assertEqual(product_zero.location, 'UK')
        self.assertEqual(product_zero.currency, 'GBP')
        self.assertEqual(product_zero.date_created, now)

        expected_repr = '<Product(name=Banana, quantity=5, unit=bunch, price=5.00, location=UK, currency=GBP, date_created=' + str(now) + ')>'
        self.assertEqual(product_zero.__repr__(), expected_repr)
        expected_str = '5 bunch of Banana costs 5.00 GBP in UK'
        self.assertEqual(product_zero.__str__(), expected_str)

    def test_user_model(self):
        user_zero = User(id=0, name='Vikash', location='UK', currency='GBP')
        self.assertIsInstance(user_zero, User)

        self.assertEqual(user_zero.user_id, 0)
        self.assertEqual(user_zero.name, 'Vikash')
        self.assertEqual(user_zero.location, 'UK')
        self.assertEqual(user_zero.currency, 'GBP')

        expected_repr = '<User(user_id=0, name=Vikash, location=UK, currency=GBP)>'
        self.assertEqual(user_zero.__repr__(), expected_repr)
        expected_str = 'User Vikash from UK checks prices in GBP'
        self.assertEqual(user_zero.__str__(), expected_str)

        user_one = User(id=1, name='Vikash', location='California', currency='USD')
        self.assertTrue(user_zero != user_one)

    def test_new_user(self):
        user_zero = User(id=0, name='Vikash', location='UK', currency='GBP')


if __name__ == '__main__':
    unittest.main()
