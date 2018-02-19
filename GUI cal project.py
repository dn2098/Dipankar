from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title("CALCULATOR")
calculator.resizable(0, 1)

class Application(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.createWidgets()

	def replaceText(self, text):
		self.display.delete(0, END)
		self.display.insert(0, text)

	def appendToDisplay(self, text):
		self.entryText = self.display.get()
		self.textLength = len(self.entryText)

		if self.entryText == "0":
			self.replaceText(text)
		else:
			self.display.insert(self.textLength, text)

	def calculateExpression(self):
		self.expression = self.display.get()
		self.expression = self.expression.replace("%", "/ 100")

		try:
			self.result = eval(self.expression)
			self.replaceText(self.result)
		except:
			messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

	def clearText(self):
		self.replaceText("0")

	def createWidgets(self):
		self.display = Entry(self, font=("Helvetica", 20,'bold'), borderwidth=8, relief=RAISED,
                bg="sky blue" , justify=RIGHT)
		self.display.insert(0, "0")
		self.display.grid(row=0, column=0, columnspan=5)

#This is the First Row
		self.sevenButton = Button(self,padx=12,pady=14, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="7", borderwidth=6,
                command=lambda: self.appendToDisplay("7"))
		self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self,padx=12,pady=14, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="8", borderwidth=6,
                command=lambda: self.appendToDisplay("8"))
		self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self,padx=12,pady=14, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="9", borderwidth=6,
                command=lambda: self.appendToDisplay("9"))
		self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

		self.timesButton = Button(self,padx=12,pady=14, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="*", borderwidth=6,
                command=lambda: self.appendToDisplay("*"))
		self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

		self.clearButton = Button(self,padx=12, pady=14,font=("Helvetica", 14, 'bold'),
                bg="aqua", text="C", borderwidth=6,
                command=lambda: self.clearText())
		self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")

#This is the Second Row
		self.fourButton = Button(self,pady=14,padx=12, font=("Helvetica",14, 'bold' ),
                bg="aqua", text="4", borderwidth=6,
                command=lambda: self.appendToDisplay("4"))
		self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")

		self.fiveButton = Button(self,pady=14,padx=12, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="5", borderwidth=6,
                command=lambda: self.appendToDisplay("5"))
		self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")

		self.sixButton = Button(self,pady=14,padx=12, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="6", borderwidth=6,
                command=lambda: self.appendToDisplay("6"))
		self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")

		self.divideButton = Button(self,pady=14,padx=12, font=("Helvetica",14, 'bold' ),
                bg="aqua", text="/", borderwidth=6,
                command=lambda: self.appendToDisplay("/"))
		self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")

		self.percentageButton = Button(self,pady=14,padx=12, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="%", borderwidth=6,
                command=lambda: self.appendToDisplay("%"))
		self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE")

#This is the Third Row
		self.oneButton = Button(self,pady=14,padx=12, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="1", borderwidth=6,
                command=lambda: self.appendToDisplay("1"))
		self.oneButton.grid(row=3, column=0, sticky="NWNESWSE")

		self.twoButton = Button(self,pady=14,padx=12, font=("Helvetica", 14, 'bold'),
                bg="aqua", text="2", borderwidth=6,
                command=lambda: self.appendToDisplay("2"))
		self.twoButton.grid(row=3, column=1, sticky="NWNESWSE")

		self.threeButton = Button(self,pady=14,padx=12, font=("Helvetica",14, 'bold' ),
                bg="aqua", text="3", borderwidth=6,
                command=lambda: self.appendToDisplay("3"))
		self.threeButton.grid(row=3, column=2, sticky="NWNESWSE")

		self.minusButton = Button(self,pady=14, padx=12,font=("Helvetica",14, 'bold' ),
                bg="aqua", text="-", borderwidth=6,
                command=lambda: self.appendToDisplay("-"))
		self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")

		self.equalsButton = Button(self,pady=14, padx=12,font=("Helvetica",14, 'bold' ),
                bg="aqua", text="=", borderwidth=6,
                command=lambda: self.calculateExpression())
		self.equalsButton.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)

#This is the Fourth Row
		self.zeroButton = Button(self,pady=14, padx=12,font=("Helvetica", 18, 'bold'),
                bg="aqua",text="0", borderwidth=6,
                command=lambda: self.appendToDisplay("0"))
		self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="NWNESWSE")

		self.dotButton = Button(self,pady=14,padx=12, font=("Helvetica",18, 'bold' ),
                bg="aqua",text=".", borderwidth=6,
                command=lambda: self.appendToDisplay("."))
		self.dotButton.grid(row=4, column=2, sticky="NWNESWSE")

		self.plusButton = Button(self,pady=14,padx=12, font=("Helvetica",18, 'bold' ),
                bg="aqua", text="+", borderwidth=6,
                command=lambda: self.appendToDisplay("+"))
		self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")


app = Application(calculator).grid()		
calculator.mainloop()
