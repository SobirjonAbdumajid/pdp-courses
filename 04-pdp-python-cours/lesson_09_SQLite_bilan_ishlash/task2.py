'''
SQLite dan foydalanib finance.py nomli command-line application tuzing.
3ta:
   - spend (pul ishlatish)
   - earn  (pul topish)  
   - balance (balansda qancha pul qolganligini tekshirish)
imkoniyatlari bo'lsin.

Misol:
- python finance.py earn 1500  # 1500 daromad qo'shsin
- python finance.py spend 400  #  400 harajat qo'shsin
- python finance.py balance  # ekranga 1100 chiqarsin
'''

import sys
import sqlite3

class FinanceApp:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount INTEGER
            )
            """
        )
        self.db.commit()

    def earn(self, amount):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO transactions (type, amount)
            VALUES (?, ?)
            """,
            ('earn', amount)
        )
        self.db.commit()

    def spend(self, amount):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO transactions (type, amount)
            VALUES (?, ?)
            """,
            ('spend', amount)
        )
        self.db.commit()

    def balance(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT SUM(CASE WHEN type='earn' THEN amount ELSE -amount END) as balance
            FROM transactions
            """
        )
        return cursor.fetchone()[0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('At least one argument required')

    command = sys.argv[1]
    valid_commands = ('earn', 'spend', 'balance')

    if command not in valid_commands:
        sys.exit(f'Unknown command "{command}". Available commands: {valid_commands}')

    with sqlite3.connect('finance.db') as db:
        app = FinanceApp(db)
        app.create_table()

        if command == 'earn':
            if len(sys.argv) != 3:
                sys.exit('Amount argument required for "earn" command')
            amount = int(sys.argv[2])
            app.earn(amount)
            print(f'Earned {amount} successfully')

        elif command == 'spend':
            if len(sys.argv) != 3:
                sys.exit('Amount argument required for "spend" command')
            amount = int(sys.argv[2])
            app.spend(amount)
            print(f'Spent {amount} successfully')

        elif command == 'balance':
            balance = app.balance()
            print(f'Current balance: {balance}')