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
frame1.grid(columnspan=13)
Label(frame1,image=img).grid(row=0,column=3,padx=p)
Label(root,text=' ').grid(row=1,column=0,padx=150)
Label(root,text='Online Bus booking System',bg='light blue',fg='red',font='times 20 bold').grid(row=2,column=2,columnspan=7)
Label(root,text=' ').grid(row=3,column=0,padx=150)
Label(root,text='Add Bus Details',fg='green',font='times 18 bold').grid(row=4,column=2,columnspan=7,rowspan=2)
Label(root,text=' ').grid(row=5,column=0,padx=150)
Label(root,text=' ').grid(row=6,column=0,padx=150)
Label(root,text='Bus Id',font='aerial 12 bold').grid(row=7,column=0)
bid=Entry(root)
bid.grid(row=7,column=1)
bus_type=StringVar()
Label(root,text='Bus Type',font='aerial 12 bold').grid(row=7,column=2)
bus_type.set("SELECT BUS TYPE")
option=('2X2','2X2 AC','3X3','3X3 AC')
d_menu=OptionMenu(root,bus_type,*option)
d_menu.grid(row=7,column=3)
Label(root,text='Capacity',font='aerial 12 bold').grid(row=7,column=4)
capacity=Entry(root)
capacity.grid(row=7,column=5)
Label(root,text='Fare Rs.',font='aerial 12 bold').grid(row=7,column=6)
fare=Entry(root)
fare.grid(row=7,column=7)
Label(root,text='Operator id',font='aerial 12 bold').grid(row=7,column=8)
opid=Entry(root)
opid.grid(row=7,column=9)
Label(root,text='Route id',font='aerial 12 bold').grid(row=7,column=10)
rid=Entry(root)
rid.grid(row=7,column=11)
def added():
    if bid.get()!='':
        cur.execute("""insert into bus(bid,bus_type,capacity,fare,rid,opid) values(?,?,?,?,?,?)""",(bid.get(),bus_type.get(),capacity.get(),fare.get(),rid.get(),opid.get()))
        Label(root,text=bid.get()+" "+bus_type.get()+" "+capacity.get()+" "+fare.get()+" "+rid.get()+" "+opid.get()).grid(row=8,column=2,columnspan=7)
        showinfo('Detail','Successfully Added')
    else:
        showerror('Error','No Bus Id')
def edited():
    Label(root,text=bid.get()+" "+bus_type.get()+" "+capacity.get()+" "+fare.get()+" "+rid.get()+" "+opid.get()).grid(row=8,column=2,columnspan=7)
    showinfo('Detail','Successfully Edited') 
Label(root,text=' ').grid(row=9,column=0,padx=150)
Button(root,text='Add Bus',font='aerial 12 bold',bg='light green',command=added).grid(row=10,column=4)
Button(root,text='Edit Bus',font='aerial 12 bold',bg='light green',command=edited).grid(row=10,column=6,rowspan=2)
imgh=PhotoImage(file='.\\home.png')
def home():
    root.destroy()
    import SECOND_MAIN_MENU.py
Button(root,image=imgh,bg='green',command=home).grid(row=10,column=8)
root.mainloop()
con.commit()

