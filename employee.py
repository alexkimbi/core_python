#!/usr/bin/python3
class Employee:
    """Employee class  contains first name, last name and salary
    """
    def __init__(self, fname, lname, salary, years):
        self.fname  = fname
        self.lname  = lname
        self.salary = salary
        self.years  = years
        
    def calculate_paycheck(self):
        """Paycheck is weekly which is salary devided by 52 

        Returns:
            int: weekly paycheck
        """
        return self.salary/52
        # return int(self.years)
