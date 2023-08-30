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
Label(frame1,text='Add Bus Running Details',fg='green',font='times 18 bold').grid(row=4,column=3,padx=50)
Label(root,text=' ').grid(row=5,column=0,padx=150)
Label(root,text=' ').grid(row=6,column=0,padx=150)
Label(root,text='Bus Id',font='aerial 14').grid(row=7,column=0)
bid=Entry(root)
bid.grid(row=7,column=1)
Label(root,text='Running Date',font='aerial 14').grid(row=7,column=2)
rdate=Entry(root)
rdate.grid(row=7,column=3)
Label(root,text='Seat Available',font='aerial 14').grid(row=7,column=4)
available=Entry(root)
available.grid(row=7,column=5)

def added():
    if bid.get()!='':
        cur.execute("""insert into run(bid,rdate,available) values(?,?,?)""",(bid.get(),rdate.get(),available.get()))
        Label(root,text=bid.get()+" "+rdate.get()+" "+available.get()).grid(row=8,column=1,columnspan=5)
        showinfo('Detail','Successfully Added')
    else:
        showerror('Error','No Route Id')
def deleted():
    Label(root,text=bid.get()+" "+rdate.get()+" "+available.get()).grid(row=8,column=1,columnspan=5)
    showinfo('Detail','Successfully Deleted') 
Button(root,text='Add Run',bg='light green',font='aerial 12 bold',command=added).grid(row=7,column=6)
Button(root,text='Delete Run',fg='red',bg='light green',font='aerial 12 bold',command=deleted).grid(row=7,column=7,rowspan=2)
imgh=PhotoImage(file='.\\home.png')
Label(root,text=' ').grid(row=9,column=0,padx=150)
def home():
   root.destroy()
   import SECOND_MAIN_MENU.py
Button(root,image=imgh,bg='green',command=home).grid(row=10,column=4)
root.mainloop()
con.commit()

