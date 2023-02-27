import psycopg2
import psqlConfig


class EnergyProductionAPI:

    def __init__(self):
        '''
        Read in our csv data set and initialize a list of all states as an instance variable
        '''

        self.conn = psycopg2.connect(
            database=psqlConfig.database, user=psqlConfig.user, password=psqlConfig.password)

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

        self.abbreviation_to_state_dictionary = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
                                                 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
                                                 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
                                                 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
                                                 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan',
                                                 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
                                                 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
                                                 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota',
                                                 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
                                                 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
                                                 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
                                                 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}

    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "WI" or "wi" or "Wi" or even "wI"
        
        -A not valid state (either as a string or another data-types)
            -Input: 'Wisconsin' or 56 or 'Test' or True or 'Bilbo Baggins'
            
    """

    def getEnergyForState(self, stateAbbreviation):
        """Sums all electricity generation by all catagories in a given state

        Retrieves columns in the current working dataset pertaining to each category of electricity 
        generation for a single state, sums the values in these columns and returns that number

        Args:
            state: a string indicating an abbreviation of a specified state

        Returns:
            returns a float indicating the sum of the total electricity generation for the
            provided state      
        """

        # Try to run the function as normal
        try:
            # Turn abbreviation into valid full name of state here:
            fullStateName = self.abbreviation_to_state_dictionary[stateAbbreviation]

            # If the state is a valid input run the function as normal
            if fullStateName in self.state_list:

                # Build the query string and execute the query
                queryStr = f"SELECT total FROM {fullStateName} WHERE categoryofproduction = 'All fuels';"

                self.cursor.execute(queryStr)

                stateEnergySumList = self.cursor.fetchall()

                # Extract the sum out of list of a single tuple returned from the query
                stateEnergySum = stateEnergySumList[0][0]

                return stateEnergySum

            # If the state inputted is not valid, raise an exception
            else:
                raise Exception('invalid input')

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except TypeError:
            return 'Invalid input. Please enter a state abbreviation not a (full name)'
    """
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "WI" or "wi" or "Wi" or even "wI"
        
        -A not valid state (either as a string or another data-types)
            -Input: 'Wisconsin' or 56 or 'Test' or True or 'Bilbo Baggins' 
    
    """

    def getTotalRenewableEnergyByState(self, stateAbbreviation):
        '''
            Sums and returns the total amount of renewable energy for the specified state

            Retrieves columns in the current working dataset pertaining to each category of renewable 
            electricity generation for each state in a specific month, sums the values in these columns 
            and returns that number

            Args:
                state: a string indicating an abbreviation of a specified state

            Returns:
                returns an integer indicating the sum of the total electricity generation from renewable sources 
                for the current state in the current working dataset

        '''

        # Try to run the function as normal
        try:
            if stateAbbreviation in self.abbreviation_to_state_dictionary:

                # Turn abbreviation into valid full name of state here:
                fullStateName = self.abbreviation_to_state_dictionary[stateAbbreviation]

                # If the state is a valid input run the function as normal

                # Build the query string and execute the query
                queryStr = f"SELECT SUM(total) FROM {fullStateName} WHERE categoryofproduction <> 'All fuels';"
                self.cursor.execute(queryStr)

                renewableEnergySumList = self.cursor.fetchall()

                # Extract the sum out of list of a single tuple returned from the query
                renewableEnergySum = renewableEnergySumList[0][0]

                return renewableEnergySum

                # If the state inputted is not valid, raise an exception
            else:
                raise Exception('invalid input')

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except KeyError:
            return 'Invalid input. Please enter a state abbreviation not a (full name)'

    """
    Equivalence Classes:
        -A valid state (only in America)
            -Input: "WI" or "wi" or "Wi" or even "wI"
        
        -A string that is not a state
            -Input: 'Montreal' or '12' or 'WI'
    """

    def getTotalEnergyForStateByMonth(self, stateAbbreviation):
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
            # Turn abbreviation into valid full name of state here:
            fullStateName = self.abbreviation_to_state_dictionary[stateAbbreviation]

            # If the state is a valid input run the function as normal
            if fullStateName in self.state_list:

                # builds the query string and execute the query
                queryStr = f"SELECT january, february, march, april, may, june, july, august, september, october, november, december FROM {fullStateName} WHERE categoryofproduction = 'All fuels';"

                self.cursor.execute(queryStr)

                listOfSumsForMonths = self.cursor.fetchall()

                # Create the result dictionary
                dictOfSumsForMonths = {}

                # Extract the value of each month stored in the single tuple returned from the query
                for i in range(12):
                    dictOfSumsForMonths[self.month_list[i]
                                        ] = listOfSumsForMonths[0][i]

                return dictOfSumsForMonths

            else:
                raise Exception('invalid input')

        except TypeError:
            return 'Invalid input. Please enter a state abbreviation not a (full name)'

    """
        Equivalence Classes:
        -Valid state (as a string):
            -Input: 'Wisconsin'
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins' or 'MN'   
    """

    def getEnergyByCategoryForState(self, stateAbbreviation):
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
            # Turn abbreviation into valid full name of state here:
            fullStateName = self.abbreviation_to_state_dictionary[stateAbbreviation]

            # If the state is a valid input run the function as normal
            if fullStateName in self.state_list:

                # Builds the query string and executes it
                queryStr = f"SELECT categoryofproduction, total FROM {fullStateName} WHERE categoryofproduction != 'All fuels';"

                self.cursor.execute(queryStr)

                listOfSumsForCategories = self.cursor.fetchall()

                """Creates a dictionary from the result of the query and where the keys are months 
                and the values are the total amount of renewable energy produced in that month"""
                dictOfSumsForCategories = {}

                for category in listOfSumsForCategories:
                    dictOfSumsForCategories[category[0]] = category[1]

                return dictOfSumsForCategories

            # If the state inputted is not valid, raise an exception
            else:
                raise Exception('invalid input')

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        # and returning false
        except TypeError:
            return 'Invalid input. Please enter a state abbreviation not a (full name)'


if __name__ == "__main__":
    print('Database connection successful')
