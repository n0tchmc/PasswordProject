# こにちわ！Programmer ~ Michael Reyes
import string
import random
import time

print("Welcome to Michael's password generator!\nThis program works by asking you to type in a 5 - 10 character "
      "long word.\nAfterwards, a strong password will be created based on that word."
      "\nAll passwords generated on here will not be logged or saved, your generated passwords will not"
      " be revealed.")

# Asks for the word to be inputted, this process makes sure it is between 5 - 10 character mark.
intro = 1
while intro == 1:
    word = input("Please type in a 5 - 10 character word: ")
    if len(word) < 5:
        print("That word is less than 5 characters, please try again!")
    if len(word) > 10:
        print("That word is greater than 10 characters, please try again!")
    if 5 <= len(word) <= 10:
        print("Creating password!")
        intro = 0

# Password generation functions.
if len(word) == 5:
    # Grabs each letter of the word, and capitalizes the 2nd and 4th letter.
    x1 = word[0]
    x2 = word[1].swapcase()
    x3 = word[2]
    x4 = word[3].swapcase()
    x5 = word[4]
    # Randomly generates and chooses 2 digits, 2 punctuation marks, and 2 letters.
    x6 = random.choice(string.digits)
    x7 = random.choice(string.digits)
    x8 = random.choice(string.punctuation)
    x9 = random.choice(string.punctuation)
    x10 = random.choice(string.ascii_letters)
    x11 = random.choice(string.ascii_letters)
    x12 = random.choice(string.punctuation)
    x13 = random.choice(string.digits)
    # Compiles each character of the word and each randomly generated character into a list, then shuffles it.
    # Following that, the list is then recombined to generate the completed password.
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)
if len(word) == 6:
    # Does basically the same thing as the previous function, only with more characters!
    x1 = word[0]
    x2 = word[1].swapcase()
    x3 = word[2]
    x4 = word[3].swapcase()
    x5 = word[4].swapcase()
    x6 = word[5]
    # More random generations!
    x7 = random.choice(string.digits)
    x8 = random.choice(string.digits)
    x9 = random.choice(string.punctuation)
    x10 = random.choice(string.punctuation)
    x11 = random.choice(string.ascii_letters)
    x12 = random.choice(string.digits)
    x13 = random.choice(string.punctuation)
    # You get the idea of what's going on lol
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)
if len(word) == 7:
    # Really self explanatory at this point lol
    x1 = word[0]
    x2 = word[1].swapcase()
    x3 = word[2]
    x4 = word[3].swapcase()
    x5 = word[4].swapcase()
    x6 = word[5]
    x7 = word[6].swapcase()
    # My Generation - The Who
    x8 = random.choice(string.digits)
    x9 = random.choice(string.digits)
    x10 = random.choice(string.punctuation)
    x11 = random.choice(string.punctuation)
    x12 = random.choice(string.digits)
    x13 = random.choice(string.digits)
    # Everyday I'm shuffling
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)
if len(word) == 8:
    # Really self explanatory at this point lol
    x1 = word[0].swapcase()
    x2 = word[1]
    x3 = word[2]
    x4 = word[3]
    x5 = word[4].swapcase()
    x6 = word[5]
    x7 = word[6].swapcase()
    x8 = word[7].swapcase()
    # gen z
    x9 = random.choice(string.digits)
    x10 = random.choice(string.digits)
    x11 = random.choice(string.punctuation)
    x12 = random.choice(string.punctuation)
    x13 = random.choice(string.digits)
    # miami dade county
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)
if len(word) == 9:
    # Really self explanatory at this point lol
    x1 = word[0].swapcase()
    x2 = word[1]
    x3 = word[2].swapcase()
    x4 = word[3]
    x5 = word[4].swapcase()
    x6 = word[5]
    x7 = word[6]
    x8 = word[7].swapcase()
    x9 = word[8]
    # pepsi generation
    x10 = random.choice(string.digits)
    x11 = random.choice(string.digits)
    x12 = random.choice(string.punctuation)
    x13 = random.choice(string.punctuation)
    # michael jackson shuffle
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)
if len(word) == 10:
    # haha funny numbers got capitalized
    x1 = word[0].swapcase()
    x2 = word[1]
    x3 = word[2].swapcase()
    x4 = word[3]
    x5 = word[4].swapcase()
    x6 = word[5]
    x7 = word[6].swapcase()
    x8 = word[7]
    x9 = word[8]
    x10 = word[9].swapcase()
    # these comments are more random than these random generations
    x11 = random.choice(string.digits)
    x12 = random.choice(string.digits)
    x13 = random.choice(string.punctuation)
    x14 = random.choice(string.punctuation)
    # i coded this at 12 am which probably explains my randomness right now
    generated = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6), str(x7), str(x8), str(x9), str(x10), str(x11),
                 str(x12), str(x13), str(x14)]
    random.shuffle(generated)
    password = "".join(generated)
    print("Your generated password is: \"", password, "\"")
    print("Note: Password is within the first and last quotation marks.")
    print("Program will close in 1 minute.")
    time.sleep(60)

