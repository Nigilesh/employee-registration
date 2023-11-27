from tkinter import *
import mysql.connector
from functools import partial  
   
conn = mysql.connector.connect(host="localhost",database="Register",user="root",password="Nigi@909" )
print(conn)
cur = conn.cursor()

def call_result(label_result, n1, n2,n3,n4):  
    rollno = int((n1.get()))  
    name = (n2.get())
    city = (n3.get())
    state = (n4.get())
    cur.execute(f"select * from information where id='{rollno}'")
    if cur.fetchall():
        label_result.config(text='already exists',fg='black')
        return
    else:
        key="INSERT INTO information(id,name,city, state) VALUES(%s ,%s ,%s ,%s)"
        value=[rollno,name,city,state]
        try:
            dbs = cur.execute(key,value)
            conn.commit()
        except:
            print("Error")
        print(cur.rowcount,"record inserted!")
        label_result.config(text='inserted',fg='green')
def delete(lab,n1):
    rollno=int(n1.get())
    cur.execute(f"select * from information where id='{rollno}'")
    if cur.fetchall():
        try:
            cur.execute(f"delete from information where id='{rollno}'")
            conn.commit()
        except:
            print('error Query')
        print(cur.rowcount,"record deleted!")
        lab.config(text='deleted',fg='green')
        return
    else:
        lab.config(text='not inside',fg='black')
def update(lab, n1, n2,n3,n4):
    rollno = int((n1.get()))  
    name = (n2.get())
    city = (n3.get())
    state = (n4.get())
    cur.execute(f"select * from information where id='{rollno}'")
    if cur.fetchall():
        try:
            cur.execute(f"update information set name='{name}', city='{city}', state='{state}' where id='{rollno}'")
            conn.commit()
        except:
            print('error')
        print(cur.rowcount,"record updated!")
        lab.config(text='updated',fg='green')
        return
    else:
        lab.config(text='not inside',fg='black')
def colu(lab,n1):
    data = n1.get()
    try:
        cur.execute(f"alter table information add {data} varchar(20)")
        conn.commit()
    except:
        print('error query')
    print(cur.rowcount,"added")
    lab.config(text='added col',fg='green')
       
            



    
root = Tk()  
root.geometry('1000x500')    
root.title('RegistrationForm')  
   
rollno = StringVar()  
name = StringVar()
city = StringVar()
state = StringVar()
new = StringVar()


n=Label(root,text="Simple registration Form with DB Connection",font=("Arial", 12), fg = 'white' , bg='Blue').grid(row=3, column=2)

labelNum1 = Label(root, text="Emp_ID").grid(row=4, column=0)   
labelNum2 = Label(root, text="Emp_Name").grid(row=5, column=0)
labelNum3 = Label(root, text="Emp_City").grid(row=6, column=0)
labelNum4 = Label(root, text="Emp_state").grid(row=7, column=0)
labelNum5 = Label(root, text="Add column").grid(row=6, column=8)


  
labelResult = Label(root)  
labelResult.grid(row=14, column=2)  

#Entry to Create Text field 
entryNum1 = Entry(root, textvariable=rollno).grid(row=4, column=2)  
entryNum2 = Entry(root, textvariable=name).grid(row=5, column=2)
entryNum3 = Entry(root, textvariable=city).grid(row=6, column=2)
entryNum4 = Entry(root, textvariable=state).grid(row=7, column=2)
entryNum5 = Entry(root, textvariable=new).grid(row=6, column=10)

call_result = partial(call_result, labelResult, rollno, name,city, state)  
delete = partial(delete, labelResult, rollno)
update = partial(update, labelResult, rollno, name,city, state)
colu = partial(colu, labelResult, new)

buttonCal = Button(root, text="add data", command=call_result).grid(row=9, column=0)  
buttonCal1 = Button(root, text="Delete", command=delete).grid(row=9, column=1)
buttonCal2 = Button(root, text="Update", command=update).grid(row=11, column=0)
buttonCal3 = Button(root, text="Add col", command=colu).grid(row=7, column=8)

root.mainloop()  
myconn.close()
