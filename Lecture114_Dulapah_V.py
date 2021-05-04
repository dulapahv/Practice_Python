import datetime
from tkinter import ttk
from tkinter import *
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

# Declare Variables
CRates = CurrencyRates()
CCodes = CurrencyCodes()
CurrencyList = ["USD", "JPY", "EUR", "THB", "IDR", "BGN", "ILS", "GBP", "AUD", "CHF", "HKD"]
date = list(range(1, 32))
month = list(range(1, 13))
year = list(range(2000, 2022))


# Event when user left-click the Calculate button
def cal(event):
    # Check for error and invalid input, if there is none, calculate and display result
    try:
        int(money.get())
    except ValueError:
        Result.config(text="Please enter a valid amount of money!", fg="red")
    if currency1.get() == '':
        Result.config(text="Please select currency to convert from!", fg="red")
    elif currency2.get() == '':
        Result.config(text="Please select currency to convert into!", fg="red")
    elif money.get() == '':
        Result.config(text="Please enter amount of money!", fg="red")
    elif int(money.get()) < 0:
        Result.config(text="Please enter positive amount of money!", fg="red")
    elif year.get() == '' or month.get() == '' or date == '':
        Result.config(text="Please select date, month, and year!", fg="red")
    else:
        date_selected = datetime.date(int(year.get()), int(month.get()), int(date.get()))
        result = CRates.convert(currency1.get(), currency2.get(), float(money.get()), date_selected)
        Result.config(text=result, fg="black")


# Initialize Tk windows and program's title name
MainWindow = Tk()
MainWindow.title('Exchange Rate Converter')

# Prompt user for currency to convert from
PromptCurrency1 = Label(MainWindow, text="Select currency to convert from", height=2, width=25)
PromptCurrency1.grid(row=0, column=0)
currency1 = ttk.Combobox(MainWindow, values=CurrencyList, width=32)
currency1.grid(row=0, column=1)

# Prompt user for currency to convert into
PromptCurrency2 = Label(MainWindow, text="Select currency to convert into", height=2, width=25)
PromptCurrency2.grid(row=1, column=0)
currency2 = ttk.Combobox(MainWindow, values=CurrencyList, width=32)
currency2.grid(row=1, column=1)

# Prompt user for amount of money to convert
PromptMoney = Label(MainWindow, text="Enter amount of money", height=2, width=25)
PromptMoney.grid(row=3, column=0)
money = Entry(MainWindow, width=35)
money.grid(row=3, column=1)

# Prompt user for Date/Month/Year of the currency rate to use
PromptTime = Label(MainWindow, text="Select date (D/M/Y)", height=2, width=25)
PromptTime.grid(row=4, column=0)
date = ttk.Combobox(MainWindow, values=date, width=3)
date.place(x=182.3, y=115)
month = ttk.Combobox(MainWindow, values=month, width=3)
month.place(x=229, y=115)
year = ttk.Combobox(MainWindow, values=year, width=6)
year.place(x=275.7, y=115)

# Button for user to press in order to start conversion
Calculate = Button(MainWindow, text="Calculate", height=1)
Calculate.grid(row=5, column=0)
Calculate.bind('<Button-1>', cal)

# Show the conversion result
Result = Label(MainWindow, text="", height=2)
Result.grid(row=5, column=1)

MainWindow.mainloop()
