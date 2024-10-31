# # my_list = [1,2,3]


# # interator = iter(my_list)
# # element = next(interator)
# # print(element)
# # element = next(interator)
# # print(element)

# # ------------------------------------------------
# # iterator = iter(my_list)
# # while True:
# #     try:
# #         element = next(iterator)
# #     except StopIteration:
# #         break
# #     print(element)

# # # ikkalasi bir xil cod

# # for i in my_list:
# #     print(i)
# # ------------------------------------------------



# class Counter:
#     def __init__(self, count: int):
#         self.i = 0
#         self.count = count

#     def __iter__(self):
#         print('got iter call')
#         return self

#     def __next__(self):
#         print('got next call')
#         self.i += 1
#         if self.i == self.count:
#             print('raised stop interation')
#             raise StopIteration
#         return self.i
    
# counter = Counter(5)
# for i in counter:
#     print(i)


# -----------------------------------------------------

# import time

# def answer():
#     time.sleep(1)
#     yield(2)

#     time.sleep(2)
#     yield(3)

# somsa = answer()
# for i in somsa:
#     print(i)

# -----------------------------------------------------

# import time
# def counter(count):
#     for i in range(count):
#         time.sleep(1)
#         yield i

# for i in counter(5):
#     print(i)

# -----------------------------------------------------


# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b


# def calc(func, a, b):
#     return func(a,b)

# somsa = calc(sub, 4,5)
# print(somsa)

# while True:
#     yield 4





# product app qo'shimaiz
# post get(id)(hammasi) 