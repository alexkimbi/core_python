class School:
    def __init__(self, students, student_class, fees):
        self.students = students
        self.student_class = student_class
        self.fees = fees
        
sch1 = School("Beiweh Simon", "f2", 10000)
sch2 = School("Song Caston", "f3", 20000)  

print(sch1.students, sch1.student_class, sch1.fees)
print(sch2.students, sch2.student_class, sch2.fees)