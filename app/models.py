#!/usr/bin/env python3
"""
models.py - Defines models to represent data
"""

import datetime

from app import db


history_table = db.Table('history',
                         db.Column('product_id', db.Integer, db.ForeignKey(
                             'product_table.product_id')),
                         db.Column('user_id', db.String, db.ForeignKey('user_table.user_id'))
                         )


class Product(db.Model):
    __tablename__ = 'product_table'

    KG = 'kilogram'
    BUNCH = 'bunch'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.Enum(KG, BUNCH, name='product_unit'))
    price = db.Column(db.Integer)
    location = db.Column(db.String)
    currency = db.Column(db.String)
    date_created = db.Column(db.DateTime)

    def __init__(self, name='', quantity=0, unit=KG, price=0, location='', currency='', date=None):
        """Stores product prices"""
        if date is None:
            date = datetime.datetime.now()
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price = price
        self.location = location
        self.currency = currency
        self.date_created = date

    def __repr__(self):
        """Return an unambiguous representation of a product"""
        return '<Product(name={}, quantity={}, unit={}, price={:.2f}, location={}, currency={}, date_created={})>'.format(
            self.name, self.quantity, self.unit, self.price, self.location, self.currency, self.date_created)

    def __str__(self):
        """Returns a human-readable representation of a product"""
        return '{} {} of {} costs {:.2f} {} in {}'.format(
            self.quantity, self.unit, self.name, self.price, self.currency, self.location)


class User(db.Model):
    __tablename__ = 'user_table'

    user_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    currency = db.Column(db.String)
    history = db.relationship("Product",
                              secondary=history_table,
                              backref=db.backref('products'))

    def __init__(self, id='', name='', location='', currency=''):
        """Stores user details and history"""
        self.user_id = id
        self.name = name
        self.location = location
        self.currency = currency

    def __repr__(self):
        """Return an unambiguous representation of a user"""
        return '<User(user_id={0}, name={1}, location={2}, currency={3})>'.format(
            self.user_id, self.name, self.location, self.currency)

    def __str__(self):
        """Returns a human-readable representation of a product"""
        return 'User {0} from {1} checks prices in {2}'.format(
            self.name, self.location, self.currency)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
