import os
import random

from dotenv import load_dotenv
from betty import betty_phrases
from base.category import MatchType, MatchPriority
from base.reply_bot import ReplyBot
from zalgo_text import zalgo

load_dotenv()


class BettyBot(ReplyBot):

    GENERIC_KEY = 'generic'
    HIGH_PRIORITY = ['bloody_mary', 'ouija', 'tiddies', 'poop_in_the_sink', 'black_betty']
    MEDIUM_PRIORITY = ['difficulty', 'swear_words', 'age', 'greeting_words', 'location', 'gender']

    BLOODY_MARY_COUNTER = 0

    def __init__(self):
        super().__init__(os.getenv('CLIENT_TOKEN'))
        self.__add_all_categories()
        self.add_channel('phasmophobia')

    def __add_all_categories(self):
        self.__add_partial_categories()
        self.__add_full_categories()

    def __add_partial_categories(self):
        for key in betty_phrases.PARTIAL_PHRASES:
            self.add_category(key, MatchType.PARTIAL, self.__get_priority(key))
            self.add_phrases(key, betty_phrases.PARTIAL_PHRASES[key])
            self.__add_responses(key)

    def __add_full_categories(self):
        for key in betty_phrases.FULL_PHRASES:
            self.add_category(key, MatchType.FULL, self.__get_priority(key))
            self.add_phrases(key, betty_phrases.FULL_PHRASES[key])
            self.__add_responses(key)

    def __add_responses(self, category_name):
        if category_name in betty_phrases.RESPONSES:
            self.add_responses(category_name, betty_phrases.RESPONSES[category_name])
        else:
            self.add_responses(category_name, betty_phrases.RESPONSES[self.GENERIC_KEY])

    def __get_priority(self, category_name):
        if category_name in self.HIGH_PRIORITY:
            return MatchPriority.HIGH
        if category_name in self.MEDIUM_PRIORITY:
            return MatchPriority.MEDIUM

        return MatchPriority.LOW

    def choose_response(self, matched_categories):
        print('Choosing response')
        if not matched_categories:
            return

        # Check for special match conditions
        has_name_match = False
        for category in matched_categories:
            if category.category_name == 'name':
                has_name_match = True
            if category.category_name == 'bloody_mary':
                self.BLOODY_MARY_COUNTER += 1

        # Handle the special bloody mary case
        if self.BLOODY_MARY_COUNTER == 3:
            self.BLOODY_MARY_COUNTER == 0
            return self.__intensify_text(self.categories['bloody_mary'].choose_respones())

        # Skip category randomization for high priority matches
        if matched_categories[0].match_priority == MatchPriority.HIGH:
            return self.__intensify_text(matched_categories[0].choose_response(), matched_categories)

        # Randomly decide between not responding, a generic message, or a specific category message
        return self.__choose_random_message_category(matched_categories, has_name_match)

    def __choose_random_message_category(self, matched_categories, has_name_match):
        message_type = random.randrange(3)
        # Increase odds of special messages if the name has been used
        message_type += 1 if has_name_match else 0
        if message_type == 0:
            return ''
        elif message_type == 1:
            return self.__intensify_text(self.categories[self.GENERIC_KEY].choose_response(), has_name_match)
        else:
            return self.__intensify_text(matched_categories[0].choose_response(), has_name_match)

    def __intensify_text(self, text, has_name_match):
        # Randomly alter capitalization and add spoopiness
        message_intensity = random.randrange(3)
        message_intensity += 1 if has_name_match else 0
        transformed_text = ''
        if message_intensity == 0:
            transformed_text = transformed_text.lower()
        elif message_intensity == 1:
            transformed_text = text
        elif message_intensity == 2:
            transformed_text = text.upper()
        else:
            transformed_text = self.__add_spaces(text.upper())

        return zalgo.zalgo().zalgofy(transformed_text)

    # Add spaces in between letters to increase spoopiness
    def __add_spaces(self, text):
        spaced_string = ''
        for character in text:
            spaced_string += character + ' '
        return spaced_string
