from tkinter import *
from tkinter.messagebox import *

import sqlite3
con=sqlite3.connect('MyDB')
cur=con.cursor()

root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
p=w//3
img=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(columnspan=10,padx=p)
Label(frame1,image=img).grid(row=0,column=3)
Label(root,text=' ').grid(row=1,column=0,padx=150)
Label(frame1,text='ONLINE BUS BOOKING SYSTEM',fg='red',bg='light blue',font='times 20 bold').grid(row=2,column=3,padx=50)
Label(root,text=' ').grid(row=3,column=0,padx=150)
Label(frame1,text='Add Bus Route Details',fg='green',font='times 18 bold').grid(row=4,column=3,padx=50)
Label(root,text=' ').grid(row=5,column=0,padx=150)
Label(root,text=' ').grid(row=6,column=0,padx=150)
Label(root,text='Route Id',font='aerial 14').grid(row=7,column=0)
rid=Entry(root)
rid.grid(row=7,column=1)
Label(root,text='Station Name',font='aerial 14').grid(row=7,column=2)
sname=Entry(root)
sname.grid(row=7,column=3)
Label(root,text='Station Id',font='aerial 14').grid(row=7,column=4)
sid=Entry(root)
sid.grid(row=7,column=5)

def added():
    if rid.get()!='':
        cur.execute("""insert into route(rid,sid,sname) values(?,?,?)""",(rid.get(),sid.get(),sname.get())) 
        Label(root,text=rid.get()+" "+sid.get()+" "+sname.get()).grid(row=8,column=1,columnspan=5)
        showinfo('Detail','Successfully Added')
    else:
        showerror('Error','No Route Id')
def deleted():
    Label(root,text=rid.get()+" "+sname.get()+" "+sid.get()).grid(row=8,column=1,columnspan=5)
    showinfo('Detail','Successfully Deleted') 
Button(root,text='Add Route',bg='light green',font='aerial 12 bold',command=added).grid(row=7,column=6)
Button(root,text='Delete Route',fg='red',bg='light green',font='aerial 12 bold',command=deleted).grid(row=7,column=7,rowspan=2)
imgh=PhotoImage(file='.\\home.png')
Label(root,text=' ').grid(row=9,column=0,padx=150)
def home():
   root.destroy()
   import SECOND_MAIN_MENU.py
Button(root,image=imgh,bg='green',command=home).grid(row=10,column=4)
root.mainloop()
con.commit()
