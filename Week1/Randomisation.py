
import random


#random.random(): Returns a random float between 0.0 and 1.0.

print(random.random())

#random.randint(a, b): Returns a random integer between a and b (inclusive).

print(random.randint(1,10))

#random.randrange(start, stop[, step]): Returns a randomly selected element from range(start, stop, step).

print(random.randrange(0, 10, 2))

#random.choice(sequence): Returns a random element from a non-empty sequence (like a list or string).
colors = ['red', 'blue', 'green']
print(random.choice(colors))
colors = ['rock', 'paper', 'scissors']
print(random.choice(colors))

#random.shuffle(sequence): Shuffles the elements of a list in place.

cards = ['Ace', 'King', 'Queen', 'Jack','jisan']
random.shuffle(cards)
print(cards)
#random.sample(sequence, k): Returns a list of k unique random elements from the sequence.


numbers = range(1, 50)
print(random.sample(numbers, 5))
#random.seed(a=None): Seeds the random number generator, making the random results reproducible.
random.seed(42)
print(random.random())

#random.uniform(a, b): Returns a random float N such that a <= N <= b.
print(random.uniform(1.0, 10.0))
#strong random numbers, suitable for managing data such as passwords and tokens.
import secrets
print(secrets.token_bytes(16))


#secrets.choice(sequence): Returns a securely random element from the sequence.
i=input("give your choice");
print (i)
secure_random = secrets.SystemRandom()
print(secure_random.choice(['rock', 'paper', 'scissors']))

import random


def roll_dice(num_dice=2):
    return [random.randint(1, 6) ]

# Simulate rolling two dice
print("You rolled:", roll_dice(2))

'''
Basic Random Functions:

random.random(): Generates a random float between 0.0 and 1.0.
random.randint(a, b): Generates a random integer between a and b (inclusive).
random.randrange(start, stop[, step]): Chooses a random number from the specified range.
random.choice(sequence): Selects a random element from a sequence.
random.shuffle(sequence): Shuffles the elements of a list in place.
random.sample(sequence, k): Returns k unique random elements from the sequence.
random.seed(a=None): Seeds the random number generator for reproducibility.
random.uniform(a, b): Generates a random float between a and b.
Secure Random Functions:

secrets.token_bytes(16): Generates a secure random byte string.
secrets.choice(sequence): Selects a secure random element from a sequence.
Dice Rolling Function:

The function roll_dice currently returns only one dice roll due to the incorrect list construction. 
To roll the specified number of dice, it should be adjusted to include a loop to generate multiple dice rolls.

'''
