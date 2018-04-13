#!/usr/bin/env python3
"""
nlp.py - Convert natural language into a structured query
"""

from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet

from app import db
from models import User, Product


def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)


def remove_noise(tokens):
    noise_list = {'I', 'would', 'like', 'price', 'kilogram'}
    tokens_without_noise = tokens
    for token in tokens:
        if token in stopwords.words('english') or token in noise_list:
            tokens_without_noise.remove(token)
    return tokens_without_noise


def synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms


def lexicon_normalization(tokens):
    normalised_tokens = []
    stem = PorterStemmer()
    lem = WordNetLemmatizer()
    for token in tokens:
        lemm = slem.lemmatize(token, pos_tag(token))
        stemm = self.stem.stem(word)
        if lemm == stemm:
            normalised_tokens.append(stemm)
        else:
            normalised_tokens.append(lemm)


def to_boolean(speech):
    for token in tokenize(speech):
        if token in synonyms('yes') or token in synonyms('agree'):
            return True
    for token in tokenize(speech) or token in synonyms('disagree'):
        if token == 'no':
            return False
    return None


def to_noun(speech):
    tokens = tokenize(speech)
    tokens = remove_noise(tokens)
    for tag in pos_tag(tokens):
        if tag[1] == 'NNP':
            return tag[0]
    for tag in pos_tag(tokens):
        if tag[1] == 'NN':
            return tag[0]
    for token in tokens:
        if token == 'bananas' or token == 'mangos':
            return token


def to_result(product):
    return str(product)


def to_assume(product):
    return 'the price of {} {} of {} in {} {}'.format(product.quantity, product.unit, product.name, product.location, product.currency)


def to_query(user_id, speech):
    user = User.query.get(user_id)

    product = Product()
    product.name = to_noun(speech)
    product.quantity = 1
    product.unit = Product.KG
    product.price = 200
    if user:
        if product.location == '' and user.location != '':
            product.location = user.location
        if product.currency == '' and user.currency != '':
            product.currency = user.currency
    # Mock existing data
    db.save(product)
    return product


if __name__ == '__main__':
    import doctest
    doctest.testmod()
