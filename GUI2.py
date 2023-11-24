import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import mysql.connector
from PIL import Image, ImageTk
root = Tk()

root.geometry("600x600")
root.title("TinyShot")

root.configure(background='#31363b')

frame = Frame(root)
frame.pack(padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

bgimage = ImageTk.PhotoImage(Image.open("bg2.jpg"))
bglabel = Label(frame, image=bgimage)
bglabel.place(relx=0.5, rely=0.5, anchor=CENTER)

# Verifies if the booster checkbutton is checked or not
def check_changed():
    if check_var.get() == 1:
        booster_combobox.config(state='enabled')
        booster_schedule_calendar.config(state='enabled')
    else:
        booster_combobox.config(state='disabled')
        booster_schedule_calendar.config(state='disabled')

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

# What happens when you click the enter button
def get_data():
    try:
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        sex = sex_combobox.get()
        vaccine = vaccine_combobox.get()
        booster_shot = booster_combobox.get() if check_var.get() else "None"
        vaccine_schedule = vaccine_schedule_calendar.get_date()
        booster_schedule = booster_schedule_calendar.get_date() if check_var.get() else "None"
        
        query = "INSERT INTO tb_users (first_name, last_name, sex, vaccine, booster_shot, vaccine_schedule, booster_schedule) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, sex, vaccine, booster_shot, vaccine_schedule, booster_schedule))
        conn.commit()
        
        # Clear the entry fields after a successful insertion
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        sex_combobox.set("")  # Set to an appropriate default value
        vaccine_combobox.set("")  # Set to an appropriate default value
        booster_combobox.set("")  # Set to an appropriate default value
        vaccine_schedule_calendar.set_date(None)
        booster_schedule_calendar.set_date(None)
        
    except mysql.connector.Error as e:
        print("Error executing query:", e)
        
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)


def page3():
    root.destroy()
    import decoyguiy3

# User Info and first Frame
user_info_frame = LabelFrame(frame, text="User Information", font=('Arial','9','bold') ,bg='cyan4',fg='white')
user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="news")


first_name_label = Label(user_info_frame, text="First Name", font=('Arial','12','bold') ,bg='cyan4',fg='white')
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text="Last Name", font=('Arial','12','bold') ,bg='cyan4',fg='white')
last_name_label.grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

sex_label = Label(user_info_frame, text="Sex", font=('Arial','12','bold') ,bg='cyan4',fg='white')
sex_label.grid(row=0, column=2)
sex_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female"], width=7)
sex_combobox.grid(row=1, column=2)

# Every widget in user_info_frame will have a padding
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Medicine Info and second Frame
medicine_info_frame = LabelFrame(frame, text="Medicine Information", font=('Arial','9','bold') ,bg='cyan4',fg='white')
medicine_info_frame.grid(row=1, column=0, padx=20, pady=10, sticky="news")

vaccine_label = Label(medicine_info_frame, text="Vaccine", font=('Arial','12','bold') ,bg='cyan4',fg='white')
vaccine_label.grid(row=0, column=0)
vaccine_combobox = ttk.Combobox(medicine_info_frame, values=["Pfizer", "Moderna", "Sinovac"])
vaccine_combobox.grid(row=1, column=0)

booster_label= Label(medicine_info_frame, text="Booster Shot", font=('Arial','12','bold') ,bg='cyan4',fg='white')
booster_label.grid(row=0, column=2)
booster_combobox = ttk.Combobox(medicine_info_frame, state='disabled', values=["None", "Pfizer", "Moderna"])
booster_combobox.grid(row=1, column=2)

# Enables the booster combobox if checked
check_var = IntVar()
booster_checkbutton = Checkbutton(medicine_info_frame, text="Booster Shot", variable=check_var, command=check_changed, font=('Arial','9','bold') ,bg='cyan4',fg='white')
booster_checkbutton.grid(row=1, column=1)

# Every widget in medicine_info_frame will have a padding
for widget in medicine_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Date Info and third Frame
date_info_frame = LabelFrame(frame, text="Date Information", font=('Arial','9','bold') ,bg='cyan4',fg='white')
date_info_frame.grid(row=2, column=0, padx=20, pady=10, sticky="news")

vaccine_schedule_label = Label(date_info_frame, text="Vaccine Date", font=('Arial','12','bold') ,bg='cyan4',fg='white')
vaccine_schedule_label.grid(row=0, column=0)
vaccine_schedule_calendar = DateEntry(date_info_frame)
vaccine_schedule_calendar.grid(row=0, column=1)

booster_schedule_label = Label(date_info_frame, text="Booster Date", font=('Arial','12','bold') ,bg='cyan4',fg='white')
booster_schedule_label.grid(row=1, column=0)
booster_schedule_calendar = DateEntry(date_info_frame, state='disabled')
booster_schedule_calendar.grid(row=1, column=1)

# Every widget in date_info_frame will have a padding
for widget in date_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Button and fourth Frame

enter_button = Button(frame, text="Enter Data", command=get_data, font=('Arial','9','bold'), bg='deepskyblue4',fg='white')
enter_button.grid(row=3, column=0, padx=20, pady=10, sticky="news")
view_button = Button(frame, text="View Tables", command=page3, font=('Arial','9','bold'), bg='deepskyblue4',fg='white')
view_button.grid(row=4, column=0, padx=20, pady=10, sticky="news")


root.mainloop()