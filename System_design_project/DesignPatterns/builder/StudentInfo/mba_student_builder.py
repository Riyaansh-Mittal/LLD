from student_builder import StudentBuidler

class MBAStudentBuilder(StudentBuidler):

    def set_subjects(self) -> StudentBuidler:
        subs = ["Micro Economics","Business Studies","Operations Management"]
        self.subjects = subs
        return self