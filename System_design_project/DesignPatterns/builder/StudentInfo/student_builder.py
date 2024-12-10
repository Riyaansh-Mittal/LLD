"""  
StudentBuilder 
  -> MBAStudentBuilder
  -> EngineeringStudentBuilder
"""
from abc import ABC, abstractclassmethod
from  student import Student
from typing import List

class StudentBuidler:

    def __init__(self):
        self.roll_number = None
        self.age = None
        self.name = None
        self.father_name = None
        self.mother_name = None
        self.subjects = []

    def set_roll_number(self, roll_number: int):
        self.roll_number = roll_number
        return self
    
    def set_age(self, age: int):
        self.age = age
        return self
    
    def set_name(self, name: str):
        self.name = name
        return self
    
    def set_father_name(self, father_name: str):
        self.father_name = father_name
        return self
    
    def set_mother_name(self, mother_name: str):
        self.mother_name = mother_name
        return self
    
    @abstractclassmethod
    def set_subject(self):
        pass
    
    def build(self):
        return Student(self)