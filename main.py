import sys, os, json

version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])




# Game loop functions
def render(game,current):
    ''' Displays the current room '''

print('You are in the ' + game['rooms'][current]['name'])
print(game['rooms'][current]['desc'])
if len(game['rooms'][current]['inventory']):
    print("The following items are here:")
for i in inventory:
    print(i)

def getInput():
    ''' Asks the user for input and normalizes the inputted value. Returns a list 
of commands '''
    toReturn = input('\nwhat would you like to do?').strip().lower().split()
    if (len(toReturn)):
        #assume the first word is the verb
        toReturn[0] = normalizeVerb(toReturn[0],verbs)
    return toReturn

response = input('What would you like to do? ').strip().upper()
return response


def update(response,game,current,flags):
    ''' Process the input and update the state of the world '''
    
    if response == 'pick up key' and "key" in game['rooms'][current]["inventory"]:
        game['rooms'][current]['inventory'] = []
    flags['haveKey'] = True

for "weapon" in game['rooms'][current]['inventory']: 
    if response == 'take weapon' and "weapon" in game['rooms'][current]["inventory"]:
        flags['haveWeapon'] = True

for monster in game['rooms'][current]["inventory"]:
    if response == 'attack' and "weapon" in game['rooms'][current]["inventory"]:
        flags['beatMonster'] = True
    elif response == 'attack monster' and "weapon" not in game['rooms'][current]["inventory"]:
        print('you died!')
for e in game['rooms'][current]['exits']:
    if response == e['verb']:
        current = e['target']
return current



def main():

    game = {}
    with open('Untitled-1.json') as json_file:
        game = json.load(json_file)

current = 'START'

quit = False
inventory = []
flags = [
    'beatMonster': False,
    'haveKey': False,
    'haveWeapon': False
]

while not quit:

render(game,current)
response = getInput()
current = update(response,game,current,flags)

if response == 'QUIT':
quit = True




if __name__ == '__main__':
main()
