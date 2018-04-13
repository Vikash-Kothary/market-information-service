#!/usr/bin/env python3
"""
test_app.py - Tests for nlp.py
"""

from flask_testing import TestCase

from app import _create_app, _create_db, app
from chatbot import chatbot
from listenbot import listenbot
from models import User, Product


class TestChatbot(TestCase):

    def create_app(self):
        #app = _create_app(environment='testing')
        app.register_blueprint(listenbot)
        app.register_blueprint(chatbot)
        return app

    def setUp(self):
        self.app = self.create_app()
        with self.app.app_context():
            self.db = _create_db(self.app)
        self.client = self.app.test_client()
        self.client.testing = True
        with self.client.session_transaction() as sess:
            sess['user_id'] = 'testing'

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            testing_user = self.db.session.query(User).filter(User.user_id == 'testing')
            if testing_user:
                testing_user.delete()
            self.db.session.commit()
            self.db.drop_all()

    def test_greeting(self):
        # New user
        response = self.client.post('/greeting')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Welcome to the Market Information Service!</Say><Say language="en" voice="alice">Have you use this service before? If not, I can tell you a bit more out us.</Say><Say language="en" voice="alice">Say yes if you would like to learn how to use this service.</Say><Gather action="/new_user" hints="yes, no" input="speech" /><Redirect method="GET">/new_user</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shilling')
        self.db.save(known_user)

        response = self.client.get('/greeting')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">This is the Market Information Service!</Say><Say language="en" voice="alice">Welcome back vikash!</Say><Say language="en" voice="alice">What can we help you with?</Say><Redirect method="GET">/assumption</Redirect></Response>'
        self.assertTrue(expected in response.data)

    def test_on_board(self):
        # New user
        response = self.client.post('/on_board')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">The Market Information Service provides price transparency to farmers all over Africa.</Say><Say language="en" voice="alice">Ask us for the price of any produce and we can find it out for you.</Say><Say language="en" voice="alice">We provide prices specific to your location and currency.</Say><Gather action="/learn" input="speech" /><Redirect method="GET">/learn</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/on_board')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Same if known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shilling')
        self.db.save(known_user)

        response = self.client.get('/on_board')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_learn(self):
        # New user
        response = self.client.post('/learn')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Is it ok if we store your data to improve your service with us.</Say><Say language="en" voice="alice">Say yes to allow us to remember your data.</Say><Gather action="/save_data" hints="yes, no" input="speech" /><Redirect method="GET">/save_data</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/learn')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Same if known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shilling')
        self.db.save(known_user)

        response = self.client.get('/learn')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_learn_name(self):
        # New user
        response = self.client.post('/learn/name')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">What is your name?</Say><Gather action="/name" hints="Vikash, Jamie" input="speech" /><Redirect method="GET">/name</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/learn/name')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        self.db.save(known_user)

        response = self.client.get('/learn/name')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Is this vikash?</Say><Gather action="/confirm/name" hints="yes, no" input="speech" /><Redirect method="GET">/confirm/name</Redirect></Response>'
        self.assertTrue(expected in response.data)

    def test_learn_location(self):
        # New user
        response = self.client.post('/learn/location')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">What country are you in?</Say><Gather action="/location" hints="Kenya" input="speech" /><Redirect method="GET">/location</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/learn/location')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        self.db.save(known_user)

        response = self.client.get('/learn/location')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Is this price for kenya?</Say><Gather action="/confirm/location" hints="yes, no" input="speech" /><Redirect method="GET">/confirm/location</Redirect></Response>'
        self.assertTrue(expected in response.data)

    def test_learn_currency(self):
        # New user
        response = self.client.post('/learn/currency')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">What currency would you like the price in?</Say><Gather action="/currency" hints="Shillings" input="speech" /><Redirect method="GET">/currency</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/learn/currency')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        self.db.save(known_user)

        response = self.client.get('/learn/currency')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Do you want the price in shillings?</Say><Gather action="/confirm/location" hints="yes, no" input="speech" /><Redirect method="GET">/confirm/location</Redirect></Response>'
        self.assertTrue(expected in response.data)

    def test_assumption(self):
        # New user
        response = self.client.post('/assumption')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">What would you like to find out the price for?</Say><Gather action="/query" hints="What, price, banana, kenya, shillings" input="speech" /><Redirect method="GET">/query</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/assumption')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        old_product = Product(name='Banana', quantity=5,
                              unit=Product.BUNCH, price=5.00, location='Kenya', currency='GBP')
        known_user.history.append(old_product)
        self.db.save(known_user)

        response = self.client.get('/assumption')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Do you want to find out the price of 5 bunch of Banana in Kenya GBP?</Say><Say language="en" voice="alice">If not, then please state what you would like to query.</Say><Gather action="/query" hints="yes, no" input="speech" /><Redirect method="GET">/query</Redirect></Response>'
        self.assertTrue(expected in response.data)

    def test_result(self):
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        result_product = Product(name='Mango', quantity=1,
                                 unit=Product.KG, price=200.00, location='Kenya', currency='GBP')
        self.db.save(known_user)
        self.db.save(result_product)

        response = self.client.post('/result/{}'.format(result_product.product_id))
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">1 kilogram of Mango costs 200.00 GBP in Kenya</Say><Say language="en" voice="alice">Is there anything else we can help you with?</Say><Gather action="/done" hints="yes, no" input="speech" /><Redirect method="GET">/done</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/result/{}'.format(result_product.product_id))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_end_call(self):
        # New user
        response = self.client.post('/end_call')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Thank you for calling the Market Information Service!</Say><Say language="en" voice="alice">Have a nice day.</Say><Hangup /></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/end_call')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # Known user
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        self.db.save(known_user)

        response = self.client.get('/end_call')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Thank you for calling the Market Information Service!</Say><Say language="en" voice="alice">Have a nice day, vikash.</Say><Hangup /></Response>'
        self.assertTrue(expected in response.data)


if __name__ == '__main__':
    import unittest
    unittest.main()
