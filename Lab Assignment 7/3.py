from tkinter import *

expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


my_calculator = Tk()

my_calculator.title("Calculator")
my_calculator.geometry("270x150")

equation = StringVar()
expression_field = Entry(my_calculator, textvariable=equation) # takes input of operation
expression_field.grid(columnspan=4, ipadx=70)

# buttons and their commands
button1 = Button(my_calculator, text=' 1 ', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(my_calculator, text=' 2 ', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(my_calculator, text=' 3 ', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(my_calculator, text=' 4 ', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(my_calculator, text=' 5 ', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(my_calculator, text=' 6 ', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(my_calculator, text=' 7 ', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(my_calculator, text=' 8 ', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(my_calculator, text=' 9 ', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(my_calculator, text=' 0 ', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(my_calculator, text=' + ', bg='blue',
				command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(my_calculator, text=' - ', bg='blue',
				command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(my_calculator, text=' * ', bg='blue',
					command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(my_calculator, text=' / ', bg='blue',
					command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(my_calculator, text=' = ', bg='yellow',
				command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(my_calculator, text='Clear', bg='red',
				command=clear, height=1, width=7)
clear.grid(row=5, column='1')

Decimal= Button(my_calculator, text='.', bg='green',
					command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)
	
my_calculator.mainloop()
