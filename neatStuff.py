#!/usr/bin/env python3
'''This module contains functions to be used as responses in main.py'''
import os
import random

def rollDice(dieSides=6):
    '''Preconditions: an integer (dieSides). Default is 6.
    Postconditions: returns an integer between 1 and dieSides.'''
    return random.randint(1, dieSides)

def deathclock():
    '''Returns a number between 1 and 100, and matches it to the appropriate phrase.'''
    years = random.randint(1, 100)
    if years > 30:
        return 'Sorry friend, you still have %d years to suffer through.' %years
    elif years > 20 and years <= 30:
        return 'Not too bad, %d years left.' %years
    elif years > 10 and years <= 20:
        return 'Congratulations, only %d more years to go of this disgusting nightmare for you.' %years
    elif years <= 10:
        return 'Aww hell yeah, you only have %d more years to go buddy. It\'s almost over!' %years

def sendMeme():
    '''Check to make sure meme directory exists, and create it if it doesn't. If it does exist, randomly select one and return its path.'''
    if os.path.exists('./memes') and len(os.listdir('./memes')) != 0:
        files = os.listdir('./memes')
        return './memes/' + files[random.randint(0, len(files) - 1)]
    elif os.path.exists('./memes'):
        print('sendMeme() was called, but no memes are in ./memes')
    else:
        os.mkdir('./memes')
        print('memes directory does not exist, creating...')
        sendMeme()

if __name__ == '__main__':
    print(sendMeme())