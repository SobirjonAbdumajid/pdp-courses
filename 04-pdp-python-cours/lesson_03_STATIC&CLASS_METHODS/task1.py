'''
Student nomi class yarating, __init__ da ism, familiyani qabul qilsin.
Misol:  student = Student('John', 'Smith')

Student classga from_full_name nomli class metod qo'shing, to'liq ismni qabul qilsin va qabul qilingan stringdan ism va familiyani ajratib olib student yaratsin.

Misol:
student = Student.from_full_name('John Smith')
print(student.first_name) # 'John'
print(student.last_name) # 'Smith'
'''

class Student:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
    
    @classmethod
    def from_full_name(cls, fullname):
        name, surename = fullname.split()
        return cls(name, surename)
    
student1 = Student.from_full_name('Sobirjon Abdumajidov')
# student2 = Student.from_full_name('Sardorbek Odiljonov')
print(student1.name)
print(student1.surename)

# somsa = 'somsa, zor'
# _split = somsa.split(',')
# print(_split)