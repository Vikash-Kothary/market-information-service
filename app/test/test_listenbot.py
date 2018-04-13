#!/usr/bin/env python3
"""
test_listenbot.py - Tests for listenbot.py
"""

from flask_testing import TestCase

from app import _create_app, _create_db, app
from listenbot import listenbot
from chatbot import chatbot
from models import User, Product


class TestListenbot(TestCase):

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

    def test_new_user(self):
        # Yes to on board
        speech = dict(SpeechResult='yes')
        response = self.client.post('/new_user', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/on_board</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # No to on board
        speech = dict(SpeechResult='no')
        response = self.client.post('/new_user', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Other
        response = self.client.post('/new_user')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/new_user" hints="boolean" input="speech" /><Redirect method="GET">/new_user</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/new_user')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_save_data(self):
        new_user = User.query.get('testing')
        self.assertEqual(new_user, None)

        # No to save data
        speech = dict(SpeechResult='no')
        response = self.client.post('/save_data', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/assumption</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Doesn't create user
        new_user = User.query.get('testing')
        self.assertEqual(new_user, None)

        # Yes to save data
        speech = dict(SpeechResult='yes')
        response = self.client.post('/save_data', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/name</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Creates user in database
        new_user = User.query.get('testing')
        self.assertEqual(new_user.user_id, 'testing')

        # Other
        response = self.client.post('/save_data')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/save_data" hints="boolean" input="speech" /><Redirect method="GET">/save_data</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/save_data')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        # User.query.filter_by(user_id='testing').delete()
        # self.db.save()

    def test_name(self):
        new_user = User(id='testing')
        self.db.save(new_user)
        self.assertEqual(new_user.name, '')

        # Yes to save data
        speech = dict(SpeechResult='vikash')
        response = self.client.post('/name', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Is your name vikash?</Say><Gather action="/confirm/name" hints="boolean" input="speech" /><Redirect method="GET">/confirm/name</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Saves user name
        new_user = User.query.get('testing')
        self.assertEqual(new_user.name, 'vikash')

        # Other
        response = self.client.post('/name')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/name" input="speech" /><Redirect method="GET">/name</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/name')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_location(self):
        new_user = User(id='testing', name='vikash')
        self.db.save(new_user)
        self.assertEqual(new_user.location, '')

        # Yes to save data
        speech = dict(SpeechResult='kenya')
        response = self.client.post('/location', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Are you from kenya?</Say><Gather action="/confirm/location" hints="boolean" input="speech" /><Redirect method="GET">/confirm/location</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Saves user location
        new_user = User.query.get('testing')
        self.assertEqual(new_user.location, 'kenya')

        response = self.client.get('/location')
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/location" input="speech" /><Redirect method="GET">/location</Redirect></Response>'
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        response = self.client.post('/location')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_currency(self):
        new_user = User('testing', 'vikash', 'kenya')
        self.db.save(new_user)
        self.assertEqual(new_user.currency, '')

        # Yes to save data
        speech = dict(SpeechResult='shilling')
        response = self.client.post('/currency', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">Is your currency shilling?</Say><Gather action="/confirm/currency" hints="boolean" input="speech" /><Redirect method="GET">/confirm/currency</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Saves user location
        new_user = User.query.get('testing')
        self.assertEqual(new_user.currency, 'shilling')

        response = self.client.get('/currency')
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/currency" input="speech" /><Redirect method="GET">/currency</Redirect></Response>'
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        response = self.client.post('/currency')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_confirm_name(self):
        new_user = User(id='testing', name='vikash')
        self.db.save(new_user)

        # Correct name
        speech = dict(SpeechResult='yes')
        response = self.client.post('/confirm/name', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/location</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is stored
        keeps_name = User.query.get(new_user.user_id)
        self.assertEqual(keeps_name.name, new_user.name)

        # Incorrect name
        speech = dict(SpeechResult='no')
        response = self.client.post('/confirm/name', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/name</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is deleted
        deletes_name = User.query.get(new_user.user_id)
        self.assertEqual(deletes_name.name, '')

        # Other
        response = self.client.post('/confirm/name')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/confirm/name" input="speech" /><Redirect method="GET">/confirm/name</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/confirm/name')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_confirm_location(self):
        new_user = User(id='testing', name='vikash', location='kenya')
        self.db.save(new_user)

        # Correct name
        speech = dict(SpeechResult='yes')
        response = self.client.post('/confirm/location', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/currency</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is stored
        keeps_name = User.query.get(new_user.user_id)
        self.assertEqual(keeps_name.location, new_user.location)

        # Incorrect name
        speech = dict(SpeechResult='no')
        response = self.client.post('/confirm/location', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/location</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is deleted
        deletes_name = User.query.get(new_user.user_id)
        self.assertEqual(deletes_name.location, '')

        # Other
        response = self.client.post('/confirm/location')
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/confirm/location" input="speech" /><Redirect method="GET">/confirm/location</Redirect></Response>'
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

        response = self.client.get('/confirm/location')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_confirm_currency(self):
        new_user = User(id='testing', name='vikash', location='kenya', currency='shilling')
        self.db.save(new_user)

        # Correct name
        speech = dict(SpeechResult='yes')
        response = self.client.post('/confirm/currency', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/assumption</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is stored
        keeps_name = User.query.get(new_user.user_id)
        self.assertEqual(keeps_name.currency, new_user.currency)

        # Incorrect name
        speech = dict(SpeechResult='no')
        response = self.client.post('/confirm/currency', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/learn/currency</Redirect></Response>'
        self.assertTrue(expected in response.data)
        # Name is deleted
        deletes_name = User.query.get(new_user.user_id)
        self.assertEqual(deletes_name.currency, '')

        response = self.client.post('/confirm/currency')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/confirm/currency" input="speech" /><Redirect method="GET">/confirm/currency</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/confirm/currency')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_query(self):
        known_user = User(id='testing', name='vikash', location='kenya', currency='shillings')
        result_product = Product(name='Mango', quantity=1,
                                 unit=Product.KG, price=200.00, location='Kenya', currency='GBP')
        self.db.save(known_user)
        self.db.save(result_product)

        # Product Id and Yes
        # speech = dict(SpeechResult='yes')
        # response = self.client.post('/query/{}'.format(result_product.product_id), data=speech)
        # self.assertEqual(response.status_code, 200)
        # expected = b'<Response><Redirect method="GET">/result/100</Redirect></Response>'
        # self.assertTrue(expected in response.data)

        # Product Id and No
        # speech = dict(SpeechResult='no')
        # response = self.client.post('/query/{}'.format(result_product.product_id), data=speech)
        # self.assertEqual(response.status_code, 200)
        # expected = b'<Response><Redirect method="GET">/assumption</Redirect></Response>'
        # self.assertTrue(expected in response.data)

        speech = dict(SpeechResult='How much does it cost for 1 kg of mango')
        response = self.client.post('/query', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b''
        print(response.data)
        self.assertTrue(expected in response.data)

        response = self.client.post('/query')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/query" input="speech" /><Redirect method="GET">/query</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/query')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)

    def test_done(self):
        # Wants another query
        speech = dict(SpeechResult='yes')
        response = self.client.post('/done', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/assumption</Redirect></Response>'
        self.assertTrue(expected in response.data)

        # Wants to end the call
        speech = dict(SpeechResult='no')
        response = self.client.post('/done', data=speech)
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Redirect method="GET">/end_call</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.post('/done')
        self.assertEqual(response.status_code, 200)
        expected = b'<Response><Say language="en" voice="alice">I don\'t understand. Can you say that again?</Say><Gather action="/done" input="speech" /><Redirect method="GET">/done</Redirect></Response>'
        self.assertTrue(expected in response.data)

        response = self.client.get('/done')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(expected in response.data)


if __name__ == '__main__':
    import unittest
    unittest.main()
