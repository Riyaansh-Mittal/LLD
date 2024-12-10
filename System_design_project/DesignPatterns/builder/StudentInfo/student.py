"""  
Builder here is StudentBuilder

"""

class Student:
    
    def __init__(self, builder):
        self.roll_number = builder.roll_number
        self.age = builder.age
        self.name = builder.name
        self.father_name = builder.father_name
        self.mother_name = builder.mother_name
        self.subjects = builder.subjects
    
    def to_string(self) -> str:
        return ( 
            f"Roll No. {self.roll_number} "
            f"Age {self.age}"
            f"Name {self.age}"
            f"Father Name {self.father_name}"
            f"Mother Name {self.mother_name}"
            f"Subject {self.subjects[0]}, {self.subjects[1]}"
        )

    