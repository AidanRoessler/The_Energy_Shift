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
        #result = self.energy_test.getEnergyByCategoryForState(input)
        
        
        # TODO: change this to assertRaises to catch the exception
        self.assertRaises(Exception, self.energy_test.getEnergyForState, input)

    def test_validState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return the correct list of
        floats when given the valid input of 'Wisconsin'
        """
        input = 'Wisconsin'
        result = self.energy_test.getEnergyByCategoryForState(input)
        self.assertEqual(result, {'Other renewables': 3031.96, 'Conventional hydroelectric': 2144.8900000000003, 'Nuclear': 9970.199999999999,
                         'Utility-scale photovoltaic': 366.82, 'All utility-scale solar': 366.82, 'All solar': 548.86, 'Wind': 1593.48})

    def test_invalidState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return a message to the user
        when their input is invalid
        """
        input = 56
        
        '''
        we probabaly don't need the result
        
        '''
        #result = self.energy_test.getEnergyByCategoryForState(input)
        
        
        self.assertRaises(Exception, self.energy_test.getEnergyByCategoryForState, input)
        
    def test_validState_getTotalEnergyForStateByMonth(self):
        """
        Test to see if getTotalEnergyForStateByMonth() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalEnergyForStateByMonth(input)

        self.assertEqual(result, {'Location': 'Alabama', 'Category of Production': 'All fuels', '21-Jan': 12574.68, '21-Feb': 11267.83, '21-Mar': 10343.43, '21-Apr': 8972.6,
                         '21-May': 11274.04, '21-Jun': 12255.95, '21-Jul': 13545.99, '21-Aug': 13862.05, '21-Sep': 12089.57, '21-Oct': 11731.84, '21-Nov': 12408.92, '21-Dec': 12406.44})

    def test_invalidState_getTotalEnergyForStateByMonth(self):
        """
        Test to see if getTotalEnergyForStateByMonth() can successfully return a message to the user
        when their input is invalid
        """
        input = 'Montreal'
        
        '''
        we probably don't need the result
        
        '''
        #result = self.energy_test.getTotalEnergyForStateByMonth(input)
        
        self.assertRaises(Exception, self.energy_test.getTotalEnergyForStateByMonth, input)
        

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
        #result = self.energy_test.getTotalEnergyForStateByMonth(input)
        
        self.assertRaises(Exception, self.energy_test.getTotalRenewableEnergyByState, input)
        

    if __name__ == '__main__':
        unittest.main()
