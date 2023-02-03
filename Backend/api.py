import csv
import pandas as pd
import numpy as np


class EnergyProductionAPI:

    def __init__(self, filename):

        with open(filename, newline='') as energyFile:
            self.energy_df = pd.read_csv(energyFile)
            
        self.state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
                           'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
                           'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                           'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 
                           'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                           'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
                           'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
                           'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
                           'Washington', 'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming']


    """
        Equivalence Classes:
        -Valid state (as a string):
            -Input: 'Wisconsin'
        
        -A not valid state (either as a string or another data-types)
            -Input: 56 or 'Test' or True or 'Bilbo Baggins' or 'MN'   
    """

    def getEnergyByCategoryForState(self, state):
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
        try:
            if state in self.state_list:
                state_only = self.energy_df.loc[(self.energy_df["Location"] == state)]
                state_only = state_only[state_only['Category of Production'].str.contains(
                    'All fuels') == False]
                state_only.drop(['Location', 'Category of Production'],
                                axis=1, inplace=True)
                state_only = state_only.sum(axis=1)
                state_only_list = state_only.to_list()
                
                return state_only_list
            else:
                raise("Invalid state input")
        except Exception as e:
            print('Please enter the full name of a state in the United States (abbreviations are not accepted)')
            print("Error:")
            print(e)
            return False
    """
    NEEDED

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
        try:
            if state in self.state_list:
                state_only = self.energy_df.loc[(self.energy_df["Location"] == state)
                                                & (self.energy_df["Category of Production"] == 'All fuels')]
                state_minus_strings = list(state_only)
                state_minus_strings.remove('Location')
                state_minus_strings.remove('Category of Production')

                state_minus_strings_sum = state_only[state_minus_strings].sum(axis=1)

                return state_minus_strings_sum.iloc[0]
            else:
                raise("Invalid state input")
        except Exception as e:
            print('Please enter the full name of a state in the United States (abbreviations are not accepted)')
            print("Error:")
            print(e)
            return False

    """
    Equivalence Classes:
        -A valid state (only in America)
            -Input: 'Wisconsin' or 'Colorado' or 'Minnesota'
        
        -A string that is not a state
            -Input: 'Montreal' or '12' or 'WI'
    """

    def getTotalEnergyForMonthByState(self, state):
        """Retrieves monthly total electricity generation throughout the year for a given state

        Retrieves each individual column in the row labeled 'All fuels', returing those numbers in a sequential
        list of floats.

        Args:
            state: a string indicating one of the 50 states in America
        Returns:
            returns a list of floats indicating the sum of the total electricity generation for each month
            in the year for the given state. Note: the list will be in sequential order (Jan, Feb, ... Dec)

        """
        try:
            if state in self.state_list:
                state_for_each_month = self.energy_df.loc[(self.energy_df["Location"] == state)
                                                        & (self.energy_df["Category of Production"] == 'All fuels')]

                return state_for_each_month.to_dict('records')[0]
            else:
                raise("Invalid state input")

        except Exception as e:
            print('Please enter the full name of a state in the United States (abbreviations are not accepted)')
            print("Error:")
            print(e)
            return False
    """
    NEEDED

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

        # print("The total energy generated renewable was 14 billion KWH")
        try:
            if state in self.state_list:

                state_only = self.energy_df.loc[(
                    self.energy_df["Location"] == state)]
                state_only = state_only[state_only['Category of Production'].str.contains(
                    'All fuels') == False]
                state_only.drop(
                    ['Location', 'Category of Production'], axis=1, inplace=True)
                state_only = state_only.sum(axis=1)
                state_only = state_only.sum(axis=0)

            return state_only
        
        except Exception as e:
            print("Please enter the full name of a state in the United States (abbreviations are not accepted)")
            print("Error")
            print(e)
            return False


if __name__ == "__main__":
    energy = EnergyProductionAPI('./Data/total_energy_production_modified.csv')
    # print(energy.getEnergyForState('Ohio'));
    # print(energy.getEnergyForState('Colorado'));
    # print(energy.getEnergyForState('Alabama'));
    print(energy.getTotalEnergyForMonthByState('Alabama'))
    # print(energy.getEnergyByCategoryForState('Wisconsin'))
    # print(energy.getTotalEnergyForMonthByState('Wisconsin'))
