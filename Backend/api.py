import csv


class EnergyProductionAPI:

    def __init__(self, filename):

        with open(filename, newline='') as energyFile:
            self.energy_production = list(csv.DictReader(energyFile))

    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "Alabama"
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins', 'MN'       
    
    """
    def isolateDatasetByState(state):
        """
            Prunes the working dataset down by the given State (ie. only Wisconsin's data)

            Retrieves all columns in the current working data set containing the given State, 
            regardless of category of production.

            Args:
                stateList: a string containing specified state

            Returns:
                A list of data that contains all of the cells that correspond to the specified state.
        """

        # print("The database has be paired down to only include", stateList)

        return 0

    """
    Equivalence Classes:
        -List of valid months in the integer format specified in the Args documentation below
            -Input: [12,2, ... ,10]
        
        -A list with one or more invalid month integers 
            -Input: [13, 25, -6, 0]
        
        -A list with one or more invalid month integers that are different data types:
            -Input: ['Bilbo Baggins', 'Foo', 10.56, True]

    """
    def isolateDatasetByMonth(monthList):
        """
            Pairs current dataset down by the given month (ie. the data only for March, May, or/and October)

            Retrieves all columns in the current working dataset 
            for each state that containing the given month.

            Args:
                monthList: a list of integers indicating the specified month(A month integer must be written in the format of month + year, 
                with no non-numeric symbols in between. For example: January = 1, December = 12 )

            Returns:
                A list of data that contains all of the cells that correspond to the specified month.

        """
        # monthDictionary = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        #         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

        # if monthList not in monthDictionary.keys():
        #     print("Not a valid month. Please enter an integer from 1-12 (inclusive)")
        #     return 0

        # print("The database has be paired down to only include", monthDictionary[monthList])

        return 0

    """
    Equivalence Classes:
        -List of valid categories of production (as strings)
            -Input: ['Nuclear', ... 'All Fuels']
        
        -A list with one or more invalid catagories of production (either as invalid strings or other data types)
            -Input: ['Nucelar', 'Test', 56, True]
        
    """
    def isolateDatasetByCategoryOfProduction(categoryOfProductionList):
        '''
            Pairs data down to just a single category of production 

            Retrieves all columns in the current working dataset that contain the category of 
            production specified in the parameter

            Args:
                categoryOfProductionList: a list of strings indicating specified categories of energy production

            Returns:
                A list of data that contains all of the cells that correspond to the specified month.

        '''

        # print("The database has be paired down to only include", categoryOfProductionList)

        return 0

    """
    Equivalence Classes:
        -Valid category of production (as a string)
            -Input: 'Nuclear' or 'All Fuels'
        
        -An invalid catagory of production (either as invalid strings or other data types)
            -Input: 'Test' or 56 or True or 'Bilbo Baggins'
            
    """
    def getTotalEnergyForCategoryOfProduction(categoryOfProduction):
        """Sums energy use across all states and months with a specified category of production

        Retrieves columns in the current working dataset pertaining to the given category of
        production for all states and months

        Args:
            categoryOfProduction: a string indicating a specified category of energy production

        Returns:
         s   returns an integer indicating the sum of total energy production from the provided energy source

        """

        # print("The total energy generated by",
        #     categoryOfProduction, "was 14 billion KWH")

        return 0

    """ 
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "Alabama"
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins', 'MN'
            
    """
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

        # print("The total energy generated by", state, "was 14 billion KWH")

        return 0

    """
    Equivalence Classes:
        -A valid month (as an integer between 1-12)
            -Input: 12 or 10 or 1
        
        -An integer that does not represent a month
            -Input: 13 or 25 or -6 or 0
        
        -An invalid data types (not integer):
            -Input: 'Bilbo Baggins' or 'Foo' or 10.56 or True

    """
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

        # monthDictionary = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        #         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

        # if month not in monthDictionary.keys():
        #     print("Not a valid month. Please enter an integer from 1-12 (inclusive)")
        #     return 0

        # print("The total energy generated during", monthDictionary[month], "was 14 billion KWH")

        return 0

    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "Alabama"
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins', 'MN'       
    
    """
    def getRenewableEnergy(state):
        '''
            Sums and returns the total amount of renewable energy for the specfied state

            Retrieves columns in the current working dataset pertaining to each category of renewable 
            electricity generation for each state in a specific month, sums the values in these columns 
            and returns that number

            Args:
                state: a string indicating the specified state (must spell the states name out,
            no abbreviations like MN)

            Returns:
                returns an integer indicating the sum of the total electricity generation from renewable sources 
                for the current state in the current working dataset

        '''

        # print("The total energy generated renewable was 14 billion KWH")

        return 0


if __name__ == "__main__":
    energy = EnergyProductionAPI('data/total_energy_production_modified.csv')

    print(energy.energy_production)
