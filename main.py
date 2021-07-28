from models.organization import Organization
from utils.employee_factory import EmployeeFactory

TEST_INPUT_FILE = "test_input.json"

def main():
    # Read input from local file
    employees = EmployeeFactory.EmployeesFromJsonFile(TEST_INPUT_FILE)
    org = Organization(employees)
    # Print ASCII Employee Tree
    org.print_organization()
    # Print Total Salary requirements for the company
    org.print_salary_requirement()
    # Print employees alphabetically
    org.print_employees_alphabetically()

if __name__ == "__main__":
    main()