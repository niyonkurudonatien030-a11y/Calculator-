# Small Mobile Calculator GUI

from tkinter import *

root = Tk()
root.title("Mini Calculator")
root.geometry("240x320")
root.resizable(False, False)

# Display
entry = Entry(
    root,
    font=("Arial", 16),
    bd=5,
    relief=RIDGE,
    justify=RIGHT
)
entry.pack(fill=BOTH, padx=5, pady=5, ipady=8)

# Functions
def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = Frame(root)
frame.pack()

for row in buttons:
    row_frame = Frame(frame)
    row_frame.pack()

    for btn in row:

        action = equal if btn == "=" else lambda x=btn: click(x)

        Button(
            row_frame,
            text=btn,
            font=("Arial", 12),
            width=4,
            height=2,
            command=action
        ).pack(side=LEFT, padx=2, pady=2)

# Clear Button
Button(
    root,
    text="CLEAR",
    font=("Arial", 12),
    width=18,
    height=1,
    bg="red",
    fg="white",
    command=clear
).pack(pady=5)

root.mainloop()