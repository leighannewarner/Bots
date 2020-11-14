# Betty/betty_client.py
import os
import discord
import random

from dotenv import load_dotenv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from zalgo_text import zalgo

load_dotenv()
client = discord.Client()

questions = {
  'poop_in_the_sink': [
    'poop in the sink', 
    'shit in the sink', 
    'crap in the sink', 
    'dump in the sink', 
    'make poop in the sink'
  ],
  'black_betty': [
    'Whoa, Black Betty',
    'Black Betty had a child',
    'The damn thing gone wild',
    'She said, "I\'m worryin\' outta mind"',
    'The damn thing gone blind',
    'I said "Oh, Black Betty"',
    'Oh, Black Betty',
    'She really gets me high',
    'You know that\'s no lie',
    'She\'s so rock steady',
    'And she\'s always ready',
    'She\'s from Birmingham',
    'Way down in Alabam\'',
    'Well, she\'s shakin\' that thing',
    'Boy, she makes me sing'
  ],
  'name': ['Betty', 'Clark'], 
  'age': [
    'How old are you',
    'How young are you',
    'What is your age',
    'When were you born',
    'Are you a child',
    'Are you old',
    'Are you young'
  ], 
  'gender': [
    'Are you a girl?'
    'Are you a boy?',
    'Are you male',
    'Are you female',
    'Who are you',
    'What are you',
    'Who is this',
    'Who are we talking to',
    'Who am I talking to',
    'What is your name',
    'Can you give me your name',
    'What is your gender',
    'What gender',
    'Are you male or female',
    'Are you a man',
    'Are you a woman'
  ], 
  'location': [
    'Where are you?',
    'Are you close?',
    'Can you show yourself?',
    'Give us a sign',
    'Let us know you are here',
    'Show yourself',
    'Can you talk?',
    'Speak to us',
    'Are you here?',
    'Are you with us?',
    'Anybody with us?',
    'Is anyone here?',
    'Anyone in the room?',
    'Anyone here?',
    'Is there a spirit here?',
    'Is there a Ghost here?',
    'What is your location?'
  ], 'difficulty': [
    'What do you want?',
    'Why are you here?',
    'Do you want to hurt us?',
    'Are you angry?',
    'Do you want us here?',
    'Shall we leave?',
    'Should we leave?',
    'Do you want us to leave?',
    'What should we do?',
    'Can we help?',
    'Are you friendly?',
    'What are you?'
  ], 'generic': [
    'Can you speak',
    'Show us',
    'Let us know you are here',
    'Do something',
    'Is there anyone with me',
    'Are you alone',
    'Can we speak',
    'would like to speak to you',
    'Is there anyone here',
    'May I ask you',
    'Can you speak to us',
    'Would you like to talk',
    'Are you the only one here',
    'Are you waiting',
    'Is there anything that I can do',
    'Do you know who we are',
    'Are you happy',
    'Are you here all the time',
    'Are you male or female',
    'Are there children here',
    'Do you want us to leave',
    'Make a noise',
    'Can I ask you',
    'Can you make a sound',
    'Show us your presence',
    'Knock something',
    'Make a sound',
    'Open the door',
    'Throw something',
    'Talk to me',
    'Talk to us',
    'We mean you no harm',
    'Open a door',
    'We are friends',
    'Is this you\'re home',
    'Can you speak to us',
    'I\'m scared',
    'I am scared',
    'Open this door',
    'Show your presence',
    'Show us',
    'Show me',
    'Turn on the light',
    'Turn off the light',
    'Are there any ghosts',
    'Give us a sign',
    'GHOST GHOST GHOST',
  ], 
}
words = {
  'bloody_mary': ['bloody mary'],
  'swear_words': [
    'Fuck', 'Bitch', 'Shit',  'Cunt', 'Ass', 'Bastard',  'Motherfucker',
    'Arsehole', 'Asshole', 'Crap', 'Pussy',  'Dickhead', 'Dumbass',
  ],
  'fear_words': [
    'Frighten', 'panic',  'Fright',  'Hide',  'Run', 'scared',
    'scary', 'spooky', 'Horror', 'Scare', 'Scream',
  ],
  'greeting_words': [
     'Hello', 'Hi', 'Hewwo',
  ],
  'tiddies': [
    'tibby', 'tibbies', 'tiddy', 'tiddies', 'titty', 'titties', 
    'boobs', 'boobies', 'breasts'
    ],
  'ouija': [
    'ouija', 'luigi', 'weegee','wegi',
    'quiche','weeger', 'wa weg', 'wega',
  ], 
}
responses = {
  'bloody_mary': [
    'Sacrifice', 'Kill', 'Run', 'Die', 'Leave', 'Sanguinary Betty'
  ],
  'poop_in_the_sink': [
    'That is not where the poop goes',
    'You\'ll never 100% clear me',
    'No',
  ],
  'tiddies': [
    'Do the girl aliens have tiddies?',
    'Left one is still attached',
    'Show feet',
  ],
  'black_betty': ['(Bam-ba-Lam)'],
  'name': [
    'Betty Clark',
    'Black Betty (Bam-ba-Lam)',
    'There is no Betty only Zuul'
  ], 
  'age': [
    'Adult', 'A lady never tells',
  ], 
  'location': [
    'Behind you', 'Here', 'Close', 'Near', 'Far',
  ],
  'gender': [
    'Female'
  ],
  'difficulty': [
     'Kill', 'Run', 'Die', 'Leave',
  ], 
  'generic': [
    'E', 'Boo', 'oooooooooooo', '.?',
    ], 
  'swear_words': [
    'You kiss your mother with that mouth?', 
    'I am rubber you are glue',
    'Rude',
    'Kill',
    'Run',
    'Die',
    'Leave',
  ],
  'greeting_words': [
    'hello', 'hi', 'hewwo', 'hewwo mr. pwesident', 'Come play with me',
  ],
  'ouija': [
    'How to do weegi board?',
    'What is a wega board?',
    'How to ojo board works?',
    'How to do planchit withot using ooji board?',
    'Is it dangerous to play OIJA board?',
    'Oujiji board??????',
    'My oujis board is cussing me out?',
    'Is the oueja board online fake or real?',
    'It the wija i real game',
    'Weegee bored or whatever?',
    'How do I find if there is a ghost in my house without using a weggy board?',
    'A wiggy board game?',
    'quiche board',
    'Wa weg board is that how u spell that evil game thing?'
    'Luigi board?',
    'Have you played the Luigi Board?',
    'My Friends did a Luigi board....and it mentioned me! PLEAS HELP?',
    'How do Luigi boards work?',
    'are luigi boards dangerous if you ask something about ghost?',
    'whats up with the luigi board game is it creepy or what is it possible to die for playing this game?',
    'Do quija boards actually works?',
    '(WEEGER) Quija Board Experiences?',
    'Help pls! : Quija Board (Wega Board) help pls',
    'how to use wedgie board and is it real?', 
    'Do wedgie board really work and if so what happened?',
    'Where do I obtain a wedgie board? Do I have to make my own or can I buy one from a witch or vegan?',
    'GHOST!!!! GHOST!!!!! GHOST!!!!!!.?',
  ], 
}

