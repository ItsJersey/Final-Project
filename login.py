from tkinter import *
from PIL import ImageTk  #Install pip install pillow for jpg images
import mysql.connector
from tkinter import messagebox

#Function

def signup():
    login.destroy()
    import signup
def hide():
    openeye.config(file='closedeye.png')
    passEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if userEntry.get()=='Username':
     userEntry.delete(0,END)
def pass_enter(event):
    if passEntry.get()=='Password':
     passEntry.delete(0,END)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        database="exampledb",
        password=""
    )
    cursor = conn.cursor()
except mysql.connector.Error as e:
    print("Error connecting to the database:", e)

def get_GUI2():
    entered_username = userEntry.get()
    entered_password = passEntry.get()
    
    try:
        query = "SELECT * FROM tb_accounts WHERE username = %s"
        cursor.execute(query, (entered_username,))
        tb_accounts = cursor.fetchone()
        
        if tb_accounts:
            stored_password = tb_accounts[3]
            if entered_password == stored_password:
                login.destroy()
                import GUI2
            else:
                messagebox.showinfo(title="Failed", message="Failed Login. Wrong Password")
        else:
            messagebox.showinfo(title="Failed", message="Failed Login. Wrong Username")
    except mysql.connector.Error as e:
        print("Error executing query", e)

#GUI
login=Tk()
login.resizable(0,0)#no more maximize haha
login.title('Login TinyShot')

bgIntro=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login,image=bgIntro)
bgLabel.pack()

title=Label(login,text='Tiny Shot',font=('Arial',25,'bold')
            ,bg='cyan4',fg='white')
title.place(x=205,y=200)

heading=Label(login,text='USER LOGIN',font=('Salina',26,'bold')
              ,bg='white',fg='dark violet')
heading.place(x=580,y=120)#place for fixing x,y

userEntry=Entry(login,width=25,font=('Arial',12,'bold')
                ,bd=0,fg='deepskyblue4')
userEntry.place(x=550,y=200)
userEntry.insert(0,'Username')

userEntry.bind('<FocusIn>',user_enter)#Clicking inside the entry field

frame2=Frame(login,width=250,height=2,bg='deepskyblue4')
frame2.place(x=550,y=282)

passEntry=Entry(login,width=25,font=('Arial',12,'bold')
                ,bd=0,fg='deepskyblue4')
passEntry.place(x=550,y=260)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_enter)

frame2=Frame(login,width=250,height=2,bg='deepskyblue4')
frame2.place(x=550,y=222)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login,image=openeye, bd=0, bg='white',activebackground='white',command=hide)
eyeButton.place(x=775,y=255)


forgotButton=Button(login,text='Forget Password?', bd=0, bg='white',activebackground='white',font=('Arial',10,'bold')
                ,fg='deepskyblue4')
forgotButton.place(x=685,y=285)

logButton=Button(login,text='Login', bd=0, bg='deepskyblue4',activebackground='white',width=15,font=('Arial',20,'bold')
                ,fg='white', command=get_GUI2)
logButton.place(x=545,y=330)

bindacc=Label(login,text='-------------- Or Use ------------', bd=0, bg='white',activebackground='deepskyblue4',font=('Arial',15,'bold')
                ,fg='deepskyblue4')
bindacc.place(x=540,y=410)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login,image=facebook_logo,bg='white')
fbLabel.place(x=600,y=440)

google_logo=PhotoImage(file='google.png')
gLabel=Label(login,image=google_logo,bg='white')
gLabel.place(x=660,y=440)


twit_logo=PhotoImage(file='twitter.png')
twitLabel=Label(login,image=twit_logo,bg='white')
twitLabel.place(x=720,y=440)

noacc=Label(login,text='Dont have an account?', bd=0, bg='white',activebackground='deepskyblue4',font=('Arial',10,'bold')
                ,fg='deepskyblue4')
noacc.place(x=540,y=500)

createButton=Button(login,text='Create Account', bd=0, bg='white',activebackground='dark violet',font=('Arial',10,'bold underline')
                ,fg='dark violet',command=signup)
createButton.place(x=690,y=497)


login.mainloop()