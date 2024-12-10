from student_builder import StudentBuidler

class EngineeringStudentBuilder(StudentBuidler):

    def set_subjects(self) -> StudentBuidler:
        subs = ["DSA","OS","Computer Architecture"]
        self.subjects = subs
        return self