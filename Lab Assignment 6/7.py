# Creating empty Classes
class Student:
    pass 
class Marks:
    pass 

print('Creating an instance ABC of Student and DEF of Marks')
ABC = Student()
DEF = Marks()

# Checking Instances
print('ABC is an instance of Student:', isinstance(ABC, Student))
print('ABC is an instance of Marks:', isinstance(ABC, Marks))
print('DEF is an instance of Student:', isinstance(DEF, Student))
print('DEF is an instance of Marks:', isinstance(DEF, Marks)) 
print()

# Checking subclasses
print('Is Student a subclass of built-in object class:', issubclass(Student, object))
print('Is Marks a subclass of built-in object class:', issubclass(Marks, object))
