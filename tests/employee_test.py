from models.employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """
    Tests for the employee class
    """
    def test_init_constructor(self):
        """
        Test creating an instance of employees
        """
        test_id = 1
        test_name = 'Test'
        test_manager = 2
        test_salary = 110

        employee = Employee(test_id, test_name, test_manager, test_salary)
        self.assertEqual(employee.id, test_id)
        self.assertEqual(employee.first_name, test_name)
        self.assertEqual(employee.manager_id, test_manager)
        self.assertEqual(employee.salary, test_salary)

    def test_dictionary_constructor(self):
        """
        Tests generating an employee from a dictionary object
        """
        data = {
            'id': 1,
            'first_name': 'Test',
            'manager': 2,
            'salary': 110
        }

        employee = Employee.fromDictionary(data)
        self.assertEqual(employee.id, data['id'])
        self.assertEqual(employee.first_name, data['first_name'])
        self.assertEqual(employee.manager_id, data['manager'])
        self.assertEqual(employee.salary, data['salary'])

    def test_lt(self):
        """
        Tests the lt operator for sorting employees
        """
        employee_low = Employee(first_name = 'Albert')
        employee_high = Employee(first_name = 'Zebra')

        self.assertTrue(employee_low < employee_high)
        self.assertFalse(employee_low > employee_high)

    def test_adding_employees(self):
        """
        Test creating an instance of employees
        """
        # Create a manager
        manager = Employee()
        # Create some dummy employees
        employee_1 = Employee(id=1)
        employee_2 = Employee(id=2)

        # Assign these employees to the manager
        manager.add_employee(employee_1)
        manager.add_employee(employee_2)

        # Retrieve the employees from the manager
        employees = manager.get_employees()
        # assert there 2 employees assigned to the manager
        self.assertEqual(len(employees), 2)
        # Assert that the employees match the ids that we added
        self.assertEqual(employees[0].id, 1)
        self.assertEqual(employees[1].id, 2)

    def test_assign_employee_data(self):
        """
        Test that data is properly assigned when we update
        the manager's data
        """
        test_id = 77

        manager = Employee(id=test_id)
        employee = Employee(id=test_id, first_name='Jeff', manager_id='99', salary='110')

        manager.assign_employee_data(employee)


        self.assertEqual(manager.id, test_id)
        self.assertEqual(manager.first_name, employee.first_name)
        self.assertEqual(manager.manager_id, employee.manager_id)
        self.assertEqual(manager.salary, employee.salary)

    def test_is_manager(self):
        """
        Confirm the manager check returns True when the employee has
        subordinates
        """

        manager = Employee()
        # No subordinates means no manager
        self.assertFalse(manager.is_manager())

        subordinate = Employee()
        manager.add_employee(subordinate)
        self.assertTrue(manager.is_manager())

