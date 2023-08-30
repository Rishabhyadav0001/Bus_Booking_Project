from tkinter import *
root=Tk()
Label(root,text=' ').grid(row=0,column=0,padx=150)
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
Label(frame1,text='Add New Details To Database',fg='green',font='times 16 bold').grid(row=4,column=3,padx=50)
Label(root,text=' ').grid(row=5,column=0,padx=150)
Label(root,text=' ').grid(row=6,column=0,padx=150)
def operator():
   root.destroy()
   import SIXTH_OPERATOR.py
def bus():
   root.destroy()
   import SEVENTH_BUS_DETAIL.py
def route():
   root.destroy()
   import EIGHT_ROUTE.py
def run():
   root.destroy()
   import NINE_BUS_RUN.py
Button(root,text='New Operator',bg='green',font='times 16',command=operator).grid(row=7,column=1)
Button(root,text='New Bus',bg='orange',font='aerial 14',command=bus).grid(row=7,column=2)
Button(root,text='New Route',bg='blue',fg='white',font='aerial 14',command=route).grid(row=7,column=3)
Button(root,text='New Run',bg='pink',font='aerial 14',command=run).grid(row=7,column=4)
root.mainloop()
