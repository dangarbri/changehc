from models.employee import Employee
import json

class Organization:
    """
    An organization made of employees and managers

    Contains dictionaries of all employees and managers in
    an organization
    """
    def __init__(self, employee_list):
        # CEO is the special manager that does not have a manager
        self._ceo = None
        # Dictionary mapping all employees to their employee IDs. This is used
        # to quickly lookup employees and assign new employees to managers.
        self._employees = {}
        # Add all employees from the list to the org
        for employee in employee_list:
            self.add_employee(employee)

    def print_organization(self):
        self._ceo.list_employees()

    def print_salary_requirement(self):
        total_salary = 0
        for employee_id in self._employees:
            total_salary += self._employees[employee_id].salary
        print("Total Salary: " + str(total_salary))

    def print_employees_alphabetically(self):
        # Generate a list of all employees since you can't sort a dictionary
        sorted_employees = list(self._employees.values())
        sorted_employees.sort()
        print("Employees Alphabetized:")
        print(sorted_employees)

    def get_employee_by_id(self, id):
        # Attempt to get the employee from the dictionary
        try:
            return self._employees[id]
        # If the employee is not in the list, return None
        except KeyError:
            return None

    def add_employee(self, employee_to_add):
        """
        Adds an employee to the organization

        The goal of this function to essentially build the organization
        hiearchy.

        The entire hiearchy is built in one pass over the employee data. The
        biggest challenge here is when an employee is added before their
        manager. When this happens, an empty manager is created, and their
        details are added in later when that manager is loaded from the data
        source.

        The goal of my design here is to build the whole organization in one
        pass over the data. I considered loading all the employees, and then
        building the hiearchy, which probably would have been much simpler, but
        much less efficient since it would require more passes over the dataset.
        """
        # An employee cannot be their own manager as it would cause an infinite
        # loop when attempting to walk through the hiearchy
        assert employee_to_add.id != employee_to_add.manager_id
        # Check if the employee's ID is already in the org. If so, it means
        # they are a manager of an employee that was previously added. Fill
        # in their details here.
        existing_employee = self.get_employee_by_id(employee_to_add.id)
        if existing_employee:
            self._update_employee_details(existing_employee, employee_to_add)
            employee_to_add = existing_employee

        # If the employee is not the org yet, add them to the org and assign
        # them to a manager
        else:
            self._employees[employee_to_add.id] = employee_to_add

        # Every employee has a manager, unless they're the CEO. Add each
        # employee to their manager's list.
        self._assign_employee_to_manager(employee_to_add, employee_to_add.manager_id)

    def _assign_employee_to_manager(self, employee, manager_id):
        # If this is the CEO, assign them to the boss field
        if (manager_id is None):
            # Assumption: Input data may not have co-founders
            assert self._ceo == None
            self._ceo = employee
        # Otherwise, get the manager and assign the employee to them.
        else:
            # Get the manager from the org
            manager = self._get_or_create_manager(manager_id)
            # Add the employee to the manager
            manager.add_employee(employee)

    def _get_or_create_manager(self, manager_id):
        """
        Retrieves a manager from the employee list. If the manager's ID
        doesn't exist, then this will create and return an empty manager.

        This supports inserting employees before their manager has been added.
        """
        # Get the manager from the org
        manager = self.get_employee_by_id(manager_id)
        # If the manager doesn't exist, create an empty manager to enter the
        # employee into the hiearchy.
        if manager is None:
            manager = Employee(manager_id)
            self._employees[manager_id] = manager

        return manager

    def _update_employee_details(self, existing_employee, employee_details):
        existing_employee.assign_employee_data(employee_details)
