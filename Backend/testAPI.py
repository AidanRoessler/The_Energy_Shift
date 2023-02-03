import unittest
import api

class APITester(unittest.TestCase):
    def setUp(self):
        self.energy_test = api.EnergyProductionAPI('../data/total_energy_production_modified.csv')
    

    # def test_getEnergyByMonthForState(self):
    #     return 0

    def test_sucessful_getEnergyByCategoryForState(self):
        """
        Testt osee if getEnergyByCategoryForState() can succcesfully return the corrent list of
        floats when given the valid input of 'Wisconsin'
        """
        input = 'Wisconsin'
        result = self.energy_test.getEnergyByCategoryForState(self, input)
        self.assertEqual(result, [3031.96, 2144.8900000000003, 9970.199999999999, 366.82, 366.82, 548.86, 1593.48])
    
    def test_fail_getEnergyByCategoryForState(self):
        """
        Test to see if getEnergyByCategoryForState() can successfully return a message to the user
        when their input is invalid
        """

    # def test_getTotalEnergyForState(self):
    #     return 0
    def test_getTotalEnergyForMonthByState(self):
        """
        Test to see if getTotalEnergyForMonthByState() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalEnergyForMonthByState(input)
        self.assertEqual(result, 62387.66)

    def test_successful_getTotalRenewableEnergyByState(self):
        """
        Test to see if getTotalRenewableEnergyByState() can successfully return the correct float
        value when given the valid input of "Alabama"
        """
        input = 'Alabama'
        result = self.energy_test.getTotalRenewableEnergyByState(input)
        self.assertEqual(result, 62387.66)

    def test_fail_getTotalRenewableEnergyByState(self):
        """
        Test to see if getTotalRenewableEnergyByState() can successfully return a message to the 
        user when their input is invalid
        """
        input = 56
        result = self.energy_test.getTotalRenewableEnergyByState(input)
        self.assertEqual(
            result, 'Please enter the full name of a state in the United States (abbreviations are not accepted)')

    if __name__ == '__main__':
        unittest.main()
