# base/reply_base.py

from base import bot_base
from base.category import Category


class ReplyBot(bot_base.BaseBot):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.categories = {}

    # EVENT OVERRIDES -------------------------------------------------------------------------------------------------
    async def on_message(self, message):
        if not self.can_reply(message):
            return

        category = self.__get_match_category(message)
        if not category:
            return

        response = self.choose_response(category)
        print('Chose ' + response)
        await self.send_response(message, response)

    # CONDITIONS  -----------------------------------------------------------------------------------------------------
    def add_category(self, name, match_type):
        category = Category(name)
        category.set_match_type(match_type)
        self.categories[name] = category

    def add_phrases(self, category_name, phrase_list):
        self.categories[category_name].add_phrases(phrase_list)

    def add_responses(self, category_name, response_list):
        self.categories[category_name].add_responses(response_list)

    def choose_response(self, category):
        return category.choose_response()

    def __get_match_category(self, message):
        for category in self.categories.values():
            if category.has_match(message.content):
                return category
