
import re
from peewee import *
import unittest


string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 111-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 222-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 333-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 444-555-5558, @joykesten'''


words = re.findall(r'''
            \b[ken]+\b
            #[^-\d]+
            #\b
            ''', string, re.VERBOSE|re.I)

#words2 = re.match(r'Love', string)
#print(words2.group(0))

#print(words)

string2 = '\root\usr\bin\Alan'

folder = re.search(r'[^\\]+', string2)

print(folder.group(0))

phoneString = "555 555-5555"

#phone = re.findall(r"\(*\d{3}\)*( |-)*\d{3}( |-)*\d{4}", string)

phone = re.findall(r"(\(*\d{3}\)*\s?-?\d{3}\s?-?\d{4})", string)

#phone = re.findall(r"(\(*\d{3}\)*\s?-?d{3}\s?-?d{4})", string)

print(phone)

#if not(phone == None):
#    print(phone.group(0))
#else:
#    print("invalid")
print('-'*10)
golbang = re.search('(?P<address>@\w+.?\w+.?\w+)', string)
print(golbang.groupdict())

print('-'*10)
golbang = re.findall('(?P<address>@\w+.?\w+.?\w+)', string)
print(golbang)

print('-'*10)
#contacts = re.search(r'[-\w\d+.]@[-\w\d.]+, \(*\d{3}\)*\s?-?\d{3}\s?-?\d{4}',string)

#contacts = re.search(r'\(*\d{3}\)*\s?-?\d{3}\s?-?\d{4}',string)

#contacts = re.search(r'[-\w\d.\+]+@[-\w\d.]+,\s\(*\d{3}\)*\s?-?\d{3}\s?-?\d{4}',string)

contacts = re.search(r'(?P<email>[-\w\d.\+]+@[-\w\d.]+),\s(?P<phone>\(*\d{3}\)*\s?-?\d{3}\s?-?\d{4})',string)

#print(contacts.group(0))

print(contacts.groups())

print('-'*10)
twitters = re.search(r'(@[\w\d]+)?$' , string, re.MULTILINE)

print(twitters.groups())



string2 = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

print('+'*10)

players = re.search(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', string2, re.MULTILINE)
print(players.groupdict())

print('-'*10)

players_com = re.compile(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', re.MULTILINE)

last_name = ''
first_name =''
score = ''

group_dict = players_com.search(string2)

print(group_dict)

player_groups = group_dict.groupdict()  #players.groupdict()

last_name = player_groups['last_name']

first_name = player_groups['first_name']

score = player_groups['score']

print('{} - {} - {}'.format(group_dict.groupdict()['last_name'], first_name, score))


players_com = re.compile(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', re.MULTILINE)

class Player:
    last_name
    first_name
    score


    def __init__(self, string):
      #group_dict = players_com.search(string)
      group_dict =  players
      self.last_name = group_dict.groupdict()['last_name']
      self.first_name = group_dict.groupdict()['first_name']
      self.score = group_dict.groupdict()['score']


player = Player(string2)
print('{}--{}--{}'.format(player.last_name, player.first_name, player.score))



print('&'*10)
stringX = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

playersX = re.search(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', string, re.MULTILINE)

class PlayerX:
    last_name = ''
    first_name = ''
    score = ''

    def __init__(self, string):
        playersX = re.search(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', string, re.MULTILINE)
        group_dict = playersX
        last_name = group_dict.groupdict()['last_name']
        first_name = group_dict.groupdict()['first_name']
        score = group_dict.groupdict()['score']
        print(last_name, first_name )


playerX = PlayerX(stringX)
print('==> {}'.format(playerX.__class__.last_name))


match_obj = re.match(r'(?P<last_name>[\w\s]+),\s(?P<first_name>[\w\s,]+):\s(?P<score>[\d]+)', string2)

print(match_obj.group(0))


print('@'*10)

db = SqliteDatabase('challenges.db')

class Challenge(Model):
      name = CharField(max_length=100)
      language = CharField(max_length=100)

      class Meta:
        database = db


db.connect()

db.create_tables([Challenge], safe=True)

Challenge.create(name='OOP', language='Ruby')
Challenge.create(name='OOP', language='Java')
Challenge.create(name='dynamic', language='Python')

#challenges = Challenge.select()
challenges = Challenge.select().where(Challenge.name.contains('OOP'), Challenge.language == 'Java')


for challenge in challenges:
    print("{}-{}".format(challenge.name, challenge.language))
    challenge.delete_instance()

print('@'*10)

challenges = Challenge.select()
for challenge in challenges:
    print("{}-{}".format(challenge.name, challenge.language))

def average(num_list):
    return sum(num_list) / len(num_list)

average_val = average([1, 2])
#num_list = [1, 2]
#average = sum(num_list) / len(num_list)
print(average_val)



