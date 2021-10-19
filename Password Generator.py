import random
import string
from tkinter import *
import paperclip

root = Tk()
root.title("Vijay Password Generator")
root.geometry("400x400")
root.resizable(0, 0)
heading = Label(root, text="Password Generator", font="arial 15 bold").pack()
pass_len = IntVar()
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=15).pack()
pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = (
            random.choice(string.ascii_uppercase)
            + random.choice(string.ascii_lowercase)
            + random.choice(string.digits)
            + random.choice(string.punctuation)
        )
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
        )
    pass_str.set(password)


Button(root, text="Generate Password", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()


root.mainloop()
