import json
from models.employee import Employee

# Generates employee objects from JSON input
class EmployeeFactory:
    @staticmethod
    def EmployeesFromJsonFile(input_file):
        """
        Generates employees from an input file
        """
        # Load JSON File and create employees
        with open(input_file, 'r') as json_input:
            json_text = json_input.read()

        # Parse the JSON into a Python list.
        json_list = json.loads(json_text)

        # Iterate over the JSON data and convert the JSON data into
        # employees
        employees = []
        for json_obj in json_list:
            new_employee = Employee.fromDictionary(json_obj)
            employees.append(new_employee)

        return employees
