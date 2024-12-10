from director import Director
from mba_student_builder import MBAStudentBuilder
from engineering_student_builder import EngineeringStudentBuilder
from student import Student

if __name__ == "__main__":

    eng_student_obj = EngineeringStudentBuilder()
    mba_student_obj = MBAStudentBuilder()
    director_obj_1: Director = Director(eng_student_obj)
    director_obj_2: Director = Director(mba_student_obj)

    eng_student: Student = director_obj_1.create_student()
    mba_student: Student = director_obj_2.create_student()

    print(eng_student.to_string())
    print(mba_student.to_string())
