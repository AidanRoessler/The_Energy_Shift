from flask import Flask
'''

API Devliverable

'''
app = Flask(__name__)

# First line is summary

def getTotalEnergyByCategoryOfProduction(categoryOfProduction):
    """Sums energy use across all states and months with a specified category of production
    
    Retrieves columns pertaining to the given category of production for all states and months, and 

    Args:
        categoryOfProduction: a string indicating a specified category of energy production
    
    Returns:
        returns an integer indicating the sum of total energy production from the provided energy source

    """

    return 0

def getEnergyByState():
    """
    
    """

    return 0

def getEnergyByMonth():
    """
    
    """
    
    return 0

if __name__ == "__main__":
    app.run(debug=True)