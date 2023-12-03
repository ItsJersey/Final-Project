import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import mysql.connector
from PIL import Image, ImageTk

root = Tk()
root.geometry("1300x550")
root.title("TinyShot")
root.configure(background='cyan4')






# Another Window for Adding Data
class AddWindow(tk.Toplevel):
    def __init__(self, root):
        def check_changed():
            if self.check_var.get() == 1:
                self.booster_combobox.config(state='enabled')
                self.booster_schedule_calendar.config(state='enabled')
            else:
                self.booster_combobox.config(state='disabled')
                self.booster_schedule_calendar.config(state='disabled')

        def add():
            added_first_name = self.first_name_entry.get()
            added_last_name = self.last_name_entry.get()
            added_sex = self.sex_combobox.get()
            added_vaccine = self.vaccine_combobox.get()
            selected_booster_date = self.booster_schedule_calendar.get()
            selected_date = self.vaccine_schedule_calendar.get_date()
            added_booster = self.booster_combobox.get() if self.check_var.get() else "None"
            added_vaccine_schedule = selected_date
            added_booster_schedule = selected_booster_date if selected_booster_date and self.check_var.get() else "None"

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="exampledb",
                    password=""
                )
                cursor = conn.cursor()
                add_query = "INSERT INTO tb_users (first_name, last_name, sex, vaccine, booster_shot, vaccine_schedule, booster_schedule) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(add_query, (added_first_name, added_last_name, added_sex, added_vaccine, added_booster, added_vaccine_schedule, added_booster_schedule))
                conn.commit()
                messagebox.showinfo(title="Success", message="Table updated successfully")
                self.destroy()
            except mysql.connector.Error as e:
                print("Error executing query:", e)
            finally:
                cursor.close()
                conn.close()


        def destroy_self():
            self.destroy()




        tk.Toplevel.__init__(self, root)
        self.title("Add Window")
        self.geometry("600x600")
        self.configure(bg='#31363b')


        bg_image = ImageTk.PhotoImage(Image.open("bg2.jpg"))

        self.mainframe = Frame(self)
        self.mainframe.pack(padx=10, pady=5)
        self.mainframe.place(relx=0.5, rely=0.5, anchor="center")

        bg_label = Label(self.mainframe, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relx=0.5, rely=0.5, anchor="center")

        self.user_info_frame = LabelFrame(self.mainframe, text="User Information", font=('Arial', '9', 'bold'),
                                          bg='cyan4', fg='white')
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=5, sticky="news")




        self.first_name_label = Label(self.user_info_frame, text="First Name", font=('Arial', '12', 'bold'),
                                      bg='cyan4', fg='white')
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)

        self.last_name_label = Label(self.user_info_frame, text="Last Name", font=('Arial', '12', 'bold'),
                                     bg='cyan4', fg='white')
        self.last_name_label.grid(row=0, column=1)
        self.last_name_entry = Entry(self.user_info_frame)
        self.last_name_entry.grid(row=1, column=1)

        self.sex_label = Label(self.user_info_frame, text="Sex", font=('Arial', '12', 'bold'),
                               bg='cyan4', fg='white')
        self.sex_label.grid(row=0, column=2)
        self.sex_combobox = ttk.Combobox(self.user_info_frame, values=["Male", "Female"])
        self.sex_combobox.grid(row=1, column=2)

        # Every widget in user_info_frame will have a padding
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.medicine_info_frame = LabelFrame(self.mainframe, text="Medicine Information", font=('Arial', '9', 'bold'), bg='cyan4', fg='white')
        self.medicine_info_frame.grid(row=1, column=0, padx=20, pady=5, sticky="news")
        self.vaccine_label = Label(self.medicine_info_frame, text="Vaccine", font=('Arial', '12', 'bold'), bg='cyan4', fg='white')
        self.vaccine_label.grid(row=0, column=0)
        self.vaccine_combobox = ttk.Combobox(self.medicine_info_frame, values=["Pfizer", "Moderna", "Sinovac"])
        self.vaccine_combobox.grid(row=1, column=0)

        self.check_var = IntVar()
        self.booster_checkbutton = Checkbutton(self.medicine_info_frame, text="Booster Shot", variable=self.check_var, command=check_changed, font=('Arial', '9', 'bold'), bg='cyan4', fg='white')
        self.booster_checkbutton.grid(row=1, column=1)

        self.booster_label = Label(self.medicine_info_frame, text="Booster Shot", font=('Arial', '12', 'bold'), bg='cyan4', fg='white')
        self.booster_label.grid(row=0, column=2)
        self.booster_combobox = ttk.Combobox(self.medicine_info_frame, state='disabled', values=["None", "Pfizer", "Moderna"])
        self.booster_combobox.grid(row=1, column=2)

        for widget in self.medicine_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.date_info_frame = LabelFrame(self.mainframe, text="Date Information", font=('Arial', '9', 'bold'), bg='cyan4', fg='white')
        self.date_info_frame.grid(row=2, column=0, padx=20, pady=5)

        self.vaccine_schedule_label = Label(self.date_info_frame, text="Vaccine Date", font=('Arial', '12', 'bold'), bg='cyan4', fg='white')
        self.vaccine_schedule_label.grid(row=0, column=0)
        self.vaccine_schedule_calendar = DateEntry(self.date_info_frame)
        self.vaccine_schedule_calendar.grid(row=0, column=1)

        self.booster_schedule_label = Label(self.date_info_frame, text="Booster Schedule", font=('Arial', '12', 'bold'), bg='cyan4', fg='white')
        self.booster_schedule_label.grid(row=1, column=0)
        self.booster_schedule_calendar = DateEntry(self.date_info_frame, state='disabled')
        self.booster_schedule_calendar.grid(row=1, column=1)

        for widget in self.date_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.update_button = Button(self.mainframe, text="Update Data", command=add, font=('Arial', '9', 'bold'), bg='deepskyblue4', fg='white')
        self.update_button.grid(row=3, column=0, padx=20, pady=5, sticky="news")
        self.view_button = Button(self.mainframe, text="View Tables", command=destroy_self, font=('Arial', '9', 'bold'), bg='deepskyblue4', fg='white')
        self.view_button.grid(row=4, column=0, padx=20, pady=5, sticky="news")













