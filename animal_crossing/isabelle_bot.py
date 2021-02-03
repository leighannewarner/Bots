# animal_crossing/isabelle_bot.py

import os
import re

from base import bot_base
from dotenv import load_dotenv

load_dotenv()


class IsabelleBot(bot_base.BaseBot):

    def __init__(self):
        super().__init__(os.getenv('ISABELLE_CLIENT_TOKEN'))
        self.add_channel('animal-crossing')

    async def on_message(self, message):
        if not self.can_reply(message):
            return

        message_content = self.strip_alerts(message.content)
        if not message_content:
            message_content = ''

        message_params = message_content.strip().split(' ')
        if len(message_content) == 0 or len(message_content) == 0 or re.match(r'help!?', message_params[0].lower()):
            await self.print_help(message)
            return
        elif len(message_params) < 2:
            await self.print_hint(message)
            return

        if re.match(r'turnips?', message_params[1]):
            if message_params[0] == 'sell':
                self.write_sell_price(message.author.id, message_params[1])
                await self.send_response(message, 'I\'m still learning how to help you with that')
                return
            elif message_params[0] == 'buy':
                self.write_buy_price(message.author.id, message_params[1])
                await self.send_response(message, 'I\'m still learning how to help you with that')
                return
            elif message_params[0] == 'predict':
                self.write_predict_price(message.author.id, message_params[1])
                await self.send_response(message, 'I\'m still learning how to help you with that')
                return

        await self.print_error(message)

    def can_reply(self, message):
        if re.match("(!ac.?)", message.content):
            return super().can_reply(message)

        for mention in message.mentions:
            if str(mention.id) == os.getenv('USER_ID'):
                return super().can_reply(message)

        return False

    async def print_help(self, message):
        await self.send_response(message,
                                 'First, get my attention with `@Isabelle` or `!ac`\n' +
                                 'Then say one of the following: \n' +
                                 '`sell turnips <price>`\n' +
                                 '`buy turnips <price>`\n' +
                                 '`predict turnips <@User or blank for your own>`\n' +
                                 'For example, you could say `@Isabelle sell turnips 100`')

    async def print_hint(self, message):
        await self.send_response(message,
                                 'Hmm, I think I need more information... '
                                 + 'If you\'re really stuck, try asking `@Isabelle` for `help`!')

    async def print_error(self, message):
        await self.send_response(message,
                                 'Sorry, but my ears are just too fluffy and muffly, I guess. '
                                 + 'Please tell me once more. '
                                 + 'If you\'re really stuck, try asking `@Isabelle` for `help`!')

    def write_buy_price(self, id, price):
        return

    def write_sell_price(self, id, price):
        return

    def get_prediction(self, id):
        return

    def strip_alerts(self, message):
        matches = re.match(r'(!ac.?|<@!\d{18}>)(.*$\b)', message)
        if matches:
            return matches.group(2)
        return None
