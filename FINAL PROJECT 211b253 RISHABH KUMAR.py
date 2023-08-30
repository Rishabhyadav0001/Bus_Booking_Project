from tkinter import*
import sqlite3
from tkinter.messagebox import *
from datetime import date
con=sqlite3.connect('my_database')
cur=con.cursor()

cur.execute('create table if not exists bus(bus_id varchar(5) not null primary key,bus_type varchar(10),capacity int,fair int,op_id varchar(5) not null,route_id varchar(5) not null,foreign key(op_id) references operator(opr_id),foreign key(route_id) references route(r_id))')
cur.execute('create table if not exists operator(opr_id varchar(5) primary key,name varchar(20),address varchar(50),phone char(10),email varchar(30))')
cur.execute('create table if not exists running(b_id varchar(5) ,run_date date,seat_avail int,foreign key(b_id) references bus(bus_id))')
cur.execute('create table if not exists route(r_id varchar(5) not null primary key,s_name varchar(20),s_id varchar(5),e_name varchar(20),e_id varchar(5) )')
cur.execute('create table if not exists booking_history(name varchar(20),gender char(1),no_of_seat int,phone char(10),age int,booking_ref varchar(10) not null primary key,booking_date date,travel_date date,bid varchar(5),foreign key(bid) references bus(bus_id))')

