# base/bot_base.py

import discord


class BaseBot(discord.Client):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.run_bot()

    def run_bot(self):
        self.run(self.api_key)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
