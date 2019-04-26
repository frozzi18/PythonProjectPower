class Employee:
    def __init__(self, name, professional_level, base_pay, hours_worked):
        self.name = name
        
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def salary(self):
        salary = self.base_pay*self.hours_worked
        print("Total salary for "+self.name+" is "+str(salary)+" dollar")



# class Employee {
# String name;
# String professional_level;
# double base_pay;;
# int hours_worked;
# double salary;
#
# Employee(String name_value, String professionalLevel, double basePay, int hoursWorked){
# this.name = name_value;
# this.professional_level = professionalLevel;
# this.base_pay = basePay;
# this.hours_worked = hoursWorked;
# }
#
#
# public boolean check() {
# if (base_pay < 8) {
# System.out.println("Error \n");
#
#
# return false;
# } else {
# if (hours_worked > 40) {
# salary = base_pay * hours_worked;
# salary = salary + (hours_worked-40) * base_pay * 0.5;
# System.out.println("Good Overtime "+salary);
# } else {
# salary = base_pay * hours_worked;
# System.out.println("Good "+salary);
# }
# return true;
#
# }
# }
#
#
#
# public
# void
# salary()
# {
#     System.out.println("Total salary for " + name + " is " + salary + " dollar");
# }
#
# public
# void
# office()
# {
# if (professional_level == "A")
# {
# System.out.println(name + " has an individual office room \n");
# } else if (professional_level == "B") {
# System.out.println(name + " has a cubicle room \n");
# }
# }
#
# public
# void
# setValue(String
# name_value, String
# professionalLevel, double
# base_pay_value, int
# hours_worked_value  ) {
#     this.name = name_value;
# this.professional_level = professionalLevel;
# this.base_pay = base_pay_value;
# this.hours_worked = hours_worked_value;
# }
#
# }

class Manager(Employee):
    def __init__(self, name, base_pay, hours_worked, office_number):
        Employee.__init__(self, name, base_pay, hours_worked)
        self.officeNumber = office_number

    def office_number(self):
        print("The office number for ", self.name, " is ", self.officeNumber)


John = Employee("John", 7.5, 38)
Annabel = Employee("Annabel", 8.2, 42)
Graham = Employee("Graham", 10.50, 41)
Bill = Manager("Bill", 15.50, 39, "A332")
Gregory = Manager("Gregory", 18.20, 40, "A415")

John.salary()
Annabel.salary()
Graham.salary()
Bill.salary()
Bill.office_number()
Gregory.salary()
Gregory.office_number()
