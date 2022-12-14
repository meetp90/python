import sqlite3

class connection:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("try.db")    
    
    def createTable(self):
        self.name = input("table name : ")
        self. table = 'CREATE TABLE %s (ID INT PRIMARY KEY, NAME VARCHAR(20))' % (self.table)
        self.conn.execute(self.table)

    def insertValues():
        table = input("enter table name : ")
        id = int(input("enter id : "))
        name = input("enter name:")
        conn = sqlite3.connect("try.db")
        cur = conn.cursor()
        cur.execute('INSERT INTO ? VALUES (?,?)',(table,id,name))

    def deleteValues():
        table = input("enter table name : ")
        name = input("enter name to delete : ")
        conn = sqlite3.connect("try.db")
        cur = conn.cursor()
        cur.execute(f'DELETE FROM  [{table}] WHERE NAME = [{name}]')

    def displayValues():
        table = input("enter table name : ")
        conn = sqlite3.connect("try.db")
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table}')    

    def updateValues():
        table = input("enter table name : ")
        id = int(input("enter ID : "))
        name = input("enter name to update : ")
        conn = sqlite3.connect("try.db")
        cur = conn.cursor()
        cur.execute(f'UPDATE  [{table}] SET NAME = [{name}]  WHERE ID = [{id}]')



def main():
    obj = connection()
    choice = 0
    while choice != 6:
        choice = int(input("Enter your choice : "))
        if choice == 1:
           obj.createTable()
        if choice == 2:
           obj.insertValues()
        if choice == 3:
            obj.deleteValues()
        if choice == 4:
            obj.displayValues()
        if choice == 5:
            obj.updateValues()
        if choice == 6:
            break


main()