from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("Bus Booking System")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
p=w//3
img=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(columnspan=18,padx=p)
frame2=Frame(root)
frame2.grid(row=12,columnspan=18)
Label(frame1,image=img).grid(row=0,column=3)
Label(root,text=' ').grid(row=1,column=0,padx=150)
Label(frame1,text='ONLINE BUS BOOKING SYSTEM',fg='red',bg='light blue',font='times 20 bold').grid(row=2,column=3,padx=50,pady=20)
Label(root,text=' ').grid(row=3,column=0,padx=150)
Label(frame1,text='Enter Journey Details',bg='light green',fg='green',font='times 18 bold').grid(row=4,column=3,padx=50)
Label(root,text='To',font='aerial 14').grid(row=4,column=0)
to=Entry(root)
to.grid(row=4,column=1)
Label(root,text='From',font='aerial 14').grid(row=4,column=2)
fom=Entry(root)
fom.grid(row=4,column=3)
Label(root,text='Journey date',font='aerial 14').grid(row=4,column=4)
Date=Entry(root)
Date.grid(row=4,column=5)
def book():
   showinfo('Status','Successfully Seat Booked')   
def perinfo():
   Label(root,text=' ').grid(row=11,column=0,padx=150)
   Label(frame2,text='Fill Passenger Details To Book The Bus Ticket',fg='red',bg='light blue',font='times 20 bold').grid(row=12)
   Label(root,text=' ').grid(row=13,column=0,padx=150)
   Label(root,text='Name',font='aerial 14').grid(row=14,column=0)
   namep=Entry(root)
   namep.grid(row=14,column=1)
   gen=StringVar()
   Label(root,text='Gender',font='aerial 12 bold').grid(row=14,column=2)
   gen.set("Gender")
   option=('Male','Female')
   d_menu=OptionMenu(root,gen,*option)
   d_menu.grid(row=14,column=3)
   Label(root,text='No. of Seats',font='aerial 14').grid(row=14,column=4)
   nos=Entry(root)
   nos.grid(row=14,column=5)
   Label(root,text='Mobile No.',font='aerial 14').grid(row=14,column=6)
   mn=Entry(root)
   mn.grid(row=14,column=7)
   Label(root,text='Age',font='aerial 14').grid(row=14,column=8)
   age=Entry(root)
   age.grid(row=14,column=9)
   Button(root,text='Book Seat',bg='light green',font='aerial 14',command=book).grid(row=14,column=10)
def buses():
   Label(root,text=' ').grid(row=5,column=0,padx=150)
   Label(root,text='Select Bus',fg='green',font='aerial 14').grid(row=6,column=0)
   Label(root,text='Operator',fg='green',font='aerial 14').grid(row=6,column=1)
   Label(root,text='Bus Type ',fg='green',font='aerial 14').grid(row=6,column=2)
   Label(root,text='Available/Capacity',fg='green',font='aerial 14').grid(row=6,column=3)
   Label(root,text='Fare',fg='green',font='aerial 14').grid(row=6,column=4)
   Button(root,text='Proceed To Book',bg='light green',font='aerial 14',command=perinfo).grid(row=7,column=7)
Button(root,text='Show Buses',bg='light green',font='aerial 14',command=buses).grid(row=4,column=7)
imgh=PhotoImage(file='.\\home.png')
def home():
   root.destroy()
   import SECOND_MAIN_MENU.py
Button(root,image=imgh,bg='green',command=home).grid(row=4,column=8)
root.mainloop()
