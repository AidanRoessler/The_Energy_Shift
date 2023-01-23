from flask import Flask
'''

API Deliverable

'''

app = Flask(__name__)

def getTotalEnergyByCategoryOfProduction(categoryOfProduction):
    """Sums energy use across all states and months with a specified category of production
    
    Retrieves columns pertaining to the given category of production for all states and months, and 

    Args:
        categoryOfProduction: a string indicating a specified category of energy production
    
    Returns:
        returns an integer indicating the sum of total energy production from the provided energy source

    """

    return 0

def getEnergyByState(state):
    """Sums all electricity generation by all catagories in a given state

    Retrieves columns pertaining to each category of electricity generation for a single state,
    sums the values in these columns and returns that number

    Args:
        state: a string indicating the specified state (must spell the states name out,
        no abbreviations like MN)
    
    Returns:
        returns an integer indicating the sum of the total electricity generation for the
        provided state

    """

    return 0

def getEnergyByMonth(month):
    """Sums all electricity generation by all catagories in a given month
    
    Retrieves columns pertaining to each category of electricity generation for each state in a specific month,
    sums the values in these columns and returns that number
    
    Args:
        month: an <int>number indicating the specified month（It must be written in the format of month + year, 
        with no non-numeric symbols in between. For example: 2021/1: 012021; 2020/12: 122020）
        
    Returns:
        returns an integer indicating the sum of the total electricity generation for the
        provided month
    
    """
    
    return 0


if __name__ == '__main__':
    app.run(debug=True)
