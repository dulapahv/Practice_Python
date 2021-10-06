from tkinter import *


def sayHelloWorld():
    print("Hello World")


MainWindow = Tk()
button = Button(MainWindow, text="Click Me!", command=sayHelloWorld, width=20, height=20).grid(row=2,column=1)
button2 = Button(MainWindow, text="Click Me!", command=sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow, text="Click Me!", command=sayHelloWorld).grid(row=0,column=2)
label = Label(MainWindow, text="Hello World", width=20).grid(row=0, column=1)
MainWindow.mainloop()
