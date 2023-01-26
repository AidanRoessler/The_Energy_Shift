'''

Imports functions from api.py,
Written by: Liam Keane, Aidan Roessler, Rachel Tan

'''
from api import *
# The command line program should allow the user to keep selecting functions until they decide to quit.
# what data will be expected by each function, in what format, etc. It should also demonstrate what data the function calls will return (and in what format).
functionNames = ["isolateDatasetByState", "isolateDatasetByMonth", "isolateDatasetByCategoryOfProduction", "getTotalEnergyForCategoryOfProduction", "getEnergyForState", "getEnergyForMonth", "getRenewableEnergy"]
# display a list of possible functions and how to properly call them
while(1):
    print("Please enter one of the following function names: \n ---")
    for function in functionNames:
        print(function)

    print("---")
    print("Note: type 'exit' to stop the program")
    # scan user's input
    userInput = input()
    # if input is valid, call the specified function
    if userInput in functionNames:
        match userInput:
            case "isolateDatasetByState":
                userInputedState = input("This function takes a string as a parameter and returns a list of objects that corresponds to the specified state. \nPlease enter a state: ")
                isolateDatasetByState(userInputedState)
            case "isolateDatasetByMonth":
                userInputedMonth = input("This function takes an integer from 1-12 (inclusive) representing a month as a parameter and returns a list of objects that corresponds to the specified month \nPlease enter a month: ")
                userInputedMonth = int(userInputedMonth)
                isolateDatasetByMonth(userInputedMonth)
            case "isolateDatasetByCategoryOfProduction":
                userInputedSource = input("This function takes a string as a parameter and returns a list of objects that corresponds to the specified category of production. \nPlease enter a specific source of energy production: ")
                isolateDatasetByCategoryOfProduction(userInputedSource)
            case "getTotalEnergyForCategoryOfProduction":
                userInputedSource = input("This function takes a string as a parameter and returns the total energy generated via that source as an int in KWH. \nPlease enter a specific source of energy production: ")
                getTotalEnergyForCategoryOfProduction(userInputedSource)
            case "getEnergyForState":
                userInputedState = input("This function takes a string as a parameter and returns the total energy generated in that State as an int in KWH. \nPlease enter a state: ")
                getEnergyForState(userInputedState)
            case "getEnergyForMonth":
                userInputedMonth = input("This function takes an integer from 1-12 (inclusive) representing a month as a parameter and returns the total energy generated during that month as an int in KWH. \nPlease enter a month: ")
                userInputedMonth = int(userInputedMonth)
                getEnergyForMonth(userInputedMonth)
            case "getRenewableEnergy":
                userInputedRenewableSource = input("This function returns the total energy generated via renewable sources as an int in KWH.")
                getRenewableEnergy()

    elif userInput == "exit":
        print("Exiting the program")
        break
    else:
        print("That is not a valid function name. ")
        continue
    
    # prompt the user if they would like to continue
    userChoice = input("Would you like to continue? Y/N: ")

    if userChoice.lower()== "n":
        print("Exiting the program")
        break
