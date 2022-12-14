from tkinter import N
from matplotlib.rcsetup import validate_float
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Mysql@123",
database="sample"
)

# print(mydb)

def createTable():
    tname = str(input("Enter table Name "))
    n = int(input("Enter number of columns "))
    command = f"create table {tname} ( "
    for i in range(n):
        columns =  list(map(str,input("\nEnter Column name and type : ").split(' ')))
        command += f" {columns[0]} {columns[1]},"
    
    command =command[:-1] +")"

    print(command)
    return command

def insert():
    cursor = mydb.cursor()  
    cursor.execute("show tables")
    for i in cursor:
        print(i)
    tname = str(input("Enter table Name "))
    cursor.execute(f"desc {tname}")
    print(cursor.fetchall())
    columns = list(map(str,input("\nEnter Column names : ").split(' ')))
    command = f"insert into {tname} ( "


    
    values = []
    string = "%s,"
    string = (string * len(columns))[:-1]
    print(string)
    

    for i in range(len(columns)):
        command += f"{columns[i]} ,"
        values.append(string)


    command = command[:-1] +f") values ({string})"
    

    n = int(input("Enter number of rows "))
    rows = []
    for i in range(n):
        values = tuple(map(str,input(f"\nEnter row {i} ").split(' ')))
        rows.append(values)
    print(command)
    print(rows)

    cursor.executemany(command, rows)
    mydb.commit()

    print(cursor.rowcount, "was inserted.")


    
    

    



if __name__ == "__main__":

    cursor = mydb.cursor()  

    # table creation
    # cursor.execute("create table students (name varchar(255) ,age int, id INT AUTO_INCREMENT PRIMARY KEY,school_name varchar(255))")


    # print("1.Create Table")
    # print("2.Insert Value")

    # cursor.execute(createTable())

    insert()

    

    # cursor.execute("show tables")
    # for i in cursor:
    #     print(i)
