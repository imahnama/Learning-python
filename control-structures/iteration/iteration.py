# For loop processes each item in a sequence, used with sequence data types - strings, tuples and lists

for x in range(13):
    # ('\t')tab character makes the output align nicely.
    print(x, '\t', 2**x)

    # While STATEMENT
# choose a for loop(definite iteration) if you know, before you start the max no of times u are looping
# if u are required to repeat some computation until some condition is met and u cant calculate in advance when it will happen choose While loop(indefinite iteration)

# Following program implements a simple guessing game

import random    #import the random module

number = random.randrange(1, 1000) #Get random n0 btwn [1 and 1000]
guesses = 0
guess = int(input("Guess my number btwn 1 and 1000"))

while guess != number:
    guesses +1
    if guess > number:
        print(guess, "is too high")
    elif guess < number:
        print(guess, "is too low")
    guess = int(input("Guess again:"))

print("\n\nGreat, you got it in", guesses,  "guesses!")
