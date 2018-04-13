#!/usr/bin/env python3
"""
chatbot.py - Handles small talk with user
"""

import datetime
from flask import Blueprint, json, jsonify, session
from nltk.chat.util import Chat, reflections

from app import db
from models import User, Product
from phone import PhoneInterface
from nlp import to_result, to_query, to_assume

chatbot = Blueprint("chatbot", __name__)


@chatbot.route('/greeting', methods=['GET', 'POST'])
def greeting():
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    if user:
        if user.name:
            response.speak('This is the Market Information Service!')
            response.speak('Welcome back {}!'.format(user.name))
            response.speak('What can we help you with?')
            response.next('chatbot.assumption')
    else:
        response.speak('Welcome to the Market Information Service!')
        response.speak(
            'Have you use this service before? If not, I can tell you a bit more out us.')
        response.speak(
            'Say yes if you would like to learn how to use this service.')
        response.listen('listenbot.new_user', 'yes, no')
    return str(response)


@chatbot.route('/on_board', methods=['GET', 'POST'])
def on_board():
    """ Explain service to new users """
    response = PhoneInterface()
    response.speak(
        'The Market Information Service provides price transparency to farmers all over Africa.')
    response.speak('Ask us for the price of any produce and we can find it out for you.')
    response.speak('We provide prices specific to your location and currency.')
    response.listen('chatbot.learn')
    return str(response)


@chatbot.route('/learn', methods=['GET', 'POST'])
def learn():
    """ Explain service to new users """
    response = PhoneInterface()
    response.speak('Is it ok if we store your data to improve your service with us.')
    response.speak('Say yes to allow us to remember your data.')
    response.listen('listenbot.save_data', 'yes, no')
    return str(response)


@chatbot.route('/learn/name', methods=['GET', 'POST'])
def learn_name():
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    if user is None or user.name == '':
        response.speak('What is your name?')
        response.listen('listenbot.name', 'Vikash, Jamie')
    else:
        response.speak('Is this {}?'.format(user.name))
        response.listen('listenbot.confirm_name', 'yes, no')
    return str(response)


@chatbot.route('/learn/location', methods=['GET', 'POST'])
def learn_location():
    """ """
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    if user is None or user.location == '':
        response.speak('What country are you in?')
        response.listen('listenbot.location', 'Kenya')
    else:
        response.speak('Is this price for {}?'.format(user.location))
        response.listen('listenbot.confirm_location', 'yes, no')
    return str(response)


@chatbot.route('/learn/currency', methods=['GET', 'POST'])
def learn_currency():
    """ """
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    if user is None or user.currency == '':
        response.speak('What currency would you like the price in?')
        response.listen('listenbot.currency', 'Shillings')
    else:
        response.speak('Do you want the price in {}?'.format(user.currency))
        response.listen('listenbot.confirm_location', 'yes, no')
    return str(response)


@chatbot.route('/assumption', methods=['GET', 'POST'])
def assumption():
    """ Predict query """
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    predict_product = None
    if user is not None:
        user = User.query.get(response.get_user_id())
        predict_product = Product.query.filter(User.history.any()).first()
    if predict_product is not None:
        response.speak('Do you want to find out {}?'.format(to_assume(predict_product)))
        response.speak('If not, then please state what you would like to query.')
        response.listen('listenbot.query', 'yes, no')
    else:
        response.speak('What would you like to find out the price for?')
        response.listen('listenbot.query', 'What, price, banana, kenya, shillings')
    return str(response)


@chatbot.route('/result/<product_id>', methods=['GET', 'POST'])
def result(product_id):
    """ Speak query result"""
    response = PhoneInterface()
    result = Product.query.get(product_id)
    response.speak(to_result(result))
    response.speak('Is there anything else we can help you with?')
    response.listen('listenbot.done', 'yes, no')
    return str(response)


@chatbot.route('/end_call', methods=['GET', 'POST'])
def end_call():
    """End call"""
    response = PhoneInterface()
    user = User.query.get(response.get_user_id())
    response.speak('Thank you for calling the Market Information Service!')
    if user is None or user.name == '':
        response.speak('Have a nice day.')
    else:
        response.speak('Have a nice day, {}.'.format(user.name))
    response.end_call()
    return str(response)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
