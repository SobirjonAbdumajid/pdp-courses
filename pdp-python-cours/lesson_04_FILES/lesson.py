# Files
# import csv
# Methods
# r - Read
# w - Write
# a - Append
# x - Write only if file doesn't exist

# file = open('bytes.txt', 'wb')

# file.write(b'byte\n')
# print(type(file.read().decode())) # decode bytedan string ko'rinishida qaytaradi

# file = open('lesson.txt', 'x')

# file.write('somsa3\n')
# print('dfg')

# ----------------------------------------------------------------------------------------------------------

# READ FILE ELEMENTS

# l = 0
# while l != 3:
#     l += 1
#     context = file.readline() # bitta qatorni chiqarib beradi
#     print(f'line {l}:', context, end='')

# context = file.read() # hammasini chiqarib beradi qator qatordan. agar element ko'p bo'lsa tezkor xotirada joy yitmay qoladi.
# print(context, end='')

# for i in file.readlines(): # file elementlarini \n bilan hammmasini chiqarib beradi
#     print(i, end='')

# context = file.read().split('\n')
# print(context, end='')




# file.close()

# file = open('bytes.txt', 'r+') # r+ o'qish ham yozishga imkon beradi.
#
# print(file.read())
# file.write('Hello World!')
#
# file.close()
# ----------------------------------------------------------------------------------------------------------

# with open("file.txt", "w+") as file: # b



# Faylni yaratish
# with open("file.txt", "r+") as file:
#     # Matnni faylga yozish
#     print(file.read())
#     file.write("Hello Filessss\n")

with open('info_uzbekistan.csv',"r+") as file:
    for line in file:
        print(line)


# files = []                    # file ochish
# for i in range(1000):
#     file = open(f'trash{i}.txt', 'w')
#     files.append(file)
#     file.close()


# files = []
# for i in range(1000):

    # with open(f'trash{i}.txt', 'w') as file:
    #     files.append(file)


# for file in files:
#     file.close()

# import os
# for i in range(1000):
#     os.remove(f'trash{i}.txt')

# import json
# from pprint import pprint

# data = {
# "key": "value",
# "name": "Sobirjon",
# "job": "Programmer",
# }

# content = json.dumps(data) # dumps datani stringga o'tqizadi.
# print(content)

# with open('file.json', 'w') as file:
#     file.write(content)

# with open('file.json', 'r') as file:
#     content1 = json.load(file) # load method jsonni filedan o'qiydi va dictionaryga aylattiradi.
#     print(content1['looking_for_job'])

# XML
"""
<document>
    <key></key>
    <name>Sobirjon</name>
    <job>Programmer</job>
</document>
"""
# ----------------------------------------------------------------------------------------------

# JSON
"""
{
"key": "value",
"name": "Sobirjon"
"job": "Programmer"
}
"""
# ----------------------------------------------------------------------------------------------

# CSV
"""
key, name, job
value1, Sobirjon, Programmer
value2, Sardorbek, Programmer
"""


# --------------------------------------------------------------------------------------
# with open('info_uzbekistan.csv') as file:
#     for line in csv.reader(file, delimiter=';'): # (;) ajartib olish
#         print(line[-1])

# from pprint import pprint
# data = []
# with open('info_uzbekistan.csv') as file:
#     for line in csv.DictReader(file, delimiter=';'): # (;) ajartib olish
#         data.append(line)
# pprint(data)

# from pprint import pprint
# data = []
# with open('info_uzbekistan.csv') as file:
#     for line in csv.DictReader(file, delimiter=';'): # (;) ajartib olish
#         dt = dict(line)
#         dt['area'] = int(dt['area'].replace(',',''))
#         data.append(dt)
#     # pprint(data)

# # pprint(sorted(data, key=lambda x: x['area'], reverse=True))
# total = 0
# for i in data:
#     total += i['area']
# print(total)