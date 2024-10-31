'''
Calculator nomli class yarating.
add, subtract, multiply, divide nomi static metodlar qo'shing.

Misol: 
print(Calculator.add(1, 2))  # 3
print(Calculator.subtract(1, 2))  # -1
print(Calculator.multiply(1, 2))  # 2
print(Calculator.divide(1, 2))  # 0.5
'''

class Calculator:
    # @staticmethod
    def add(x, y):
        return x + y

    # @staticmethod
    def substract(x, y):
        return x - y

    # @staticmethod
    def multiple(x, y):
        return x * y

    # @staticmethod
    def divide(x, y):
        return x / y
    
print(Calculator.add(1, 2))
print(Calculator.substract(1, 2))
print(Calculator.multiple(1, 2))
print(Calculator.divide(1, 2))