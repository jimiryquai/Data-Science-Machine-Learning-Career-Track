# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random;

num = random.randint(1, 10);
guess = 0;

while guess != num:
    guess = int(input("Guess a number between 1 and 10: "));
    if guess == num:
        print("Congratulations! You guessed the number!");
        break;
    else:
        print("Sorry, that's not the number. Try again!");

