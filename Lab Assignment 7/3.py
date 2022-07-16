from tkinter import *

root = Tk()
root.title('Calculator')

# Creating and placing entry
entry_box = Entry(root, width=30)
entry_box.grid(row=0, column=0, columnspan=4)

# defining Functions
def number_click(num):
    entry_box.insert(END, num)

def clear_click():
    entry_box.delete(0, END)

def plus_click():
    global num1
    global math
    math="+"
    num1 = entry_box.get() 
    num1 = float(num1)
    entry_box.delete(0, END)

def minus_click():
    global num1
    global math
    math="-"
    num1 = entry_box.get() 
    num1 = float(num1)
    entry_box.delete(0, END)

def multiply_click():
    global num1
    global math
    math="x"
    num1 = entry_box.get() 
    num1 = float(num1)
    entry_box.delete(0, END)

def divide_click():
    global num1
    global math
    math="/"
    num1 = entry_box.get() 
    num1 = float(num1)
    entry_box.delete(0, END)

def equals_click():
    global num2
    num2 = entry_box.get()
    num2 = float(num2)
    if math == "+":
        entry_box.delete(0, END)
        entry_box.insert(0, num1+num2)
    elif math == "-":
        entry_box.delete(0, END)
        entry_box.insert(0, num1-num2)
    elif math == "x":
        entry_box.delete(0, END)
        entry_box.insert(0, num1*num2)
    elif math == "/":
        entry_box.delete(0, END)
        entry_box.insert(0, num1/num2)

# Creating buttons and entries
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: number_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: number_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: number_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: number_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: number_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: number_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: number_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: number_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: number_click(9))
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: number_click(0))
button_plus = Button(root, text="+", padx=20, pady=20, command=plus_click)
button_minus = Button(root, text="-", padx=20, pady=20, command=minus_click)
button_divide = Button(root, text="/", padx=20, pady=20, command=divide_click)
button_multiply = Button(root, text="x", padx=20, pady=20, command=multiply_click)
button_equals = Button(root, text="=", padx=20, pady=20, command=equals_click)
button_clear = Button(root, text="Clear", padx=8, pady=20, command=clear_click)

# Place buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

root.mainloop()
