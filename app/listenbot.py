#!/usr/bin/env python3
"""
listenbot.py - Convert natural language into data
"""

from flask import Blueprint, request, session, url_for

from app import db
from models import User, Product
from phone import PhoneInterface
from nlp import to_boolean, to_noun, to_query

listenbot = Blueprint("listenbot", __name__)


@listenbot.route('/new_user', methods=['GET', 'POST'])
def new_user():
    """ """
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_boolean(text['SpeechResult'])
        if result == True:
            response.next('chatbot.on_board')
        else:
            response.next('chatbot.learn')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.new_user', 'boolean')
    return str(response)


@listenbot.route('/save_data', methods=['GET', 'POST'])
def save_data():
    """ """
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_boolean(text['SpeechResult'])
        if result == True:
            new_user = User()
            new_user.user_id = response.get_user_id()
            db.save(new_user)
            response.next('chatbot.learn_name')
        else:
            response.next('chatbot.assumption')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.save_data', 'boolean')
    return str(response)


@listenbot.route('/name', methods=['GET', 'POST'])
def name():
    """ """
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_noun(text['SpeechResult'])
        response.speak('Is your name {}?'.format(result))
        new_user = User.query.get(response.get_user_id())
        new_user.name = result
        db.save()
        response.listen('listenbot.confirm_name', 'boolean')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.name')
    return str(response)


@listenbot.route('/location', methods=['GET', 'POST'])
def location():
    """ """
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_noun(text['SpeechResult'])
        response.speak('Are you from {}?'.format(result))
        new_user = User.query.get(response.get_user_id())
        new_user.location = result
        db.save()
        response.listen('listenbot.confirm_location', 'boolean')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.location')
    return str(response)


@listenbot.route('/currency', methods=['GET', 'POST'])
def currency():
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_noun(text['SpeechResult'])
        response.speak('Is your currency {}?'.format(result))
        new_user = User.query.get(response.get_user_id())
        new_user.currency = result
        db.save()
        response.listen('listenbot.confirm_currency', 'boolean')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.currency')
    return str(response)


def confirmed():
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_boolean(text['SpeechResult'])
        if result == True:
            if 'name' in request.path:
                response.next('chatbot.learn_location')
            if 'location' in request.path:
                response.next('chatbot.learn_currency')
            if 'currency' in request.path:
                response.next('chatbot.assumption')
        else:
            user = User.query.get(session['user_id'])
            if 'name' in request.path:
                response.next('chatbot.learn_name')
                user.name = ''
                db.save()
            if 'location' in request.path:
                response.next('chatbot.learn_location')
                user.location = ''
                db.save()
            if 'currency' in request.path:
                response.next('chatbot.learn_currency')
                user.currency = ''
                db.save()
    else:
        response.speak("I don't understand. Can you say that again?")
        if 'name' in request.path:
            response.listen('listenbot.confirm_name')
        if 'location' in request.path:
            response.listen('listenbot.confirm_location')
        if 'currency' in request.path:
            response.listen('listenbot.confirm_currency')
    return str(response)


@listenbot.route('/confirm/name', methods=['GET', 'POST'])
def confirm_name():
    return confirmed()


@listenbot.route('/confirm/location', methods=['GET', 'POST'])
def confirm_location():
    return confirmed()


@listenbot.route('/confirm/currency', methods=['GET', 'POST'])
def confirm_currency():
    return confirmed()


@listenbot.route('/query', methods=['GET', 'POST'])
@listenbot.route('/query/<product_id>', methods=['GET', 'POST'])
def query(product_id=None):
    response = PhoneInterface()
    text = request.form
    if text:
        if product_id:
            result = to_boolean(text['SpeechResult'])
            if result:
                product = Product.query.get(product_id)
                response.redirect(url=url_for('chatbot.result',
                                              product_id=product_id), method='GET')
            else:
                response.next('chatbot.assumption')
        else:
            query = to_query(response.get_user_id(), text['SpeechResult'])
            # result = Product.query.filter(name=query.name, quantity=query.quantity,
            # unit=query.unit, location=query.location, currency=query.currency)
            response.redirect(url=url_for('chatbot.result',
                                          product_id=query.product_id), method='GET')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.query')
    return str(response)


@listenbot.route('/done', methods=['GET', 'POST'])
def done():
    response = PhoneInterface()
    text = request.form
    if text:
        result = to_boolean(text['SpeechResult'])
        if result == True:
            response.next('chatbot.assumption')
        else:
            response.next('chatbot.end_call')
    else:
        response.speak("I don't understand. Can you say that again?")
        response.listen('listenbot.done')
    return str(response)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
