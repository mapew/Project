import tkinter
import sqlite3
import tkinter.messagebox
from MainWindow import Mainwindow
from CreateNewId import Createnewid

class App():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("300x300")
        self.window.title("log in")

        self.lblID = tkinter.Label(self.window, text="Email:")
        self.lblPass = tkinter.Label(self.window, text = "Password:")

        self.textboxID = tkinter.Entry(self.window)
        self.textboxPass = tkinter.Entry(self.window,show="*")

        self.button = tkinter.Button(self.window, text= "log in",command=self.checklogin)
        self.newEmButton = tkinter.Button(self.window, text= "Create new id",command=self.new_emp_create)

        self.lblID.pack()
        self.textboxID.pack(pady=10)
        self.lblPass.pack()
        self.textboxPass.pack(pady=10)
        self.button.pack(pady= 10)
        self.newEmButton.pack(pady = 20)
    

    def checkIDNPass(self,email,password):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = """
                SELECT * FROM emp
                WHERE email = ? AND password = ?;
                """ 
        try:
            cursor.execute(query, (email.lower(), password))
            user = cursor.fetchone()
            conn.close()
        except:
            tkinter.messagebox.showerror("Error", "Invalid ID or password.")

        if user:
            user_name = user[1] + " " + user[2]
            tkinter.messagebox.showinfo("Information", ("Login successful! Welcome " + user_name))
            self.window.destroy()
            self.open_main_window()
        else:
            tkinter.messagebox.showerror("Error", "Invalid ID or password.")

    def new_emp_create(self):
        createnewids = Createnewid()
        createnewids.run()

    def open_main_window(self): 
        main_window = Mainwindow()
        main_window.run()

    def checklogin(self):
        cu_id = self.textboxID.get().strip()
        cu_passw = self.textboxPass.get().strip()

        self.checkIDNPass(cu_id,cu_passw)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
