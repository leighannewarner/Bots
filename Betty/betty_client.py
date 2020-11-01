# Betty/betty_client.py
import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

questions = {
  'bloody_mary': ['bloody mary'],
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
    'Give us a sign'
  ], 
  'swear_words': [
    'Fuck',
    'Bitch',
    'Shit',
    'Cunt',
    'Ass',
    'Bastard',
    'Motherfucker',
    'Arsehole',
    'Crap',
    'Pussy',
    'Dickhead',
  ],
  'fear_words': [
    'Frighten',
    'panic',
    'Fright',
    'Hide',
    'Run',
    'scared',
    'scary',
    'spooky',
    'Horror',
    'Scare',
    'Scream',
  ],
  'greeting_words': [
     'Hello',
  ]
}
responses = {
  'bloody_mary': ['S̰̭̜̯͕̦̳͂̆͋̈̊̏͠ Ą̨͉̠͉̘̹̱͔̞́̿́̅̊̔̂͐̅ C͇͍̞̫̹̫͉̼͋̉̐̈́̈͒̎̑̽͠ R̛̺̝̼̗̣̫͚̓̈́̆̃͘͘͢ I̘̣͇̺̜̻̰͌̃̄̈͘͜ F̶̞͙͎̞̮͙̏̅͆̾̕ I̷̡̤͚͚̪͉̟̦̱̾͆͗̎̀͊̐̀͗ Ç̹͈͍̭͈͕̫͖͓̈̍̑̏͒͐̓̂͛̀ E̢͇̭̤͚̘̓̾̇̆̓̈̀͊̊͠'],
  'name': [
    'B̵̻͓̗̞̒̾͋͟͞͡͡ Ȩ̸̪̭̠̗̩̯͓͆͆͌́̓̑͋́̆͟ Ṭ̶̨̜͖̗̼̘̻̈͑̈́̏̒ T̷̛͚̥̩̝̙̣̠̐͐́̚͘ Ỳ̪̱̬͓̰̽͋̀͠͠ C̷͓̣̝̗͆̏͑̿͗̏̈́̒͘͡ͅ L̶̬̺̪͙͚͓̑́̏͆̽̾́̉͘ À̸̧̪̳͖͈̆͛̉̾͋͐̔͋ R̡̡̞̰̝̱̼̱͂̄̓̒͑̌͠ K̝̙͓̰̳͓̏̈́̏̇̄̕͢͜',
    'B̧̬͇͖͔̲͚̿̋̌̃̊͆͠ͅ L̷͚͍̪̟̜̫̆͊́͋́̈́̌͒̕͜͠ A̷̘͇̬̯̝̱͑̇͑̅̀̂̾͜͟ Ç̸̛͎̱̠̞͇̬̓̏̐̈̈́͒͌ K̛̝̗͚̳̰̪͋̔͒̃̊ B̡̝͖̦̫͑̿̅̏̍͊͡ É̷̯̣̘͖͇͕̏͂̐̒́̇͌͢͠͡ T̢̧̛͙̰̙̀̌̈́͛̈́̊̎̕͝ Ṭ̷̨̡͓̪̮̎̈́̓͆͊̊̏̍̏͟͠ Ÿ̩̫̘̻́͂́̄̓͛̎̾͟ (̷̧̛̺̖̞̈́̑̽͐̄͛̂̚͞ͅB̨̨͎͙̣͓̞͛̓̋̿̓͡A͈̘̥͎̣͐̅́́̏̾̈́̏̐̃M̸̛̤̲̪̫͓͇͖̑͆͛̎̍͒̍̚͜͞ͅA̸̹͉͔̬͎̗͑́̄̓̓͆L̵̨̢̛͕͖͚̟̘̗̺͚̈̎̿̓̎̄͠Ā̭̙̭͎̬́̈͛̊̽̈́̉̕M̸̰͔̰̱̠̑́̔͒̄̇)̷̨̡̘̮̪̙̐̊͑͗̃͞ͅ',
    'ť̪̞̝͖̲̭͓͊͌͐̇̐̌̇ȟ͍̭̹̙̭̱͚̰̲̲́̚̕̚è͈͇̹̞̙̪̫͈̾̿̄̒̉͟͞͡͠r̴̜͍̪̘̯̫̮̾̈́͌̃̉̚͘è̡̨̯̠̠̬̽̏͊͋̍̆̍̚͜ i̢̨̺͉̻̯̙̼̺͂͂̓͌͛͘͠͝s̸͖̟̺̬̥͐͗͐̽͜͢͞͝ n̨̘̜͕͈̝̆͂͊̔̿̍ͅo̮̦͇͉͔̲̯̍͑̿͋͟͝ B̴̡̝̟͎͓̳͇̀̎̓̎̿̏͛̎e̢̧͕̝̹̝͕̊͂̈́͒͘͟͡ť̵̢̮͓̩̻͙̒̐͗͒͛t̡̤̲̳͕̝͚̼̿͌̒̈̈̆́́͜͜ẏ̗͇͉̘̔̂͋̃͜͢ ȏ̴̘̺̲̟̹͔̖̺͚̑̅̂̑͟͝n̟̪̣̼͓͛̓̀͆͋͂͟ļ̶̱̥̳̹̎̾̋͋͐̍y͉̳̖͙̤͔͋̅̾͐̒̎̃͟͞͠ Z̡͕̝͚̙̱̘͓̈̽͂͆̔͢u̸̡̱̤̹̝̲̭͐̓͂̋̕͘͠u̱͇͚͚͚̙͔̽̑͑̍͌͐̓͢l̢̢̛̤͙̥̺͉̞̭͐̐̄́́̈ͅ'
  ], 
  'age': [
    'Ǻ̴̡͍̼̳̪̟́́̾̃̐͐̍͞ D̴̢͇̙̩͗̆́̇̓́̐̕͢͡ U̶̻̼̝̻̪͖͗́͌̾̄̍̄̀̅̂ L̷̳̹͙͈̙͍̱̺͆̃͆͗̊ͅ Ţ̸͍̰̤̺̮̰̙̹́́͆͆̐̄',
    'Ą̵̧͚̫͉̣̻̓̾́̎̀ L̳̺̜̥̖̾̒̋̿̋̏͘͢͠͝A̭̮̬̼̍́̈̈́̏͊̆̐͐ͅD̢͙̩̹͍͊͆̐̌̄̾͘͟ͅY̰̘̳̋͛̈̃͘͜͜͞ Ņ̸̧̭͚͗̀̋͛͒̿̓͞͠͠ͅĘ͔̪͇͕̑̋̈́̀̈́͒̍͋͠V̵̧̫̺͍̘̻̰̏̐̀͂̓͐͡͠Ę̵̺͈̼̝͎̳͇̳̓͐̍̂̔̔̅́͢R̸̤̖̬̬̜̟̭̟̹̂͐̄͆̽́̔͝͞͠ͅ T̢̡͎̰͍̝̹̓̊̾͋̌͗̿͜͜͠Ĕ̮͚͓̰͇̐͌̂̕L̵̢̖̰͍̞̮̩͍̐͗̿̄̅͋̕͜L̶͍̱̯̭̜͕̼͚͆̎̇͂̔̈̚Ṣ̢̛̪̭̈̆́̓̕͟͞',
  ], 
  'location': [
    'B͓̯̖̱̤̩̭̜͐̄̈̓̅̂͑͝Ȩ̨͔̖̝̳̹͇͍̳̿̈́͛̍͑̓Ĥ͈̲͖͔̲̤͈̬͆͗̑̉̈̒͢͠I̶̡̦̙̘̹͙̮̹̻̫̓͂̄͂̑̇̓̀̕Ń̩̯̱̖̲̤̹̺̓̆̓̃̃̚͝D̶̫͚̦̜͓̥̗̗͚́̒̓͋̉͜ Y̷̧̠̟̹͙̮̔̋̑͒̅͡O̷̢̭͍͙̘̙̬̤̜̊̃̔́̃̋̈͡U̸̡̪̥͉̤̫̰͚̓́̆͋͊̔͘͝', 
    'Ḧ̸̛̫̙̰̮̭̼͍́̿͆͒͛̏͢͢Ę̲̞͖͍̏̃̉̑̽R̰̤̺̬͚̳̥̟̩̎̄̌͑́͞E̶̬͔͕̠̣̍̈̉̅̂̇̊̏͞', 'C̛̛̞̱͍̤͉̟̓͗̓̀͡ͅ L̼̺̩̭̣͇͑̈́̅̔͊͋͑̈́̋ O̵̠͇͎̺̫̰̖͙͒̆̂̕͠͠͠͡ S̶͍̭̰͚͎̥̘̝̫̃͗̋̌̾̊̀͛̚ͅ Ê̘̬̪͙̮͒̏́͗̌͜͟͡',
    'C̢͉̼̜͖͇͔͈͈̿̂̂̇̇̾̒̓̒͞l̵͇̘̖̬̞̤͂̄̓̈̇̍̅͡ò̪͙͚̼͎̪̲̑̎̈́̆̆͞s̵̹̯͎̰̗̮͔̣̣̆͒͗̿͆͟͝͡e͕͖̙͖̪̙̽̓̎̌̈́̅͗̃̄͘ͅ'
  ], 
  'difficulty': [
    'K͍̳̻̣͖̂͂̋͗̀́͜͠ Ȉ̼͍̤̲͎̼̭́̇͗́̅̚̚̕͠ L͔̱̯̱̯̲̥̣̓́͊̓͘͜ L̖̖̣̮̩̈̊͒͋̈́͢', 'R̻̙̜̫̬̪̉̊̄̒̚͟Ȕ͎̖̙̭̒́̐̄͊͒͟͝N̨̢̢͙̩̬̭̤͈̟̄͊̄̍͊͠',
    'Ṟ̷̛̬̺͈̱͇̲̈̀̅̐̃͢͡ Ů̵̧̨̨͈͓͈̯̦̜͓͂͛̾̀̓̅͡͞ Ǹ̸̹͇̘̣͔̭̭̱̗̈́̂̍͞',
    'D̴̢̧̠̱̦͔̮̜͌́̈́̔͂̕͟I͈̣͖̹͈͂̈̏̅̂̓̔́̚E̼̝͍͚͗͑͋͒͋̐̐̀̚ͅ,',
    'Ĺ̢̳͓̣̟̼̙̲̓́̀̅̽́̀͑͛É̺̞̙͙̜̟̮̱̀̋͡͠ͅA̧̮͇̭̭̗̓̂̍̉͗͢͠V̶̢̻̬͙͈͓̅̇̔̏͘Ĕ̴̛̛̜͍̝͕͎̬̪̍̾̀͐̕',
  ], 
  'generic': [
    '    E̪͖̣̩̰̟͙̳̜͋̑́̊͗̇ͅ',
    'B̢̩̞̺̩̥̣̙̾̆͗́͂̀̽͘Ǒ̡͍̙̹̭̘͖͓̂͐̿̌̑̄̌̚O͚̥͎̜̜̽̂̋́̈͊̽͜͡ͅ', 
    'ǫ͇͓͇̱̳̾̆̾́͂̿͠͞͝ö̷̧̡̰̗̝̞͙̬̠̘̾̅̾͂͋͊͝͝͝ǫ̸̮̳̰̠̙̩̯͂̈́̀́̍͢ơ̵̢͎̳̣̘͊̇͋͌̋̅͗̚o̧̝͈̻͚̤͆̿̇̾͘o̞̦̙͚͎͆̎̍͞͠ͅŏ̷̺͔̰̺̘͇̎̽̑̇͛̑̽͠ȯ̵̦̲̘̣͓̦͎̻̰͎̔̈̎̾̊̏ǫ̳̘̞̲͂͆̍̿̕ǫ̛͇̜̯͔͒̇͆̾͞ͅ'
    ], 
  'swear_words': [
    'Y̨̥̲̬̩͙̩͚͔̝͒̃̎̓̂̈́͗o̷̡̠̖̠͇̦̼̲̬̾̍̃̕͞u̴͔̯̪̘̣̥̲̍̆̎̋͊͡ k̸̞̱͉̥̖̊̇̅̓̇̽̊͋̕i̶̘̯͇̦̲̱̘̹̱̾͒́̂̾̂̅͛̈̚͟s̵̡̗̟̩̣̊̑͂͐̀̑͘ś̷̢̹̬͎̟͎͓̳̃̏̃̾͐̔͊ ỳ̵͓̪̗̟̬̝̖͙͛͂̅͐̓̉̆͋ò̗̙̫̟͓̍̿͋̈͘͟ͅú̶̥͙̹͔̭͐̓̐̚r̬̳͍̯̬̻̠̩̀̏̊̏́̈́̊̑͢ m̧̯̹̤͇̘̫͈͕̿͑̈̒͢͠o̸̧̰̬̦̙̹̳̟͕͛̀̓̌̃̎̆t̴̟̰͇̼̦͎̞̑̒̑̄͘h̡̛͚͖̭̪̻͔̅͋̂͒̇̑͊͞͝ę̶̛̮͙̭̯̿̔͊͒̽̐ř̗̣̞̰̖̻̩͍̩̎͐͌̉̂̚͝ w͉̪̭̯̪̟͖͗͑̏͐̀̍͢͝i̢̹͖͙̜͙̖̿͊̀̃̀̎̽̃̓̍͢͟͢t̛͔͙̬͖͔͖̲̭͐̓́͗͆͂̀̇h̷̛̦͈̯̟̮̉̉͗͛̉ t̫̱̼̮̝̏̉̓͛̌̇͡͝h̷̬͙̞̳͖͗͛̑̉́̋͘͜ͅa̴̛̩͔̪̫̼͓̫͋́̅̀́̌͒͜͠ͅț̛̹̯̺̯̻̝̪̞͗̀̆̇͛̑̚͝ m̷̨̪̝̭͇̦̙͊̄̓̉̑̐ō̦͇͈̙͉̭̗̪̌̄̍̒̚͜͞͡͠ư̧̨̢̟̗̘͈̞̤̓̇̏͊̅̆͑͘͝ͅt̴̨̟͕͖̙̔̈̑̔̅̅̀͌̂͟h̴͕͇͎̥̯̐̈́̌̽̕͜͠͡?̧̰̦͙̥̰̜̦̹̇̾̈̃̎̍̅͜͡', 
    'Į̶̣̼̖̫̖̞̯̰͛͊͂̽͛̓̇̏̈́̎\'̵͍̗̳̣̠̙͖̈́̆̋̌͌̊̉͊́̌͢m̛͔̱̥̰͎̯̙̟̑̑͒͆̆͝͝ ř̵̨͎̟̱̻͇̮̥̌͂̿͒̅̓̀̓͢ự̴̧͓͉̯̬͆͋̃͊̓͆̇b̸̬̣̘̺̭̻̼́͂̀͐̂̚͜͡ͅb̸̨̝͎̘̙̮͓̞͛͗́͆̋͑̌̌͋ë̷̼̰̹́̎̀̑̐͋̕͟͡ͅr̡͇̖͇͎̗̗̫̂̽̒̔̉̚͜ͅ y͉̘̘̙̪̭̝̝̣̱̓̄͋͂̌̀̆́͆o̴͚̰̻͎̯͒̍̀͐̓ư̸̪̖͖̜͉̭̩̔̐̐͐͘̕\'̨̢̛̮͓̱̏͂̈́̌̑̄̾̚͢r̛̪̝̝̯̱̘̱̼̉̀̎̒͜͝è̗͖͕͓̼͊͒͂͂͌͊͌̋͘ g̸̛̛̳͉̤̩̯̤̝̫̬̍͊̅͋͛͝͡ͅĺ̨͕̝̤͖̯̤͐̈͌̐ͅů̴̪̠̱̞̭͍́̄̎̌́͘͟͟ę̵͕̫̣̭̣̩̫̐̍̅͆͂̿̎̎͘'
  ],
  'greeting_words': [
    'H͈͇̞͖͍͋̅̾̎͆̉̅̓͟͠E̴͕̠̱̥͓̔̈̈̈́͑͜͜ͅĻ̴̳̫̫̻̫̙͖͕̠̽̍̓̿͠͠L͇̗̲͔̦͌̋̎̋̓̾̍̓̄̕͢ͅO̢̖̗̯͛́́̓̍͒ͅͅ',
  ]
}

bloody_mary_counter = 0

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
  return ''
  
def has_match(message_text, key):
  for phrase in questions[key]:
    if(message_text.lower().find(phrase.lower()) != -1):
      print('Matched "' + phrase + '" in category ' + key)
      return True
  return False

async def send_message(message):
  global bloody_mary_counter

  key = get_key(message.content)
  response = get_message(key)
  if not response:
    return
  if key == 'bloody_mary':
    await message.channel.send(response)
    await message.channel.send(response)
    await message.channel.send(response)
  
    return
  
  await message.channel.send(response)

def get_message(key):
  global bloody_mary_counter
  
  if not key:
    return ''
  
  if key == 'bloody_mary':
    bloody_mary_counter += 1
    if bloody_mary_counter == 3:
      blood_mary_counter = 0
      return pick_random(responses['bloody_mary'])
    else:
      return ''
    
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
  index = random.randrange(len(list))
  return list[index]

client.run(os.getenv("CLIENT_TOKEN"))
