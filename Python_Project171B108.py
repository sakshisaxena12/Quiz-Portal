from Tkinter import *
s=Tk()
s.geometry('2000x1200')
s.title('Quiz Portal')
s.configure(bg='wheat')
img1=PhotoImage(file='sakshi1.gif')
lb=Label(s,image=img1)
Label(s,text='WELCOME TO QUIZ PORTAL:',font='Times 40 bold',bg='wheat').place(x=350,y=0)

def fun(e=0):
      
      s.destroy()
      import MY_QUIZ_PORTAL 
      
lb.after(5000,fun)
lb.place(x=500,y=100)


Label(s,text='Name: SAKSHI SAXENA ',font='Times 20 bold',bg='wheat',justify=CENTER).place(x=500,y=500)
Label(s,text='Enrollment No.: 171B108',font='Times 20 bold',bg='wheat',justify=CENTER).place(x=490,y=530)
Label(s,text=' Phone No.: +91 6261224379',font='Times 20 bold',bg='wheat',justify=CENTER).place(x=470,y=560)
Label(s,text='Email: sakshi.saxena120@gmail.com',font='Times 20 bold',bg='wheat',justify=CENTER).place(x=450,y=590)

s.mainloop()
