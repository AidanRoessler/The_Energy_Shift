'''

Imports functions from api.py,
Written by: Liam Keane, Aidan Roesller, Rachel Tan

'''
from api import *
# The command line program should allow the user to keep selecting functions until they decide to quit.
# what data will be expected by each function, in what format, etc. It should also demonstrate what data the function calls will return (and in what format).

# display a list of possible functions and how to properly call them
print("Please enter one of the following function names: \n isolateDatasetByState \n isolateDatasetByMonth \n isolateDatasetByCategoryOfProduction \n getTotalEnergyForCategoryOfProduction \n getEnergyForState \n getEnergyForMonth \n \n ")

# scan user's input
userInput = input()
# if input is valid, call the specified function

# print the function's output to the terminal