class bus_booking:

    def home_page(self):
        root = Tk()
        root.title("HOME PAGE")                                                                                                                                      

        bus = PhotoImage(file='Bus_for_project.png')
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        Label(root, text='\n\n\n\n').grid(row=0, column=0)
        Label(root, image=bus).grid(row=1, column=1, columnspan=12, padx=w // 2.5)
        Label(root, text="Online Bus Booking System", font='Arial 20 bold', bg='light blue', fg='red').grid(row=2,column=2,columnspan=9,padx=w // 2.5)

        def home_to_jouney_detail():
            root.destroy()
            self.journey_detail_page()

        def home_to_check_booking():
            root.destroy()
            self.check_booking_page()

        def home_to_db_add_page():
            root.destroy()
            self.db_add_page()

        Label(root, text='\n\n\n\n\n\n').grid(row=3, column=4)
        Button(root, text='Seat Booking', font='Arial 14 bold', bg='green', fg='black',command=home_to_jouney_detail).grid(row=4, column=4)
        Label(root, text='\n\n\n\n\n\n').grid(row=3, column=6)
        Button(root, text='Check Booked Seat', font='Arial 14 bold', bg='green', fg='black',command=home_to_check_booking).grid(row=4, column=6)
        Label(root, text='\n\n\n\n\n\n').grid(row=3, column=8)
        Button(root, text='Add Bus Details', font='Arial 14 bold', bg='green', fg='black',command=home_to_db_add_page ).grid(row=4, column=8)
        Label(root, text='\n').grid(row=5, column=8)
        Label(root, text='For Admin Only', fg='red',font=' times').grid(row=6, column=8)

        root.mainloop()

    def cover_page(self):
        root = Tk()
        root.title("COVER PAGE")
        bus = PhotoImage(file='Bus_for_project.png')
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        root.geometry('%dx%d'%(w,h))
        p=w//3
        img=PhotoImage(file='.\\Bus_for_project.png')
        frame1=Frame(root)
        frame1.grid(row=0,column=0,columnspan=10)
        Label(frame1,image=img).grid(row=0,column=6,padx=p)
        Label(root,text='ONLINE BUS BOOKING SYSTEM',bg='light blue',fg='red',font='times 20 bold').grid(row=2,column=3,rowspan=3,padx=p)
        Label(root,text=' ').grid(row=3,column=0)
        Label(root,text=' ').grid(row=4,column=0)
        Label(root,text='Name : RISHABH KUMAR ',fg='blue',font='times 18 bold').grid(row=5,column=3,rowspan=3,padx=p)  
        Label(root,text=' ').grid(row=6,column=0)
        Label(root,text=' ').grid(row=7,column=0)
        Label(root,text='Er. : 211B253',fg='blue',font='times 18 bold').grid(row=8,column=3,rowspan=3,padx=p)
        Label(root,text=' ').grid(row=9,column=0)
        Label(root,text=' ').grid(row=10,column=0)
        Label(root,text='Mobile : 9054489105',fg='blue',font='times 18 bold').grid(row=11,column=3,rowspan=3,padx=p)
        Label(root,text=' ').grid(row=12,column=0)
        Label(root,text=' ').grid(row=13,column=0)
        Label(root,text='Submitted to : Dr. Mahesh Kumar',bg='light blue',fg='red',font='times 20 bold').grid(row=14,column=3,rowspan=3,padx=p)
        Label(root,text=' ').grid(row=15,column=0)
        Label(root,text=' ').grid(row=16,column=0)
        Label(root,text='Project Based Learning',fg='red',font='times 18 bold').grid(row=22,column=3,rowspan=3,padx=p)

        def cover_to_home(event):
            root.destroy()
            self.home_page()

        root.bind("<KeyPress>", cover_to_home)
        root.mainloop()

    def journey_detail_page(self):
        root = Tk()
        root.title("SEAT BOOKING PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        def journey_to_home():
            root.destroy()
            self.home_page()

        def show_bus():
            tp=to_place.get()
            fp=from_place.get()
            jd=journey_date.get()

            if tp.isalpha() and fp.isalpha():
                if not jd=='':
                    tp = tp.lower()
                    fp = fp.lower()
                    cur.execute('select r_id from route where s_name=? and e_name=?', (fp, tp))
                    res_route = cur.fetchall()
                    if len(res_route)==0:
                        showerror('no route found','we are currently not running on this route')
                    else:
                        for i in res_route:
                            for j in i:
                                val_route = str(j)

                        cur.execute('select bus_id from bus where route_id=?', (val_route))
                        res_bid = cur.fetchall()

                        if len(res_bid)==0:
                            showerror('no bus found','we have not started any bus on this route yet!!')
                        else:
                            val_bid = []
                            for i in res_bid:
                                for j in i:
                                    val_bid.append(j)
                            res_new_bid=[]
                            for i in range(len(val_bid)):
                                cur.execute('select b_id from running where run_date=? and b_id=? ',(jd, val_bid[i]))
                                res_new_bid.append(cur.fetchall())
                            #print(res_new_bid)
                            b=[]
                            for i in res_new_bid:
                                for j in i:
                                    b.append(j[0])

                            #print(b)
                            if len(b)==0:
                                showerror('no running bus',"try another date!!")
                            else:
                                Label(root,text='select bus ',font='Arial 10 bold').grid(row=6,column=3)
                                Label(root, text='operator ', font='Arial 10 bold').grid(row=6, column=4)
                                Label(root, text='bus_type ', font='Arial 10 bold').grid(row=6, column=5)
                                Label(root, text='Available Capacity ', font='Arial 10 bold').grid(row=6, column=6)
                                Label(root, text='fare ', font='Arial 10 bold').grid(row=6, column=7)
                                r=7
                                bus_no=IntVar()
                                bus_select = IntVar()
                                serial_no=1
                                for i in b:
                                    bus_no=i
                                    cur.execute('select op_id from bus where bus_id=?',(i))
                                    res_opr_id=cur.fetchall()
                                    for j in res_opr_id:
                                        opr_id=j[0]

                                    cur.execute('select name from operator where opr_id=?',(opr_id))
                                    res_opr_name=cur.fetchall()
                                    for j in res_opr_name:
                                        opr_name=j[0]

                                    cur.execute('select bus_type from bus where bus_id=?',(i))
                                    res_bus_type=cur.fetchall()
                                    for j in res_bus_type:
                                        bus_type=j[0]

                                    cur.execute('select seat_avail from running where run_date=? and b_id=?',(jd,i))
                                    res_seat_avail=cur.fetchall()
                                    for j in res_seat_avail:
                                        seat_avail=j[0]
                                    cur.execute('select capacity from bus where bus_id=?',(i))
                                    rishabh=cur.fetchall()
                                    for j in rishabh:
                                        capacity=j[0]
                                        
                                    cur.execute('select fair from bus where bus_id=?',(i))
                                    res_fare=cur.fetchall()
                                    for j in res_fare:
                                        fare=j[0]

                                    def show_button():
                                        Button(root, text='PROCEED', bg='green', fg='black', font='Arial 12 bold',
                                               command=proceed).grid(row=10, column=9, padx=30)

                                    var=Radiobutton(root,value=bus_no,variable=bus_select,command=show_button)
                                    var.grid(row=r,column=3)
                                    Label(root, text=opr_name, font='Arial 10 bold').grid(row=r, column=4)
                                    Label(root, text=bus_type, font='Arial 10 bold').grid(row=r, column=5)
                                    Label(root, text=str(seat_avail)+'/'+str(capacity), font='Arial 10 bold').grid(row=r, column=6)
                                    Label(root, text=fare, font='Arial 10 bold').grid(row=r, column=7)

                                    r+=1
                                    serial_no+=1

                                def proceed():
                                    f_bus_id = bus_select.get()
                                    Label(root,text="\n\n\n").grid(row=10,columnspan=12)
                                    Label(root,text='Fill passenger details to book the bus', fg='red', font='Arial 18 bold').grid(row=11,columnspan=12)
                                    Label(root, text="\n\n\n").grid(row=12,columnspan=12)

                                    Label(root,text='name',font='Arial 10 bold').grid(row=13,column=3)
                                    pname = Entry(root, font='Arial 12 bold')
                                    pname.grid(row=13,column=4)

                                    gender = StringVar()
                                    gender.set("Select Gender")
                                    opt = ["Male", "Female", "other"]
                                    g_menu = OptionMenu(root, gender, *opt)
                                    g_menu.grid(row=13, column=6)

                                    Label(root, text='no of seats', font='Arial 10 bold').grid(row=13, column=7)
                                    pseat=Entry(root, font='Arial 12 bold')
                                    pseat.grid(row=13,column=8)

                                    Label(root, text='mobile', font='Arial 10 bold').grid(row=14, column=3)
                                    pmobile = Entry(root, font='Arial 12 bold')
                                    pmobile.grid(row=14, column=4)

                                    Label(root, text='age', font='Arial 10 bold').grid(row=14, column=5)
                                    page = Entry(root, font='Arial 12 bold')
                                    page.grid(row=14, column=6)

                                    def book_seat():
                                        name=pname.get()
                                        gen=gender.get()
                                        seats=pseat.get()
                                        seats=int(seats)
                                        age=page.get()
                                        age=int(age)
                                        mobile=pmobile.get()
                                        bid=bus_select.get()
                                        if len(mobile)==10:
                                            if len(name)>0 and len(name)<20:
                                                if age>0 and age<150:
                                                    cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                    res_s=cur.fetchall()
                                                    s=res_s[0][0]
                                                    if seats<s+1 and seats>0:
                                                        #print(name, gen, age, mobile, seats, bid)
                                                        booking_ref=1
                                                        cur.execute('select booking_ref from booking_history')
                                                        res_ref=cur.fetchall()
                                                        ref=[]
                                                        for i in res_ref:
                                                            ref.append(i[0])
                                                        booking_ref=len(ref)+1
                                                        #print(booking_ref)
                                                        cur_date=date.today()
                                                        cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                        con.commit()
                                                        cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                        res_s=cur.fetchall()
                                                        s=res_s[0][0]
                                                        s=s-seats
                                                        cur.execute('update running set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                        con.commit()
                                                        showinfo("succefull","booking successfull")
                                                        root.destroy()
                                                        def ticket():
                                                            root=Tk()
                                                            Label(root,text='').grid(row=0,column=0,padx=150)
                                                            h,w=root.winfo_screenwidth(),root.winfo_screenheight()
                                                            root.geometry('%dx%d+0+0'%(h,w))
                                                            frame1=Frame(root)
                                                            Label(frame1, text = "").grid(row = 0, column = 0, padx = 225)
                                                            Label(root, text = "").grid(row = 0, column = 0, padx = 250)
                                                            frame1.grid(row=0,column=0,columnspan=10)
                                                            root.title("online bus booking system")
                                                            Img=PhotoImage(file='.\\Bus_for_project.png')
                                                            Label(frame1,image=Img).grid(row=0,column=1,columnspan=10)
                                                            Label(frame1,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,columnspan=10)
                                                            Label(frame1,text="Seat Booked",fg='forest green',font=("Arial bold",20),bg='light green').grid(row=2,column=1,pady=30,columnspan=10)
                                                                
                                                            showinfo('Booking','Seat Booked')
                                                            frame=Frame(root,relief='groove',bd=5)
                                                            frame.grid(column=1,columnspan=8,padx=150,pady=20)
                                                            Label(frame,text="Passenger:"+str(name),font=("Arial bold",12)).grid(row=2,column=2)
                                                            Label(frame,text="Gender:"+str(gen),font=("Arial bold",12)).grid(row=2,column=4)
                                                            Label(frame,text="No. of seats:"+ str(seats),font=("Arial bold",12)).grid(row=3,column=2)
##                                                            Label(frame,text="Phone:"+ str(pmobile),font=("Arial bold",12)).grid(row=3,column=4)
                                                            Label(frame,text="Age:" + str(age),font=("Arial bold",12)).grid(row=4,column=2)
                                                            Label(frame,text="Fare:"+ str(fare),font=("Arial bold",12)).grid(row=4,column=4)
##                                                            Label(frame,text="Booking Ref:"+str(b_ref),font=("Arial bold",12)).grid(row=5,column=2)
                                                            #Label(frame,text="Travel on:"+ travel_date,font=("Arial bold",12)).grid(row=5,column=4)
                                                        ticket()

                                                    else:
                                                        showerror("booking limit exceed","The seats are not sufficient")
                                                else:
                                                    showerror("incorrect age","enter valid age")
                                            else:
                                                showerror("incorrect name","enter valid name")
                                        else:
                                            showerror("invalid mobile no","enter valid mobile no")


                                    Button(root, text='BOOK SEAT', bg='green', fg='black', font='Arial 12 bold',
                                           command=book_seat).grid(row=16, column=9, padx=30)



                else:
                    showerror('error','enter journey date')


            else:
                showerror('ERROR',"enter correctly!!")


        bus = PhotoImage(file='Bus_for_project.png')
        Label(root, image=bus).grid(row=0, column=3, columnspan=12)
        Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=2,column=3,pady=20,columnspan=12)
        Label(root, text='Enter Journey Details', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=3,column=3,columnspan=12,pady=20)
        Label(root, text='To', fg='black', font='Arial 12 bold').grid(row=4, column=3, padx=30)
        to_place = Entry(root, font='Arial 12 bold', fg='black')
        to_place.grid(row=4, column=4, padx=50)

        Label(root, text='From', fg='black', font='Arial 12 bold').grid(row=4, column=5, padx=30)
        from_place = Entry(root, font='Arial 12 bold', fg='black')
        from_place.grid(row=4, column=6, padx=50)

        Label(root, text='Journey date', fg='black', font='Arial 12 bold').grid(row=4, column=7, padx=30)
        journey_date = Entry(root, font='Arial 12 bold', fg='black')
        journey_date.grid(row=4, column=8, padx=50)
        Label(root,text="date formate YYYY-MM-DD").grid(row=5,column=8)

        Button(root, text='Show Bus', bg='green', fg='black', font='Arial 12 bold',command=show_bus).grid(row=4, column=9, padx=30)

        home = PhotoImage(file='home.png')

        Button(root, image=home,command=journey_to_home).grid(row=4, column=10)

        root.mainloop()

    def check_booking_page(self):
        root = Tk()
        root.title("CHECK BOOKING PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='Bus_for_project.png')
        home=PhotoImage(file='home.png')

        def check_booking_to_home():
            root.destroy()
            self.home_page()
        def check_tkt():
            mobile=mob.get()
            if len(mobile)==10 and mobile.isdigit():
                cur.execute('select * from booking_history where phone=?',[mobile])
                res_tkt=cur.fetchall()
                for i in res_tkt:
                    name=i[0]
                    gen=i[1]
                    seat=i[2]
                    phone=i[3]
                    age=i[4]
                    ref=i[5]
                    book_date=i[6]
                    travel_date=i[7]
                    b_i_d=i[8]
                cur.execute('select fair,route_id from bus where bus_id=?',[b_i_d])
                res_bus=cur.fetchall()
                fare=res_bus[0][0]
                route_id=res_bus[0][1]
                cur.execute('select s_name,e_name from route where r_id=?',[route_id])
                res_route=cur.fetchall()
                s_name=res_route[0][0]
                e_name=res_route[0][1]
                cur.execute('select booking_ref from booking_history where phone=?',[phone])
                res_ref=cur.fetchall()
                b_ref=res_ref[0][0]
                Label(root,text=' ').grid(row=8,column=0,padx=150)
                Label(root,text=' ').grid(row=9,column=0,padx=150)
                frame=Frame(root,relief='groove',bd=10)
                frame.grid(column=1,columnspan=8,padx=150)
                Label(frame,text='Passenger :' + str(name),font='aerial 14').grid(row=10,column=2)
                Label(frame,text=' ',font='aerial 14').grid(row=10,column=3)
                Label(frame,text='Gender :' + gen,font='aerial 14').grid(row=10,column=4)
                Label(frame,text='No. of seats :'+str(seat),font='aerial 14').grid(row=11,column=2)
                Label(frame,text=' ',font='aerial 14').grid(row=11,column=3)
                Label(frame,text='Phone :'+phone,font='aerial 14').grid(row=11,column=4)
                Label(frame,text='Age :'+ str(age),font='aerial 14').grid(row=12,column=2)
                Label(frame,text=' ',font='aerial 14').grid(row=12,column=3)
                Label(frame,text='Fare : '+ str(fare),font='aerial 14').grid(row=12,column=4)
                Label(frame,text='Booking Ref. :'+b_ref,font='aerial 14').grid(row=13,column=2)
                Label(frame,text=' ',font='aerial 14').grid(row=13,column=3)
                Label(frame,text='Travel on :' + travel_date,font='aerial 14').grid(row=13,column=4)
                Label(frame,text='Booked On:'+ book_date,font='aerial 14').grid(row=14,column=2)
                Label(frame,text=' ',font='aerial 14').grid(row=14,column=3)
                Label(frame,text='*Total fare is to be paid at the time of boarding' + str(fare*seat),font='times 12 italic').grid(row=15,column=2,columnspan=2)
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        root.geometry('%dx%d'%(w,h))
        p=w//3
        img=PhotoImage(file='.\\Bus_for_project.png')
        frame1=Frame(root)
        frame1.grid(row=0,column=0,columnspan=10)
        Label(frame1,image=img).grid(row=0,column=6,padx=p)
        Label(root,text='Online Bus booking System',bg='light blue',fg='red',font='aerial 16 bold').grid(row=1,column=2)
        Label(root,text=' ').grid(row=2,column=0,padx=150)
        Label(root,text='Check Your Booking',fg='green',bg='light green',font='times 16 bold').grid(row=3,column=2)
        Label(root,text=' ').grid(row=4,column=0,padx=150)
        Label(root,text=' ').grid(row=5,column=0,padx=150)
        Label(root,text='Enter Your Mobile No.',font='times 14 bold').grid(row=6,column=1)
        mob=Entry(root,font='aerial 12 ')
        mob.grid(row=6,column=2)

        Button(root, text='Check Booking', font='Arial 12',command=check_tkt).grid(row=6,column=3)
        Button(root, image=home,command=check_booking_to_home).grid(row=5, column=7,pady=20)
        root.mainloop()

    def db_add_page(self):
        root = Tk()
        root.title("ADMIN PAGE")
        root.title('Database Add Page')
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        bus = PhotoImage(file='.\\Bus_for_project.png')

        def db_add_to_add_op():
            root.destroy()
            self.add_bus_op_details_page()

        def db_add_to_add_bus():
            root.destroy()
            self.add_bus_page()

        def db_add_to_add_route():
            root.destroy()
            self.add_route_page()

        def db_add_to_add_running():
            root.destroy()
            self.add_bus_running_page()

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
        Button(root,text='New Operator',bg='green',font='times 16',command=db_add_to_add_op).grid(row=7,column=1)
        Button(root,text='New Bus',bg='orange',font='aerial 14',command=db_add_to_add_bus).grid(row=7,column=2)
        Button(root,text='New Route',bg='blue',fg='white',font='aerial 14',command=db_add_to_add_route).grid(row=7,column=3)
        Button(root,text='New Run',bg='pink',font='aerial 14',command=db_add_to_add_running).grid(row=7,column=4)
         
        root.mainloop()

    def add_bus_op_details_page(self):
        root = Tk()
        root.title("ADD BUS OPERATOR PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        bus = PhotoImage(file='Bus_for_project.png')
        home=PhotoImage(file='home.png')

        def op_add():
            iid = opr_id.get()
            iname = name.get()
            iaddress = address.get()
            iphone = phone.get()
            iemail = email.get()
            cur.execute('select opr_id from operator')
            res=cur.fetchall()
            
            if len(iid) > 0 and len(iid) <= 5 and iid.isnumeric():
                if  len(iname) < 20 and len(iname) > 0:
                    if len(iaddress) < 50 and len(iaddress) > 0:
                        if iphone.isnumeric() and len(iphone) == 10:
                            if len(iemail) > 0 and len(iemail) < 30:
                                if (iid,) in res:
                                    showerror("ERROR","operator id already exists!!")
                                else:
                                    cur.execute('insert into operator (opr_id,name,address,phone,email)values(?,?,?,?,?)',(iid, iname, iaddress, iphone, iemail))
                                    con.commit()
                                    showinfo('success', "operator added successfully!!")

                                
                            else:
                                showerror("invalid input", "enter email correctly")
                        else:
                            showerror("invalid input", "enter phone correctly")
                    else:
                        showerror("invalid input", "enter address correctly")
                else:
                    showerror("invalid input", "enter name correctly")
            else:
                showerror("invalid input", "enter id correctly")


        def db_add_to_home():
            root.destroy()
            self.home_page()
        
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
        opr_id=Entry(root)
        opr_id.grid(row=7,column=1)
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


        Button(root, text="Add", font='Arial 12 bold', bg='green2', fg='black',command=op_add).grid(row=7,column=11)
        Button(root, text="Edit", font='Arial 12 bold', bg='green2', fg='black').grid(row=7,column=12,rowspan=2)

        
        Button(root, image=home,command=db_add_to_home).grid(row=11,column=9)
        root.mainloop()

    def add_bus_page(self):
        root = Tk()
        root.title("ADD BUS PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        bus = PhotoImage(file='Bus_for_project.png')
        
        def bus_add():
            bid=b_id.get()
            dmenu=bus_type.get()
            capa=capacity.get()
            fare_rs=fare.get()
            opid=op_id.get()
            route_id=r_id.get()
            cur.execute('select bus_id from bus')
            res=cur.fetchall()
            if (bid,) in res:
                showerror("error","bus id already exists!!!")
            else:
                data="bus_id="+bid+"     bus_type="+dmenu+"     capacity="+capa+"     fare="+fare_rs+"     op_id="+opid+"     route_id="+route_id
                cur.execute('insert into bus(bus_id,bus_type,capacity,fair,op_id,route_id) values(?,?,?,?,?,?)',(bid,dmenu,capa,fare_rs,opid,route_id))
                con.commit()
                showinfo('success', "bus added successfully!!")
                Label(root,text=data).grid(row=6,columnspan=12)
                
        '''def edit_bus():
            bid=b_id.get()
            dmenu=bus_type.get()
            capa=capacity.get()
            fare_rs=fare.get()
            opid=op_id.get()
            route_id=r_id.get()
            cur.execute('select bus_id from bus')
            res=cur.fetchall()
            if (bid,) in res:
                data="bus_id="+bid+"     bus_type="+dmenu+"     capacity="+capa+"     fare="+fare_rs+"     op_id="+opid+"     route_id="+route_id
                cur.execute('update bus set bus_type=dmenu, capacity=capa, fair=fare_rs, route_id=route_id where bus_id==bid')
                con.commit()
                Label(root,text=data).grid(row=6,columnspan=12)
            else:
                showerror("error","no such bus id exists, add new bus !!!")'''
                
                
            

        def add_bus_to_home():
            root.destroy()
            self.home_page()

        Label(root, image=bus).grid(row=0, column=0, columnspan=12)
        Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=1,column=0,columnspan=12)
        Label(root, text="Add Bus Details", font='Arial 20 bold', bg='gainsboro', fg='green4').grid(row=2, column=0,pady=20,columnspan=12)
        Label(root, text="Bus ID", font='Arial 12 bold', fg='black').grid(row=3, column=1, pady=50)
        b_id = Entry(root, font="Arial 12")
        b_id.grid(row=3, column=2)

        bus_type = StringVar()
        bus_type.set("Select Bus Type")
        opt = ["2x2", "AC 2x2", "3x2", "AC 3x2"]
        d_menu = OptionMenu(root, bus_type, *opt)
        d_menu.grid(row=3, column=3)
        
        Label(root, text="Capacity", font='Arial 12 bold', fg='black').grid(row=3, column=4)
        capacity = Entry(root, font="Arial 12")
        capacity.grid(row=3, column=5)
        
        Label(root, text="Fare Rs", font='Arial 12 bold', fg='black').grid(row=3, column=6)
        fare = Entry(root, font="Arial 12")
        fare.grid(row=3, column=7)
        
        Label(root, text="Operator ID", font='Arial 12 bold', fg='black').grid(row=3, column=8)
        op_id = Entry(root, font="Arial 12")
        op_id.grid(row=3, column=9)
        
        Label(root, text="Route ID", font='Arial 12 bold', fg='black').grid(row=3, column=10)
        r_id = Entry(root, font="Arial 12")
        r_id.grid(row=3, column=11)

        Button(root, text="Add Bus", font='Arial 12 bold', bg='green2', fg='black',command=bus_add).grid(row=5, column=4, pady=20,
                                                                                         columnspan=4)
        Button(root, text="Edit Bus", font='Arial 12 bold', bg='green2', fg='black').grid(row=5, column=5, pady=20,
                                                                                          columnspan=4)

        
        home = PhotoImage(file='home.png')
        Button(root, image=home,command=add_bus_to_home).grid(row=5, column=6, columnspan=3)
        
        root.mainloop()

    def add_route_page(self):

        root=Tk()
        root.title("ADD ROUTE PAGE")
        def add_route_to_home():
            root.destroy()
            self.home_page()
        def add_route():
            route_id=r_id.get()
            start_station=s_station.get()
            start_id=s_id.get()
            end_station=e_station.get()
            end_id=e_id.get()

            cur.execute('select r_id from route')
            res=cur.fetchall()
            if (route_id,) in res:
                showerror('ERROR',"Route id already exists")
            else:
                start_station=start_station.lower()
                end_station=end_station.lower()
                cur.execute('insert into route(r_id,s_name,s_id,e_name,e_id) values(?,?,?,?,?)',(route_id,start_station,start_id,end_station,end_id))
                con.commit()
                showinfo('success',"route added successfully!!")

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        bus = PhotoImage(file='Bus_for_project.png')
        Label(root, image=bus).grid(row=0, column=0, columnspan=12)
        Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=1,column=0,columnspan=12)
        Label(root, text="Add Bus Route Details", font='Arial 20 bold', bg='gainsboro', fg='green4').grid(row=2,column=0,pady=20,columnspan=12)

        Label(root, text="Route ID", font='Arial 12 bold', fg='black').grid(row=3, column=0, pady=50)
        r_id=Entry(root, font="Arial 12")
        r_id.grid(row=3, column=1, padx=50)

        Label(root, text="Staring station", font='Arial 12 bold', fg='black').grid(row=3, column=2)
        s_station=Entry(root, font="Arial 12")
        s_station.grid(row=3, column=3, padx=50)

        Label(root, text="Station ID", font='Arial 12 bold', fg='black').grid(row=3, column=4)
        s_id=Entry(root, font="Arial 12")
        s_id.grid(row=3, column=5, padx=50)

        Label(root, text="ending station", font='Arial 12 bold', fg='black').grid(row=4, column=2)
        e_station=Entry(root, font="Arial 12")
        e_station.grid(row=4, column=3, padx=50)

        Label(root, text="Station ID", font='Arial 12 bold', fg='black').grid(row=4, column=4)
        e_id=Entry(root, font="Arial 12")
        e_id.grid(row=4, column=5, padx=50)

        Button(root, text="Add Route", font='Arial 12 bold', bg='green2', fg='black',command=add_route).grid(row=3, column=7, pady=20,padx=10)
        Button(root, text="Delete Route", font='Arial 12 bold', bg='green2', fg='black').grid(row=3, column=9, pady=20,padx=10)

        home = PhotoImage(file='home.png')
        Button(root, image=home,command=add_route_to_home).grid(row=4, column=9)

        root.mainloop()

    def add_bus_running_page(self):
        root = Tk()
        root.title("ADD RUNNING PAGE")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        bus = PhotoImage(file='Bus_for_project.png')

        def add_bus_running_to_home():
            root.destroy()
            self.home_page()
        def add_run():
            bid=bus_id.get()
            run_date=running_date.get()
            s_avail=seat_avail.get()
            cur.execute('insert into running(b_id,run_date,seat_avail) values (?,?,?)',(bid,run_date,s_avail))
            con.commit()
            showinfo('sucess','run added successfully!!')

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
        bus_id=Entry(root)
        bus_id.grid(row=7,column=1)
        Label(root,text='Running Date',font='aerial 14').grid(row=7,column=2)
        running_date=Entry(root)
        running_date.grid(row=7,column=3)
        Label(root,text='Seat Available',font='aerial 14').grid(row=7,column=4)
        seat_avail=Entry(root)
        seat_avail.grid(row=7,column=5)
        Button(root, text="Add Run", font='Arial 12 bold', bg='green2', fg='black',command=add_run).grid(row=7,column=6)
        Button(root, text="Delete Run", font='Arial 12 bold', bg='green2', fg='black').grid(row=7,column=7,rowspan=2)

        home = PhotoImage(file='home.png')

        Button(root, image=home,command=add_bus_running_to_home).grid(row=10,column=4)

        root.mainloop()



obj=bus_booking()
obj.cover_page()
