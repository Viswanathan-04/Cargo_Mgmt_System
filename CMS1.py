#For executing and storing the data ,Please make sure that MYSQL installed in your device
#using pip install mysql-connector in the command prompt [command - pip install mysql-connector]

#Importing Libraries to be used
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
import time

#Connecting to the database
connection = sql.connect(host='localhost',database='cms',user='root',password='Admin@123')
cursor = connection.cursor()

#Creating required database and tables
'''sql1="create table if not exists login(Username varchar(50),Password varchar(50),Login_Time varchar(50))"
cursor.execute(sql1)'''
sql2="create table if not exists import (Billing_ID int primary key,Carrier_Name varchar(50),Origin varchar(50),Destination varchar(50),Container_Dimensions varchar(50),Mode_of_Transport varchar(50),Payment_Amount int)"
cursor.execute(sql2)
sql3="create table if not exists export (Billing_ID int primary key,Carrier_Name varchar(50),Origin varchar(50),Destination varchar(50),Container_Dimensions varchar(50),Mode_of_Transport varchar(50),Payment_Amount int)"
cursor.execute(sql3)
sql4="create table if not exists employee(Employee_ID int primary key,Employee_FName varchar(50),Employee_LName varchar(50),Date_of_Birth date,Designation varchar(50),Employee_PhNo bigint)"
cursor.execute(sql4)


#Registering New user
def register():
    window.destroy()
    time.sleep(1)
    a=Tk()
    def submit():
        username=name.get()
        password=passw.get()
        np=key.get()
        cn=na.get()
        if name.get()=="":
            messagebox.showerror(parent=a,title="ERROR",message="Please Enter your name")
        elif passw.get()=="":
            messagebox.showerror(parent=a,title="ERROR",message="Please Enter your password")
        elif key.get()=="":
            messagebox.showerror(parent=a,title="ERROR",message="Please Enter your pin number")
        elif key.get()=="":
            messagebox.showerror(parent=a,title="ERROR",message="Please Enter your Company Name")
        elif key.get().isdigit()==False:
            messagebox.showerror(parent=a,title="ERROR",message="Please Enter a Pin Number.\nYou have Entered an alphabet")
        elif passw.get()!=conpas.get():
            messagebox.showerror(parent=a,title="ERROR",message="Password's aren't same Please Check")
            passw.delete(0,'end')
            conpas.delete(0,'end')
        elif passw.get()==conpas.get() and key.get().isdigit():
            b=open("up.txt","w")
            b.write(username+"\n")
            b.write(password+"\n")
            b.write(np+"\n")
            b.write(cn)
            b.close()
            name.delete(0,'end')
            passw.delete(0,'end')
            conpas.delete(0,'end')
            key.delete(0,'end')
            na.delete(0,'end')
            messagebox.showinfo(parent=a,title="SUCCESS",message="New User Registered successfully")
            messagebox.showinfo(parent=a,title="Information",message="Please Relaunch your Application to save the details")
            a.destroy()
        else:
            return
            
    global username
    global password
    global name
    global passw

    def info():
        messagebox.showinfo(parent=a,title="Information",message="Please enter a pin number . This is asked in order to fetch the password if you forget")
    
    rl=Label(a,text='Register Yourself Here',font='Calibri 18',fg='lemon chiffon',bg='brown')
    rl.place(x=100,y=20)
    name_label = Label(a, text = 'Username : ',font='14',bg='lemon chiffon') 
    name_label.place(x=20,y=85)
    name = Entry(a,text = "",font='14',width=14,justify=LEFT) 
    name.place(x=210,y=85)
    passw_label = Label(a,text = 'Password : ',font='14',bg='lemon chiffon') 
    passw_label.place(x=20,y=125)
    passw=Entry(a,text = "",show = '*',font='14',width=14,justify=LEFT)
    passw.place(x=210,y=125)
    conpas_label=Label(a,text = 'Confirm Password : ',font='14',bg='lemon chiffon') 
    conpas_label.place(x=20,y=165)
    conpas=Entry(a,text = "",show = '*',font='14',width=14,justify=LEFT)
    conpas.place(x=210,y=165)
    key_label = Label(a, text = 'Set a Pin Number : ',font='14',bg='lemon chiffon') 
    key_label.place(x=20,y=205)
    key = Entry(a,text = "",font='14',show = '*',width=14,justify=LEFT) 
    key.place(x=210,y=205)
    na_label = Label(a, text = 'Company Name : ',font='14',bg='lemon chiffon') 
    na_label.place(x=20,y=245)
    na = Entry(a,text = "",font='14',width=14,justify=LEFT) 
    na.place(x=210,y=245)

    def sp():
        if cd.get()==1:
            passw.config(show="")
            conpas.config(show="")
            key.config(show="")
        elif cd.get()==0:
            passw.config(show="*")
            conpas.config(show="*")
            key.config(show="*")
    cd=IntVar()
    sp_btn=Checkbutton(a,text='Show Password & Pin',command=sp,onvalue=1,offvalue=0,variable=cd,width=16,font='Arial 10',bg='brown')
    sp_btn.place(x=25,y=290)

    c=Button(a,text=" ? ",command=info,font='Calibri 12',bg='lemon chiffon',bd=1)
    c.place(x=373,y=204)
    login_btn=Button(a,text = 'Register',command=submit,bg='lemon chiffon',bd=1)
    a.bind('<Return>', lambda i : submit())
    login_btn.place(x=280,y=290)
    a.title("Register Yourself Here")
    a.geometry("400x330+400+200")
    a.resizable(0,0)
    a.config(bg="brown")
    a.mainloop()
    
#++++++++++++++++++++++++PROJECT BEGINS HERE++++++++++++++++++++++++#
#Loading screen
load=Tk()
progress = ttk.Progressbar(load, orient = HORIZONTAL,length = 300)
l=Label(load,text="Loading...",font=' Arial 20 italic',bg='black',fg='gold')
l.place(x=165,y=120)
rt=Label(load,text=time.strftime("%d/%m/%Y"),font='10',bg='black',fg='turquoise')
rt.place(x=10,y=15)
q=Label(load,text="Cargo Management\nSystem",font=' Arial 16 italic',bg='black',fg='deepskyblue3',justify='right')
q.place(x=240,y=15)
qe=Label(load,text="Version 1.1®",font=' Arial 12 italic',bg='black',fg='red',justify='right')
qe.place(x=10,y=260)


progress.config(mode='determinate',maximum=100, value = 0)
progress.start(63)
progress.after(6800, lambda:progress.stop())
progress.place(x=80,y=180)

a1="Loading...."
a2="Loading....."
a3="Loading......"
a4="Loading......."
b="Opening Application...."
load.after(3000, lambda:l.config())
load.after(2000, lambda:l.config(text=a1))
load.after(3000, lambda:l.config(text=a2))
load.after(4000, lambda:l.config(text=a3))
load.after(5000, lambda:l.config(text=a4))
load.after(6000, lambda:l.place(x=80,y=120))
load.after(6000, lambda:l.config(text=b))

load.after(6800, lambda:load.destroy())
load.geometry('450x300+525+225')
load.config(bg="black")
load.overrideredirect(True)
load.mainloop()

time.sleep(0.5)

