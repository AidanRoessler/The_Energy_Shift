import unittest
import api

class APITester(unittest.TestCase):
    def setUp(self):
        self.energy_test = api.EnergyProductionAPI('../data/total_energy_production_modified.csv')
    

    # def test_getEnergyByMonthForState(self):
    #     return 0

    # def test_getEnergyByCategoryForState(self):
    #     return 0

    # def test_getTotalEnergyForState(self):
    #     return 0

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
        Test to see if getTotalRenewableEnergyByState() can successfully return the a message to the 
        user when their input is invalid
        """
        input = 56
        result = self.energy_test.getTotalRenewableEnergyByState(input)
        self.assertEqual(
            result, 'Please enter the full name of a state in the United States (abbreviations are not accepted)')

    if __name__ == '__main__':
        unittest.main()
