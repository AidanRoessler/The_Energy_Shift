
from flask import Flask

app = Flask(__name__)

def isolateDatasetByState(state):
    """
        Prunes the working dataset down by the given State (ie. only Wisconsin's data)
        
        Retrieves all columns in the current working data set containing the given State, 
        regardless of category of production.
        
        Args:
            state: a string containing the specified state in written format

        Returns:
            A paired down version of the data base containing only the columns labeled the specific state(s).
    """
    
    print("The database has be paried to only include", state)
    
    return 0

def isolateDatasetByMonth(month):
    """
        Pairs current dataset down by the given month(s) (ie. the data only for March, May, or/and October)
        
        Retrieves all columns in the current working datset 
        for each state that containing the given month.

        Args:
            month: an integer indicating the specified month(It must be written in the format of month + year, 
            with no non-numeric symbols in between. For example: 2021/1: 012021; 2020/12: 122020)
        
        Returns:
            A paired down version of the data base containing only the columns labeled the specific month(s).

        
    """

    print("The database has be paried to only include", month)
    
    return 0

def isolateDatasetByCategoryOfProduction(categoryOfProduction):
    '''
        Pairs data down to just a single catagory of production 

        Retrives all columns in the current working dataset that contain the category of 
        production specified in the parameter

        Args:
            categoryOfProduction: a string indicating a specified category of energy production
        
        Returns:
            A paired down version of the data base containing only the columns of the category
            specified 

    '''

    print("The database has be paried to only include", categoryOfProduction)

    return 0

def getTotalEnergyForCategoryOfProduction(categoryOfProduction):
    """Sums energy use across all states and months with a specified category of production
    
    Retrieves columns in the current working dataset pertaining to the given category of
    production for all states and months

    Args:
        categoryOfProduction: a string indicating a specified category of energy production
    
    Returns:
        returns an integer indicating the sum of total energy production from the provided energy source

    """

    print()

    return 0

def getEnergyForState(state):
    """Sums all electricity generation by all catagories in a given state

    Retrieves columns in the current working dataset pertaining to each category of electricity 
    generation for a single state, sums the values in these columns and returns that number

    Args:
        state: a string indicating the specified state (must spell the states name out,
        no abbreviations like MN)
    
    Returns:
        returns an integer indicating the sum of the total electricity generation for the
        provided state

    """

    return 0

def getEnergyForMonth(month):
    """Sums all electricity generation by all catagories in a given month
    
    Retrieves columns in the current working dataset pertaining to each category of electricity
    generation for each state in a specific month, sums the values in these columns and returns 
    that number
    
    Args:
        month: an integer indicating the specified month(It must be written in the format of month + year, 
        with no non-numeric symbols in between. For example: 2021/1: 012021; 2020/12: 122020)
        
    Returns:
        returns an integer indicating the sum of the total electricity generation for the
        provided month
    
    """
    
    return 0

def getRenewableEnergy():
    '''
        Sums and returns the total amount of renewable energy for the current state that the dataset has 
        been "paired down to" 

        Retrieves columns in the current working dataset pertaining to each category of renewable 
        electricity generation for each state in a specific month, sums the values in these columns 
        and returns that number


        Returns:
            returns an integer indicating the sum of the total electricity generation from renewable sources 
            for the current state in the current working dataset

    '''
    return 0

@app.route("/")
def home():
    return "<h1> Home Page!! <h1>"



if __name__ == '__main__':
    app.run(debug=True)
