class Employee:
    def __init__(self, name, base_pay, hours_worked):
        self.name = name
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def salary(self):
        salary = self.base_pay*self.hours_worked
        print("Total salary for "+self.name+" is "+str(salary)+" dollar")


class Manager(Employee):
    def __init__(self, name, base_pay, hours_worked, office_number):
        Employee.__init__(self, name, base_pay, hours_worked)
        self.officeNumber = office_number

    def office_number(self):
        print(self.name, self.officeNumber)



John = Manager("John", 7.5, 38, "rozzi")
John.salary()
John.office_number()
