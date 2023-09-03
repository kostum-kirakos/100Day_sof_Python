print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

Q1 = input("you found a split way in the island do you want to go left or right?")
q1 = Q1.lower()
if q1 == 'left' :
  print("Game Over")
  exit
elif q1 == 'right' :
  Q2 = input("you meet an Aged witch she gives you to choose between two candy one red and the other is blue, which one you want to take?")
  q2 = Q2.lower()
  if q2 == 'blue':
    print("Game Over")
    exit
  elif q2 == 'red':
    Q3 = input("after you toke the candy she gaves you a key to open one of tree doors, wooden, steel ,and gold which one you go in? ")
    q3 = Q3.lower()
    if q3 == 'wooden' :
      print("Burned by fire")
      print("Game Over")
      exit
    elif q3 == 'steel' :
      print("Eaten by beasts")
      print("Game Over")
      exit
    elif q3 == 'gold':
      print("You found the treasure, You Win")
      exit
    
  


