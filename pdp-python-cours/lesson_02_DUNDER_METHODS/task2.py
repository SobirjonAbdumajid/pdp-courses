'''
Dars davomida yaratilgan Vector class ga ayirish imkoniyatini qo'shing.

Misol:
v1 = Vector(3, 4)
v2 = Vector(2, 4)

v3 = v1 - v2
# v3 - Vector(1, 0) bo'lishi kerak.
# Vectorlar haqida qo'shimcha o'rganish uchun resurs - https://www.mathsisfun.com/algebra/vectors.html
'''

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'Vector{self.x, self.y}'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

v1 = Vector(3, 4)
v2 = Vector(2, 4)

v3 = v1 - v2
print(v3)