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
    def getEnergyByCategoryForState(state):
        """
        Returns the total renewable energy by category of renewable energy for a specified state 

        Retrieves columns in the current working dataset pertaining to the categories of renewable
        energy production for a specified state and sums up all of the values of the categories for
        each month's record and returns this data as a object where the keys are the category of 
        renewable energy production and the values are the summed value that was calculated

        Arguments:
            state: a string indicating a specified state (abbreviations like MN won't work)

        Returns:
            an object where the keys are the category of renewable energy production and the values
            are the total energy produced in that category in the specified state across all months
            of the year

        """

        print("Here is the total energy generated by each category for", state, 
             {"Solar": 100, "Wind": 200})

        return 0

    """
    NEEDED

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
    NEEDED

    Equivalence Classes:
        -A valid month (as an integer between 1-12)
            -Input: 12 or 10 or 1
        
        -An integer that does not represent a month
            -Input: 13 or 25 or -6 or 0
        
        -An invalid data types (not integer):
            -Input: 'Bilbo Baggins' or 'Foo' or 10.56 or True

    """
    def getEnergyByMonthForState(month):
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
    NEEDED

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
