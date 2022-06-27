import discord
import config

TOKEN = config.token_bot()
client = discord.Client()


def busca_canal():
    text_channel_list = []
    for server in client.servers:
        for channel in server.channels:
            if channel.type == 'Text':
                text_channel_list.append(channel)