#Creating main window
window=Tk()
#Assigning username and password with string variables
name_var=StringVar() 
passw_var=StringVar()
#Retriving Username and Password
name=name_var.get() 
password=passw_var.get()
#Opening and reading login credentials from text file 
with open("up.txt", "r") as fd:
    i = fd.read().splitlines()
    if len(i)!=0:
        name=i[0]
        password=i[1]
        np=i[2]
        cn=i[3]

#Defining Login Button's command
def login():
    '''un=name_entry.get()
    pw=passw_entry.get()
    tm=time.strftime("%H:%M:%S")
    sql23="insert into login values(%s,%s,%s)"
    vl=un,pw,tm
    cursor.execute(sql23,vl)
    connection.commit()'''
    #Verifying Username and Password 
    if (name_entry.get()==i[0]) and (passw_entry.get()==i[1]):
        name_entry.delete(0,'end')
        passw_entry.delete(0,'end')
        messagebox.showinfo(parent=window,title="SUCCESS",message=("User Login successful.\n\nWelcome back "+i[0]))
        #Destroying Main window
        window.destroy()
        win=Tk()
        #Editing table Import
        def imp():
            a=Tk()
            #Inserting into Import
            def insert():
                b=Tk()
                def submit():
                    if (e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()==""):
                        messagebox.showerror(parent=b,title="ERROR",message="Please Enter all the details")
                    else:
                        try:
                            sql="insert into import values (%s,%s,%s,%s,%s,%s,%s)"
                            values=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get()
                            cursor.execute(sql,values)
                            connection.commit()
                            e1.delete(0,'end')
                            e2.delete(0,'end')
                            e3.delete(0,'end')
                            e4.delete(0,'end')
                            e5.delete(0,'end')
                            e6["state"]='normal'
                            e6.delete(0,'end')
                            e6["state"]='readonly'
                            e7.delete(0,'end')
                            messagebox.showinfo(parent=b,title="SUCCESS",message="Details inserted successfully")
                            b.destroy()
                        except:
                            messagebox.showerror(parent=b,title="ERROR",message="Couldn't insert the values")
                    
                l1=Label(b,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(b,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(b,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(b,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(b,text="Container Dimensions : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(b,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(b,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                
                e1=Entry(b,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                sql="select max(Billing_ID) from import"
                cursor.execute(sql)
                a=cursor.fetchall()
                if a[0][0]==None:
                    c=1000
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                else:
                    c=a[0][0]+1
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                e2=Entry(b,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(b,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(b,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(b,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=ttk.Combobox(b,font='Arial 14',width=12,state="readonly")
                e6['values']=("Seaways","Airways","Roadways")
                e6.place(x=370,y=430)
                e7=Entry(b,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                
                l = Label(b, text = 'INSERT IMPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                add_btn=Button(b,text = 'INSERT',command=submit,bg='gold',bd=1,height=2,width=10)
                b.bind('<Return>', lambda i : submit())
                add_btn.place(x=550,y=490)
                b.title("INSERT IMPORT DETAILS")
                b.geometry("650x550+350+150")
                b.resizable(0,0)
                b.config(bg='brown')
                b.mainloop()

            #Updating Import
            def update():
                messagebox.showinfo(parent=a,title="INFORMATION",message="Enter Billing ID to fetch and update the details")
                c=Tk()
                def reset():
                    e1["state"]='normal'
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6["state"]='normal'
                    e6.delete(0,'end')
                    e6["state"]='readonly'
                    e7.delete(0,'end')
                    
                def fetch():
                    sql="select * from import where Billing_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e1["state"]='readonly'
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6["state"]='normal'
                            e6.insert('end',row[5])
                            e6["state"]='readonly'
                            e7.insert('end',row[6])
                    else:
                        messagebox.showerror(parent=c,title="Error",message="No details found with Billing ID you entered")
                        
                def submit():
                    try:
                        sql='update import set Carrier_Name="%s",Origin="%s",Destination="%s",Container_Dimensions="%s",Mode_of_Transport="%s",Payment_Amount="%s" where Billing_ID="%s"'%(e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e1.get())
                        cursor.execute(sql)
                        e1["state"]='normal'
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6["state"]='normal'
                        e6.delete(0,'end')
                        e6["state"]='readonly'
                        e7.delete(0,'end')
                        messagebox.showinfo(parent=c,title="SUCCESS",message="Details updated successfully")
                        connection.commit()
                    except:
                        messagebox.showerror(parent=c,title="ERROR",message="Couldn't Update the details")
                    c.destroy()
                    
                    
                l1=Label(c,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(c,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(c,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(c,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(c,text="Container Dimensions : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(c,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(c,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                e1=Entry(c,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                e2=Entry(c,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(c,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(c,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(c,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=ttk.Combobox(c,font='Arial 14',width=12,state="readonly")
                e6['values']=("Seaways","Airways","Roadways")
                e6.place(x=370,y=430)
                e7=Entry(c,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                
                fet_btn=Button(c,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=440)
                upd_btn=Button(c,text = 'UPDATE',command=submit,bg='gold',bd=1,height=2,width=10) 
                upd_btn.place(x=550,y=490)
                res=Button(c,text = 'RESET',command=reset,bg='gold',bd=1,height=2,width=10)
                res.place(x=550,y=390)
                
                l = Label(c, text = 'UPDATE IMPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                
                c.title("UPDATE IMPORT DETAILS")
                c.geometry("650x550+350+150")
                c.resizable(0,0)
                c.config(bg='brown')
                c.mainloop()

            #Fetching from Import
            def fetch():
                d=Tk()
                def fetchmany():
                    sql="select * from import where %s='%s' order by %s asc"%(c1.get(),e8.get(),c1.get())
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    if len(row)!=0:
                        tv.delete(*tv.get_children())
                        for i in row:
                            e8.delete(0,'end')
                            tv.insert('','end',values=i)
                        connection.commit()
                    elif e8.get()=="":
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="Please Enter Billing ID")
                    else:
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="No details found with "+c1.get()+" you entered")
                        
                def fetchall():
                    tv.delete(*tv.get_children())
                    sql='select * from import order by Billing_ID asc'
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    for i in row:
                        e8.delete(0,'end')
                        tv.insert('','end',values=i)
                    connection.commit()
                
                tv=ttk.Treeview(d,columns=("Billing ID","Carrier Name","Origin","Destination","Container Dimensions","Mode of Transport","Payment Amount"),height=24,selectmode='browse')
                tv.place(x=20,y=70)
                tv.heading("Billing ID",text="Billing ID")
                tv.heading("Carrier Name",text="Carrier Name")
                tv.heading("Origin",text="Origin")
                tv.heading("Destination",text="Destination")
                tv.heading("Container Dimensions",text="Container Dimensions")
                tv.heading("Mode of Transport",text="Mode of Transport")
                tv.heading("Payment Amount",text="Payment Amount")
                tv['show']='headings'
                tv.column("Billing ID",width=120)
                tv.column("Carrier Name",width=140)
                tv.column("Origin",width=120)
                tv.column("Destination",width=120)
                tv.column("Container Dimensions",width=120)
                tv.column("Mode of Transport",width=120)
                tv.column("Payment Amount",width=120)

                l1=Label(d,text="Search by : ",font=["Lucida Calligraphy","14"],bg='gold')
                l1.place(x=10,y=15)
                c1=ttk.Combobox(d,font='Arial 14',width=12,state="readonly")
                c1['values']=("Billing_ID","Carrier_Name","Origin","Destination","Container_Dimensions","Mode_of_Transport","Payment_Amount")
                c1.place(x=150,y=15)
                s=ttk.Scrollbar(d,orient="vertical",command=tv.yview)
                tv.configure(yscroll=s.set)
                s.pack(side=RIGHT,fill=Y)

                e8=Entry(d,text="",font='Arial 14',width=14)
                e8.place(x=320,y=17)
                fetchall()
                fet_btn=Button(d,text = 'FETCH',command=fetchmany,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=505,y=10)
                if e8.get()!=None:
                    d.bind('<Return>', lambda i : fetchmany())
                    
                fa=Button(d,text="FETCH ALL",command=fetchall,bg='gold',bd=1,height=2,width=10)
                fa.place(x=600,y=10)
                d.title("FETCH IMPORT DETAILS")
                d.geometry("920x600+200+100")
                d.resizable(0,0)
                d.config(bg='brown')
                d.mainloop()

            #Deleting from Import
            def delete():
                e=Tk()
                def reset():
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6["state"]='normal'
                    e6.delete(0,'end')
                    e6["state"]='readonly'
                    e7.delete(0,'end')
                    
                def fetch():
                    sql="select * from import where Billing_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6["state"]='normal'
                            e6.insert('end',row[5])
                            e6["state"]='readonly'
                            e7.insert('end',row[6])
                    else:
                        messagebox.showerror(parent=e,title="Error",message="No details found with Billing ID you entered")
                        
                def submit():
                    dele=messagebox.askyesno(parent=e,title="DELETE RECORD CONFIRMATION",message="Would you like to delete the selected Details?")
                    if dele>0:
                        sql='delete from import where Billing_ID="%s"'%(e1.get())
                        cursor.execute(sql)
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6["state"]='normal'
                        e6.delete(0,'end')
                        e6["state"]='readonly'
                        e7.delete(0,'end')
                        messagebox.showinfo(parent=e,title="SUCCESS",message="Details Deleted successfully")
                        connection.commit()
                    else:
                        return
                    e.destroy()
                    
                l1=Label(e,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(e,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(e,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(e,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(e,text="Container Dimensions : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(e,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(e,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                
                e1=Entry(e,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                e2=Entry(e,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(e,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(e,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(e,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=Entry(e,text="",font='Arial 14',width=14)
                e6.place(x=370,y=430)
                e7=Entry(e,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                
                l = Label(e, text = 'DELETE IMPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                fet_btn=Button(e,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=440)
                add_btn=Button(e,text = 'DELETE',command=submit,bg='gold',bd=1,height=2,width=10) 
                add_btn.place(x=550,y=490)

                e.title("DELETE IMPORT DETAILS")
                e.geometry("650x550+350+150")
                e.resizable(0,0)
                e.config(bg='brown')
                e.mainloop()

            def ret():
                a.destroy()
             
            l = Label(a, text = 'EDIT IMPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='lemon chiffon') 
            l.place(x=150,y=50)
            ins=Button(a,text = 'Insert Import Details',command=insert,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=10,y=250)
            upd=Button(a,text = 'Fetch Import Details',command=fetch,bg='lemon chiffon',bd=1,height=4,width=20) 
            upd.place(x=170,y=250)
            de=Button(a,text = 'Update Import Details',command=update,bg='lemon chiffon',bd=1,height=4,width=20) 
            de.place(x=330,y=250)
            ins=Button(a,text = 'Delete Import Details',command=delete,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=490,y=250)
            r=Button(a,text="Return to Main Window",command=ret,bg='brown',fg='lemon chiffon',bd=0,height=1)
            r.place(x=500,y=10)
            a.title("IMPORT TABLE EDIT PAGE")
            a.geometry("650x550+350+150")
            a.resizable(0,0)
            a.config(bg='brown')
            a.mainloop()

        #Editing table Export
        def exp():
            a=Tk()
            #Inserting into Export
            def insert():
                b=Tk()
                def submit():
                    if (e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()==""):
                        messagebox.showerror(parent=b,title="ERROR",message="Please Enter all the details")
                    else:
                        try:
                            sql="insert into export values (%s,%s,%s,%s,%s,%s,%s) "
                            values=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get()
                            cursor.execute(sql,values)
                            connection.commit()
                            e1.delete(0,'end')
                            e2.delete(0,'end')
                            e3.delete(0,'end')
                            e4.delete(0,'end')
                            e5.delete(0,'end')
                            e6["state"]='normal'
                            e6.delete(0,'end')
                            e6["state"]='readonly'
                            e7.delete(0,'end')
                            messagebox.showinfo(parent=b,title="SUCCESS",message="Details inserted successfully")
                            b.destroy()
                        except:
                            messagebox.showerror(parent=b,title="ERROR",message="Couldn't Enter the details")
                    
                l1=Label(b,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(b,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(b,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(b,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(b,text="Container Dimensions : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(b,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(b,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                
                e1=Entry(b,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                sql="select max(Billing_ID) from export"
                cursor.execute(sql)
                a=cursor.fetchall()
                if a[0][0]==None:
                    c=1000
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                else:
                    c=a[0][0]+1
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                e2=Entry(b,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(b,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(b,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(b,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=ttk.Combobox(b,font='Arial 14',width=12,state="readonly")
                e6['values']=("Seaways","Airways","Roadways")
                e6.place(x=370,y=430)
                e7=Entry(b,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                
                l = Label(b, text = 'INSERT EXPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                add_btn=Button(b,text = 'INSERT',command=submit,bg='gold',bd=1,height=2,width=10)
                b.bind('<Return>', lambda i : submit())
                add_btn.place(x=550,y=490)

                b.title("INSERT EXPORT DETAILS")
                b.geometry("650x550+350+150")
                b.resizable(0,0)
                b.config(bg='brown')
                b.mainloop()

            #Updating Export
            def update():
                messagebox.showinfo(parent=a,title="INFORMATION",message="Enter Billing ID to fetch and update the details")
                c=Tk()
                def reset():
                    e1["state"]='normal'
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6["state"]='normal'
                    e6.delete(0,'end')
                    e6["state"]='readonly'
                    e7.delete(0,'end')
                    
                def fetch():
                    sql="select * from export where Billing_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e1["state"]='readonly'
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6["state"]='normal'
                            e6.insert('end',row[5])
                            e6["state"]='readonly'
                            e7.insert('end',row[6])
                    else:
                        messagebox.showerror(parent=c,title="Error",message="No details found with Billing ID you entered")
                        
                def submit():
                    try:
                        sql='update export set Carrier_Name="%s",Origin="%s",Destination="%s",Container_Dimensions="%s",Mode_of_Transport="%s",Payment_Amount="%s" where Billing_ID="%s"'%(e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e1.get())
                        cursor.execute(sql)
                        e1["state"]='normal'
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6["state"]='normal'
                        e6.delete(0,'end')
                        e6["state"]='readonly'
                        e7.delete(0,'end')
                        messagebox.showinfo(parent=c,title="SUCCESS",message="Details updated successfully")
                        connection.commit()
                        c.destroy()
                    except:
                        messagebox.showerror(parent=c,title="ERROR",message="Couldn't Update the details")
                    
                l1=Label(c,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(c,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(c,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(c,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(c,text="Container Dimensions : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(c,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(c,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                
                e1=Entry(c,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                e2=Entry(c,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(c,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(c,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(c,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=ttk.Combobox(c,font='Arial 14',width=12,state="readonly")
                e6['values']=("Seaways","Airways","Roadways")
                e6.place(x=370,y=430)
                e7=Entry(c,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                
                fet_btn=Button(c,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=440)    
                upd_btn=Button(c,text = 'UPDATE',command=submit,bg='gold',bd=1,height=2,width=10) 
                upd_btn.place(x=550,y=490)
                res=Button(c,text = 'RESET',command=reset,bg='gold',bd=1,height=2,width=10)
                res.place(x=550,y=390)
                l = Label(c, text = 'UPDATE EXPORT DETAILS',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                
                c.title("UPDATE EXPORT DETAILS")
                c.geometry("650x550+350+150")
                c.resizable(0,0)
                c.config(bg='brown')
                c.mainloop()

            #Fetching from Export
            def fetch():
                d=Tk()
                def fetchmany():
                    sql="select * from export where %s='%s' order by %s asc"%(c1.get(),e8.get(),c1.get())
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    if len(row)!=0:
                        tv.delete(*tv.get_children())
                        for i in row:
                            tv.insert('','end',values=i)
                        connection.commit()
                        e8.delete(0,'end')
                    elif e8.get()=="":
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="Please Enter Billing ID")
                    else:
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="No details found with "+c1.get()+" you entered")
                        
                def fetchall():
                    tv.delete(*tv.get_children())
                    sql='select * from export order by Billing_ID asc'
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    for i in row:
                        e8.delete(0,'end')
                        tv.insert('','end',values=i)
                    connection.commit()
                
                tv=ttk.Treeview(d,columns=("Billing ID","Carrier Name","Origin","Destination","Container Dimensions","Mode of Transport","Payment Amount"),height=24,selectmode='browse')
                tv.place(x=20,y=70)
                tv.heading("Billing ID",text="Billing ID")
                tv.heading("Carrier Name",text="Carrier Name")
                tv.heading("Origin",text="Origin")
                tv.heading("Destination",text="Destination")
                tv.heading("Container Dimensions",text="Container Dimensions")
                tv.heading("Mode of Transport",text="Mode of Transport")
                tv.heading("Payment Amount",text="Payment Amount")
                tv['show']='headings'
                tv.column("Billing ID",width=120)
                tv.column("Carrier Name",width=140)
                tv.column("Origin",width=120)
                tv.column("Destination",width=120)
                tv.column("Container Dimensions",width=120)
                tv.column("Mode of Transport",width=120)
                tv.column("Payment Amount",width=120)

                l1=Label(d,text="Search by : ",font=["Lucida Calligraphy","14"],bg='gold')
                l1.place(x=10,y=15)
                c1=ttk.Combobox(d,font='Arial 14',width=12,state="readonly")
                c1['values']=("Billing_ID","Carrier_Name","Origin","Destination","Container_Dimensions","Mode_of_Transport","Payment_Amount")
                c1.place(x=150,y=15)
                s=ttk.Scrollbar(d,orient="vertical",command=tv.yview)
                tv.configure(yscroll=s.set)
                s.pack(side=RIGHT,fill=Y)

                e8=Entry(d,text="",font='Arial 14',width=14)
                e8.place(x=320,y=17)
                fetchall()
                fet_btn=Button(d,text = 'FETCH',command=fetchmany,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=505,y=10)
                if e8.get()!=None:
                    d.bind('<Return>', lambda i : fetchmany())
                    
                fa=Button(d,text="FETCH ALL",command=fetchall,bg='gold',bd=1,height=2,width=10)
                fa.place(x=600,y=10)
                d.title("FETCH FROM EXPORT")
                d.geometry("920x600+200+100")
                d.resizable(0,0)
                d.config(bg='brown')
                d.mainloop()

            #Deleting from Export
            def delete():
                e=Tk()
                def reset():
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6["state"]='normal'
                    e6.delete(0,'end')
                    e6["state"]='readonly'
                    e7.delete(0,'end')
                    
                def fetch():
                    sql="select * from export where Billing_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e1["state"]='readonly'
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6["state"]='normal'
                            e6.insert('end',row[5])
                            e6["state"]='readonly'
                            e7.insert('end',row[6])
                    else:
                        messagebox.showerror(parent=e,title="Error",message="No details found with Billing ID you entered")
                        
                def submit():
                    dele=messagebox.askyesno(parent=e,title="DELETE RECORD CONFIRMATION",message="Would you like to delete the selected Details?")
                    if dele>0:
                        sql='delete from export where Billing_ID="%s"'%(e1.get())
                        cursor.execute(sql)
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6["state"]='normal'
                        e6.delete(0,'end')
                        e6["state"]='readonly'
                        e7.delete(0,'end')
                        messagebox.showinfo(parent=e,title="SUCCESS",message="Details Deleted successfully")
                        connection.commit()
                    else:
                        return
                    e.destroy()
                    
                l1=Label(e,text="Billing ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=10,y=80)
                l2=Label(e,text="Carrier Name : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=10,y=145)
                l3=Label(e,text="Origin : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=10,y=215)
                l4=Label(e,text="Destination : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=10,y=290)
                l5=Label(e,text="Container Dimensions: ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=10,y=355)
                l6=Label(e,text="Mode of Transport : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=10,y=425)
                l7=Label(e,text="Payment Amount : ",font=["Algerian","18"],bg="lemon chiffon")
                l7.place(x=10,y=490)
                
                e1=Entry(e,text="",font='Arial 14',width=14)
                e1.place(x=370,y=80)
                e2=Entry(e,text="",font='Arial 14',width=14)
                e2.place(x=370,y=150)
                e3=Entry(e,text="",font='Arial 14',width=14)
                e3.place(x=370,y=220)
                e4=Entry(e,text="",font='Arial 14',width=14)
                e4.place(x=370,y=290)
                e5=Entry(e,text="",font='Arial 14',width=14)
                e5.place(x=370,y=360)
                e6=Entry(e,text="",font='Arial 14',width=14)
                e6.place(x=370,y=430)
                e7=Entry(e,text="",font='Arial 14',width=14)
                e7.place(x=370,y=490)
                    
                l = Label(e, text = 'DELETE EXPORT DETAILS',font=["Lucida Calligraphy",'20'],fg='snow',bg='brown') 
                l.place(x=125,y=10)
                fet_btn=Button(e,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=440)
                add_btn=Button(e,text = 'DELETE',command=submit,bg='gold',bd=1,height=2,width=10) 
                add_btn.place(x=550,y=490)

                e.title("DELETE EXPORT DETAILS")
                e.geometry("650x550+350+150")
                e.resizable(0,0)
                e.config(bg='brown')
                e.mainloop()

            def ret():
                a.destroy()
             
            l = Label(a, text = 'EDIT TABLE EXPORT',font=["Lucida Calligraphy",'20'],bg='brown',fg='lemon chiffon') 
            l.place(x=170,y=50)
            ins=Button(a,text = 'Insert Export Details',command=insert,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=10,y=250)
            upd=Button(a,text = 'Fetch Export Details',command=fetch,bg='lemon chiffon',bd=1,height=4,width=20) 
            upd.place(x=170,y=250)
            de=Button(a,text = 'Update Export Details',command=update,bg='lemon chiffon',bd=1,height=4,width=20) 
            de.place(x=330,y=250)
            ins=Button(a,text = 'Delete Export Details',command=delete,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=490,y=250)
            r=Button(a,text="Return to Main Window",command=ret,bg='brown',fg='lemon chiffon',bd=0,height=1)
            r.place(x=500,y=10)
            a.title("EXPORT TABLE EDIT PAGE")
            a.geometry("650x550+350+150")
            a.resizable(0,0)
            a.config(bg='brown')
            a.mainloop()

        #Editing table Employee
        def emp():
            a=Tk()
            #Inserting New Employee
            def insert():
                b=Tk()
                def submit():
                    if (e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" ):
                        messagebox.showerror(parent=b,title="ERROR",message="Please Enter all the details")
                    else:
                        try:
                            sql="insert into employee values (%s,%s,%s,%s,%s,%s) "
                            values=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
                            cursor.execute(sql,values)
                            connection.commit()
                            e1.delete(0,'end')
                            e2.delete(0,'end')
                            e3.delete(0,'end')
                            e4.delete(0,'end')
                            e5.delete(0,'end')
                            e6.delete(0,'end')
                            messagebox.showinfo(parent=b,title="SUCCESS",message="New Details inserted successfully")
                            b.destroy()
                        except:
                            messagebox.showerror(parent=b,title="ERROR",message="Couldn't insert the values")

                l1=Label(b,text="Employee ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=15,y=80)
                l2=Label(b,text="Employee FirstName : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=15,y=145)
                l3=Label(b,text="Employee LastName",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=15,y=215)
                l4=Label(b,text="Date Of Birth(YYYY-MM-DD) : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=15,y=290)
                l5=Label(b,text="Employee Designation : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=15,y=355)
                l5=Label(b,text="Employee Phone Number : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=15,y=420)
                e1=Entry(b,text="",font='Arial 14',width=14)
                e1.place(x=380,y=80)
                e2=Entry(b,text="",font='Arial 14',width=14)
                e2.place(x=380,y=150)
                e3=Entry(b,text="",font='Arial 14',width=14)
                e3.place(x=380,y=220)
                sql="select count(*) from employee"
                cursor.execute(sql)
                a=cursor.fetchall()
                if a[0][0]=="None":
                    c=1000
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                else:
                    c=a[0][0]+1000
                    e1["state"] = "normal"
                    e1.insert('end',c)
                    e1["state"] = "disabled"
                e4=Entry(b,text="",font='Arial 14',width=14)
                e4.place(x=380,y=290)
                e5=Entry(b,text="",font='Arial 14',width=14)
                e5.place(x=380,y=360)
                e6=Entry(b,text="",font='Arial 14',width=14)
                e6.place(x=380,y=425)

                
                l = Label(b, text = 'CREATE A NEW EMPLOYEE',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                add_btn=Button(b,text = 'INSERT',command=submit,bg='gold',bd=1,height=2,width=10) 
                b.bind('<Return>', lambda i : submit())
                
                add_btn.place(x=450,y=490)
                b.title("CREATE NEW EMPLOYEE")
                b.geometry("650x550+350+150")
                b.resizable(0,0)
                b.config(bg='brown')
                b.mainloop()

            #Updating Employee Details
            def update():
                messagebox.showinfo(parent=a,title="INFORMATION",message="Enter Employee ID to fetch and update the details")
                c=Tk()
                def reset():
                    e1["state"]='normal'
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6.delete(0,'end')
                    
                def fetch():
                    sql="select * from employee where Employee_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e1["state"]='readonly'
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6.insert('end',row[5])
                    else:
                        messagebox.showerror(parent=c,title="Error",message="No details found with Employee ID you entered")
                def submit():
                    try:
                        sql='update employee set Employee_FName="%s",Employee_LName="%s",Date_of_Birth="%s",Designation="%s",Employee_PhNo="%s" where Employee_ID="%s"'%(e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e1.get())
                        cursor.execute(sql)
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6.delete(0,'end')
                        messagebox.showinfo(parent=c,title="SUCCESS",message="Details updated successfully")
                        connection.commit()
                    except:
                        messagebox.showerror(parent=c,title="ERROR",message="Couldn't Update the details")
                    c.destroy()

                l1=Label(c,text="Employee ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=15,y=80)
                l2=Label(c,text="Employee FirstName : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=15,y=145)
                l3=Label(c,text="Employee LastName : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=15,y=215)
                l4=Label(c,text="Date Of Birth(YYYY-MM-DD) : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=15,y=290)
                l5=Label(c,text="Designation : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=15,y=355)
                l6=Label(c,text="Employee PhNo : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=15,y=420)
                e1=Entry(c,text="",font='Arial 14',width=14)
                e1.place(x=380,y=80)
                e2=Entry(c,text="",font='Arial 14',width=14)
                e2.place(x=380,y=150)
                e3=Entry(c,text="",font='Arial 14',width=14)
                e3.place(x=380,y=220)
                e4=Entry(c,text="",font='Arial 14',width=14)
                e4.place(x=380,y=290)
                e5=Entry(c,text="",font='Arial 14',width=14)
                e5.place(x=380,y=360)
                e6=Entry(c,text="",font='Arial 14',width=14)
                e6.place(x=380,y=425)

                fet_btn=Button(c,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=365)
                upd_btn=Button(c,text = 'UPDATE',command=submit,bg='gold',bd=1,height=2,width=10) 
                upd_btn.place(x=550,y=465)
                res=Button(c,text = 'RESET',command=reset,bg='gold',bd=1,height=2,width=10)
                res.place(x=550,y=415)
                l = Label(c, text = 'UPDATE DETAILS OF AN EMPLOYEE',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=50,y=10)
                
                c.title("UPDATE EMPLOYEE DETAILS")
                c.geometry("650x550+350+150")
                c.resizable(0,0)
                c.config(bg='brown')
                c.mainloop()

            #Fetching Employee Details
            def fetch():
                d=Tk()
                def fetchmany():
                    sql="select * from employee where %s='%s' order by %s asc"%(c1.get(),e8.get(),c1.get())
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    if len(row)!=0:
                        tv.delete(*tv.get_children())
                        for i in row:
                            e8.delete(0,'end')
                            tv.insert('','end',values=i)
                        connection.commit()
                    elif e8.get()=="":
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="Please Enter Billing ID")
                    else:
                        e8.delete(0,'end')
                        tv.delete(*tv.get_children())
                        messagebox.showerror(parent=d,title="Error",message="No details found with "+c1.get()+" you entered")
                        
                def fetchall():
                    tv.delete(*tv.get_children())
                    sql='select * from Employee order by Employee_ID asc'
                    cursor.execute(sql)
                    row=cursor.fetchall()
                    for i in row:
                        e8.delete(0,'end')
                        tv.insert('','end',values=i)
                    connection.commit()
                
                tv=ttk.Treeview(d,columns=("Employee ID","Employee FirstName","Employee LastName","Date Of Birth","Designation","Employee PhNo"),height=24,selectmode='browse')
                tv.place(x=25,y=70)
                tv.heading("Employee ID",text="Employee ID")
                tv.heading("Employee FirstName",text="Employee FirstName")
                tv.heading("Employee LastName",text="Employee LastName")
                tv.heading("Date Of Birth",text="Date Of Birth")
                tv.heading("Designation",text="Designation")
                tv.heading("Employee PhNo",text="Employee PhNo")
                tv['show']='headings'
                tv.column("Employee ID",width=140)
                tv.column("Employee FirstName",width=140)
                tv.column("Employee LastName",width=140)
                tv.column("Date Of Birth",width=140)
                tv.column("Designation",width=140)
                tv.column("Employee PhNo",width=140)

                l1=Label(d,text="Search by : ",font=["Lucida Calligraphy","14"],bg='gold')
                l1.place(x=10,y=15)
                c1=ttk.Combobox(d,font='Arial 14',width=12,state="readonly")
                c1['values']=("Employee_ID","Employee_FName","Employee_LName","Date_of_Birth","Designation","Employee_PhNo","Year(Date_of_Birth)","Month(Date_of_Birth)")
                c1.place(x=150,y=15)
                s=ttk.Scrollbar(d,orient="vertical",command=tv.yview)
                tv.configure(yscroll=s.set)
                s.pack(side=RIGHT,fill=Y)

                e8=Entry(d,text="",font='Arial 14',width=14)
                e8.place(x=320,y=17)
                fetchall()
                fet_btn=Button(d,text = 'FETCH',command=fetchmany,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=505,y=10)
                if e8.get()!=None:
                    d.bind('<Return>', lambda i : fetchmany())
                
                fa=Button(d,text="FETCH ALL",command=fetchall,bg='gold',bd=1,height=2,width=10)
                fa.place(x=600,y=10)
                d.title("FETCH FROM EMPLOYEE")
                d.geometry("920x600+200+100")
                d.resizable(0,0)
                d.config(bg='brown')
                d.mainloop()

            #Removing an Employee
            def delete():
                e=Tk()
                def reset():
                    e1["state"]='normal'
                    e1.delete(0,'end')
                    e2.delete(0,'end')
                    e3.delete(0,'end')
                    e4.delete(0,'end')
                    e5.delete(0,'end')
                    e6.delete(0,'end')
                    
                def fetch():
                    sql="select * from employee where Employee_ID='%s'"%(e1.get())
                    cursor.execute(sql)
                    rows=cursor.fetchall()
                    reset()
                    if len(rows)!=0:
                        for row in rows:
                            e1.insert('end',row[0])
                            e1["state"]='readonly'
                            e2.insert('end',row[1])
                            e3.insert('end',row[2])
                            e4.insert('end',row[3])
                            e5.insert('end',row[4])
                            e6.insert('end',row[5])
                    else:
                        messagebox.showerror(parent=e,title="Error",message="No details found with Employee ID you entered")
                        
                def submit():
                    dele=messagebox.askyesno(parent=e,title="DELETE RECORD CONFIRMATION",message="Would you like to delete the selected Details?")
                    if dele>0:
                        sql='delete from employee where Employee_ID="%s"'%(e1.get())
                        cursor.execute(sql)
                        e1.delete(0,'end')
                        e2.delete(0,'end')
                        e3.delete(0,'end')
                        e4.delete(0,'end')
                        e5.delete(0,'end')
                        e6.delete(0,'end')
                        messagebox.showinfo(parent=e,title="SUCCESS",message="Details Deleted successfully")
                        connection.commit()
                    else:
                        return
                    e.destroy()

                l1=Label(e,text="Employee ID : ",font=["Algerian","18"],bg="lemon chiffon")
                l1.place(x=15,y=80)
                l2=Label(e,text="Employee FirstName : ",font=["Algerian","18"],bg="lemon chiffon")
                l2.place(x=15,y=145)
                l3=Label(e,text="Employee LastName : ",font=["Algerian","18"],bg="lemon chiffon")
                l3.place(x=15,y=215)
                l4=Label(e,text="Date Of Birth(YYYY-MM-DD) : ",font=["Algerian","18"],bg="lemon chiffon")
                l4.place(x=15,y=290)
                l5=Label(e,text="Designation : ",font=["Algerian","18"],bg="lemon chiffon")
                l5.place(x=15,y=355)
                l6=Label(e,text="Employee PhNo : ",font=["Algerian","18"],bg="lemon chiffon")
                l6.place(x=15,y=420)
                e1=Entry(e,text="",font='Arial 14',width=14)
                e1.place(x=380,y=80)
                e2=Entry(e,text="",font='Arial 14',width=14)
                e2.place(x=380,y=150)
                e3=Entry(e,text="",font='Arial 14',width=14)
                e3.place(x=380,y=220)
                e4=Entry(e,text="",font='Arial 14',width=14)
                e4.place(x=380,y=290)
                e5=Entry(e,text="",font='Arial 14',width=14)
                e5.place(x=380,y=360)
                e6=Entry(e,text="",font='Arial 14',width=14)
                e6.place(x=380,y=425)
                
                l = Label(e, text = 'REMOVE AN EMPLOYEE',font=["Lucida Calligraphy",'20'],bg='brown',fg='snow') 
                l.place(x=125,y=10)
                fet_btn=Button(e,text = 'FETCH',command=fetch,bg='gold',bd=1,height=2,width=10) 
                fet_btn.place(x=550,y=420)
                add_btn=Button(e,text = 'REMOVE',command=submit,bg='gold',bd=1,height=2,width=10) 
                add_btn.place(x=550,y=470)
                
                e.title("REMOVE AN EMLOYEE")
                e.geometry("650x550+350+150")
                e.resizable(0,0)
                e.config(bg='brown')
                e.mainloop()
                
            def ret():
                a.destroy()
                
            l = Label(a, text = 'EDIT TABLE EMPLOYEE',font=["Lucida Calligraphy",'20'],bg='brown',fg='lemon chiffon') 
            l.place(x=150,y=50)
            ins=Button(a,text = 'Insert Employee Details',command=insert,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=10,y=250)
            upd=Button(a,text = 'Fetch Employee Details',command=fetch,bg='lemon chiffon',bd=1,height=4,width=20) 
            upd.place(x=170,y=250)
            de=Button(a,text = 'Update Employee Details',command=update,bg='lemon chiffon',bd=1,height=4,width=20) 
            de.place(x=330,y=250)
            ins=Button(a,text = 'Remove an Employee',command=delete,bg='lemon chiffon',bd=1,height=4,width=20) 
            ins.place(x=490,y=250)
            r=Button(a,text="Return to Main Window",command=ret,bg='brown',fg='lemon chiffon',bd=0,height=1)
            r.place(x=500,y=10)
            a.title("EMPLOYEE TABLE EDIT PAGE")
            a.geometry("650x550+350+150")
            a.resizable(0,0)
            a.config(bg='brown')
            a.mainloop()

        '''def setting():
            wint=Tk()
            def lh():
                a=Tk()
                tv=ttk.Treeview(a,columns=("Username","Password","Login Time"),height=13,selectmode='browse')
                tv.place(x=15,y=15)
                tv.heading("Username",text="Username")
                tv.heading("Password",text="Password")
                tv.heading("Login Time",text="Login Time")
                tv['show']='headings'
                tv.column("Username",width=150)
                tv.column("Password",width=150)
                tv.column("Login Time",width=150)
                s=ttk.Scrollbar(a,orient="vertical",command=tv.yview)
                tv.configure(yscroll=s.set)
                s.pack(side=RIGHT,fill=Y)
                tv.delete(*tv.get_children())
                sql='select * from login order by Login_Time asc'
                cursor.execute(sql)
                row=cursor.fetchall()
                for i in row:
                    tv.insert('','end',values=i)
                connection.commit()
            
                def de():
                    dele=messagebox.askyesno(parent=a,title="DELETE LOGIN HISTORY CONFIRMATION",message="Are you sure you want to delete Login History?")
                    if dele>0:
                        sql='truncate table login'
                        cursor.execute(sql)
                        connection.commit()
                        tv.delete(*tv.get_children())
                        messagebox.showinfo(parent=a,title='SUCCESS',message="Login History Deleted successfully")
                        a.destroy()
                    else:
                        return

                d=Button(a,text="Delete History",command=de,width=10)
                d.place(x=400,y=315)

                a.title("LOGIN HISTORY")
                a.geometry("500x350+450+250")
                a.resizable(0,0)
                a.config(bg='brown')
                a.mainloop()
            def dele():
                dele=messagebox.askyesno(parent=win,title="DELETE USER CONFIRMATION",message="Are you sure you want to delete current user?")
                if dele>0:
                    sql='drop table import,export,employee,login'
                    cursor.execute(sql)
                    connection.commit()
                    c=open('up.txt','w')
                    c.truncate()
                    c.close()
                    messagebox.showinfo(parent=win,title="SUCCESS",message="Current User deleted successfully")
                    wint.destroy()
                    win.destroy()

                else:
                    return
            def upd():
                wind=Tk()

                def sub():
                    username=name.get()
                    password=passw.get()
                    np=key.get()
                    cn=na.get()

                    if name.get()=="" or passw.get()=="" or conpas.get()=="" or key.get()=="" or na.get()=="":
                        messagebox.showerror(parent=wind,title="ERROR",message="Please Enter all the details")
                    elif passw.get()!=conpas.get():
                        messagebox.showerror(parent=wind,title="ERROR",message="Password's aren't same Please Check")
                        passw.delete(0,'end')
                        conpas.delete(0,'end')
                    elif key.get().isdigit()==False:
                        messagebox.showerror(parent=wind,title="ERROR",message="Please Enter a Pin Number.\nYou have Entered an alphabet")
                    elif passw.get()==conpas.get() and key.get().isdigit():
                        b=open("up.txt","w")
                        b.write(username+"\n")
                        b.write(password+"\n")
                        b.write(np+"\n")
                        b.write(cn)
                        b.close()
                        name.delete(0,'end')
                        passw.delete(0,'end')
                        conpas.delete(0,'end')
                        key.delete(0,'end')
                        na.delete(0,'end')
                        messagebox.showinfo(parent=wind,title="SUCCESS",message="User Details Updated successfully")
                        messagebox.showinfo(parent=wind,title="Information",message="Please Relaunch your Application to save the details")
                        wind.destroy()
                    else:
                        return

                name_label = Label(wind, text = 'Username : ',font='14',bg='lemon chiffon') 
                name_label.place(x=50,y=65)
                name = Entry(wind,text = "",font='14',width=14,justify=LEFT) 
                name.place(x=275,y=65)
                passw_label = Label(wind,text = 'Password : ',font='14',bg='lemon chiffon') 
                passw_label.place(x=50,y=105)
                passw=Entry(wind,text = "",show="*",font='14',width=14,justify=LEFT)
                passw.place(x=275,y=105)
                conpas_label=Label(wind,text = 'Confirm Password : ',font='14',bg='lemon chiffon') 
                conpas_label.place(x=50,y=145)
                conpas=Entry(wind,text = "",show="*",font='14',width=14,justify=LEFT)
                conpas.place(x=275,y=145)
                key_label = Label(wind, text = 'Set a Pin Number : ',font='14',bg='lemon chiffon') 
                key_label.place(x=50,y=185)
                key = Entry(wind,text = "",show="*",font='14',width=14,justify=LEFT) 
                key.place(x=275,y=185)
                na_label = Label(wind, text = 'Company Name : ',font='14',bg='lemon chiffon') 
                na_label.place(x=50,y=225)
                na = Entry(wind,text = "",font='14',width=14,justify=LEFT) 
                na.place(x=275,y=225)

                def sp():
                    if c.get()==1:
                        c.set(0)
                        passw.config(show="")
                        conpas.config(show="")
                        key.config(show="")
                    elif c.get()==0:
                        c.set(1)
                        passw.config(show="*")
                        conpas.config(show="*")
                        key.config(show="*")
                c=IntVar()
                c.set(1)
                sp_btn=Checkbutton(wind,text='Show Password & Pin',command=sp,onvalue=0,offvalue=1,variable=c,width=16,font='Arial 10',bg='brown')
                sp_btn.place(x=80,y=270)
                login_btn=Button(wind,text = 'Save Changes',command=sub,bg='lemon chiffon',bd=1,width=13)
                wind.bind('<Return>', lambda i : sub())
                login_btn.place(x=330,y=270)

                with open("up.txt", "r") as fd:
                    j = fd.read().splitlines()
                    if len(j)!=0:
                        name.insert('end',j[0])
                        passw.insert('end',j[1])
                        conpas.insert('end',j[1])
                        key.insert('end',j[2])
                        na.insert('end',j[3])
                wind.title("UPDATE USER DETAILS")
                wind.geometry("500x350+450+250")
                wind.resizable(0, 0)
                wind.config(bg='brown')
                wind.mainloop()

            l=Label(wint,text="User Settings",bg="brown",fg="Gold",font='Algerian 24',bd=1)
            l.place(x=140,y=20)
            f1=Frame(wint,height=250,width=400)
            f1.place(x=50,y=70)
            u=Button(f1,text="Update User \nDetails",command=upd,fg="brown",font='10',bg="snow",height=2,bd=0)
            u.place(x=140,y=170)
            d=Button(f1,text="Delete User",command=dele,fg="brown",bg="snow",font='10',width=10,height=2,bd=0)
            d.place(x=140,y=90)
            l=Button(f1,text="Login History",command=lh,fg="brown",bg="snow",font='10',width=10,height=2,bd=0)
            l.place(x=140,y=10)
            wint.title("USER SETTINGS")
            wint.geometry("500x350+450+250")
            wint.resizable(0,0)
            wint.config(bg='brown')
            wint.mainloop()'''

        def logout():
            dele=messagebox.askyesno(parent=win,title="LOG OUT CONFIRMATION",message="Are you sure you want to logout?")
            if dele>0:
                win.destroy()
            else:
                return
            
        #Label and Buttons for second window
        l = Label(win, text = 'CHOOSE YOUR TABLE HERE',font=["Lucida Calligraphy",'20'],bg='brown',fg='lemon chiffon') 
        l.place(x=100,y=50)
        imp=Button(win,text = 'IMPORT',command=imp,bg='lemon chiffon',bd=1,height=4,width=20) 
        imp.place(x=250,y=150)
        exp=Button(win,text = 'EXPORT',command=exp,bg='lemon chiffon',bd=1,height=4,width=20) 
        exp.place(x=250,y=250)
        emp=Button(win,text = 'EMPLOYEE',command=emp,bg='lemon chiffon',bd=1,height=4,width=20) 
        emp.place(x=250,y=350)
        
        v=Label(win,text="CMS version 1.1",bg="brown",font=(None,12))
        v.place(x=520,y=520)
        '''l=Button(win,text="User Settings",command=setting,bg="brown",fg="snow",width=10,height=2,bd=0)
        l.place(x=20,y=500)'''
        lo=Button(win,text="Logout",command=logout,bg='brown',fg='lemon chiffon',font="Arial 14 italic",bd=0,height=1)
        lo.place(x=560,y=10)
        win.title("CARGO MANAGEMENT SYSTEM EDIT PAGE")
        win.geometry("650x550+350+150")
        win.resizable(0,0)
        win.config(bg='brown')
        win.mainloop()

    elif (name_entry.get() =="") and (passw_entry.get() ==""):
        messagebox.showerror("Error","Please Enter your Username and Password")
    elif (name_entry.get() =="") :
        messagebox.showerror("Error","Please Enter your Username")
    elif (passw_entry.get() =="") :
        messagebox.showerror("Error","Please Enter your Password")
    elif (name_entry.get() !=i[0]) and (passw_entry.get() !=i[1]):
        messagebox.showerror("Error","The Username and Password you Entered is Incorrect")
        name_entry.delete(0,'end')
        passw_entry.delete(0,'end')
    elif (passw_entry.get() !=i[1]) :
        passw_entry.delete(0,'end')
        messagebox.showerror("Error","The Password you Entered is Incorrect")
    elif name_entry.get() != i[0]:
        messagebox.showerror("Error","The Username you Entered does not Exist")
        name_entry.delete(0,'end')
        

#About this software
def info():
    at=Tk()
    #Opening and reading a text file
    a=open("info.txt","r")
    c=a.read()
    a.close()
    info_lbl=Label(at,text="About this Software : ",font=['Ink Free','20','bold'],bg='brown',fg='gold')
    info_lbl.place(x=10,y=10)
    con=Text(at,font=['Ink Free','14','bold'],bg='brown',fg='snow',height=14,width=40,bd=0)
    con.insert('end',c)
    s=ttk.Scrollbar(at,orient="vertical",command=con.yview)
    con.configure(yscroll=s.set)
    s.pack(side=RIGHT,fill=Y)
    con.place(x=10,y=60)  
    at.title("About this Software")
    at.geometry("530x400+275+175")
    at.resizable(0, 0)
    at.config(bg='brown')
    at.mainloop()

#Function for Forgot Password
def forpas():
    at=Tk()
    def submit():
        if (npn.get()==i[2]):
            messagebox.showinfo("Information","Your Password is "+i[1])
            at.destroy()

        elif (npn.get()) =="":
            messagebox.showerror("Error","Please enter your Pin Number to fetch Password")

        elif (npn.get()) !=i[2] :
            messagebox.showerror("Error","The Pin Number you entered is incorrect")
            at.destroy()
            
    def info():
        messagebox.showinfo(parent=at,title="Information",message="Please enter the pin number you entered while registering yourself")
        
    wl=Label(at, text = 'Verify Your Pin Number',font='18',fg='lemon chiffon',bg='brown')
    wl.place(x=110,y=30)
    np_label = Label(at, text = 'Pin Number : ',font='14',bg='lemon chiffon') 
    np_label.place(x=50,y=125)
    npn = Entry(at,text = "",show = '*',font='Arial 14',width=14)
    npn.place(x=195,y=125)
    sub_btn=Button(at,text = 'Verify Pin',command=submit,bg='lemon chiffon',bd=1)
    at.bind('<Return>', lambda i : submit())
    sub_btn.place(x=250,y=200)
    c=Button(at,text="  ?  ",command=info,bg='lemon chiffon',bd=1)
    c.place(x=360,y=127)
    at.title("FORGOT PASSWORD")
    at.geometry("400x300+400+200")
    at.resizable(0, 0)
    at.config(bg='brown')
    at.mainloop()
    
#Defining Labels and Buttons for Login page    
welcome_label = Label(window, text ='Cargo Management System',font=['Ink Free','22','bold'],bg='brown',fg="lemon chiffon",width=38) 
welcome_label.place(x=5,y=40)
name_label = Label(window, text = 'Username : ',font="Arial 16 bold italic",fg='lemon chiffon',bg='brown') 
name_label.place(x=70,y=320)
name_entry = Entry(window,text='',font="Arial 15",width=14,justify=LEFT) 
name_entry.place(x=200,y=325)
passw_label = Label(window,text = 'Password : ',font="Arial 16 bold italic",fg='lemon chiffon',bg='brown') 
passw_label.place(x=70,y=360)
passw_entry=Entry(window,text='',show = '*',font="Arial 15",width=14,justify=LEFT)
passw_entry.place(x=200,y=365)

'''def sp():
    if c.get()==1:
        passw_entry.config(show="")
    elif c.get()==0:
        passw_entry.config(show="*")
c=IntVar()
sp_btn=Checkbutton(window,text='Show Password',command=sp,onvalue=1,offvalue=0,variable=c,width=13,font='Arial 10',bg='brown')
sp_btn.place(x=475,y=370)'''
login_btn=Button(window,text = 'Login Here',command=login,bg='lemon chiffon',bd=1,height=2,width=14) 
login_btn.place(x=475,y=320)
for_btn=Button(window,text = 'Forgot Password',command=forpas,bg='lemon chiffon',bd=1,height=2,width=14)
for_btn.place(x=475,y=270)
reg=Button(window,text='Register here',command=register,bg='lemon chiffon',bd=1,height=2,width=14)
reg.place(x=475,y=220)

if len(i)!=4:
    login_btn["state"]="disabled"
    for_btn["state"]="disabled"
if len(i)==4:
    reg["state"]="disabled"
    for_btn["state"]="normal"
    welcome_label.config(text=i[3]+"\nCargo Management System")
v=Label(window,text="CMS version 1.1",bg="brown",font=(None,12))
v.place(x=520,y=520)
info=Button(window,text='Click here to view\nabout this software',command=info,bg='brown',fg="lemon chiffon",bd=0)
info.place(x=20,y=500)
if len(i)==4:
    window.bind('<Return>', lambda i : login())
elif len(i)!=4:
    window.bind('<Return>', lambda i : register())

#Inserting an Image
b=PhotoImage(file='F:\\My file 1\\CMS Project Files\\images.png')
lbl=Label(window,image=b)
lbl.place(x=140,y=150)
window.title("WELCOME TO CARGO MANAGEMENT SYSTEM")
window.geometry("650x550+350+150")
window.resizable(0,0)
window.config(bg='brown')
window.mainloop()

#=================PROGRAM OVER  THANK YOU================#