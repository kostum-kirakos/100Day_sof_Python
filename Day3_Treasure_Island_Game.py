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

# Initial choice
print("\nYou find a split way on the island. Do you want to go left or right?")
choice1 = input("Type 'left' or 'right': ").lower()

if choice1 == 'left':
    print("\nYou've chosen the left path.")
    print("You come across a deep ravine. You can't proceed this way.")
    print("Game Over.")
elif choice1 == 'right':
    # Candy choice
    print("\nYou meet an aged witch who offers you two candies, one red and the other blue.")
    choice2 = input("Which candy do you want to take, 'red' or 'blue'? ").lower()

    if choice2 == 'blue':
        print("\nThe blue candy was poisonous.")
        print("Game Over.")
    elif choice2 == 'red':
        # Door choice
        print("\nAfter you take the red candy, the witch gives you a key to open one of three doors: wooden, steel, and gold.")
        choice3 = input("Which door do you want to open, 'wooden', 'steel', or 'gold'? ").lower()

        if choice3 == 'wooden':
            print("\nThe wooden door leads to a room filled with fire. You're burned alive.")
            print("Game Over.")
        elif choice3 == 'steel':
            print("\nThe steel door leads to a dark room with hungry beasts. They devour you.")
            print("Game Over.")
        elif choice3 == 'gold':
            print("\nYou open the golden door and find the treasure chest.")
            print("Congratulations! You've found the treasure and won the game!")
        else:
            print("\nInvalid choice. You're trapped forever.")
            print("Game Over.")
    else:
        print("\nInvalid choice. The witch curses you.")
        print("Game Over.")
else:
    print("\nInvalid choice. You're lost on the island forever.")
    print("Game Over.")













