#from configparser import LegacyInterpolation
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.font import BOLD, Font
from tkinter import messagebox 
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector.abstracts import TLS_VER_NO_SUPPORTED
from mysql.connector.errors import DatabaseError

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='Gym_management')
cursor=mydb.cursor()
root =Tk()
root.title("Gym Management")
root.geometry("1200x688+140+55")



def check(newwindow) :

   


    def clear_frame():
        for widgets in f3.winfo_children():
            widgets.destroy()


    

    def mem_plans():
        clear_frame()
        newwindow.update()
        l=Label(f3,text="Membership Plans",bg='Red',fg="white",width=15,height=3,font = "Arial 16 bold")
        l1=Label(f3,text="POPULAR\n Rs 300/month",bg='sky blue',fg="white",width=20,height=5,font = "Helvetica 13 bold")
        l2=Label(f3,text="GOLDEN\n Rs 700/month",bg='green',fg='white',width=20,height=5,font = "Helvetica 13 bold")
        l3=Label(f3,text="PROFESSIONAL\n Rs 1500/month",bg='orange',fg='white',width=20,height=5,font = "Helvetica 13 bold")
        l4=Label(f3,text="✓ Training Overview   \n ✓ Beginner Classes     \n X Personal Training    \n X Foundation Training ",bg="White",width=20,height=10,font = "Helvetica 13 bold")
        l5=Label(f3,text="✓ Training Overview   \n ✓ Beginner Classes     \n ✓ Personal Training    \n X Foundation Training ",bg="White",width=20,height=10,font = "Helvetica 13 bold")
        l6=Label(f3,text="✓ Training Overview   \n ✓ Beginner Classes     \n ✓ Personal Training    \n ✓ Foundation Training ",bg="White",width=20,height=10,font = "Helvetica 13 bold")
        l.place(x=400,y=25)
        l1.place(x=30,y=170)
        l2.place(x=400,y=170)
        l3.place(x=830,y=170)
        l4.place(x=30,y=270)
        l5.place(x=400,y=270)
        l6.place(x=830,y=270)


    def dashboard():
        clear_frame()
        cursor.execute("select * from members")
        data=cursor.fetchall()
        count1=cursor.rowcount
        
        cursor.execute("select * from trainer")
        data=cursor.fetchall()
        count2=cursor.rowcount

        cursor.execute("select fee from members")
        data=cursor.fetchall()
        fee=0
        for i in data:
            for j in i:
                fee+=j

        l0=Label(f3,text="Welcome",fg="Green",width=15,height=3,font = "Arial 20 bold")
        l1=Label(f3,text="👨",bg='white',fg="Green",width=6,height=3,font = "Arial 30 bold")
        l2=Label(f3,text=count1,bg='white',fg="Green",width=11,height=3,font = "Arial 17 bold")
        l3=Label(f3,text="Membership",bg='white',fg="Green",width=16,height=4,font = "Arial 12")
        l0.place(x=430)
        l1.place(x=75,y=70)
        l2.place(x=173,y=70)
        l3.place(x=183,y=136)

        l4=Label(f3,text="💰",bg='white',fg="Green",width=6,height=3,font = "Arial 30 bold")
        l5=Label(f3,text=fee,bg='white',fg="Green",width=11,height=3,font = "Arial 17 bold")
        l6=Label(f3,text="Monthly Revenue",bg='white',fg="Green",width=16,height=4,font = "Arial 12")
        l4.place(x=800,y=70)
        l5.place(x=898,y=70)
        l6.place(x=908,y=136)

        l7=Label(f3,text="👨",bg='white',fg="Green",width=6,height=3,font = "Arial 30 bold")
        l8=Label(f3,text=count2,bg='white',fg="Green",width=11,height=3,font = "Arial 17 bold")
        l9=Label(f3,text="Trainers",bg='white',fg="Green",width=16,height=4,font = "Arial 12")
        l7.place(x=75,y=280)
        l8.place(x=173,y=280)
        l9.place(x=183,y=346)

        cursor.execute("select salary from trainer")
        data=cursor.fetchall()
        salary=0
        for i in data:
            for j in i:
                salary+=j

        l10=Label(f3,text="💴",bg='white',fg="Green",width=6,height=3,font = "Arial 30 bold")
        l11=Label(f3,text=salary,bg='white',fg="Green",width=11,height=3,font = "Arial 17 bold")
        l12=Label(f3,text="Monthly Expenses",bg='white',fg="Green",width=16,height=4,font = "Arial 12")
        l10.place(x=800,y=280)
        l11.place(x=898,y=280)
        l12.place(x=908,y=346)

 #💴  👨   🗹
    

    def Traniners():
        clear_frame()
        cursor.execute("select * from Trainer")
        Data=cursor.fetchall()
        l1= Label(f3,height =1,width=20, text="Trainer's Details", font=("times new roman", 30 ,"bold"), fg="sky blue",pady=20)
        l1.pack(pady=55)
    
        style = ttk.Style()    # Create an object of Style widget
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(f3, column=("Id", "Name", "Experiene","Specialisation","Salary","Contact No"), show='headings', height=8)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Experiene")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Specialisation")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Salary")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text="Contact No")
        # Insert the data in Treeview widget
        for row in Data:
            tree.insert('', 'end', text="1", values=row)
    
        tree.pack(side=LEFT,fill='y',pady=11)
    
    def Members():
            clear_frame()
            cursor.execute("select * from members")
            Data=cursor.fetchall()
            l1= Label(f3,height =1,width=20, text="Member's Details", font=("times new roman", 30 ,"bold"), fg="sky blue",pady=20)
            l1.pack(pady=55)
            
            style = ttk.Style()    # Create an object of Style widget
            style.theme_use('clam')
        # Add a Treeview widget
            tree = ttk.Treeview(f3, column=( "Name","Member_id", "Mobile No","Fee","Address","Start Date","Expiry Date","Weight","Height","Age"), show='headings', height=8)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Name")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Member_id")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Mobile No")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Fee")
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="Address")
            tree.column("# 6", anchor=CENTER)
            tree.heading("# 6", text="Start Date")
            tree.column("# 7", anchor=CENTER)
            tree.heading("# 7", text="Expiry Date")
            tree.column("# 8", anchor=CENTER)
            tree.heading("# 8", text="Weight")
            tree.column("# 9", anchor=CENTER)
            tree.heading("# 9", text="Height")
            tree.column("# 10", anchor=CENTER)
            tree.heading("# 10", text="Age")
        # Insert the data in Treeview widget
            for row in Data:
                tree.insert('', 'end', text="1", values=row)
    
            tree.pack(side=LEFT,fill='y',pady=11)

    def workouts(): 

        def chest() :

            Label(f4,text="Chest press machine",fg="black",font= ("times new roman",18)).place(x=60,y=70)
            Label(f4,text="3 sets of 8 reps",fg="black",font= ("times new roman",12)).place(x=90,y=100)

            Label(f4,text="Barbell Press(Flat bench)",fg="black",font= ("times new roman",18)).place(x=60,y=130)
            Label(f4,text="3 sets of 8 reps",fg="black",font= ("times new roman",12)).place(x=90,y=160)

            Label(f4,text="Dumbell press(Flat bench)",fg="black",font= ("times new roman",18)).place(x=60,y=190)
            Label(f4,text="3 sets of 8 reps",fg="black",font= ("times new roman",12)).place(x=90,y=220)

            Label(f4,text="Barbell Press(Incline bench)",fg="black",font= ("times new roman",18)).place(x=60,y=250)
            Label(f4,text="4 sets of 12 reps",fg="black",font= ("times new roman",12)).place(x=90,y=280)

            Label(f4,text="Cross Cable Fly",fg="black",font= ("times new roman",18)).place(x=60,y=310)
            Label(f4,text="4 sets of 12 reps",fg="black",font= ("times new roman",12)).place(x=90,y=340)

            Label(f4,text="Peck Deck Fly",fg="black",font= ("times new roman",18)).place(x=60,y=370)
            Label(f4,text="4 sets of 12 reps",fg="black",font= ("times new roman",12)).place(x=90,y=400)

            Label(f4,text="Dumbell Press(Incline Bench)",fg="black",font= ("times new roman",18)).place(x=60,y=430)
            Label(f4,text="3 sets of 8 reps",fg="black",font= ("times new roman",12)).place(x=90,y=460)

            Label(f4,text="Flat Dumbell Fly",fg="black",font= ("times new roman",18)).place(x=470,y=70)
            Label(f4,text="4 sets of 10 reps",fg="black",font= ("times new roman",12)).place(x=490,y=100)

            Label(f4,text = "Incline dumbell Fly ",fg="black",font= ("times new roman",18)).place(x=470,y=130)
            Label(f4,text="4 sets of 10 reps",fg="black",font= ("times new roman",12)).place(x=490,y=160)

            Label(f4,text="Peck Deck fly",fg="black",font= ("times new roman",18)).place(x=470,y=190)
            Label(f4,text="6 sets of 12 reps",fg="black",font= ("times new roman",12)).place(x=490,y=220)

            Label(f4,text="Flat Dumbell press)",fg="black",font= ("times new roman",18)).place(x=470,y=250)
            Label(f4,text="4 sets of 10 reps",fg="black",font= ("times new roman",12)).place(x=490,y=280)

            Label(f4,text="Incline Dumbell press",fg="black",font= ("times new roman",18)).place(x=470,y=310)
            Label(f4,text="4 sets of 10 reps",fg="black",font= ("times new roman",12)).place(x=490,y=340)

            Label(f4,text="Dumbell PullOvers",fg="black",font= ("times new roman",18)).place(x=470,y=370)
            Label(f4,text="4 sets of 12 reps",fg="black",font= ("times new roman",12)).place(x=490,y=400)



            return


        newwindow1 = Toplevel(newwindow)
        newwindow1.geometry("1200x688+140+55")
        newwindow1.title("Gym Management")
        
             
        f2 = Frame(newwindow1, borderwidth=6, bg="indigo", relief=RIDGE)
        f2.pack(side=TOP, fill="x")
        f3 = Frame(newwindow1,  bg="indigo", relief=RIDGE,height=30)
        f3.pack(side=BOTTOM, fill="x")
        l = Label(f2,height =1,width=20, text="Gym Management", font=("times new roman", 30 ,"bold"), fg="dark violet",pady=12)
        l.pack(pady=10)
        f4 = Frame(newwindow1,borderwidth=6,relief=RIDGE,height=500,width=750)
        f4.pack(side=RIGHT,padx=80,anchor="n",pady=20)
        f5 = Frame(f4,relief=RIDGE,height=495,width=8,bg="dark violet")
        f5.place(x=375,y=-2)


        Label(f4,text="Beginner",fg="dark violet",font=("times new roman",25,"bold","underline")).place(x=110,y=10)
        Label(f4,text="Intermediate",fg="dark violet",font=("times new roman",25,"bold","underline")).place(x=475,y=10)


        Button(newwindow1,fg="black", bg = "violet",text="Chest Workout",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=11,command=chest).place(x=80,y=155)
        Button(newwindow1,fg="black", bg = "violet",text="Back workout",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=11,command=chest).place(x=80,y=235)
        Button(newwindow1,fg="black", bg = "violet",text="Bicep ans Triceps",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=12,command=chest).place(x=80,y=315)
        Button(newwindow1,fg="black", bg = "violet",text="Shoulder Workout",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=12,command=chest).place(x=80,y=395)
        Button(newwindow1,fg="black", bg = "violet",text="Leg Workout",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=11,command=chest).place(x=80,y=475)
        Button(newwindow1,fg="black", bg = "violet",text="Exit",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=11,command=chest).place(x=80,y=555)
        
        
        
        
        


    def add_member() :



        def update() :

            memberdelete = membervar.get()
            memberdeletet = (memberdelete,)
            cursor.execute("Select member_id from members where member_id =%s",memberdeletet)
            result = cursor.fetchall()
            if result == [] :

                popup = Toplevel(newwindow1)
                popup.geometry("300x125+600+300")
                popup.title("warning")
                popup.configure(bg="white")
                def exit1() :
                    popup.destroy()

                Label(popup,text="Enter a valid memberID",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
                Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)

                return

            if namevar.get() =="" or membervar.get() =="" or mobnovar.get() =="" or mailvar.get() == 0 or addressvar.get() == "" or datevar.get() == "" or EndDatevar.get() == "" or weightvar.get() == "" or heightvar.get() == "" or Agevar.get() == ""   :

                popup1()
                
                return


            s1 = "update members set name = %s , member_id = %s, mob_no = %s,fees = %s,address = %s,start_date = %s,end_date = %s,weight = %s,height = %s,age = %s where member_id = %s"
            s2 = (namevar.get(),membervar.get(),mobnovar.get(),mailvar.get(),addressvar.get(),datevar.get(),EndDatevar.get(),weightvar.get(),heightvar.get(),Agevar.get(),membervar.get())
            cursor.execute(s1,s2)
            mydb.commit()
            reset()

            popup = Toplevel(newwindow1)
            popup.geometry("300x125+600+300")
            popup.title("Done")
            popup.configure(bg="white")
            def exit1() :
                popup.destroy()

            Label(popup,text="Member Upadted Successfully",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
            Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)






        def delete() :

            memberdelete = membervar.get()
            memberdeletet = (memberdelete,)
            cursor.execute("Select member_id from members where member_id =%s",memberdeletet)
            result = cursor.fetchall()
            if result == [] :

                popup = Toplevel(newwindow1)
                popup.geometry("300x125+600+300")
                popup.title("warning")
                popup.configure(bg="white")
                def exit1() :
                    popup.destroy()

                Label(popup,text="Enter a valid memberID",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
                Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)

                return
            deletes = "DELETE FROM members WHERE member_id = %s"
            

            cursor.execute(deletes,memberdeletet)  
            mydb.commit()
            popup = Toplevel(newwindow1)
            popup.geometry("300x125+600+300")
            popup.title("Done")
            popup.configure(bg="white")
            def exit1() :
                popup.destroy()

            Label(popup,text="Member Deleted Successfully",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
            Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)

            

                
            

        def popup1() :

            popup = Toplevel(newwindow1)
            popup.geometry("250x125+600+300")
            popup.title("warning")
            popup.configure(bg="white")
            def exit1() :
                popup.destroy()

            Label(popup,text="All fields are required",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
            Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)




        def reset() :
            namevar.set("")
            membervar.set("")
            mobnovar.set("")
            mailvar.set(0)
            addressvar.set("")
            datevar.set("")
            EndDatevar.set("")
            weightvar.set("")
            heightvar.set("")
            Agevar.set("")

        def addMember() :

            if namevar.get() =="" or membervar.get() =="" or mobnovar.get() =="" or mailvar.get() == 0 or addressvar.get() == "" or datevar.get() == "" or EndDatevar.get() == "" or weightvar.get() == "" or heightvar.get() == "" or Agevar.get() == ""   :

                popup1()
                
                return

            memberdelete = membervar.get()
            memberdeletet = (memberdelete,)
            cursor.execute("Select member_id from members where member_id =%s",memberdeletet)
            result = cursor.fetchall()

            if(result != []) :
                
                popup = Toplevel(newwindow1)
                popup.geometry("250x125+600+300")
                popup.title("warning")
                popup.configure(bg="white")
                def exit1() :
                    popup.destroy()

                Label(popup,text="MemberId already exist",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
                Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)

                return

            sc = "INSERT INTO members(name,member_id,mob_no,fees,address,start_date,end_date,weight,height,age)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            tup_addMember = (namevar.get(),membervar.get(),mobnovar.get(),mailvar.get(),addressvar.get(),datevar.get(),EndDatevar.get(),weightvar.get(),heightvar.get(),Agevar.get())
            cursor.execute(sc,tup_addMember)
            mydb.commit()
            #reset()

            popup = Toplevel(newwindow1)
            popup.geometry("300x125+600+300")
            popup.title("DONE")
            popup.configure(bg="white")
            def exit1() :
                popup.destroy()

            Label(popup,text="Member Added Successfully",bg="white",font=("times new roman",15,"bold")).pack(side=TOP,pady=20,padx=10)
            Button(popup,text="OK",font=("times new roman",10,"bold"),pady=10,command=exit1).pack(side=TOP)



        newwindow1 = Toplevel(newwindow)
        newwindow1.geometry("1200x688+140+55")
        newwindow1.title("Gym Management")
        
             
        f2 = Frame(newwindow1, borderwidth=6, bg="indigo", relief=RIDGE)
        f2.pack(side=TOP, fill="x")
        f3 = Frame(newwindow1,  bg="indigo", relief=RIDGE,height=30)
        f3.pack(side=BOTTOM, fill="x")
        l = Label(f2,height =1,width=20, text="Gym Management", font=("times new roman", 30 ,"bold"), fg="dark violet",pady=12)
        l.pack(pady=10)
        f4 = Frame(newwindow1,borderwidth=6,relief=RIDGE,height=500,width=950)
        f4.pack(side=LEFT,padx=30)
        f5 = Frame(f4,relief=RIDGE,height=495,width=8,bg="dark violet")
        f5.place(x=475,y=-2)
        name = Label(f4, text="Name",fg="dark violet",font = ("times new roman" ,25, "bold"))
        memberId = Label(f4, text="Member Id",fg="dark violet",font = ("times new roman" ,20, "bold"))
        mobno = Label(f4, text="MobileNo",fg="dark violet",font = ("times new roman" ,20, "bold"))
        mail = Label(f4, text="Fees",fg="dark violet",font = ("times new roman" ,20, "bold"))
        address = Label(f4, text="Address",fg="dark violet",font = ("times new roman" ,20, "bold"))
        date = Label(f4,text="Start Date",fg="dark violet",font = ("times new roman" ,20, "bold"))
        Height = Label(f4,text="Height",fg="dark violet",font = ("times new roman" ,20, "bold"))
        weight = Label(f4,text="Weight",fg="dark violet",font = ("times new roman" ,20, "bold"))
        EndDate = Label(f4,text="Expiry Date",fg="dark violet",font = ("times new roman" ,20, "bold"))
        age = Label(f4,text="Age",fg="dark violet",font = ("times new roman" ,20, "bold"))
        name.place(x=50,y=50)
        memberId.place(x=50,y=140)
        mobno.place(x= 50,y=230)
        mail.place(x=50,y=320)
        address.place(x=50,y=410)
        date.place(x=525,y=50)
        EndDate.place(x=525,y=140)
        weight.place(x=525,y=230)
        Height.place(x=525,y=320)
        age.place(x=525,y=410)
        
        
        namevar = StringVar()
        membervar = StringVar()
        mobnovar = StringVar()
        mailvar = IntVar()
        addressvar = StringVar()
        datevar = StringVar()
        EndDatevar = StringVar()
        heightvar = StringVar()
        weightvar = StringVar()
        Agevar = StringVar()
        
        nameentry = Entry(f4,textvariable=namevar,font=("times new roman",15),borderwidth=2)
        memberentry = Entry(f4,textvariable=membervar,font=("times new roman",15),borderwidth=2)
        mobnoentery  = Entry(f4,textvariable=mobnovar,font=("times new roman",15),borderwidth=2)
        mailentry = Entry(f4,textvariable=mailvar,font=("times new roman",15),borderwidth=2)
        addressentry = Entry(f4,textvariable=addressvar,font=("times new roman",15),borderwidth=2)
        dateentry = Entry(f4,textvariable=datevar,font=("times new roman",15),borderwidth=2)
        EndDateentry = Entry(f4,textvariable=EndDatevar,font=("times new roman",15),borderwidth=2)
        Heightentry = Entry(f4,textvariable=heightvar,font=("times new roman",15),borderwidth=2)
        weightentry = Entry(f4,textvariable=weightvar,font=("times new roman",15),borderwidth=2)
        ageentry = Entry(f4,textvariable=Agevar,font=("times new roman",15),borderwidth=2)
        
        
        
        nameentry.place(x=210, y=60)
        memberentry.place(x=210,y=150)
        mobnoentery.place(x=210,y=240)
        mailentry.place(x=210,y=330)
        addressentry.place(x=210,y=420)
        dateentry.place(x = 700,y=60)
        EndDateentry.place(x=700,y=150)
        Heightentry.place(x=700,y=240)
        weightentry.place(x = 700,y=330)
        ageentry.place(x=700,y=420)
        
        def exit1() :
            newwindow1.destroy()
        
        Button(newwindow1,fg="black", bg = "violet",text="Add Member",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=10,command=addMember).place(x=1025,y=150)
        Button(newwindow1,fg="black", bg = "violet",text="Delete",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=10,command=delete).place(x=1025,y=250)
        Button(newwindow1,fg="black", bg = "violet",text="Update",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=10,command=update).place(x=1025,y=350)
        Button(newwindow1,fg="black", bg = "violet",text="Reset",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=10,command=reset).place(x=1025,y=450)
        Button(newwindow1,fg="black", bg = "violet",text ="Exit",font=("times new roman",13,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=10,command= exit1).place(x=1025,y=550)



        

    newwindow.geometry("1200x688+140+55")
    newwindow.title("Gym Management")
    f2 = Frame(newwindow, borderwidth=6, bg="indigo", relief=RIDGE)
    f2.pack(side=TOP, fill="x")
    f1 = Frame(newwindow, bg="indigo", borderwidth=4, relief=RIDGE,width=9)
    f1.pack(side=LEFT, fill="y")
    l = Label(f2,height =1,width=20, text="Gym Management", font=("times new roman", 30 ,"bold"), fg="dark violet",pady=12)
    l.pack(pady=10)
    home = Button(f1,fg="dark violet", bg = "white",text="Home",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command=dashboard)
    home.pack(pady = 30,padx=5)

    f3 = Frame(newwindow,height=1000,relief = RIDGE)
    f3.pack(side = TOP,padx=15,fill="x")
    
    add_member = Button(f1, fg="dark violet", bg = "white",text="Add Member",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command = add_member)
    add_member.pack(padx=5)

    members = Button(f1, fg="dark violet", bg = "white",text="Members",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command=Members)
    members.pack(pady=30,padx=5)

    trainer = Button(f1, fg="dark violet", bg = "white",text="Trainer",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command=Traniners)
    trainer.pack(padx=5)

    workouts = Button(f1, fg="dark violet", bg = "white",text="Workouts",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command=workouts)
    workouts.pack(pady = 30,padx= 5)

    stock = Button(f1, fg="dark violet", bg = "white",text="Protein Stock",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8)
    stock.pack(padx=5)

    plans = Button(f1, fg="dark violet", bg = "white",text="Plans",font=("times new roman",12,"bold"),pady=5,padx=10,borderwidth=4,border=5,width=8,command = mem_plans)
    plans.pack(padx=5,pady=30)


def validiate():
    user_name=e1.get()
    passwd=e2.get()
    cursor.execute("select * from Login")
    data=cursor.fetchall()
    temp=False
    for i in data:
        if i[0]==user_name and i[1]==passwd:
            temp=TRUE
        else:
            continue
    if temp!=TRUE:
        newwindow=Toplevel(root)
        check(newwindow)
    else:
        messagebox.showinfo('Waring','Wrong Credintials')



f1=Frame(root,height=700,width=600,bg='white')
f1.propagate(0)
img=ImageTk.PhotoImage(Image.open('E:\Gym management\gym1.jpg'))
img_label=Label(f1,image=img)
img_label.pack(side=LEFT)
f1.pack(side=LEFT)
f = Frame(root,height=700,width=790,bg="white")
f.propagate(0)
f.pack(side=RIGHT,fill=Y)

l1=Label(f,text="Login",bg='white',fg="sky blue",font = "Arial 50 bold")
l2= Label(f,text="Welcome to the GYM MANAGEMENT Application by  and n\n\n",bg='white',font = "Arial 10")
l3= Label(f,text="Username",bg='white',font = "Helvetica 15 ")
Label(f,text="*",bg="white",fg ="red",font = "Helvetica 15 ").place(x= 345,y=215)
Label(f,text="*",bg="white",fg ="red",font = "Helvetica 15 ").place(x= 345,y=300)
l4= Label(f,text="Password",bg='white',font = "Helvetica 15 ")

e1=Entry(f,width=25,bg="white",fg="Black",font=("Arial",14))
        
e2=Entry(f,width=25,bg="White",fg="black",show="*",font=("Arial",14))
        
l1.pack(padx=0,pady=25)
l2.pack()
l3.pack(padx=0,pady=10)
e1.pack(padx=0,pady=5)
l4.pack(padx=0,pady=10)
e2.pack(padx=0,pady=5)

login_btn=ImageTk.PhotoImage(Image.open('E:\Gym management\Loginbutton.png'))
b1=Button(f,image=login_btn,borderwidth=0,bg='white',command= lambda:validiate()).pack(pady=50)


root.mainloop()