# Connecting to the database
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


# Another Window for Updating the data
class UpdateWindow(tk.Toplevel):
    def __init__(self, root, selected_item):
        def check_changed():
            if self.check_var.get() == 1:
                self.booster_combobox.config(state='enabled')
                self.booster_schedule_calendar.config(state='enabled')
            else:
                self.booster_combobox.config(state='disabled')
                self.booster_schedule_calendar.config(state='disabled')

        def update_data():
            updated_first_name = self.first_name_entry.get()
            updated_last_name = self.last_name_entry.get()
            updated_sex = self.sex_combobox.get()
            updated_vaccine = self.vaccine_combobox.get()
            updated_booster = self.booster_combobox.get() if self.check_var.get() else "None"
            updated_vaccine_schedule = self.vaccine_schedule_calendar.get_date()
            updated_booster_schedule = (
                self.booster_schedule_calendar.get_date() if self.check_var.get() else "None"
            )

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="exampledb",
                    password=""
                )
                cursor = conn.cursor()
                update_query = """
                    UPDATE tb_users
                    SET first_name = %s, last_name = %s, sex = %s, vaccine = %s, booster_shot = %s, vaccine_schedule = %s, booster_schedule = %s
                    WHERE Patient_Number = %s
                """
                cursor.execute(update_query, (
                    updated_first_name, updated_last_name, updated_sex, updated_vaccine, updated_booster,
                    updated_vaccine_schedule, updated_booster_schedule, self.primary_key))
                conn.commit()
                messagebox.showinfo(title="Success", message="Data updated successfully")
                self.destroy()
            except mysql.connector.Error as e:
                print("Error executing query:", e)
            finally:
                cursor.close()
                conn.close()

        def destroy_self():
            self.destroy()




        tk.Toplevel.__init__(self, root)
        self.title("Update Window")
        self.geometry("600x600")
        self.configure(bg='cyan4')

        self.primary_key = selected_item[0]
        self.first_name = selected_item[1]
        self.last_name = selected_item[2]
        self.sex = selected_item[3]
        self.vaccine = selected_item[4]
        self.booster_shot = selected_item[5]
        self.vaccine_schedule = selected_item[6]
        self.booster_schedule = selected_item[7]

        self.mainframe = Frame(self)
        self.mainframe.pack(padx=10, pady=5)
        self.mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.user_info_frame = LabelFrame(self.mainframe, text="User Information",font=('Arial','9','bold')
            ,bg='deepskyblue4',fg='white')
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=5)

        self.first_name_label = Label(self.user_info_frame, text="First Name")
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)

        self.last_name_label = Label(self.user_info_frame, text="Last Name")
        self.last_name_label.grid(row=0, column=1)
        self.last_name_entry = Entry(self.user_info_frame)
        self.last_name_entry.grid(row=1, column=1)

        self.sex_label = Label(self.user_info_frame, text="Sex")
        self.sex_label.grid(row=0, column=2)
        self.sex_combobox = ttk.Combobox(self.user_info_frame, values=["Male", "Female"])
        self.sex_combobox.grid(row=1, column=2)

        # Every widget in user_info_frame will have a padding
        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.medicine_info_frame = LabelFrame(self.mainframe, text="Medicine Information")
        self.medicine_info_frame.grid(row=1, column=0, padx=20, pady=5, sticky="news")
        self.vaccine_label = Label(self.medicine_info_frame, text="Vaccine")
        self.vaccine_label.grid(row=0, column=0)
        self.vaccine_combobox = ttk.Combobox(self.medicine_info_frame, values=["Pfizer", "Moderna", "Sinovac"])
        self.vaccine_combobox.grid(row=1, column=0)

        self.check_var = IntVar()
        self.booster_checkbutton = Checkbutton(self.medicine_info_frame, text="Booster Shot", variable=self.check_var, command=check_changed)
        self.booster_checkbutton.grid(row=1, column=1)

        self.booster_label = Label(self.medicine_info_frame, text="Booster Shot")
        self.booster_label.grid(row=0, column=2)
        self.booster_combobox = ttk.Combobox(self.medicine_info_frame, state='disabled', values=["None", "Pfizer", "Moderna"])
        self.booster_combobox.grid(row=1, column=2)

        for widget in self.medicine_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.date_info_frame = LabelFrame(self.mainframe, text="Date Information")
        self.date_info_frame.grid(row=2, column=0, padx=20, pady=5)

        self.vaccine_schedule_label = Label(self.date_info_frame, text="Vaccine Date")
        self.vaccine_schedule_label.grid(row=0, column=0)
        self.vaccine_schedule_calendar = DateEntry(self.date_info_frame)
        self.vaccine_schedule_calendar.grid(row=0, column=1)

        self.booster_schedule_label = Label(self.date_info_frame, text="Booster Schedule")
        self.booster_schedule_label.grid(row=1, column=0)
        self.booster_schedule_calendar = DateEntry(self.date_info_frame, state='disabled')
        self.booster_schedule_calendar.grid(row=1, column=1)

        for widget in self.date_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.update_button = Button(self.mainframe, text="Update Data", command=update_data)
        self.update_button.grid(row=3, column=0, padx=20, pady=5, sticky="news")
        self.view_button = Button(self.mainframe, text="View Tables", command=destroy_self)
        self.view_button.grid(row=4, column=0, padx=20, pady=5, sticky="news")

