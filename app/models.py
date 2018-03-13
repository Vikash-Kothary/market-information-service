#!/usr/bin/env python3
"""
models.py - Defines models to represent data
"""

import datetime


class Product():

    def __init__(self, id=None, name=None, quantity=None, unit=None, price=None, currency=None, date=None):
        """Stores product prices"""
        if date is None:
            date = datetime.datetime.now()
        self.product_id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price = price
        self.currency_code = currency
        self.date_created = date

    def __repr__(self):
        """Return an unambiguous representation of a product"""
        return '<Product(product_id={0}, name={1}, quantity={2}, unit={3}, price={4:.2f}, currency_code={5}, date_created={6})>'.format(
            self.product_id, self.name, self.quantity, self.unit, self.price, self.currency_code, self.date_created)

    def __str__(self):
        """Returns a human-readable representation of a product"""
        return '{0} {1} of {2} costs {3:.2f} {4} on {5}'.format(
            self.quantity, self.unit, self.name, self.price, self.currency_code, self.date_created)


class User():

    def __init__(self, id=None, name=None, location=None, currency=None, history=None):
        """Stores user details and history"""
        if history is None:
            history = []
        self.user_id = id
        self.name = name
        self.location = location
        self.currency_code = currency
        self.history = history

    def __repr__(self):
        """Return an unambiguous representation of a user"""
        return '<User(user_id={0}, name={1}, location={2}, currency_code={3}, history={4})>'.format(
            self.user_id, self.name, self.location, self.currency_code, self.history)

    def __str__(self):
        """Returns a human-readable representation of a product"""
        return 'User {0} from {1} checks prices in {2} such as {3}'.format(
            self.name, self.location, self.currency_code, self.history)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
