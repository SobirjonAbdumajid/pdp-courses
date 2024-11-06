# from sqlite3 import connect

# with connect('task2.db') as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE iF NOT EXISTS contacts(
#         first_name VARCHAR,
#         last_name VARCHAR,
#         phone_number VARCHAR
#         )
#         """
#     )
#     # cursor.execute(
#     #     '''
#     #     INSERT INTO contacts (first_name, last_name, phone_number)
#     #     VALUES ("Sardorbek", "Odiljonov", "+123456")
#     #     '''
#     # )

#     cursor.execute(
#         """
#         SELECT * FROM contacts WHERE first_name='Sobirjon'
#         """
#     )
#     row = cursor.fetchone()
#     print(row)



# ---------------------------------------------------------------------------------


# import sys
# import sqlite3
# from prettytable import PrettyTable 

# class ContactsRepo:
#     def __init__(self, db):
#         self.db = db
    
#     def add(self, first_name, second_name, phone_number):
#         cursor = db.cursor()
#         cursor.execute(
#             """
#             INSERT INTO contacts (first_name, last_name, phone_number)
#             VALUES (?, ?, ?)
#             """,
#             (first_name, second_name, phone_number)
#         )
#         db.commit()

#     def list(self):
#         cursor = db.cursor()
#         cursor.execute(
#             """
#             SELECT * FROM contacts
#             """
#         )
#         return cursor.fetchall()

#     def search(self, first_name):
#         cursor = db.cursor()
#         cursor.execute(
#             """
#             SELECT * FROM contacts WHERE first_name=?
#             """,
#             (first_name,)
#         )
#         return cursor.fetchall()



# if __name__=='__main__':
#     if len(sys.argv) != 2:
#         sys.exit('Only one argument required')
    
#     avialable_command = ('add', 'search', 'list')
#     command = sys.argv[1]
#     # print(command)
#     if command not in avialable_command:
#         sys.exit(f'Unknown command {command} \navailable commands: {avialable_command}')

# with sqlite3.connect('task2.db') as db:
#     repo = ContactsRepo(db)
#     if command == 'add':
#         first_name = input('First name: ')
#         second_name = input('Second name: ')
#         phone_number = input('Phone number: ')
#         repo.add(first_name,second_name,phone_number)
#         print('Contacts created successfully')
#     elif command == 'list':
#         contacts = repo.list()
#         myTable = PrettyTable(['First name', 'Second name', 'Phone number'])
#         for i in contacts:
#             myTable.add_row(i)
#         print(myTable)
        
#     elif command == 'search':
#         first_name = input('First name: ')
#         contacts = repo.search(first_name)
#         myTable = PrettyTable(['First name', 'Second name', 'Phone number'])
#         for i in contacts:
#             myTable.add_row(i)
#         print(myTable)
#         # print(*contacts, sep='\n')
