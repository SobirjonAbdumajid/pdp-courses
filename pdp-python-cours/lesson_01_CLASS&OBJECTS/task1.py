'''
Student nomli class yarating. 
__init__ metodi orqali studentning ismi, yoshi va h,k larni qabul qilsin.
about nomli metod ham qo'shing.
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def about(self):
        return f'I am {self.name}. i am {self.age} years old'
person1 = Student('Sobirjon', 19)
print(person1.about)