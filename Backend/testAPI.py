import unittest
import api


class APITester(unittest.TestCase):
    """
    A suite of tests for the EnergyProductionAPI classes' methods
    Please note, your current working directory must be the Backend folder for all tests to work
    because otherwise api will not be imported 
    """

    # A note on asserting exceptions: instead of asserting if equal, it would pass the test when it raises a certain exception.

    def setUp(self):
        '''
        Set up the test methods by creating an instance of the EnergyProductionAPI class with our
        csv passed in as data
        '''
        self.energy_test = api.EnergyProductionAPI(
            '../Data/total_energy_production_modified.csv')
        self.maxDiff = None

    def test_validState_getEnergyForState(self):
        """
        Test to see if getEnergyForState() can successfully return the correct list of
        floats when given the valid input of 'Alabama'
        """
        input = "Alabama"
        result = self.energy_test.getEnergyForState(input)
        self.assertEqual(result, 142733.34)

    def test_invalidState_getEnergyForState(self):
        """
        Test to see if getEnergyForState() can successfully return a message to the user when
        their input is invalid
        """
        input = 56

        '''
        we probabaly don't need the result
        
        '''
        result = self.energy_test.getEnergyByCategoryForState(input)

        self.assertEqual(
            result, 'Invalid input. Please enter the full name of a valid US state (abbreviations not accepted)(first letter must be capitalized)')

    def test_validState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return the correct list of
        floats when given the valid input of 'Wisconsin'
        """
        input = 'Alabama'
        result = self.energy_test.getEnergyByCategoryForState(input)
        self.assertEqual(result, {'Other renewables': 3805.24, 'Conventional hydroelectric': 11520.8, 'Nuclear': 46036.5, 'Utility-scale photovoltaic': 494.0, 'All utility-scale solar': 494.0, 'All solar': 37.12})

    def test_invalidState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return a message to the user
        when their input is invalid
        """
        input = 56

        '''
        we probabaly don't need the result
        
        '''
        result = self.energy_test.getEnergyByCategoryForState(input)

        self.assertEqual(
            result, 'Invalid input. Please enter the full name of a valid US state (abbreviations not accepted)(first letter must be capitalized)')

    def test_validState_getTotalEnergyForStateByMonth(self):
        """
        Test to see if getTotalEnergyForStateByMonth() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalEnergyForStateByMonth(input)

        self.assertEqual(result, {'January': 12574.68, 'February': 11267.83, 'March': 10343.43, 'April': 8972.6, 'May': 11274.04, 'June': 12255.95, 'July': 13545.99, 'August': 13862.05, 'September': 12089.57, 'October': 11731.84, 'November': 12408.92, 'December': 12406.44})

    def test_invalidState_getTotalEnergyForStateByMonth(self):
        """
        Test to see if getTotalEnergyForStateByMonth() can successfully return a message to the user
        when their input is invalid
        """
        input = 'Montreal'

        '''
        we probably don't need the result
        
        '''
        result = self.energy_test.getTotalEnergyForStateByMonth(input)

        self.assertEqual(
            result, 'Invalid input. Please enter the full name of a valid US state (abbreviations not accepted)(first letter must be capitalized)')

    def test_validState_getTotalRenewableEnergyByState(self):
        """
        Test to see if getTotalRenewableEnergyByState() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalRenewableEnergyByState(input)
        self.assertEqual(result, 62387.66)

    def test_invalidState_getTotalRenewableEnergyByState(self):
        """
        Test to see if getTotalRenewableEnergyByState() can successfully return a message to the 
        user when their input is invalid
        """
        input = 56

        '''
        we probabaly don't need the result
        
        '''
        result = self.energy_test.getTotalEnergyForStateByMonth(input)

        self.assertEqual(
            result, 'Invalid input. Please enter the full name of a valid US state (abbreviations not accepted)(first letter must be capitalized)')

    if __name__ == '__main__':
        unittest.main()
