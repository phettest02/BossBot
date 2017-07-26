#!/usr/bin/python3
'''BossBot: An adaptable Discord bot written in Python.
This file contains all functions that need direct interaction with Discord.
Author: William Harrell'''
import asyncio
import configHandler
import neatStuff
import discord
from discord.ext import commands

bot_prefix = '$' #this is the prefix to be used in a Discord channel to get the bot's attention
description = 'Hello! I can do many things, like the stuff below. Get my attention with %s' %bot_prefix

bot = commands.Bot(description=description, command_prefix=bot_prefix) #create an instance of Bot

async def memeHandler(context):
    '''performs the appropriate action based on what neatStuff.sendMeme() returns'''
    meme = neatStuff.sendMeme()
    if meme[:2] == './':
        print('sending meme %s' %meme)
        await bot.send_file(context.message.channel, meme)
        print('%s was successfully uploaded' %meme)
    elif meme == 'no memes':
        await bot.send_message(context.message.channel, 'I don\'t have any memes. Try sending me some!')
    else:
        print('An error occured when trying to send a meme.')

async def getIcon(context):
    '''send the avatar urls of the mentioned users in a message, to be used with icon command
    Preconditions: context, which is the context the message is sent with'''
    if len(context.message.mentions) == 0:
        await bot.send_message(context.message.channel, 'Make sure to mention a user(s) after using this command!')
    else:
        for member in context.message.mentions:
            await bot.send_message(context.message.channel, 'Icon of %s: %s' %(member.mention, member.avatar_url))

@bot.event
async def on_ready():
    '''prints Discord login information and version info to console when the bot has logged in'''
    print('\n==INITIALIZATION COMPLETE==')
    print('BossBot is logged in, reporting for duty!')
    print('Username: %s' %bot.user.name)
    print('ID: %s' %str(bot.user.id))
    print('Running on Discord.py ' + discord.__version__)

@bot.command(pass_context=True) #passes context from command
async def ping(context):
    '''play pong'''
    await bot.send_message(context.message.channel, 'Pong!')

@bot.command(pass_context=True)
async def sergals(context):
    '''get an interesting sergal fact'''
    await bot.send_message(context.message.channel, neatStuff.sendSergalFact())

@bot.command(pass_context=True)
async def dice(context):
    '''roll a dice'''
    await bot.send_message(context.message.channel, '%s rolled a %d' %(context.message.author.mention, neatStuff.rollDice()))

@bot.command(pass_context=True)
async def death(context):
    '''find out when you will die'''
    await bot.send_message(context.message.channel, neatStuff.deathclock())

@bot.command(pass_context=True)
async def meme(context):
    '''sends a meme to the channel'''
    await memeHandler(context)

@bot.command(pass_context=True)
async def icon(context):
    '''When no arguments are given, return the bot's icon. When a valid user is given, return the user's icon.'''
    await getIcon(context)

@bot.command(pass_context=True)
async def invite(context):
    '''use this to receive a link to add me to your server'''
    await bot.send_message(context.message.channel, 'PMing %s an invite link...' %context.message.author.mention)
    await bot.send_message(context.message.author, discord.utils.oauth_url(bot.user.id))

def init():
    '''Imports the configuration from "./config/main.conf" and starts the bot'''
    configHandler.makeConfig()
    apiKeys = configHandler.readApiKeys()
    print('Discord API Key: %s' %apiKeys[0])
    bot.run(str(apiKeys[0])) #login to Discord using a Bot API in place of token

if __name__ == '__main__':
    init()

'''
Research used:
    Discord bot beginning tutorial (used for learning how to initially set up the bot, and what additional skills would need to be gained before the bot could be written: https://youtu.be/bYfhQODnH0g
    Discord.py Documentation: https://discordpy.readthedocs.io/en/latest/api.html#client
    Video on Python Decorators: https://youtu.be/mZ5IwFfqvz8
'''
