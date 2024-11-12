import tkinter
from tkinter import scrolledtext
import tkinter.messagebox
import google.generativeai as genai

class Mainwindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Employee AI Chart")
        self.window.geometry("600x500")

        self.txtapiKey = tkinter.Entry(self.window)
        self.labelapiKey = tkinter.Label(self.window,text = "API Key")
        self.labelapiKey.pack()
        self.txtapiKey.pack()
 
        self.lblWelcome = tkinter.Label(self.window, text="Welcome Please ask me about Micro test price and TAT!", font=("Arial", 16))
        self.lblWelcome.pack(pady=20)

        chat_frame = tkinter.Frame(self.window)
        chat_frame.pack(padx=10, pady=10)

        self.chat_window = scrolledtext.ScrolledText(chat_frame, wrap=tkinter.WORD, width=50, height=15, state=tkinter.DISABLED)
        self.chat_window.pack()

        self.message_entry = tkinter.Entry(self.window, width=40)
        self.message_entry.pack(padx=120, pady=10, side=tkinter.LEFT)

        send_button = tkinter.Button(self.window, text="Send", width=10,command=self.sendMessage)
        send_button.pack(padx=10, pady=10, side=tkinter.RIGHT)

        self.chat_window.config(state=tkinter.NORMAL)
        self.chat_window.insert(tkinter.END, "The test list includes gluten, Salmonella, Listeria, heavy metals, E. coli, and total coliforms.\n")
        self.chat_window.insert(tkinter.END, "The AI can answer questions about price and turnaround time.\n")
        self.chat_window.insert(tkinter.END, "ex. What is the price of the gluten test?\n")
        self.chat_window.insert(tkinter.END, "ex. Today is November 12, 2024. When can I receive the Salmonella result?\n")
        self.chat_window.insert(tkinter.END, "Please ask me!\n")
        
        self.chat_window.config(state=tkinter.DISABLED) 

        self.prompt = """ Here are test name, price and TAT. Answer the user question base on this information
                        gluten test:
                        price: $120
                        TAT: 5 business days,
                        Salmonella test:
                        price: $70
                        TAT: 3 days,
                        Listeria test:
                        price: $ 50
                        TAT: 3 days
                        heavy metals test:
                        price: $110
                        TAT: 5 Business days,
                        e.coli test:
                        price: $20
                        TAT: 3 Business days,
                        total coliforms test:
                        price: $20
                        TAT: 3 Business days,
                        """

    def sendMessage(self):
        user_message = self.message_entry.get()
        if user_message.strip() == "":
            return

        bot_message = self.AIresponse(user_message)

        if bot_message == None:
            return

        self.chat_window.config(state=tkinter.NORMAL) 
        self.chat_window.insert(tkinter.END, f"You: {user_message}\n")

        self.chat_window.insert(tkinter.END, f"AI: {bot_message}\n\n")

        self.chat_window.yview(tkinter.END)
        
        self.message_entry.delete(0, tkinter.END)

        self.chat_window.config(state=tkinter.DISABLED) 

    def AIresponse(self,use_input):
        my_api_key = self.txtapiKey.get()
        #my_api_key = "API_Key"

        if my_api_key == "":
            tkinter.messagebox.showerror("Error", "Please Enter google AI API Key on API key textbox")
        else:
            try:
                genai.configure(api_key=str(my_api_key))
                model = genai.GenerativeModel(model_name="gemini-pro")
                response = model.generate_content([self.prompt,use_input])
                return response.text
            except:
                tkinter.messagebox.showerror("Error", "Invalid API Key. please enter correct API Key")

    def run(self):
        self.window.mainloop()
