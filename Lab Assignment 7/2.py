from tkinter import *
from calendar import *

root = Tk()
root.title("Calendar")

# Creating entries, labels, textbox
Label1 = Label(root, text="Enter year")
Year_entry = Entry(root)
textbox = Text(root)

# Packing Entries and Labels
Label1.pack()
Year_entry.pack()

def print_calendar():
    Year = int(Year_entry.get())
    Calendar_of_year = calendar(Year)
    textbox.delete(0.0, END)
    textbox.insert(INSERT, Calendar_of_year)
    textbox.pack()

Button1 = Button(root, text = "Show", command=print_calendar)
Button1.pack()

root.mainloop()
