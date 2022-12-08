# app.py
# This is a program to memorize the Planck's Constant.
# also os and sys is for clearing the terminal.
import time
import os, sys
PLANCKS_CONSTANT = "6.62607015"

# Functions
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.75)

def lose():
    print("You lost!")
    exit()

def win():
    print("Hey, you won!")
    exit()

# First Round
print_slow("6.6")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.6":
    lose()
# Second Round
print_slow("6.62")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.62":
    lose()
# Third Round
print_slow("6.626")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.626":
    lose()
# Forth Round
print_slow("6.6260")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.6260":
    lose()
# Fifth Round
print_slow("6.62607")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.62607":
    lose()
# Sixth Round
print_slow("6.626070")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.626070":
    lose()
# Seventh Round
print_slow("6.6260701")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.6260701":
    lose()
# Eighth Round
print_slow("6.62607015")
os.system("cls")
PLANCKS_CONSTANT = input()
os.system("cls")
if not PLANCKS_CONSTANT == "6.62607015":
    lose()
if PLANCKS_CONSTANT == "6.62607015":
    win()


# end of code