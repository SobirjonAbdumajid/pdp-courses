class Stock:
    def __init__(self):
        self.elements = []
    
    def push(self, items):
        return self.elements.append(items)
    
    def pop(self):
        return self.elements.pop()

    # def top(self):
    #     return self.elements[-1]
    
    # def __len__(self):
    #     return len(self.elements)
    
    # def __str__(self):
    #     return f'Elements: {self.elements}. Size: {len(self)}'

    # def __repr__(self):
    #     return f'Sobirjon: {self.elements}'

    # def empty(self):
    #     return len(self) == 0
# stock = Stock()

# stock.push("Apple")
# stock.push("Banana")
# stock.push("Orange")

# print(stock)  # Elements: ['Apple', 'Banana', 'Orange']. Size: 3

# print(stock.pop())  # Orange
# print(stock.top())  # Banana

# print(len(stock))  # 2

# print(stock.empty())  # False

# print(stock)  # Elements: ['Apple', 'Banana']. Size: 2
# print(repr(stock))  # Sobirjon: ['Apple', 'Banana']
# stock = Stock()
# stock.push(1)
# stock.push(2)
# stock.push(3)
# stock.push(4)
# print(stock.pop(1))
# # print(stock.size())
# print(len(stock))
# print([stock])


import math
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Vector: <{self.x, self.y}>'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __lt__(self, other: 'Vector'):
        return self.magnitude < other.magnitude

    def __gt__(self, other: 'Vector'):
        return self.magnitude > other.magnitude

    def __bool__(self):
        print(self.magnitude)
        return self.magnitude == 0

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __int__(self):
        pass
    
    def __float__(self):
        pass

v1 = Vector(3, 2)
v2 = Vector(3, 2)

print(v1)

# if v1>v2:
#     print(True)
# else:
#     print(False)
# v3 = v1 - v2
# print(v3)
# print(v1 == v2)
# print(v1 < v2)
# print(v1 > v2)


# matonat = set(['Matem','Inngliz tili','Ona tili'])
# obru = set(['Matem','Fizika','Ona tili'])

# print(matonat ^ obru)




# class Set:
#     def __and__(self, other):
#         return 'and'

#     def __or__(self, other):
#         return 'or'

#     def __sub__(self, other):
#         return 'sub'

    

# print(Set() - Set())


