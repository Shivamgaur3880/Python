class Employee:
    company='Google'
    salary=500

janak=Employee()
raju=Employee()

janak.salary=1000               # instance attributes
raju.salary=800

print(janak.salary)
print(raju.salary)