# Show the data on the table
def fetch_data():
    exampledb = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'exampledb',
    }
    try:
        connection = mysql.connector.connect(**exampledb)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_users")
        data = cursor.fetchall()

        # Clear any previous data in the table
        for row in tree_view.get_children():
            tree_view.delete(row)
        # Insert the fetched data into the table
        for row in data:
            tree_view.insert('', 'end', values=row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def search_database():
    search_query = search_entry.get()
    gender_filter = gender_combobox.get()

    # Connect to the SQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="exampledb"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM tb_users WHERE first_name LIKE %s OR last_name LIKE %s"
    cursor.execute(query, ("%" + search_query + "%", "%" + search_query + "%"))

    results = cursor.fetchall()





    #Gender Filtering
    if gender_filter == "All":
        query = "SELECT * FROM tb_users WHERE first_name LIKE %s OR last_name LIKE %s"
        cursor.execute(query, ("%" + search_query + "%", "%" + search_query + "%"))
    else:
        query = "SELECT * FROM tb_users WHERE (first_name LIKE %s OR last_name LIKE %s) AND sex = %s"
        cursor.execute(query, ("%" + search_query + "%", "%" + search_query + "%", gender_filter))

    results = cursor.fetchall()





    # Clear any previous search
    for row in result_tree_view.get_children():
        result_tree_view.delete(row)
    if results:
        for row in results:
            result_tree_view.insert('', END, values=row)

    conn.close()


def delete_row():
    selected_item = tree_view.selection()
    if not selected_item:
        messagebox.showinfo(title="Failed", message="Please select a row to delete")

    # First column ID get
    primary_key = tree_view.item(selected_item, "values")[0]

    # Delete the row
    delete_query = f"DELETE FROM tb_users WHERE Patient_Number = {primary_key}"
    cursor.execute(delete_query)
    conn.commit()

    # Update the tree
    fetch_data()


def update_row():
    selected_item = tree_view.selection()
    if not selected_item:
        messagebox.showinfo(title="Failed", message="Please select a row to update")
        return
    UpdateWindow(root, tree_view.item(selected_item, "values"))


def get_GUI2():
    root.destroy()
    import GUI2


Mainframe = Frame(root, bg='#31363b')
Mainframe.pack(padx=10, pady=10)
Mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)

