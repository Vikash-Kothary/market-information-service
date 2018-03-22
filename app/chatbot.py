#!/usr/bin/env python3
"""
chatbot.py - Handles small talk with user
"""

from models import User, Product
from nlp import NLP


class Chatbot():
    """Generate reponses to user inputs"""

    def __init__(self, user=None):
        if user is None:
            user = User()
        self.user = user
        self.speech = NLP()
        self.run()

    def run(self):
        self.greeting()
        while True:
            self.observations()
            query = self.assumptions()
            self.service(query)

    def greeting(self):
        if self.user.name is None:
            print('Welcome to the Market Information Service!')
            print('Have you use this service before? If not, I can tell you a bit more out us.')
            if self.speech.to_boolean() == True:
                self.on_board()
        else:
            print('This is the Market Information Service!')
            print('Welcome back {}!'.format(self.user.name))
            print('What can we help you with?')

    def on_board(self):
        """ Explain service to new users """
        print('The Market Information Service provides price transparency to farmers all over Africa.')
        print('Ask us for the price of any produce and we can find it out for you.')
        print('We provide prices specific to your location and currency.')
        print('Is it ok if we store your data to improve your service with us.')
        self.save_user = self.speech.to_boolean()
        print('Start by asking us the price of any produce.')

    def set_up_name(self):
        if self.user.name is None:
            print('What is your name?')
            name_check = self.speech.to_name()
            print('Is that {}'.format(name_check))
            if self.speech.to_boolean() == True:
                self.user.name = name_check

    def set_up_location_currency(self):
        if self.user.location is not None:
            print('Is this price for {}'.format(self.user.location))
        else:
            print('What country are you in?')
            self.user.location = input()
        if self.user.currency_code is not None:
            print('Do you want the price in {}'.format(self.user.currency))
        else:
            print('What currency would you like the price in?')
            self.user.currency_code = input()

    def observations(self):
        """ Gather/Comment on known knowledge """
        pass

    def assumptions(self):
        """ Predict query """
        assume = 'the price of a banana'
        print('Would you like to know {}?'.format(assume))
        print('If not, then please state what you would like to query.')
        if self.speech.to_boolean() == True:
            return 'I would like {}'.format(assume)
        return None

    def service(self, query):
        print('Let me find out the price of a banana for you')
        self.set_up_location_currency()
        # TODO: get price from database
        import datetime
        result = Product(id=0, name='Banana', quantity=5,
                         unit='pcs', price=5.00, currency='GBP', date=datetime.datetime.now())
        self.user.history.append(result)
        print(self.user.history)

if __name__ == '__main__':
    bot = Chatbot()
