# ---------------------------------------------------------------------------------

def float_range(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

for i in float_range(0, 2, 0.5):
    print(i)

def rec(n):
    print(n*q)
    q = n
    return rec(n+1)
print(rec(3))

# ---------------------------------------------------------------------------------
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# result = factorial(5)
# print(result)

# list = [1,1,1,1,1,2,2,2,3,3,3,3,3,3,3]
# somsa = []
# for l in list:
#     somsa.append(list.count(l))
#     maxx = max(somsa)
#     indexx = somsa.index(maxx)  
# print(list[indexx])