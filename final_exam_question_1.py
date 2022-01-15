#This is a guess number game.

guessesTaken = 0

secret_number = 777

print(
"""
+====================================+
|Welcome to my game, muggle!         |
|Enter an integer number             |
|and guess what number I've          |
|picked for you.                     |
|So, what is the secret number?      |
+====================================+
""")

guess = int(input("Enter an integer number: "))

if guess != secret_number: # If statement to check if the numbers match
    print("Ha ha! You're stuck in my loop!")
    
    if guess < secret_number:
        print("your guess is too low.")

    if guess > secret_number:
        print("your guess is too high.")
    
    while True:
        input("Enter an integer number: ") # Loop never end...
        
print("Well done, muggle! You are free now.") # If the program made it here, that means the user's number matched

