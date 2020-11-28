# base/category.py
import random

from enum import Enum
from fuzzywuzzy import fuzz


class MatchType(Enum):
    PARTIAL = 0  # Recommended for longer phrases
    FULL = 1  # Recommended for individual words and shorter phrases


class Category:

    FUZZ_RATIO = 85

    def __init__(self, category_name):
        self.category_name = category_name
        self.match_type = MatchType.PARTIAL
        self.phrase_list = []
        self.response_list = []

    def set_match_type(self, phrase_type):
        self.match_type = phrase_type

    def add_phrases(self, phrase_list):
        self.phrase_list += phrase_list

    def add_responses(self, response_list):
        self.response_list += response_list

    def choose_response(self):
        if not self.response_list:
            return ''

        return random.choice(self.response_list)

    def has_match(self, message_text):
        for phrase in self.phrase_list:
            if self.match_type is MatchType.PARTIAL:
                return self.__phrase_match(phrase, message_text)
            if self.match_type is MatchType.FULL:
                return self.__full_match(phrase, message_text)

    def __phrase_match(self, phrase, message_text):
        if fuzz.partial_ratio(message_text.lower(), phrase.lower()) >= self.FUZZ_RATIO:
            print('Matched "' + phrase + '" in category ' + self.category_name)
            return True
        return False

    def __full_match(self, phrase, message_text):
        for word in message_text.split(' '):
            if fuzz.ratio(word.lower(), phrase.lower()) >= self.FUZZ_RATIO:
                print('Matched "' + phrase + '" in category ' + self.category_name)
                return True
        return False
