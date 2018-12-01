from Tkinter import *
from tkMessageBox import *
import os
import sqlite3
con1=sqlite3.Connection('QuizPortal1')
cur1=con1.cursor()
con=sqlite3.Connection('QuizPortal')
cur=con.cursor()
cur1.execute("create table if not exists QuizPortal1(fname1 varchar,lname1 varchar,nname1 varchar, age1 number,dob1 varchar,college1 varchar,score1 number,attempted1 number,topic1 varchar)")
cur.execute("drop table if exists QuizPortal")
cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number,attempted number,topic varchar)")
counter=20

#==========================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#New Result Page

def newResultPage():
    rootx = Tk()
    rootx.title('Result')
    rootx.geometry("2000x1200")
    rootx.configure(bg='wheat')
    
    a1=' '
    def resete1():
        e1.delete(0,END)
    
    Button(rootx,text="Reset",command=resete1, relief=RAISED,font='Times 15').grid(row=1,column=3,sticky=E)
    Label(rootx,text="Fetch Result as per Enrollment Number\n",font='Times 30 bold',bg='wheat').grid(row=0,column=1,sticky=W,columnspan=20)
    Label(rootx,text="  Enter Enrollment No.(eg:171b108):",font='Arial 23',bg='wheat').grid(row=1,column=0,sticky=W)
    e1=Entry(bd=5,font='Arial 23')
    e1.grid(row=1,column=1,sticky=W)


    Label(rootx,text="  FirstName:",font='Arial 23',bg='wheat').grid(row=2,column=0,sticky=W)
    e2=Entry(bd=5,font='Arial 23')
    e2.grid(row=2,column=1,sticky=W)


    Label(rootx,text="  LastName:",font='Arial 23',bg='wheat').grid(row=3,column=0,sticky=W)
    e3=Entry(bd=5,font='Arial 23')
    e3.grid(row=3,column=1,sticky=W)

    Label(rootx,text="  Score:",font='Arial 23',bg='wheat').grid(row=4,column=0,sticky=W)
    e4=Entry(bd=5,font='Arial 23')
    e4.grid(row=4,column=1,sticky=W)

    Label(rootx,text="  Questions Attempted:",font='Arial 23',bg='wheat').grid(row=5,column=0,sticky=W)
    e5=Entry(bd=5,font='Arial 23')
    e5.grid(row=5,column=1,sticky=W)


    Label(rootx,text="  Topic:",font='Arial 23',bg='wheat').grid(row=6,column=0,sticky=W)
    Label(rootx,text="",bg='wheat').grid(row=6,column=0,sticky=W)
    e6=Entry(bd=5,font='Arial 23')
    e6.grid(row=6,column=1,sticky=W)

    Label(rootx,text="  College Name:",font='Arial 23',bg='wheat').grid(row=7,column=0,sticky=W)
    Label(rootx,text="",bg='wheat').grid(row=7,column=0,sticky=W)
    e7=Entry(bd=5,font='Arial 23')
    e7.grid(row=7,column=1,sticky=W)

    Label(rootx,text="  Date of Birth:",font='Arial 23',bg='wheat').grid(row=8,column=0,sticky=W)
    Label(rootx,text="",bg='wheat').grid(row=8,column=0,sticky=W)
    e8=Entry(bd=5,font='Arial 23')
    e8.grid(row=8,column=1,sticky=W)
    Label(rootx,text="",bg='wheat').grid(row=9,column=0,columnspan=20)

    def reset():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
    def shownew():
        
        a1=str(e1.get())
        cur1.execute("Select * from QuizPortal1")
        print cur1.fetchall()
        reset()
        cur1.execute("select nname1 from QuizPortal1 where nname1=?",(a1,))
        nname1=cur1.fetchone()
        nname=(nname1,)
        e1.insert(0,nname)
        
        cur1.execute("select fname1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e2.insert(0,fname)

        cur1.execute("select lname1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e3.insert(0,fname)

        cur1.execute("select score1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e4.insert(0,fname)

        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e5.insert(0,fname)

        cur1.execute("select topic1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e6.insert(0,fname)

        cur1.execute("select college1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e7.insert(0,fname)

        cur1.execute("select dob1 from QuizPortal1 where nname1=?",(a1,))
        fname1=cur1.fetchone()
        fname=(fname1,) 
        e8.insert(0,fname)

    def EXIT():
        #cur.execute('drop table if exists QuizPortal')
        con1.commit()
        rootx.destroy()
        
        
    Button(rootx,text="SHOW", font='Arial 15 bold',relief=RAISED,command=shownew,width=10,bg='cyan').grid(row=10,column=1,sticky=W)
    Button(rootx,text="EXIT",font='Arial 15 bold',relief=RAISED,command=EXIT,width=10,bg='orange').grid(row=10,column=4,sticky=E)
    rootx.mainloop()






#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Result Page:

def resultPage():
    rootx1 = Tk()
    rootx1.title('Result Page')
    rootx1.geometry("2000x1200")
    rootx1.configure(bg='wheat')
    
    a1=' '
    
    Label(rootx1,text="Results of Quiz",font='Times 40 bold',bg='wheat',justify=CENTER).grid(row=0,column=1,columnspan=2)
    Label(rootx1,text="",bg='wheat').grid(row=1,column=0,columnspan=2)
    
    Label(rootx1,text="  Enrollment: ",font='Arial 23',bg='wheat').grid(row=2,column=0,sticky=W)
    e1=Entry(font='Arial 23')
    e1.grid(row=2,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=3,column=0,columnspan=2)


    Label(rootx1,text="  First Name: ",font='Arial 23',bg='wheat').grid(row=4,column=0,sticky=W)
    e2=Entry(font='Arial 23')
    e2.grid(row=4,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=5,column=0,columnspan=2)


    Label(rootx1,text="  Last Name: ",font='Arial 23',bg='wheat').grid(row=6,column=0,sticky=W)
    e3=Entry(font='Arial 23')
    e3.grid(row=6,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=7,column=0,columnspan=2)

    Label(rootx1,text="  Score: ",font='Arial 23',bg='wheat').grid(row=8,column=0,sticky=W)
    e4=Entry(font='Arial 23')
    e4.grid(row=8,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=9,column=0,columnspan=2)

    Label(rootx1,text="  Questions Attempted: ",font='Arial 23',bg='wheat').grid(row=10,column=0,sticky=W)
    e5=Entry(font='Arial 23')
    e5.grid(row=10,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=11,column=0,columnspan=2)


    Label(rootx1,text="  Topic selected: ",font='Arial 23',bg='wheat').grid(row=12,column=0,sticky=W)
    e6=Entry(font='Arial 23')
    e6.grid(row=12,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=13,column=0,sticky=W)

    Label(rootx1,text="  College Name: ",font='Arial 23',bg='wheat').grid(row=14,column=0,sticky=W)
 
    e7=Entry(font='Arial 23')
    e7.grid(row=14,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=15,column=0,sticky=W)

    Label(rootx1,text="  Date of Birth: ",font='Arial 23',bg='wheat').grid(row=16,column=0,sticky=W)
    
    e8=Entry(font='Arial 23')
    e8.grid(row=16,column=1,sticky=W)
    Label(rootx1,text="",bg='wheat').grid(row=17,column=5,columnspan=20)
    def reset():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
    def show():
        reset()
        a1=str(e1.get())
        cur.execute("Select * from QuizPortal")
        print cur.fetchall()
        
        cur.execute("select nname from QuizPortal")
        nname1=cur.fetchone()
        nname=(nname1,)
        e1.insert(0,nname)
        
        cur.execute("select fname from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e2.insert(0,fname)

        cur.execute("select lname from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e3.insert(0,fname)

        cur.execute("select score from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e4.insert(0,fname)

        cur.execute("select attempted from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e5.insert(0,fname)

        cur.execute("select topic from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e6.insert(0,fname)

        cur.execute("select college from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e7.insert(0,fname)

        cur.execute("select dob from QuizPortal")
        fname1=cur.fetchone()
        fname=(fname1,) 
        e8.insert(0,fname)
        con1.commit()
        cur.execute('drop table QuizPortal')

    def exit1():
        con1.commit()
        cur.execute('drop table if exists QuizPortal')
        rootx1.destroy()

    def newResultPage1():
        rootx1.destroy()
        newResultPage()
        
    Button(rootx1,text="DISPLAY",font='Arial 15 bold', relief=RAISED,command=show,width=10,bg='green').grid(row=18,column=0)
    Button(rootx1,text="EXIT",font='Arial 15 bold', relief=RAISED,command=exit1,width=10,bg='red').grid(row=18,column=5,sticky=E)
    Button(rootx1,text="VIEW OTHER RESULTS",font='Arial 15 bold', relief=RAISED,command=newResultPage1,width=20,bg='cyan').grid(row=18,column=1)

    rootx1.mainloop()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 10 Page Code Begins Here

def Question10():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root11 = Tk()
    root11.geometry("2000x1200")
    root11.configure(bg='light blue')
    root11.title('Question No.10')
    counter=20
    def counter_label(label):
        
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root11.destroy()
                resultPage()   
        count()
    label=Label(root11,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root11,text="",bg='light blue').pack()
    Label(root11,text="Question 10",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root11,text="",bg='light blue').pack()
    Label(root11, text="  10) Which of the following best describes polymorphism? ",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root11,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root11, text="Ability of a class to derive members of another class as a part of its own definition", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root11, text="Bundling instance variables and methods in order to restrict access to class members", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root11, text="Focuses on variables and passing of variables to functions", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root11, text="Allows for objects of different types and behaviour to be treated as the same general type", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==4):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root11.destroy()
            resultPage()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root11.destroy()
           resultPage()


    Label(root11,text="\n\n\n\n",bg='light blue').pack()
    Button(root11,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root11,text="\n\n",bg='light blue').pack()
    label = Label(root11)
    label.pack()

    root11.mainloop()





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 9 


def Question9():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root10 = Tk()
    root10.geometry("2000x1200")
    root10.configure(bg='light blue')
    root10.title('Question No.9')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root10.destroy()
                resultPage()   
        count()
    label=Label(root10,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root10,text="",bg='light blue').pack()
    Label(root10,text="Question 9",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root10,text="",bg='light blue').pack()
    Label(root10, text="  9) Which of the following functions is a built-in function in python?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root10,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root10, text="seed()", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root10, text="sqrt()", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root10, text="factorial()", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root10, text="print()", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==4):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root10.destroy()
            Question10()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root10.destroy()
           Question10()


    Label(root10,text="\n\n\n\n",bg='light blue').pack()
    Button(root10,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root10,text="\n\n",bg='light blue').pack()
    label = Label(root10)
    label.pack()

    root10.mainloop()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 8


def Question8():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root9 = Tk()
    root9.geometry("2000x1200")
    root9.configure(bg='light blue')
    root9.title('Question No.8')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root9.destroy()
                resultPage()   
        count()
    label=Label(root9,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root9,text="",bg='light blue').pack()
    Label(root9,text="Question 8",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root9,text="",bg='light blue').pack()
    Label(root9, text="  8) What type of data is: a=[(1,1),(2,4),(3,9)]? ",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root9,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root9, text="Array of tuples", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root9, text="List of tuples", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root9, text="Tuples of lists", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root9, text="Invalid type", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==2):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root9.destroy()
            Question9()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root9.destroy()
           Question9()


    Label(root9,text="\n\n\n\n",bg='light blue').pack()
    Button(root9,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root9,text="\n\n",bg='light blue').pack()
    label = Label(root9)
    label.pack()

    root9.mainloop()




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 7 


def Question7():
   
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root8 = Tk()
    root8.geometry("2000x1200")
    root8.configure(bg='light blue')
    root8.title('Question No.7')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root8.destroy()
                resultPage()   
        count()
    label=Label(root8,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var=IntVar()
    Label(root8,text="",bg='light blue').pack()
    Label(root8,text="Question 7",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root8,text="",bg='light blue').pack()
    Label(root8, text="  7) If a is a dictionary with some key-value pairs, what does a.popitem() do?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root8,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root8, text="Removes an arbitrary element", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root8, text="Removes all the key-value pairs", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root8, text="Removes the key-value pair for the key given as an argument", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root8, text="Invalid method for dictionary", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==1):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root8.destroy()
            Question8()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root8.destroy()
           Question8()


    Label(root8,text="\n\n\n\n",bg='light blue').pack()
    Button(root8,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root8,text="\n\n",bg='light blue').pack()
    label = Label(root8)
    label.pack()

    root8.mainloop()




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 6 


def Question6():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root17 = Tk()
    root17.geometry("2000x1200")
    root17.configure(bg='light blue')
    root17.title('Question No.6')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root17.destroy()
                resultPage()   
        count()
    label=Label(root17,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root17,text="",bg='light blue').pack()
    Label(root17,text="Question 6",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root17,text="",bg='light blue').pack()
    Label(root17, text="  6) Which among them is used to create an object?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root17,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root17, text="A class", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root17, text="A function", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root17, text="A method", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root17, text="A constructor", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==4):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root17.destroy()
            Question7()
            
        else:
            
            showinfo("Result","Wrong Answer")
            #con.commit()
            #con1.commit()
            root17.destroy()
            Question7()
            
           
           


    Label(root17,text="\n\n\n\n",bg='light blue').pack()
    Button(root17,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root17,text="\n\n",bg='light blue').pack()
    label = Label(root17)
    label.pack()

    root17.mainloop()




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 5

def Question5():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root6 = Tk()
    root6.geometry("2000x1200")
    root6.configure(bg='light blue')
    root6.title('Question No.5')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root6.destroy()
                resultPage()   
        count()
    label=Label(root6,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root6,text="",bg='light blue').pack()
    Label(root6,text="Question 5",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root6,text="",bg='light blue').pack()
    Label(root6, text="  5) For tuples and list which is correct?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root6,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root6, text="List and tuples both are mutable.", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root6, text="List is mutable whereas tuples are immutable.", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root6, text="List and tuples both are immutable.", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root6, text="List is immutable whereas tuples are mutable.", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==2):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root6.destroy()
            Question6()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root6.destroy()
           Question6()


    Label(root6,text="\n\n\n\n",bg='light blue').pack()
    Button(root6,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root6,text="\n\n",bg='light blue').pack()
    label = Label(root6)
    label.pack()

    root6.mainloop()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 4


def Question4():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root5 = Tk()
    root5.geometry("2000x1200")
    root5.configure(bg='light blue')
    root5.title('Question No.4')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000,count)
            if(counter==0):
                root5.destroy()
                resultPage()   
        count()
    label=Label(root5,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root5,text="",bg='light blue').pack()
    Label(root5,text="Question 4",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root5,text="",bg='light blue').pack()
    Label(root5, text="  4) Which of the following is correct?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root5,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root5, text="An exception is an error that occurs at the runtime.", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root5, text="A syntax error is also an exception.", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root5, text="An exception is used to exclude a block of code in Python.", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root5, text="All of the above.", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==1):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root5.destroy()
            Question5()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root5.destroy()
           Question5()


    Label(root5,text="\n\n\n\n",bg='light blue').pack()
    Button(root5,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root5,text="\n\n",bg='light blue').pack()
    label = Label(root5)
    label.pack()

    root5.mainloop()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 

#Question 3
def Question3():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root4 = Tk()
    root4.geometry("2000x1200")
    root4.configure(bg='light blue')
    root4.title('Question No.3')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root4.destroy()
                resultPage() 
        count()
    label=Label(root4,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root4,text="",bg='light blue').pack()
    Label(root4,text="Question 3",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root4,text="",bg='light blue').pack()
    Label(root4, text="  3) Which one of the following have the same precedence?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root4,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root4, text="Addition and Subtraction", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root4, text="Multiplication and Division", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root4, text="Both Addition and Subtraction and Multiplication and Division", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root4, text="None of the mentioned", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==1):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur1.execute("select * from QuizPortal1")
            cur.execute("select * from QuizPortal")
            print cur.fetchall()
            root4.destroy()
            Question4()
            
        else:
           
           showinfo("Result","Wrong Answer")
           #con.commit()
           #con1.commit()
           root4.destroy()
           Question4()


    Label(root4,text="\n\n\n\n",bg='light blue').pack()
    Button(root4,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root4,text="\n\n",bg='light blue').pack()
    label = Label(root4)
    label.pack()

    root4.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 2

def Question2():
    
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")

    root3 = Tk()
    root3.geometry("2000x1200")
    root3.configure(bg='light blue')
    root3.title('Question No.2')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                root3.destroy()
                resultPage()   
        count()
    label=Label(root3,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root3,text="",bg='light blue').pack()
    Label(root3,text="Question 2",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()

    Label(root3,text="",bg='light blue').pack()
    Label(root3, text=" 2) What is used to define a block of code (body of loop, function etc.) in Python?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root3,text="\n\n",bg='light blue').pack()
    R1 = Radiobutton(root3, text="Curly braces", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root3, text="Parenthesis", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root3, text="Indentation", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root3, text="Quotation", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==3):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur.execute("select * from QuizPortal")
            cur1.execute("select * from QuizPortal1")
            print cur.fetchall()
            root3.destroy()
            Question3()
            
        else:
           
            showinfo("Result","Wrong Answer")
            #con.commit()
            #con1.commit()
            root3.destroy()
            Question3()


    Label(root3,text="\n\n\n\n",bg='light blue').pack()
    Button(root3,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=8,bg='light pink').pack(anchor=S)
    Label(root3,text="\n\n",bg='light blue').pack()
    label = Label(root3)
    label.pack()

    root3.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------# 
#Question 1

def Question1():
    counter=20
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection)

    #cur.execute("create table QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number)")
    
    global root2
    root2 = Tk()
    root2.geometry("2000x1200")
    root2.configure(bg='light blue')
    root2.title('Question No.1')
    counter=20
    def counter_label(label):
        def count():
            global counter
            counter-=1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                resultPage()
        count()
    label=Label(root2,font='Arial 35' ,fg='red')
    label.pack(anchor=N,side='right',padx=10)
    counter_label(label)
    
    var = IntVar()
    Label(root2,text="",bg='light blue').pack()
    Label(root2,text="Question 1",font="Arial 25 bold",justify=CENTER,bg='light blue').pack()



    Label(root2,text="",bg='light blue').pack()
    Label(root2, text="  1) Which of the following statements is true for Python?",font="Arial 25",bg='light blue').pack(anchor=W)
    Label(root2,text="\n\n",bg='light blue').pack()


    
    R1 = Radiobutton(root2, text="Python is a high level programming language.", variable=var, value=1,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root2, text="Python is an interpreted language.", variable=var, value=2,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root2, text="Python is an object-oriented language.", variable=var, value=3,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root2, text="All Of The Above", variable=var, value=4,command=sel,font="Arial 20 ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        cur.execute("select attempted from QuizPortal")
        cur1.execute("select attempted1 from QuizPortal1 where nname1=?",(nname1,))
        att1=cur.fetchone()
        att1=att1[0]
        att1=att1+1
        att2=(att1,)
        cur.execute("update QuizPortal set attempted=?",att2)
        cur1.execute("update QuizPortal1 set attempted1=? where nname1=?",(att1,nname1))
        if(var.get()==4):
            showinfo("Result","Correct Answer")
            Score1=()
            Score2=()
            cur.execute("select score from QuizPortal")
            Score1=cur.fetchone()
            score1=Score1[0]
            score1=score1+1
            Score2=(score1,)
            print score1
            cur.execute("update QuizPortal set score=?",Score2)
            cur1.execute("update QuizPortal1 set score1=? where nname1=?",(score1,nname1))
            #con.commit()
            #con1.commit()
            cur.execute("select * from QuizPortal")
            cur1.execute("select * from QuizPortal1")
            print cur.fetchall()
            root2.destroy()
            Question2()
            
        else:
            showinfo("Result","Wrong Answer")
            root2.destroy()
            
            Question2()


    Label(root2,text="\n\n\n\n",bg='light blue').pack()
    Button(root2,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bd=5,bg='light pink').pack(anchor=S)
    Label(root2,text="\n\n",bg='light blue').pack()
    label = Label(root2)
    label.pack()

    root2.mainloop()




#================================================================TOPICS PAGE===================================================================================================

def Topics():
    def sel():
       selection = "Selected Option: " + str(var.get())
       label.config(text = selection,bg='light blue',font='Arial 15 bold')

    root7 = Tk()
    root7.geometry("2000x1200")
    root7.configure(bg='light blue')
    root7.title('Topics')
 
    var = IntVar()
    Label(root7,text="",bg='light blue').pack()
    Label(root7,text="",bg='light blue').pack()
    Label(root7,text="Select a Topic : ",font="Times 30 bold",justify=LEFT,bg='light blue').pack()

    Label(root7,text="",bg='light blue').pack()
    Label(root7,text="",bg='light blue').pack()

  
    R1 = Radiobutton(root7, text="Full Python", variable=var, value=1,command=sel,font="Times 20 bold",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R2 = Radiobutton(root7, text="Loops/Conditions", variable=var, value=2,command=sel,font="Times 20 bold",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R3 = Radiobutton(root7, text="Functions", variable=var, value=3,command=sel,font="Times 20 bold ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R4 = Radiobutton(root7, text="Class/Objects", variable=var, value=4,command=sel,font="Times 20 bold ",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W)

    R5 = Radiobutton(root7, text="Exception Handling", variable=var, value=5,command=sel,font="Times 20 bold",justify=CENTER,padx=50,activebackground='yellow',cursor='arrow',bg='light blue').pack(anchor=W) 
    
    def calcu():
        att1=()
        att2=()
        cur.execute('select nname from QuizPortal')
        nname1=cur.fetchone()
        nname1=nname1[0]
        nname=(nname1,)
        
        if(var.get()==1):
            cur.execute("update QuizPortal set topic='Full Python'")
            cur1.execute("update QuizPortal1 set topic1='Full Python' where nname1=?",(nname1,))
        if(var.get()==2):
            cur.execute("update QuizPortal set topic='Loops/Conditions'")
            cur1.execute("update QuizPortal1 set topic1='Loops/Conditions' where nname1=?",(nname1,))

        if(var.get()==3):
            cur.execute("update QuizPortal set topic='Functions'")
            cur1.execute("update QuizPortal1 set topic1='Functions' where nname1=?",(nname1,))

        if(var.get()==4):
            cur.execute("update QuizPortal set topic='Class/Objects'")
            cur1.execute("update QuizPortal1 set topic1='Class/Objects' where nname1=?",(nname1,))

        
        if(var.get()==5):
            cur.execute("update QuizPortal set topic='Exception Handling'")
            cur1.execute("update QuizPortal1 set topic1='Exception Handling' where nname1=?",(nname1,))



            
           
        cur1.execute("select * from QuizPortal1")
        cur.execute("select * from QuizPortal")
        print cur.fetchall()
        root7.destroy()
        Question1()

   

    Label(root7,text="\n\n\n\n",bg='light blue').pack()
    Button(root7,text='Submit',command=calcu,font="Arial 20 bold", relief=RAISED,bg='cyan',width=10).pack(anchor=S)
    Label(root7,text="\n\n",bg='light blue').pack()
    label = Label(root7)
    label.pack()

    root7.mainloop()
    





#============================================SIGN UP=======================================================================================================================================

#Sign Up Page:

def SignUp():
    cur1.execute("create table if not exists QuizPortal1(fname1 varchar,lname1 varchar,nname1 varchar, age1 number,dob1 varchar,college1 varchar,score1 number,attempted1 number,topic1 varchar)")
    cur.execute("drop table if exists QuizPortal")
    cur.execute("create table if not exists QuizPortal(fname varchar,lname varchar,nname varchar, age number,dob varchar,college varchar,score number,attempted number,topic varchar)")

    a1='' 
    a2=''
    a3=''
    root1 = Tk()
    root1.geometry("2000x1200")
    root1.configure(bg='light blue')
    root1.title('Sign Up')


    

    Label(root1,text="",bg='light blue').grid(row=1)
    Label(root1,text="   Sign Up Here: ",font="Arial 30 bold",bg='light blue').grid(row=2,column=0)

    var=IntVar
        
    Label(root1,text="",bg='light blue').grid(row=3)
    Label(root1,text="",bg='light blue').grid(row=4)

    Label(root1,text="       Enter First Name: ",font="Times 23",justify=CENTER,bg='light blue').grid(row=5,column=0,sticky=W)
    e1=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e1.grid(row=5,column=1,sticky=W)
    def resete1():
        e1.delete(0,END)
    Button(root1,text="Reset",command=resete1, relief=RAISED,font='Times 15').grid(row=5,column=3,sticky=E)



    Label(root1,text="",bg='light blue').grid(row=6)
    Label(root1,text="",bg='light blue').grid(row=7)



    Label(root1,text="       Enter Last Name:",font="Times 23 ",justify=CENTER,bg='light blue').grid(row=9,column=0,sticky=W)
    e2=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e2.grid(row=9,column=1,sticky=W)
    def resete2():
        e2.delete(0,END)
    Button(root1,text="Reset",command=resete2, relief=RAISED,font='Times 15').grid(row=9,column=3,sticky=E)


    Label(root1,text="",bg='light blue').grid(row=10)
    Label(root1,text="",bg='light blue').grid(row=11)



    Label(root1,text="       Enter Enrollment:",font="Times 23 ",justify=CENTER,bg='light blue').grid(row=13,column=0,sticky=W)
    e3=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e3.grid(row=13,column=1,sticky=W)
    def resete3():
        e3.delete(0,END)
    Button(root1,text="Reset",command=resete3, relief=RAISED,font='Times 15').grid(row=13,column=3,sticky=E)



    Label(root1,text="",bg='light blue').grid(row=14)
    Label(root1,text="",bg='light blue').grid(row=15)



    Label(root1,text="       Enter age: ",font="Times 23",justify=CENTER,bg='light blue').grid(row=17,column=0,sticky=W)
    e4=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e4.grid(row=17,column=1,sticky=W)
    def resete4():
        e4.delete(0,END)
    Button(root1,text="Reset",command=resete4,font='Times 15', relief=RAISED).grid(row=17,column=3,sticky=E)




    Label(root1,text="",bg='light blue').grid(row=18)
    Label(root1,text="",bg='light blue').grid(row=19)



    Label(root1,text="    Enter Date of Birth: ",font="Times 23",justify=CENTER,bg='light blue').grid(row=21,column=0,sticky=W)
    e5=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e5.grid(row=21,column=1,sticky=W)
    def resete5():
        e5.delete(0,END)
    Button(root1,text="Reset",command=resete5,font='Times 15', relief=RAISED).grid(row=21,column=3,sticky=E)



    Label(root1,text="",bg='light blue').grid(row=22)
    Label(root1,text="",bg='light blue').grid(row=23)



    Label(root1,text="    Enter College Name:",font="Times 23 ",justify=CENTER,bg='light blue').grid(row=25,column=0,sticky=W)
    e6=Entry(font="Times 23 ",justify=CENTER,bd=4)
    e6.grid(row=25,column=1,sticky=W)
    def resete6():
        e6.delete(0,END)
    Button(root1,text="Reset",command=resete6,font='Times 15',relief=RAISED).grid(row=25,column=3,sticky=E)



        
    def reset():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)    
    def insert():
        a1=str(e1.get())
        a2=str(e2.get())
        a3=str(e3.get())
        a4=int(e4.get())
        a5=str(e5.get())
        a6=str(e6.get())
        q=(a1,a2,a3,a4,a5,a6)
        cur1.execute("insert into QuizPortal1 values(?,?,?,?,?,?,0,0,'')",q)
        cur.execute("insert into QuizPortal values(?,?,?,?,?,?,0,0,'')",q)
    def signup():
        insert()
        #con.commit()
        #con1.commit()
        root1.destroy()
        Topics()
        
    Label(root1,text="",bg='light blue').grid(row=26)
    Label(root1,text="",bg='light blue').grid(row=27)
    Button(root1,text="Reset All",command=reset,font='Times 17 bold', relief=RAISED,bg='orange',width=10).grid(row=28,column=0,sticky=E)
    Button(root1,text="Sign Up",font='Times 17 bold',command=signup, relief=RAISED,bg='orange',width=10).grid(row=28,column=3,sticky=W)

    root1.mainloop()





#=================================================================HOME SCREEN====================================================================================================================


root = Tk()
root.geometry("1200x1200")
root.title('Welcome to Quiz Portal')
var = IntVar()
root.configure(bg='light blue')
Label(root,text="\n\n\n\n",bg='light blue').place(x=500,y=0)
Label(root,text="\n\n\n\n",bg='light blue').place(x=2,y=0)

pic=PhotoImage(file='ss.gif')
Label(root,image=pic).place(x=0,y=0)

Label(root,text="  Welcome  to  Quiz  Portal  ",font='helvectica 50 bold').place(x=200,y=200)

def fun():
    root.destroy()
    SignUp()
    
def func():
    root.destroy()
def func2():
    root.destroy()
    newResultPage()

#Label(root,text="\n\n\n\n").place(x=200,y=300)


Button(root,text='Fetch Result',command =func2, font='Arial 20 bold',relief=RAISED,bd=3,width=11,bg='yellow',highlightcolor='blue').place(x=250,y=400)
Button(root,text='Start Quiz',font='Arial 20 bold',command = fun, relief=RAISED,bd=3,width=10,bg='green').place(x=550,y=400)
Button(root,text='Exit',command = func, font='Arial 20 bold',relief=RAISED,bd=3,width=10,bg='red').place(x=850,y=400)



#created by:
'''Label(root,text="\n\n\n\n").place(x=7,y=0)
Label(root,text="\n\n\n\n").place(x=8,y=0)
Label(root,text="\n\n\n\n").place(x=9,y=0)'''


Label(root, text="  Created by Sakshi Saxena",font="Times 12").place(x=0,y=0)

root.mainloop()


#===========================================================================END OF PROJECT=================================================================================================================================================================================================
