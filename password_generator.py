import random
import string
from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.title("Password Generator")
root.geometry("375x200")
root.minsize(375, 200)
root.maxsize(375, 200)
root.configure(bg='black')
n = StringVar()
password = StringVar()

data = '@$%#!&_*' + string.ascii_letters + string.digits

len = Label(root, text='Select Length: ', font='ariel 15 bold', fg='red', bg='black')
len.place(x=40, y=40)
combo = ttk.Combobox(root, width=5, textvariable=n, font='ariel 15 bold')
combo['values'] = [i for i in range(8, 17)]
combo.place(x=193, y=40)
paswd = Entry(root, textvariable=password, width='39', font='ariel 12 bold', fg='green', bg='black', bd=0,
              state="readonly")
paswd.grid(padx=10, pady=140, row=3, column=1)


def generate():
    try:
        if n.get() == '':
            messagebox.showinfo("Password Geneartor", "Please select the Length for your Password")
        passw = random.choices(data, k=int(n.get()))
        password.set("Generated Password is: " + ''.join(passw))
    except:
        pass


gen = Button(root, text='Generate', bg='black', fg='red', font=('ariel 15 bold'), relief=GROOVE, command=generate)
gen.place(x=125, y=90)

root.mainloop()