tree_view_frame = LabelFrame(Mainframe, text="Patient Information",font=('Arial','9','bold')
            ,bg='deepskyblue4',fg='white')
tree_view_frame.grid(row=0, column=1, padx=10, pady=5, sticky="news")

tree_view = ttk.Treeview(tree_view_frame,show='headings',
                         columns=["id", "first_name", "last_name", "sex", "vaccine", "booster_shot", "vaccine_schedule",
                                  "booster_schedule"])
tree_view.heading("#1", text="ID")
tree_view.heading("#2", text="First Name")
tree_view.heading("#3", text="Last Name")
tree_view.heading("#4", text="Sex")
tree_view.heading("#5", text="Vaccine")
tree_view.heading("#6", text="Booster Shot")
tree_view.heading("#7", text="Vaccine Schedule")
tree_view.heading("#8", text="Booster Schedule")

tree_view.column("id", width=100)
tree_view.column("first_name", width=100)
tree_view.column("last_name", width=100)
tree_view.column("sex", width=100)
tree_view.column("vaccine", width=100)
tree_view.column("booster_shot", width=100)
tree_view.column("vaccine_schedule", width=100)
tree_view.column("booster_schedule", width=100)
tree_view.grid(row=0, column=0, padx=10, pady=5)

result_tree_view_frame = LabelFrame(Mainframe, text="Search Results",font=('Arial','9','bold')
            ,bg='deepskyblue4',fg='white')
result_tree_view_frame.grid(row=1, column=1, padx=10, pady=5, sticky="news")

result_tree_view = ttk.Treeview(result_tree_view_frame,show='headings',columns=(
"ID", "First Name", "Last Name", "Sex", "Vaccine", "Booster Shot", "Vaccine Schedule", "Booster Schedule"))
result_tree_view.heading("#1", text="ID")
result_tree_view.heading("#2", text="First Name")
result_tree_view.heading("#3", text="Last Name")
result_tree_view.heading("#4", text="Sex")
result_tree_view.heading("#5", text="Vaccine")
result_tree_view.heading("#6", text="Booster Shot")
result_tree_view.heading("#7", text="Vaccine Schedule")
result_tree_view.heading("#8", text="Booster Schedule")
result_tree_view.grid(row=0, column=0, padx=10, pady=5, sticky="news")

for col in result_tree_view["columns"]:
    result_tree_view.column(col, width=100, anchor=W, stretch=True)

search_frame = LabelFrame(Mainframe, text="Search",font=('Arial','9','bold') ,bg='deepskyblue4',fg='white')
search_frame.grid(row=0, column=0, padx=10, pady=5, sticky="news")




#Gender filtering
search_entry = Entry(search_frame)
search_entry.grid(row=0, column=0, padx=10, pady=5)

gender_combobox_label = Label(search_frame, font=('Arial', '9', 'bold'), bg='deepskyblue4', fg='white')
gender_combobox_label.grid(row=0, column=1, padx=10, pady=5)

gender_combobox = ttk.Combobox(search_frame, values=["All", "Male", "Female"])
gender_combobox.grid(row=0, column=2, padx=10, pady=5)
gender_combobox.set("All")


#Search button for both name and gender
search_button = Button(search_frame, text="Search", command=search_database,font=('Arial','9','bold') ,bg='cyan4',fg='white')
search_button.grid(row=0, column=3, padx=10, pady=5)




def add_data():
    add_window = AddWindow(root.master)
add_button = Button(search_frame, text="Add", command=add_data,font=('Arial','9','bold') ,bg='cyan4',fg='white')
add_button.grid(row=6, column=0, padx=10, pady=5, sticky="news")




view_button = Button(search_frame, text="View Tables", command=fetch_data,font=('Arial','9','bold') ,bg='cyan4',fg='white')
view_button.grid(row=5, column=0, padx=10, pady=5, sticky="news")

delete_button = Button(search_frame, text="Delete", command=delete_row,font=('Arial','9','bold') ,bg='cyan4',fg='white')
delete_button.grid(row=3, column=0, padx=10, pady=5, sticky="news")

update_button = Button(search_frame, text="Update", command=update_row,font=('Arial','9','bold') ,bg='cyan4',fg='white')
update_button.grid(row=2, column=0, padx=10, pady=5, sticky="news")

root.mainloop()
