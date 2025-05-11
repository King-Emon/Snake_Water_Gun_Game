# Snake, Water, Gun Game
import random

computer = random.choice([1, -1, 0])
playerStr = input("Enter your choice: ")
playerDist = {"S" : 1, "W" : -1, "G" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
player = playerDist[playerStr]

# By now we have 2 numbers (variables) player and computer

print(f"Player chose: {reverseDict[player]}\nComputer chose: {reverseDict[computer]}")

if player == computer:
  print("It's a tie!")
else:
  if(player == 1 and computer == -1):
    print("Player wins!")
  elif(player == 1 and computer == 0):
    print("Player Lose!")
  elif(player == -1 and computer == 1):
    print("Player Lose!")
  elif(player == -1 and computer == 0):
    print("Player Win!")
  elif(player == 0 and computer == 1):
    print("Player Win!")
  elif(player == 0 and computer == -1):
    print("Player Lose!")
  else:
    print("Something went wrong!")

