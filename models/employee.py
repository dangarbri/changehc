class Employee:
    """
    Employee object to represent an employee
    """
    def __init__(self, id=0, first_name='', manager_id=0, salary=0):
        # Store any employees under this employee
        self._employees = []
        # Basic data model for an employee
        self.id = id
        self.first_name = first_name
        self.manager_id = manager_id
        self.salary = salary

    @staticmethod
    def fromDictionary(employee_data):
        # This is a nice factory design pattern used by Dart
        employee = Employee(employee_data['id'],
                            employee_data['first_name'],
                            employee_data['manager'],
                            employee_data['salary'])
        return employee

    def add_employee(self, employee):
        """
        Adds an employee to this manager
        """
        self._employees.append(employee)

    def is_manager(self):
        # The employee is a manager if they have employees under them
        return len(self._employees) > 0

    def assign_employee_data(self, employee):
        """
        Assigns data to an employee. IDs must match when assigning data.

        This solves the problem of employees being added before their manager.
        An empty employee that is a manager can be created to manage the overall
        hiearchy and the employee details can be added later
        """
        assert employee.id == self.id
        self.first_name = employee.first_name
        self.manager_id = employee.manager_id
        self.salary = employee.salary

    def get_employees(self):
        """
        Returns the list of employees under this manager
        """
        return self._employees

    def list_employees(self, spacing=0):
        # All subordinates will have this prefix to build the ascii hiearchy
        prefix = "--" + "--"*spacing
        # Print this employees name
        print(prefix + self.first_name)
        for subordinate in self._employees:
            subordinate.list_employees(spacing+1)

    # Python sort functions are guaranteed to use lt during
    # sorting, so define this to make sorting employees alphabetically easy.
    def __lt__(self, other):
        return self.first_name < other.first_name

    def __repr__(self):
        return self.first_name