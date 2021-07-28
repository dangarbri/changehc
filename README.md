# Coding Test for Change Healthcare
This is my submission for the coding test.

## Details
The challenge to take some basic JSON input that models a list of employees
and list out the employee hiearchy.

### My Solution
I created an employee class that encapsulates employees and managers. My
initial solution had an Employee class and a Manager class that inherited from
Employee. With this, it became difficult to manage references when I needed to
"Promote" an employee from an Employee to a Manager. To resolve this,
I consolodiated my Employee and Manager into a single class. An Employee
may have subordinates, and that is what makes them a manager.

When putting together the organization, I do it all in one pass. If an employee
is added with a manager that does not exist, then a placeholder manager is created
in the organization. Later, when an employee with a matching ID is added to the
organization, their details are filled into the placeholder manager.

Once this hiearchy is built, managing details like printing the hiearchy becomes easy.

Note: I am using Python 3.8.8 in case you have any issues with imports
Run the solution with `python main.py`


### Testing
Unit tests are in the tests directory. Testing was done mainly on constructing
the hiearchy. I did not implement tests for printing the hiearchy or salary
requirements, as these were easy to check by hand and my main concern was with
building the employee hiearchy.

You may run tests with the following command
`python -m unittest discover -s tests -p *_test.p`

### Challenges
My biggest challenge with this was managing what to do when an employee is added
with a manager_id that was not yet in the system. Eventually I chose to create
a dummy manager to assign the employee to. At first I had Employee and Manager
classes. The bigger problem arose when that
employee became a manager. In order to make them a manager, I would have to
create a new manager with the same employee data, remove the "Employee" from their
manager, add the "promoted" Manager to their manager, and then finally add the
new employee to this promoted manager. If this is hard to follow in text, that's
because it's hard to follow in general. So what solved this for me was to use
a single class to represent both Employees and Managers. This way I did not
need to deal with any reference updates and I could simply build the hiearchy
as a simple employee tree.

#### Classes & Files
`utils/employee_factory.py`
- The EmployeeFactory manages generating Employee instances from the JSON input
  file

`models/employee.py`
- The Employee model encapsulates employee data and provides functions for adding
  employees as subordinates

`models/organization.py`
- The organization takes a list of employees and builds out the organization's
  hiearchy/org chart. The main meat of this operation is in the `add_employee`
  function where it figures out where to place the employee in the organization.