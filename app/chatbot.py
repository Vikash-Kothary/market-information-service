#!/usr/bin/env python3
"""
chatbot.py - Handles small talk with user
"""

import datetime
from flask import Blueprint, jsonify

from models import User, Product

chatbot = Blueprint("chatbot", __name__)


@chatbot.route('/greeting/')
@chatbot.route('/greeting/<user>')
def greeting(user=None):
    response = []
    if user is None:
        response.append('Welcome to the Market Information Service!')
        response.append(
            'Have you use this service before? If not, I can tell you a bit more out us.')
        # if self.speech.to_boolean() == True:
        #     self.on_board()
    else:
        response.append('This is the Market Information Service!')
        response.append('Welcome back {}!'.format(self.user.name))
        response.append('What can we help you with?')
    return jsonify(response)


@chatbot.route('/on_board')
def on_board(self):
    """ Explain service to new users """
    response = []
    response.append(
        'The Market Information Service provides price transparency to farmers all over Africa.')
    response.append('Ask us for the price of any produce and we can find it out for you.')
    response.append('We provide prices specific to your location and currency.')
    response.append('Is it ok if we store your data to improve your service with us.')
    # self.save_user = self.speech.to_boolean()
    response.append('Start by asking us the price of any produce.')
    return jsonify(response)


@chatbot.route('/end_call')
@chatbot.route('/end_call/<user>')
def end_call(user=None):
    """End call"""
    response = []
    response.append('Thank you for calling the Market Information Service!')
    if user is not None:
        response.append('Have a nice day, {}.'.format(user.name))
    else:
        response.append('Have a nice day.')
    return jsonify(response)


@chatbot.route('/learn/name/<user>')
def learn_name(user=None):
    response = []
    if user is None:
        response.append('What is your name?')
        # name_check = self.speech.to_name()
        # print('Is that {}'.format(name_check))
        # if self.speech.to_boolean() == True:
        #    user.name = name_check
    return jsonify(response)


@chatbot.route('/learn/location/<user>')
def learn_location(user):
    """ """
    response = []
    if user.location is not None:
        response.append('Is this price for {}'.format(self.user.location))
    else:
        response.append('What country are you in?')
        user.location = input()
    return jsonify(response)


@chatbot.route('/learn/currency/<user>')
def learn_currency(user):
    """ """
    response = []
    if user.currency_code is not None:
        response.append('Do you want the price in {}'.format(self.user.currency))
    else:
        response.append('What currency would you like the price in?')
        # user.currency_code = input()
    return jsonify(response)


@chatbot.route('/query/<user>')
def assumption(user):
    """ Predict query """
    response = []
    assume = 'the price of a banana'
    response.append('Would you like to know {}?'.format(assume))
    response.append('If not, then please state what you would like to query.')
    # if self.speech.to_boolean() == True:
    #    return 'I would like {}'.format(assume)
    # return None
    return jsonify(response)


@chatbot.route('/query/<query>')
@chatbot.route('/query/<query>/user/<user>/')
def service(query, user=None):
    """ Resolve query """
    response = []
    response.append('Let me find out the price of a {} for you'.format(query))
    # self.set_up_location_currency()
    # TODO: get price from database
    result = Product(id=0, name='Banana', quantity=5, unit='pcs', price=5.00,
                     currency='GBP', date=datetime.datetime.now())
    if user is not None:
        user.history.append(result)
    response.append(result.__str__)
    return jsonify(response)


def observations():
    """ Gather/Comment on known knowledge """
    pass

if __name__ == '__main__':
    pass
