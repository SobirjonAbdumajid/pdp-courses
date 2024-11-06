# class Vector:
#     # class_name = 'Vector' # class variable (classga tegishli)
    
#     def __init__(self, x, y):
        # self.name = 'vector' # instance variable (obyektga tegishli)
        # self.x = x
#         self.y = y
    
#     def __str__(self):
#         return ('somsa')
    
#     def calculate_length(self):
#         return self.x ** 2, self.y ** 2
    
#     @property
#     def length(self):
#         return self.calculate_length()

#     @staticmethod # ham classda ham instanceda chaqirish usullaridan foydalansa bo'ladi.
#     def printHello():
        # return print('hello')
    
#     @classmethod
#     def methodclass(cls, magnitude, angle):       
#         return cls(magnitude, angle)


# vector = Vector.methodclass(2,3)
# vector -> instance
# Vector -> class variable

# print(Vector.printHello()) # classda chaqirish usuli
# print(vector.printHello())
# print(vector.calculate_length()) # instance usulida chaqirish
# print(vector.length)

# print(vector)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f'{self.name} login')

    def logout(self):
        print(f'{self.name} logout')
    

class Student(User):    
    def submitting_task(self):
        print(f'{self.name} submetted task')
    
class Mentor(User): # class uchun (voris olish) Inheritance 
    def checking_task(self):
        print(f'{self.name} checked task')

    def login(self):
        super(Mentor, self).login()
        print(f'{self.name} login as mentor')    
    
student = Student('Sobirjon', 're.fire761@gmail.com')
mentor = Mentor('Azimjon', 'azimjon@example.com')

# print(mentor.checking_task())

student.login()
student.logout()
student.submitting_task()
mentor.login()
mentor.logout()
mentor.checking_task()