#!/bin/python3

from Employees import Employees

e1 = Employees("John", "HR", "Manager", 50000, 15)
e2 = Employees("Jane", "IT", "Engineer", 60000, 3)

print(e1.name)
print(e2.role)
print(e1.eligible_for_retirement())