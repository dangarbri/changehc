import unittest

TEST_INPUT_FILE = "tests/data/test_input.json"

from utils.employee_factory import EmployeeFactory
class TestEmployeeFactory(unittest.TestCase):
    """
    Tests loading the json content
    """
    def test_json_loading(self):
        """
        Quick known answer test to confirm the employee factory
        can load employees from the json file
        """
        # Load employees
        employees = EmployeeFactory.EmployeesFromJsonFile(TEST_INPUT_FILE)
        # Assert that the expected number of employees have been loaded
        self.assertEqual(len(employees), 7)
        # Verify Jeff was loaded correctly, he is the 2nd employee
        # in the known json data.
        jeff = employees[1]
        self.assertEqual(jeff.id, 2)
        self.assertEqual(jeff.first_name, "Jeff")
        self.assertEqual(jeff.manager_id, None)
        self.assertEqual(jeff.salary, 110000)

