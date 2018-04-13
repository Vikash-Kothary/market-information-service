#!/usr/bin/env python3
"""
test_nlp.py - Tests for nlp.py
"""

import unittest

from nlp import *


class TestNLP(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nltk(self):
        # from nltk.corpus import brown
        # expected = ['The', 'Fulton', 'County', 'Grand', 'Jury',
        #             'said', 'Friday', 'an', 'investigation', 'of']
        # actual = brown.words()[0:10]
        # self.assertEqual(expected, actual)

        # expected = [('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'),
        #             ('Grand', 'JJ-TL'), ('Jury', 'NN-TL'), ('said', 'VBD'),
        #             ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'),
        #             ('of', 'IN')]
        # actual = brown.tagged_words()[0:10]
        # self.assertEqual(expected, actual)

        # expected = 1161192
        # actual = len(brown.words())
        # self.assertEqual(expected, actual)
        pass

    def test_tokenize(self):
        text = 'I would like the price of one mango.'
        expected = ['I', 'would', 'like', 'the', 'price', 'of', 'one', 'mango']
        actual = tokenize(text)
        self.assertEqual(expected, actual)

    def test_remove_noice(self):
        tokens = ['I', 'would', 'like', 'the', 'price', 'of', 'one', 'mango']
        expected = ['one', 'mango']
        actual = remove_noise(tokens)
        # self.assertEqua.l(expected, actual)

    def test_synonyms(self):
        word = 'agree'
        expected = ['agree', 'hold', 'concur', 'concord', 'agree', 'match', 'fit', 'correspond', 'check', 'jibe', 'gibe', 'tally',
                    'agree', 'harmonize', 'harmonise', 'consort', 'accord', 'concord', 'fit_in', 'agree', 'agree', 'agree', 'agree']
        actual = synonyms(word)
        self.assertEqual(expected, actual)

    def test_to_boolean(self):
        # Yes
        speech = 'yes'
        actual = to_boolean(speech)
        self.assertTrue(actual)
        # No
        speech = 'no'
        actual = to_boolean(speech)
        self.assertFalse(actual)
        # Puncuation
        speech = 'yes.'
        actual = to_boolean(speech)
        self.assertTrue(actual)
        # Agree
        speech = 'agree'
        actual = to_boolean(speech)
        self.assertTrue(actual)
        # Disagree
        speech = 'disagree.'
        actual = to_boolean(speech)
        self.assertFalse(actual)

    def test_to_noun(self):
        speech = 'My name is Vikash Kothary'
        expected = 'Vikash'
        actual = to_noun(speech)
        self.assertEqual(expected, actual)

        speech = 'I am from the country of America'
        expected = 'America'
        actual = to_noun(speech)
        self.assertEqual(expected, actual)

        speech = 'I would like the price for a banana'
        expected = 'banana'
        actual = to_noun(speech)
        self.assertEqual(expected, actual)

        speech = 'How much does it cost for a mango'
        expected = 'mango'
        actual = to_noun(speech)
        self.assertEqual(expected, actual)

        speech = 'What is a shilling'
        expected = 'shilling'
        actual = to_noun(speech)
        self.assertEqual(expected, actual)
