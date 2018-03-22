#!/usr/bin/env python3
"""
nlp.py - Convert natural language into a structured query
"""


class NLP():
    """Convert natural language into a structured query"""

    def __init__(self):
        pass

    def to_boolean(self, sentence=None):
        if sentence is None:
            sentence = input()
        if sentence == 'y':
            return True
        else:
            return False

if __name__ == '__main__':
    pass