bloody_mary_counter = 0
special_keys = ['bloody_mary', 'ouija', 'tiddies', 'poop_in_the_sink', 'black_betty']

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
  if message.author == client.user or message.channel.name != 'phasmophobia':
    return

  await send_message(message)
    
def get_key(message_text):
  for key in questions:
    if has_match(message_text.lower(), key):
      return key
  for key in words:
    if has_word_match(message_text.lower(), key):
      return key
  return ''
  
def has_match(message_text, key):
  for phrase in questions[key]:
    if(fuzz.ratio(message_text.lower(), phrase.lower()) >= 85):
      print('Matched "' + phrase + '" in category ' + key)
      return True
  return False
  
def has_word_match(message_text, key):
  for phrase in words[key]:
    for word in message_text.split(' '):
      if(fuzz.ratio(word.lower(), phrase.lower()) >= 85):
        print('Matched "' + phrase + '" in category ' + key)
        return True
  return False

async def send_message(message):
  global bloody_mary_counter

  key = get_key(message.content)

  if key == 'bloody_mary':
    bloody_mary_counter += 1
    print('Matched bloody_mary #' + str(bloody_mary_counter))
    if bloody_mary_counter == 3:
      await bloody_mary(message.channel)
      return
  
  response = get_message(key)
  if not response:
    return
  await message.channel.send(response)

async def bloody_mary(channel):
  global bloody_mary_counter
  bloody_mary_counter = 0
  await channel.send(pick_random(responses['bloody_mary']))
  await channel.send(pick_random(responses['bloody_mary']))
  await channel.send(pick_random(responses['bloody_mary']))

def get_message(key):
  global bloody_mary_counter
  
  if not key:
    return ''
  
  if key == 'bloody_mary':
    return ''
    
  if key in special_keys:
    return pick_random(responses[key])
    
  rand = random.randrange(3)
  if (rand == 0):
    print('Skip message')
    return
  if (rand == 1):
    print('Generic message')
    return pick_random(responses['generic'])

  print('Category ' + key + ' message')
  return pick_random(responses[key])

def pick_random(list):
  index = random.randint(0, len(list) - 1)
  return zalgo.zalgo().zalgofy(list[index])

client.run(os.getenv("CLIENT_TOKEN"))
