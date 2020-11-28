# base/category.py
import random

from enum import IntEnum
from fuzzywuzzy import fuzz


class MatchType(IntEnum):
    PARTIAL = 0  # Recommended for longer phrases
    FULL = 1  # Recommended for individual words and shorter phrases


class MatchPriority(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Category:

    FUZZ_RATIO = 85

    def __init__(self, category_name, match_type, match_priority):
        self.category_name = category_name
        self.match_type = match_type
        self.match_priority = match_priority
        self.phrase_list = []
        self.response_list = []

    def add_phrases(self, phrase_list):
        self.phrase_list += phrase_list

    def add_responses(self, response_list):
        self.response_list += response_list

    def get_name(self):
        return self.get_name()

    def choose_response(self):
        if not self.response_list:
            return ''

        return random.choice(self.response_list)

    def has_match(self, message_text):
        for phrase in self.phrase_list:
            if self.match_type is MatchType.PARTIAL:
                if self.__phrase_match(phrase, message_text):
                    print('Matched "' + phrase + '" in category ' + self.category_name)
                    return True
            if self.match_type is MatchType.FULL:
                if self.__phrase_match(phrase, message_text):
                    print('Matched "' + phrase + '" in category ' + self.category_name)
                    return True
        return False

    def __phrase_match(self, phrase, message_text):
        return fuzz.partial_ratio(message_text.lower(), phrase.lower()) >= self.FUZZ_RATIO

    def __full_match(self, phrase, message_text):
        for word in message_text.split(' '):
            if fuzz.ratio(word.lower(), phrase.lower()) >= self.FUZZ_RATIO:
                return True
        return False
