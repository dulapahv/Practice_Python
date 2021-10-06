from tkinter import *


def sayHelloWorld():
    print("Hello World")


MainWindow = Tk()
button = Button(MainWindow, text="Click Me!", command=sayHelloWorld).grid(row=0)
button2 = Button(MainWindow, text="Click Me!", command=sayHelloWorld).grid(row=1)
MainWindow.mainloop()
