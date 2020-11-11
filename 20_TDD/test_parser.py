import unittest
from parser import ConfigurationParser

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ["CUSTOMER_A","CUSTOMER_B"]
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)
    def test_parse_cust_vlan(self):
        cp = ConfigurationParser()
        cu_name = "CUSTOMER_B"
        expected_vlan = ['101', '102']
        parsed_vlan = cp.parseCustomerVlans(cu_name)
        self.assertEqual(expected_vlan, parsed_vlan)
    def test_parse_cust_ip(self):
        cp = ConfigurationParser()
        vlan = 100
        expected_IP = "10.10.100.1"
        parsed_IP = cp.parseCustomerIP(vlan)
        self.assertEqual(expected_IP, parsed_IP)
    def test_parse_cust_data(self):
        cp = ConfigurationParser()
        expected_data={'CUSTOMER_A': [[100, '10.10.100.1']], 'CUSTOMER_B': [[101, '10.10.101.1'], [102, '10.10.102.1']]}
        parsed_data = cp.parseCustomerData()
        self.assertEqual(expected_data,parsed_data)

if __name__ == "__main__":
    unittest.main()
