import psycopg2
# import os
# from dotenv import load_dotenv


class EnergyProductionAPI:

    def __init__(self, filename):
        '''
        Read in our csv data set and initialize a list of all states as an instance variable
        '''

        self.conn = psycopg2.connect(
            database='keanel', user='keanel', password="summer494spring")

        self.cursor = self.conn.cursor()

        self.state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
                           'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
                           'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                           'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                           'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                           'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
                           'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                           'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
                           'Washington', 'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming']

        self.month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                           'July', 'August', 'September', 'October', 'November', 'December']

    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "Alabama"
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins', 'MN'
            
    """

    def getEnergyForState(self, state):
        """Sums all electricity generation by all catagories in a given state

        Retrieves columns in the current working dataset pertaining to each category of electricity 
        generation for a single state, sums the values in these columns and returns that number

        Args:
            state: a string indicating the specified state (must spell the states name out,
            no abbreviations like MN)

        Returns:
            returns a float indicating the sum of the total electricity generation for the
            provided state      
        """

        # Try to run the function as normal
        try:
            # If the state is a valid input run the function as normal
            if state in self.state_list:

                queryStr = f"SELECT total FROM {state} WHERE categoryofproduction = 'All fuels';"

                self.cursor.execute(queryStr)

                stateEnergySumList = self.cursor.fetchall()

                print(stateEnergySumList)

                stateEnergySum = stateEnergySumList[0][0]

                return stateEnergySum

            # If the state inputted is not valid, raise an exception
            else:
                raise ("Invalid state input")

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except Exception:
            return 'Please enter the full name of a state in the United States (abbreviations are not accepted)'
    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "Alabama"
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins', 'MN'       
    
    """

    def getTotalRenewableEnergyByState(self, state):
        '''
            Sums and returns the total amount of renewable energy for the specified state

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
        # Old command line output
        # print("The total energy generated renewable was 14 billion KWH")

        # Try to run the function as normal
        try:
            if state in self.state_list:
                # builds the query string with the user's input
                queryStr = f"SELECT SUM(total) FROM {state} WHERE categoryofproduction <> 'All fuels';"
                self.cursor.execute(queryStr)

                renewableEnergySumList = self.cursor.fetchall()
                print(renewableEnergySumList)

                renewableEnergySum = renewableEnergySumList[0][0]

                return renewableEnergySum

            # If the state inputted is not valid, raise an exception
            else:
                raise ("Invalid state input")

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except Exception:
            return "Please enter the full name of a state in the United States (abbreviations are not accepted)"

    """
    Equivalence Classes:
        -A valid state (only in America)
            -Input: 'Alabama'
        
        -A string that is not a state
            -Input: 'Montreal' or '12' or 'WI'
    """

    def getTotalEnergyForStateByMonth(self, state):
        """Retrieves monthly total electricity generation throughout the year for a given state

        Retrieves each individual column in the row labeled 'All fuels', returning those numbers in a sequential
        list of floats.

        Args:
            state: a string indicating one of the 50 states in America
        Returns:
            returns a dictionary where the keys indicate the month while the values are floats indicating the sum of 
            the total electricity generation for each month in the year for the given state. 
            Note: the list will be in sequential order (Jan, Feb, ... Dec)

        """
        try:
            if state in self.state_list:

                # builds the query string with the user's input
                queryStr = f"SELECT january, february, march, april, may, june, july, august, september, october, november, december FROM {state} WHERE categoryofproduction = 'All fuels';"

                self.cursor.execute(queryStr)

                listOfSumsForMonths = self.cursor.fetchall()
                print(listOfSumsForMonths[0])

                dictOfSumsForMonths = {}
                for i in range(12):
                    dictOfSumsForMonths[self.month_list[i]
                                        ] = listOfSumsForMonths[0][i]

                return dictOfSumsForMonths

            else:
                raise ("Invalid state input")

        except Exception:
            return 'Please enter the full name of a state in the United States (abbreviations are not accepted)'

    """
        Equivalence Classes:
        -Valid state (as a string):
            -Input: 'Wisconsin'
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins' or 'MN'   
    """

    def getEnergyByCategoryForState(self, state):
        """
        Returns the total energy by category of energy for a specified state 

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

        try:
            if state in self.state_list:

                # builds the query string with the user's input
                queryStr = f"SELECT categoryofproduction, total FROM {state} WHERE categoryofproduction != 'All fuels';"

                self.cursor.execute(queryStr)

                listOfSumsForCategories = self.cursor.fetchall()
                print(listOfSumsForCategories)

                dictOfSumsForCategories = {}
                for category in listOfSumsForCategories:
                    print(category)
                    dictOfSumsForCategories[category[0]] = category[1]

                return dictOfSumsForCategories

            # If the state inputted is not valid, raise an exception
            else:
                print("else")
                raise ("Invalid state input")

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except Exception:
            print("exception")
            return 'Please enter the full name of a state in the United States (abbreviations are not accepted)'


if __name__ == "__main__":
    energy = EnergyProductionAPI(
        '../Data/total_energy_production_modified.csv')

    print('Database opened successfully')

    # energy.getEnergyByCategoryForState('Wisconsin')
    print(energy.getTotalEnergyForStateByMonth('Colorado'))
    print(energy.getEnergyForState('Colorado'))
    print(energy.getTotalRenewableEnergyByState('Colorado'))

    energy.cursor.close()
