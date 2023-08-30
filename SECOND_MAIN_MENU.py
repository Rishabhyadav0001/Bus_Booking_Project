from tkinter import *
root=Tk()
Label(root,text=' ').grid(row=0,column=0,padx=150)
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
p=w//3
img=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
Label(frame1,image=img).grid(row=0,column=6,padx=p)
Label(root,text='ONLINE BUS BOOKING SYSTEM',fg='red',bg='light blue',font='times 20 bold').grid(row=2,column=3,padx=50)
Label(root,text=' ').grid(row=3,column=0,padx=150)
def main_to_book():
   root.destroy()
   import THIRD_SEARCHING_BOOKING.py
def main_to_check():
   root.destroy()
   import FORTH_TICKET_CHECK.py
def main_to_detail():
   root.destroy()
   import FIFTH_DATABSE_ADD.py   
Button(root,text='Seat Booking',bg='green',font='times 16',command=main_to_book).grid(row=4,column=2)
Button(root,text='Check Booked Seat',bg='green',font='times 16',command=main_to_check).grid(row=4,column=3)
Button(root,text='Add Bus Details',bg='green',font='times 16',command=main_to_detail).grid(row=4,column=4)
Label(root,text='For Admin only',font='aerial 12').grid(row=6,column=4)
root.mainloop()
