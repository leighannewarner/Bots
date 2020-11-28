# base/bot_base.py

import discord


class BaseBot(discord.Client):
    def __init__(self, api_key):
        super().__init__()

        self.api_key = api_key
        self.active_channels = []

    def run(self):
        super().run(self.api_key)

    # EVENT OVERRIDES -------------------------------------------------------------------------------------------------
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        pass

    # CONDITIONS  -----------------------------------------------------------------------------------------------------
    # Add to the list of channels this bot is allowed to respond to
    def add_channel(self, channel):
        self.active_channels.append(channel)

    # Check whether this message is valid for this bot to reply to
    def can_reply(self, message):
        return message.author != self.user and message.channel.name in self.active_channels

    # UTILS  ----------------------------------------------------------------------------------------------------------
    async def send_response(self, message, response):
        if not response:
            return
        await message.channel.send(response)
