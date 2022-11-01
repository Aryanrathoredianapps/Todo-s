from asyncio import Task
from sqlite3 import Cursor
import mysql.connector

con = mysql.connector.connect(host = "localhost", password ="winserver" , user = "root", port = 3306, database = "todo_data")
print(con)

Cursor=con.cursor()

def insert():
    task=input("enter the task")
    sql=f"insert into todo_list(Task) values('{(task)}')"
    Cursor.execute(sql)
    # print(sql)
    # Cursor.execute(sql)
    con.commit()
    print("Done")
    menu()

def read():
    sql="select * from todo_list"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        print(*x)
    menu()

def delete():
    tno=input("enter task number")
    sql=f"delete from todo_list where ID=({tno})"

    Cursor.execute(sql)
    con.commit()
    menu()
    
def update():
    ab=input("enter id nub")
    sql=f"select * from todo_list where id-({ab})"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        Task=x[1]
    
    Task=input("updated task")
    sql=f"UPDATE todo_list SET Task=('{Task}') WHERE ID = ({ab});"
    Cursor.execute(sql)
    con.commit()
    print("Done")
    menu()

def menu():
    print("select an operation")
    ch=int(input(""))
    if(ch==1):
        insert()
    elif(ch==2):
        read()
    elif(ch==3):
        delete()
    elif(ch==4):
        update()
    else:
        print("Shai operation daliye ")


menu() 