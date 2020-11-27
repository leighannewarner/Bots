# base/reply_base.py

from base import bot_base
from category import Category


class ReplyBot(bot_base):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.categories = []

    # EVENT OVERRIDES -------------------------------------------------------------------------------------------------
    async def on_message(self, message):
        if not self.can_reply(message):
            return

        category = self.__get_match_category(message)
        if not category:
            return

        response = category.choose_response(message)
        self.send_response(response)

    # CONDITIONS  -----------------------------------------------------------------------------------------------------
    def add_category(self, name, match_type, phrases):
        category = Category(name)
        category.set_type(match_type)
        category.add_phrases(phrases)
        self.categories.push(category)

    def add_phrase(self, category_name, phrase):
        self.categories[category_name].add_phrases([phrase])

    def __get_match_category(self, message):
        for category in self.categories.values():
            if category.has_match(message.content):
                return category

