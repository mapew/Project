import sqlite3
import tkinter
import tkinter.messagebox
import re

class Createnewid():
    def __init__(self):
        self.window_new_emp = tkinter.Tk()
        self.window_new_emp.geometry("350x350")
        self.window_new_emp.title("New Employee ID")

        self.label_f_name = tkinter.Label(self.window_new_emp,text = "First Name")
        self.label_L_name = tkinter.Label(self.window_new_emp,text = "Last Name")
        self.Label_phon = tkinter.Label(self.window_new_emp,text = "Phone Number")
        self.Label_dob = tkinter.Label(self.window_new_emp,text = "Date of Birth ")
        self.Label_email = tkinter.Label(self.window_new_emp,text = "email")
        self.Label_password = tkinter.Label(self.window_new_emp,text = "Password")

        self.txt_f_name = tkinter.Entry(self.window_new_emp)
        self.txt_L_name = tkinter.Entry(self.window_new_emp)
        self.txt_phon = tkinter.Entry(self.window_new_emp)
        self.txt_dob = tkinter.Entry(self.window_new_emp)
        self.txt_email = tkinter.Entry(self.window_new_emp)
        self.txt_password = tkinter.Entry(self.window_new_emp)

        self.button_submit = tkinter.Button(self.window_new_emp, text="Submit",command=self.add_new_Emp)

        self.label_f_name.pack()
        self.txt_f_name.pack()

        self.label_L_name.pack()
        self.txt_L_name.pack()

        self.Label_phon.pack()
        self.txt_phon.pack()

        self.Label_dob.pack()
        self.txt_dob.pack()

        self.Label_email.pack()
        self.txt_email.pack()

        self.Label_password.pack()
        self.txt_password.pack()

        self.button_submit.pack(pady=40)

        #self.creaet_emp_sqlite()

    def vali_email(self,txtEmail):
        email_pa = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pa,txtEmail):
            return True
        return False


    def add_new_Emp(self):
        if self.txt_f_name.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter First Name")
            return

        if self.txt_L_name.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter Last Name")
            return

        if self.txt_password.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter Password")
            return

        if self.vali_email(self.txt_email.get()) == False:
            tkinter.messagebox.showerror("Error", "Invalid eamil. Must have @ and . ex. abc@email.com.")
        else:
            con = sqlite3.connect("data.db")

            cursor = con.cursor()

            sql_emp = """
                INSERT INTO emp (first_name, last_name, phone_number, date_of_birth, email, password)
                VALUES (?, ?, ?, ?, ?, ?);
                """
            
            emp_data = (self.txt_f_name.get().strip(), self.txt_L_name.get().strip(),self.txt_phon.get().strip(), 
                        self.txt_dob.get().strip(), self.txt_email.get().strip().lower(),self.txt_password.get().strip())  

            cursor.execute(sql_emp,emp_data)

            con.commit()

            con.close()

            self.txt_f_name.delete(0,tkinter.END)
            self.txt_L_name.delete(0,tkinter.END)
            self.txt_phon.delete(0,tkinter.END)
            self.txt_dob.delete(0,tkinter.END)
            self.txt_email.delete(0,tkinter.END)
            self.txt_password.delete(0,tkinter.END)

            tkinter.messagebox.showinfo('New Id', 'New ID is created')

            self.window_new_emp.destroy()

    #please use this function on __init__ if data.db does not exit on system (Create database table)
    def creaet_emp_sqlite(self):

        con = sqlite3.connect("data.db")

        cursor = con.cursor()

        create_table_slq = """
            CREATE TABLE IF NOT EXISTS emp (
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT,
                date_of_birth DATE,
                email TEXT UNIQUE,
                password TEXT)
            """

        cursor.execute(create_table_slq)

        con.commit()

        con.close()

    def run(self):
        self.window_new_emp.mainloop()
