# animal_crossing/isabelle_bot.py

import os
import re
import datetime

from base import bot_base
from dotenv import load_dotenv
from animal_crossing import turnip_database
from datetime import timedelta

load_dotenv()


class IsabelleBot(bot_base.BaseBot):

    def __init__(self):
        super().__init__(os.getenv('ISABELLE_CLIENT_TOKEN'))
        self.add_channel('animal-crossing')

    async def on_ready(self):
        await super().on_ready()
        for channel in self.get_all_channels():
            if channel.name in self.active_channels:
                await channel.send('Hello there, it\'s me, Isabelle!')

    async def on_message(self, message):
        if not self.can_reply(message):
            return

        message_content = strip_alerts(message.content)
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
            reply = 'I\'m sorry, something went wrong...'
            if message_params[0] == 'sell':
                reply = write_sell_price(message.author.id, message_params[2])
            elif message_params[0] == 'buy':
                reply = write_buy_price(message.author.id, message_params[2])
            elif message_params[0] == 'predict':
                reply = get_prediction(message.author.id)
            await self.send_response(message, reply)
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


def write_buy_price(user_id, price):
    if most_recent_sunday() is None:
        return 'I don\'t think that\'s quite right...'
    turnip_database.write_buy_price(user_id, price, date_fmt(most_recent_sunday()))
    return 'Playing the market this week? Good luck!'


def write_sell_price(user_id, price):
    if normalized_sell_date() is None:
        return 'I don\'t think that\'s quite right...'
    turnip_database.write_sell_price(user_id, price, normalized_sell_date())
    return 'Ok, all set.'


def get_prediction(user_id):
    sunday = most_recent_sunday()

    buy_row = turnip_database.get_buy_row(user_id, date_fmt(sunday))
    sell_rows = []

    for i in range(1, 7):
        today = sunday + timedelta(days=i)
        sell_rows.append(turnip_database.get_sell_row(user_id, datetime_fmt_am(today)))
        sell_rows.append(turnip_database.get_sell_row(user_id, datetime_fmt_pm(today)))

    buy_param = buy_row[1]
    if buy_param is None:
        buy_param = ''

    sell_param = ''
    for row in sell_rows:
        if row is None:
            sell_param += '.'
            continue
        sell_param += f'.{row[1]}'

    return f'I\'m still learning, consult an expert for now: https://turnipprophet.io?prices={buy_param}{sell_param}'


def most_recent_sunday():
    sunday = datetime.datetime.now()

    loop_cap = 1
    while sunday.weekday() != 6:
        loop_cap += 1
        sunday = sunday - timedelta(days=1)
        if loop_cap > 7:
            return None
    return sunday


def date_fmt(date):
    return date.strftime("%Y-%m-%d")


def datetime_fmt(date):
    if date.hour < 12 or date.weekday() == 6:
        return datetime_fmt_am(date)
    return datetime_fmt_pm(date)


def datetime_fmt_am(date):
    return date.strftime("%Y-%m-%d:AM")


def datetime_fmt_pm(date):
    return date.strftime("%Y-%m-%d:PM")


def normalized_sell_date():
    date = datetime.datetime.now()

    # Can't update sell price on Sundays
    if date.weekday() == 6:
        return None

    return datetime_fmt(date)


def strip_alerts(message):
    matches = re.match(r'(!ac.?|<@!\d{18}>)(.*$\b)', message)
    if matches:
        return matches.group(2)
    return None
