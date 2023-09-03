# This program tests the compatibility between two people based on their names.
print("Welcome to The Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# Convert names to lowercase for consistent comparison.
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

# Combine both names for letter counting.
both_names = lowercase_name1 + lowercase_name2

# Count the letters in the word 'true' in both names.
letter1 = both_names.count('t')
letter2 = both_names.count('r')
letter3 = both_names.count('u')
letter4 = both_names.count('e')

# Calculate the first numerical score as a string.
firts_num = str(letter1 + letter2 + letter3 + letter4)

# Count the letters in the word 'love' in both names.
letter1_1 = both_names.count('l')
letter2_1 = both_names.count('o')
letter3_1 = both_names.count('v')
letter4_1 = both_names.count('e')

# Calculate the second numerical score as a string.
second_num = str(letter1_1 + letter2_1 + letter3_1 + letter4_1)

# Calculate the final compatibility score as an integer.
score = int(firts_num + second_num)

# Determine the relationship compatibility based on the score.
if score > 90 or score < 10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

