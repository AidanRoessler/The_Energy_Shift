import unittest
import api

class APITester(unittest.TestCase):
    def setUp(self):
        self.energy_test = api.EnergyProductionAPI('../Data/total_energy_production_modified.csv')

    def test_validState_getEnergyForState(self):
        
        input = "Alabama"
        result = self.energy_test.getEnergyForState(input)
        self.assertEqual(result, 142733.34)

    def test_invalidState_getEnergyForState(self):
        """
        Test to see if getEnergyForState() can successfully return a message to the user when
        their input is invalid
        """
        input = 56
        result = self.energy_test.getEnergyForState(input)
        self.assertEqual(result, False)

        
    def test_validState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return the correct list of
        floats when given the valid input of 'Wisconsin'
        """
        input = 'Wisconsin'
        result = self.energy_test.getEnergyByCategoryForState(input)
        self.assertEqual(result, [3031.96, 2144.8900000000003, 9970.199999999999, 366.82, 366.82, 548.86, 1593.48])
    
    def test_invalidState_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return a message to the user
        when their input is invalid
        """
        input = 56
        result = self.energy_test.getEnergyByCategoryForState(input)
        self.assertEqual(result, False)

    def test_validState_getTotalEnergyForMonthByState(self):
        """
        Test to see if getTotalEnergyForMonthByState() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalEnergyForMonthByState(input)
        self.assertEqual(result, {'Location': 'Alabama', 'Category of Production': 'All fuels', '21-Jan': 12574.68, '21-Feb': 11267.83, '21-Mar': 10343.43, '21-Apr': 8972.6, '21-May': 11274.04, '21-Jun': 12255.95, '21-Jul': 13545.99, '21-Aug': 13862.05, '21-Sep': 12089.57, '21-Oct': 11731.84, '21-Nov': 12408.92, '21-Dec': 12406.44})

    def test_invalidState_getTotalEnergyForMonthByState(self):
        """
        Test to see if getTotalEnergyForMonthByState() can successfully return a message to the user
        when their input is invalid
        """
        input = 'Montreal'
        result = self.energy_test.getTotalEnergyForMonthByState(input)
        self.assertEqual(result, False)

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
        result = self.energy_test.getTotalRenewableEnergyByState(input)
        self.assertEqual(
            result, False)

    if __name__ == '__main__':
        unittest.main()
