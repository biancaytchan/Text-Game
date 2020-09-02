#set up global variables
player = {'location': 'cabin'}

game_map = {'cabin':{'east':'yard'}, 'yard':{'east':'forest', 'south':'barn','west':'cabin'}, 'forest':{'west': 'yard'}, 'barn':{'north': 'yard'}}

descriptions = {'cabin': 'You are in a quaint cabin, there is a door to the east.',
'yard':'You find yourself in a beautiful garden. There is a forest to the east, a barn to the south, and a cabin to the west.',
'forest':'You are in a spooky forest. The yard is back to the west.',
'barn': 'You are in a barn. There is a treasure chest in the middle of the room.'}

directions = ['north','east','south','west']

game_over = False
treasure_acquired = False
#describe the player's current surroundings
def look(location):
  print(descriptions[location])
#update the player's location
def move(direction):
  global game_over, treasure_acquired
  if direction in game_map[player['location']]:
    player['location'] = game_map[player['location']][direction]
    if player['location'] == 'cabin' and treasure_acquired:
      print("You returned the treasure safely. You win!")
      game_over = True
      return
    look(player['location'])
    if player['location'] == 'barn' and not treasure_acquired:
      print("You open the chest and collect the treasure. You should get the treasure back to the cabin!")
      treasure_acquired = True
  else:
    print("You cannot go {}.".format(direction))
#handle player input until the game ends

def main():
  global game_over
  look(player['location'])
  while not game_over:
    choice = input("What would you like to do?\n")
    if choice in directions:
      move(choice)
    elif choice == 'look':
      look(player['location'])
    elif choice == 'quit':
      print("Goodbye.")
      game_over = True
    elif choice == 'help':
      print("\nInstructions:\n")
      print("Enter 'north', 'east', 'south', or 'west' to move.")
      print("Enter 'look' to view the room.")
      print("Type 'quit' to exit the game.\n")
    else:
      print("I do not understand {}.".format(choice))
      
if __name__ == '__main__':
  main()