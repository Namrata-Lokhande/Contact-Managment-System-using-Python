# Contact-Managment-System-using-Python
I have to develop this project using python. I have to use Tkinter module  & Sqlite3 database to develop the system. 

print("Hello")

	……………………………..Python project code……………………….

from Tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("student.db")
      
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not firstname.get():
        t1.insert(END,"<>First name is required<>\n")
        a=1
    if not i.get():
        t1.insert(END,"<>ID is required<>\n")
        b=1
    if not lastname.get():
        t1.insert(END,"<>Last name is required<>\n")
        c=1
    if not phoneno.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not email.get():
        t1.insert(END,"<>Email Id is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_contacts():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(FIRSTNAME TEXT,I INTEGER,LASTNAME TEXT,PHONENO INTEGER,EMAIL TEXT,ADDRESS TEXT)")
                cur.execute("insert into STUDENTS values(?,?,?,?,?,?)",(firstname.get(),int(i.get()),lastname.get(),int(phoneno.get()),email.get(),address.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_contacts():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_contacts():
    
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE I=?",(int(i.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_contacts():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET FIRSTNAME=?,I=?,LASTNAME=?,PHONENO=?,EMAIL=?,ADDRESS=? where I=?",(firstname.get(),int(i.get()),lastname.get(),int(phoneno.get()),email.get(),address.get(),int(i.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")
        
def search():
        conn=connection()
        cur=conn.cursor()
        cur.execute("SELECT * FROM STUDENTS  where I=?",(int(i.get()),))
        data=cur.fetchall()
        conn.close()
        t1.insert(END," SUCCESSFULLY SEARCHED\n")
        for i1 in data:
            t1.insert(END,str(i1)+"\n")
            

def clear_contact():
        conn=connection()
        cur=conn.cursor()

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        conn.commit()
        conn.close()

def clear_data():
    conn=connection()
    cur=conn.cursor()
    
    t1.delete(0,END)

    conn.commit()
    conn.close()
        

def close():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Contact Management System")
    root.configure(background='yellow')
     
    firstname=StringVar()
    i=StringVar()
    lastname=StringVar()
    phoneno=StringVar()
    email=StringVar()
    address=StringVar()
    lblTitle1=Label(root,font=('Comic Sans MS',20,'bold'),text='Contact Details',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
    lblTitle1.grid(row=0,column=0)
    
    label1=Label(root,text="FirstName:",font=('Comic Sans MS',14,'bold'),bg='yellow')
    label1.place(x=0,y=120)

    label2=Label(root,text="Id:",font=('Comic Sans MS',14,'bold'),bg='yellow')
    label2.place(x=0,y=150)

    label3=Label(root,text="LastNAme:",font=('Comic Sans MS',14,'bold'),bg='yellow')
    label3.place(x=0,y=180)

    label4=Label(root,text="Phoneno:",font=('Comic Sans MS',14,'bold'),bg='yellow')
    label4.place(x=0,y=210)
    
    label5=Label(root,text="Address:",font=('Comic Sans MS',12,'bold'),bg='yellow')
    label5.place(x=0,y=240)

    label6=Label(root,text="EmailId:",font=('Comic Sans MS',13,'bold'),bg='yellow')
    label6.place(x=0,y=270)

    e1=Entry(root,textvariable=firstname)
    e1.place(x=130,y=120)
    
    e2=Entry(root,textvariable=i)
    e2.place(x=130,y=150)

    e3=Entry(root,textvariable=lastname)
    e3.place(x=130,y=180)

    e4=Entry(root,textvariable=phoneno)
    e4.place(x=130,y=210)
    
    e5=Entry(root,textvariable=address)
    e5.place(x=130,y=240)

    e6=Entry(root,textvariable=email)
    e6.place(x=130,y=270)

    
    
    lblTitle=Label(root,font=('Comic Sans MS',20,'bold'),text='..Contact Management System..',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
    lblTitle.grid(row=0,column=1)
    t1=Text(root,width=100,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD CONTACTS",font=('Gill Sans MT',8,'bold'),command=add_contacts,width=40,bg='red')
    b1.grid(row=11,column=0)

    clear_data=Button(root,text="CLEAR DATA",font=('Gill Sans MT',8,'bold'),command=clear_data,width=30,bg='pink')
    clear_data.grid(row=11,column=1)

    b2=Button(root,text="VIEW ALL CONTACTS",font=('Gill Sans MT',8,'bold'),command=view_contacts,width=40,bg='blue')
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE CONTACTS",font=('Gill Sans MT',8,'bold'),command=delete_contacts,width=40,bg='green')
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",font=('Gill Sans MT',8,'bold'),command=update_contacts,width=40,bg='orange')
    b4.grid(row=14,column=0)

    b5=Button(root,text="SEARCH INFO",font=('Gill Sans MT',8,'bold'),command=search,width=40,bg='cadet blue')
    b5.grid(row=15,column=0)
    
    b5=Button(root,text="CLEAR",font=('Gill Sans MT',8,'bold'),command=clear_contact,width=40,bg='brown')
    b5.grid(row=16,column=0)

    b5=Button(root,text="EXIT",font=('Gill Sans MT',8,'bold'),command=close,width=40,bg='yellow')
    b5.grid(row=17,column=0)


    root.mainloop()

