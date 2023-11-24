from tkinter import *
from PIL import ImageTk#Install pip install pillow for jpg images
from tkinter import messagebox
import mysql.connector
#pip install pymsl


#function

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
    
    
def connect_database():
    if emailEntry.get()=='' or userEntry.get()==''or passEntry.get()=='' or confirmEntry.get()=='':
      messagebox.showerror('Error','Please Input Email')# message pag dinag input lalabas to
    elif passEntry.get() != confirmEntry.get():
      messagebox.showerror('Error','Password does not match')
    elif yncheck.get()==0:
      messagebox.showerror('Error','Please check terms and conditions')#ari 0 and 1 para dun sa check box para malaman nyaa kung nakacheck or not
    else:
        try:
          email_account = emailEntry.get()
          username = userEntry.get()
          password = passEntry.get()
          confirm_password = confirmEntry.get()
          
          query = "INSERT INTO tb_accounts (email_account, username, password, confirm_password) VALUES (%s, %s, %s, %s)"
          cursor.execute(query, (email_account, username, password, confirm_password))
          conn.commit()
        except mysql.connector.Error as e:
          print("Error executing query", e)
          

          
def login():
    signup.destroy()
    import login



#gui
signup=Tk()
signup.title('Sign up TinyShot')
signup.resizable(False,False)
bgImage=ImageTk.PhotoImage(file='background.jpg')

bgLabel=Label(signup,image=bgImage)
bgLabel.grid()

frame=Frame(signup,bg='white')
frame.place(x=500,y=95)

heading=Label(frame,text='SIGN UP TINYSHOT',font=('Salina',19,'bold')
              ,bg='white',fg='dark violet')
heading.grid(row=0,column=0,padx=10,pady=10)#place for fixing x,y

emailLabel=Label(frame,text='Email',font=('Salina',10,'bold')
                 ,bg='white',fg='deepskyblue4')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))#sticky para sa pag lipat like w s n

emailEntry=Entry(frame,width=35,font=('salina',10,'bold')
                 ,fg='white',bg='deepskyblue4')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

userLabel=Label(frame,text='Username',font=('Salina',10,'bold')
                 ,bg='white',fg='deepskyblue4')
userLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))#sticky para sa pag lipat like w s n

userEntry=Entry(frame,width=35,font=('salina',10,'bold')
                 ,fg='white',bg='deepskyblue4')
userEntry.grid(row=4,column=0,sticky='w',padx=25)

passLabel=Label(frame,text='Password',font=('Salina',10,'bold')
                 ,bg='white',fg='deepskyblue4')
passLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))#sticky para sa pag lipat like w s n

passEntry=Entry(frame,width=35,font=('salina',10,'bold')
                 ,fg='white',bg='deepskyblue4')
passEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Salina',10,'bold')
                 ,bg='white',fg='deepskyblue4')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))#sticky para sa pag lipat like w s n

confirmEntry=Entry(frame,width=35,font=('salina',10,'bold')
                 ,fg='white',bg='deepskyblue4')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

yncheck = IntVar()#like 0 and 1 para malaman kung nakacheck na or inde pa
check=Checkbutton(frame,text='I agree to the terms and conditions',font=('salina',10,'bold')
                  ,bg='white',variable=yncheck)
check.grid(row=9,column=0,padx=15,pady=10)

signButton=Button(frame,text='Signup',font=('salina',15,'bold'),bd=0,fg='white',bg='deepskyblue4'
                  ,width=15,activeforeground='deepskyblue4',activebackground='white',command=connect_database)
signButton.grid(row=10,column=0,padx=10)

askLabel=Label(frame,text='Do you already have an account?',font=('Salina',8,'bold')
                 ,bg='white',fg='deepskyblue4')
askLabel.grid(row=11,column=0,sticky='w',padx=20,pady=20)#sticky para sa pag lipat like w s n

loginButton=Button(frame,text='Login',font=('salina',8,'bold underline'),bd=0,fg='dark violet',bg='white'
                  ,activeforeground='deepskyblue4',activebackground='white',command=login)
loginButton.place(x=200,y=367)



signup.mainloop()