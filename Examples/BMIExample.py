from tkinter import *
import math


def leftClickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    labelResult.configure(text="Your BMI is " + str(result))
    if result >= 30:
        resultExplain.configure(text="You are extremely obese.", fg="red", bg="black")
    elif 25 <= result <= 29.9:
        resultExplain.configure(text="You are obese.", fg="orange", bg="black")
    elif 23 <= result <= 24.9:
        resultExplain.configure(text="You are overweight.", fg="yellow", bg="black")
    elif 18.6 <= result <= 22.9:
        resultExplain.configure(text="You are healthy.", fg="green", bg="black")
    elif result <= 18.5:
        resultExplain.configure(text="You are underweight.", fg="blue", bg="black")


MainWindow = Tk()
labelHeight = Label(MainWindow, text="Height (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="Weight (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=3, column=0)
labelResult = Label(MainWindow)
labelResult.grid(row=2, column=1)
resultExplain = Label(MainWindow)
resultExplain.grid(row=3, column=1)
MainWindow.mainloop()
