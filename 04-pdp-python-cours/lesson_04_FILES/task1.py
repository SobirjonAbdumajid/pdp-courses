'''
Quyidagi ishlarni bajaradigan dastur tuzing:
    file.txt nomli text fayl yaratib,
    ichiga "Hello Files" deb yozsin.
'''

folder = open('file.txt', 'w')


folder.write('Hello Files\n')


folder.close()



