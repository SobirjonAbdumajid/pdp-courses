'''
Yangi Teacher classini hosil qiling va u dars mobaynida yaratilgan User classidan voris olsin.
Dars mobaynida yaratilgan Mentor classi User class dan emas Teacher classdan voris olsin. 
Teacher classiga subclass bo'lgan yangi Assistant classini ham yarating.

'''

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f'{self.name} login')

    def logout(self):
        print(f'{self.name} logout')

class Teacher(User):
    pass

class Mentor(User): # class uchun (voris olish) Inheritance 
    def checking_task(self):
        print(f'{self.name} checked task')

class Assistant(Teacher):
    pass


user = User('Sobirjon', 're.fire761@gamil.com')
mentor = Mentor('Azimjon', 'Azimjon@example.com')
teacher = Teacher('Shohruh', 'Malikov@gmail.com')
assistant = Assistant('Assistant', 'Assistant@gamil.com')

print(user.login())
print(mentor.checking_task())
print(teacher.login())
print(assistant.login())