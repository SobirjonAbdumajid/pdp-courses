'''
O'tgan dars vazifa sifatida yaratilgan Student classni o'zgartiring.
Student class'dan yaratilgan obyektni print qiliganda studentni ismi ekranga  chiqarilsin.

Misol:
student = Student(name="John")
print(student)
# John
'''

class Student:
    def __init__(self, name):
        self.name = name

    
    def __str__(self):
        return f"{self.name}"

user1 = Student(name = 'Sobirjon')
print(user1)