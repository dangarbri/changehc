from models.organization import Organization
from models.employee import Employee
import unittest

class TestOrganization(unittest.TestCase):
    """
    Tests for the organization class
    """
    def test_single_employee_organization(self):
        """
        Test creating an organization from a list of employees
        """
        employee = Employee(id=1, first_name='Jeff', manager_id=None, salary=1000000)
        org = Organization([employee])

        self.assertEqual(org._ceo, employee)
        self.assertEqual(len(org._employees), 1)

    def test_employee_added_before_manager(self):
        """
        Test for adding an employee, and then their manager

        First, add an employee with a specified manager_id
        At this point, confirm the employee and their manager are added to the org.
        Next, add the manager
        Finally, confirm there are still only the employee and manager in the org.
        """
        employee = Employee(id=1, first_name='Woody', manager_id=2, salary=100)
        manager = Employee(id=2, first_name='Buzz', manager_id=None, salary=200)

        org = Organization([])
        org.add_employee(employee)
        # Expect two employees since the organization knows that Woody has
        # a manager
        self.assertEqual(len(org._employees), 2)
        # Confirm the manager is empty at this time
        blank_manager = org.get_employee_by_id(2)
        self.assertEqual(blank_manager.first_name, '')

        # Now add Buzz to the org
        org.add_employee(manager)
        # Verify these are still the only two members of the organization
        self.assertEqual(len(org._employees), 2)
        # Now the ceo should be Buzz
        # But since Woody was added with buzz as the manager first, it won't be
        # the same reference.
        self.assertNotEqual(org._ceo, manager)
        self.assertEqual(org._ceo.first_name, manager.first_name)

        # Confirm Buzz has woody listed as his employee
        employees = org._ceo.get_employees()
        # There should only be one employee, Woody, under Buzz
        self.assertEqual(len(employees), 1)

    def test_2_managers_one_employee(self):
        """
        If the organization can handle adding nested managers, then
        it will scale for any organization
        """
        ceo = Employee(id=1, manager_id=None)
        manager_1 = Employee(id=2, manager_id=1)
        manager_2 = Employee(id=3, manager_id=2)

        org = Organization([])
        # Order they are added should not matter
        org.add_employee(manager_1)
        org.add_employee(manager_2)
        org.add_employee(ceo)

        # Verify CEO is set
        self.assertEqual(org._ceo.id, ceo.id)

        # Verify CEO subordinate is manager 1
        ceo_subordinates = org._ceo.get_employees()
        self.assertEqual(len(ceo_subordinates), 1)
        self.assertEqual(ceo_subordinates[0].id, manager_1.id)

        # Verify Manager 1 Subordinate is Manager 2.
        manager_subordinates = ceo_subordinates[0].get_employees()
        self.assertEqual(len(manager_subordinates), 1)
        self.assertEqual(manager_subordinates[0].id, manager_2.id)

