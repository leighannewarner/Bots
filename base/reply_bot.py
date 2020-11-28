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

        matched_categores = self.__get_match_categories(message)
        if not matched_categores:
            print('No matched categories')
            return

        response = self.choose_response(matched_categores)
        await self.send_response(message, response)

    # CONDITIONS  -----------------------------------------------------------------------------------------------------
    def add_category(self, name, match_type, match_priority):
        category = Category(name, match_type, match_priority)
        self.categories[name] = category

    def add_phrases(self, category_name, phrase_list):
        self.categories[category_name].add_phrases(phrase_list)

    def add_responses(self, category_name, response_list):
        self.categories[category_name].add_responses(response_list)

    def choose_response(self, matched_categores):
        return matched_categores[0].choose_response()

    def __get_match_categories(self, message):
        matched_categores = []
        for category in self.categories.values():
            if category.has_match(message.content):
                matched_categores.append(category)
        return sorted(matched_categores, key=lambda value: value.match_priority, reverse=True)
