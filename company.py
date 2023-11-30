from employee import Employee
class Company:
    def __init__(self):
        self.employees = []
        self.top_employees = {}
    def add_employee(self, new_employee):
        # Expects employee's fname, lname and salary 
        self.employees.append(new_employee)
       
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        
    def pay_employees(self):
        print('Paying employees')
        for i  in self.employees:
            print('Paycheck for ', i.fname.upper(), i.lname.upper())
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('-------------------------------------') 

    def top_pay_employees(self):
        for i in self.employees:
            if i.calculate_paycheck() > 3000:
                 print(i.fname, i.calculate_paycheck())
                 self.top_employees[i.fname.upper()] = i.calculate_paycheck()
        print(self.top_employees)
        
# Assignment to add employees salary with 2 or more years of service by 5%
    # def years_of_service(self):
    #     print('The years of empoyment:')
    #     for i in self.employees:
    #         # if i.years() > 1:
    #         print(i.years)
    #         self.years[i.fname, i.lname()]
    #     print(self.years_of_service)
                 
        
def main():
    my_company = Company()
    
    employee1 = Employee('Sarah', 'Hess', 50000, 1 )
    my_company.add_employee(employee1)
    employee2 = Employee('Lee', 'smith', 60000, 1 )
    my_company.add_employee(employee2)
    employee3 = Employee('Bob', 'Brown', 250000, 2 )
    my_company.add_employee(employee3)
   
    # my_company.years_of_service()
    my_company.top_pay_employees()
   # my_company.display_employees()
    my_company.pay_employees()
  
main()
