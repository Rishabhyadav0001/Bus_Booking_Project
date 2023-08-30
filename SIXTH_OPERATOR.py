from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('MyDB')
cur=con.cursor()

root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
p=w//3
img=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(columnspan=15,padx=p)
Label(frame1,image=img).grid(row=0,column=3)
Label(root,text=' ').grid(row=1,column=0,padx=150)
Label(frame1,text='ONLINE BUS BOOKING SYSTEM',fg='red',bg='light blue',font='times 20 bold').grid(row=2,column=3,padx=50)
Label(root,text=' ').grid(row=3,column=0,padx=150)
Label(frame1,text='Add Bus Operator Details',fg='green',font='times 18 bold').grid(row=4,column=3,padx=50)
Label(root,text=' ').grid(row=5,column=0,padx=150)
Label(root,text=' ').grid(row=6,column=0,padx=150)
Label(root,text='Operator Id',font='aerial 14').grid(row=7,column=0)
opid=Entry(root)
opid.grid(row=7,column=1)
Label(root,text='Name',font='aerial 14').grid(row=7,column=2)
name=Entry(root)
name.grid(row=7,column=3)
Label(root,text='Address',font='aerial 14').grid(row=7,column=4)
address=Entry(root)
address.grid(row=7,column=5)
Label(root,text='Phone',font='aerial 14').grid(row=7,column=6)
phone=Entry(root)
phone.grid(row=7,column=7)
Label(root,text='Email',font='aerial 14').grid(row=7,column=8)
email=Entry(root)
email.grid(row=7,column=9)
def added():
    if opid.get()!='':
        cur.execute("""insert into operator(opid,name,address,phone,email) values(?,?,?,?,?)""",(opid.get(),name.get(),address.get(),phone.get(),email.get()))
        Label(root,text=opid.get()+" "+name.get()+" "+address.get()+" "+phone.get()+" "+email.get()).grid(row=9,column=2,columnspan=7)
        showinfo('Detail','Successfully Added')
        cur.execute("select * from operator")
        res=cur.fetchall()
        print(res)
    else:
        showerror('Error','No Operator Id')
def edited():
    Label(root,text=opid.get()+" "+name.get()+" "+address.get()+" "+phone.get()+" "+email.get()).grid(row=9,column=2,columnspan=7)
    showinfo('Detail','Successfully Edited')
Button(root,text='Add',bg='light green',font='aerial 12 bold',command=added).grid(row=7,column=11)
Button(root,text='Edit',bg='light green',font='aerial 12 bold',command=edited).grid(row=7,column=12,rowspan=2)
imgh=PhotoImage(file='.\\home.png')
Label(root,text=' ').grid(row=10,column=0,padx=150)
def home():
   root.destroy()
   import SECOND_MAIN_MENU.py
Button(root,image=imgh,bg='green',command=home).grid(row=11,column=9)
root.mainloop()
con.commit()
