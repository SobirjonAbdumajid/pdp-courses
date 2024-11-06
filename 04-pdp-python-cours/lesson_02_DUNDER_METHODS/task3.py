'''
Student class yarating, name va age attributlari bo'lsin.
Student class obyektlariga yosh bo'yicha taqqoslash  imkoniyatini qo'shing.

Misol:
john = Student(name="John", age=21)
bob = Student(name="Bob", age=32)
alice = Student(name="Alice", age=21)


print(john > bob)  # False
print(john < bob)  # True  
print(john == alice)  # True chiqishi kerak

'''

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age
    
 

sobirjon = Student(name = 'Sobirjon', age = 21)
sardorbek = Student(name = 'Sardorbek', age = 32)
abduqahhor = Student(name = 'Abduqahhor', age = 21)


print(sobirjon > sardorbek)
print(sobirjon < sardorbek)
print(sobirjon == abduqahhor)