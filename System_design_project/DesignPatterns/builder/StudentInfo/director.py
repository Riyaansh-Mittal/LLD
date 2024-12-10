from student_builder import StudentBuidler
from student import Student
from mba_student_builder import MBAStudentBuilder
from engineering_student_builder import EngineeringStudentBuilder

class Director:
    
    def __init__(self, student_builder: StudentBuidler):
        self.student_builder = student_builder

    def create_student(self) -> Student:
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            print("HERE")
            return self.create_engineering_student()
        elif isinstance(self.student_builder, MBAStudentBuilder):
            return self.create_mba_student()
        
        return None
    
    def create_engineering_student(self) -> Student:
        return self.student_builder.set_roll_number(11).set_age(22).set_name("xyz").set_subject().build()
        
    def create_mba_student(self) -> Student:
        return self.student_builder.set_roll_number(2).set_age(24).set_name("xyz").set_father_name("Myfathername").set_mother_name("mymothername").set_subject().build()