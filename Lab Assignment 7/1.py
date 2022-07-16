from tkinter import *

root = Tk()
root.title('GST Finder')

# Creating Entries and Labels
Label1 = Label(root, text="Enter Original cost and Net price:")
Original_cost_entry = Entry(root)
Net_price_entry = Entry(root)

# Packing entries and Labels in program
Label1.pack()
Original_cost_entry.pack()
Net_price_entry.pack()

# Defining GST function
def GST():
    Net_price = int(Net_price_entry.get())
    Original_cost = int(Original_cost_entry.get())
    Label2 = Label(root, text="Your GST rate is:")
    Label2.pack()
    Gst_rate = Label(root, text = ((Net_price-Original_cost)*100) / Original_cost)
    Gst_rate.pack()

# Creating and Packing button
GST_button = Button(root, text='Calculate GST', command=GST)
GST_button.pack()

root.mainloop()
