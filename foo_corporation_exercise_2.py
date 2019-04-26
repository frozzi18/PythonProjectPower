class Employee:

    salary = 0

    def __init__(self, name, professional_level, base_pay, hours_worked):
        self.name = name
        self.professional_level = professional_level
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def check(self):
        if self.base_pay < 8:
            print("Error \n")
            return False
        else:
            if self.hours_worked > 40:
                salary = self.hours_worked * self.hours_worked
                salary = salary + (self.hours_worked-40) * self.base_pay * 0.5
                print("Good Overtime. The salary is ", salary)
            else:
                salary = self.hours_worked * self.hours_worked
                print("The salary is ", salary)
            return True

    def salary(self):
        salary = self.base_pay*self.hours_worked
        print("Total salary for "+self.name+" is "+str(salary)+" dollar")

    def office(self):
        if self.professional_level == "A":
            print(self.name, "has an individual office room \n")
        elif self.professional_level == "B":
            print(self.name, "has a cubicle room \n")


John = Employee("John", "B", 7.5, 38)
John.salary()
John.office()



