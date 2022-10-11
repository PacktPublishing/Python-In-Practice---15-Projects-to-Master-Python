# Python Programming Course : GUI Applications
#                                  -Rahul Mula
# Length Converter ( Meter <-> Inch <-> Foot )

from tkinter import *

# Main window
App = Tk()
App.title("Length Converter")
App.geometry('350x150')
# Scales to be used
scales = ['Meters', 'Inches', 'Foot']

# The scale of the length to be used for conversion
_from = StringVar()
from_menu = OptionMenu(App, _from, *scales)
from_menu.grid(row=0, column=0, pady=5)

# In between label
lbl = Label(App, text=' convert to ')
lbl.grid(row=0, column=1, pady=5)

# The scale of the length to convert the value to
to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=2, pady=5)

# Entry pre-label
numL = Label(App, text='Enter the number: ')
numL.grid(row=1, column=0, columnspan=2, pady=5)

# Entry field
numE = Entry(App)
numE.grid(row=1, column=2, columnspan=2, pady=5)


# Converter function
def num_con():
    froM = _from.get()
    tO = to_.get()
    num = int(numE.get())

    # Scales:
    # 1 meter = 39.37 inches
    # 1 meter = 3.28 foot
    # 1 foot = 12 inches

    if froM == 'Meters' and tO == 'Inches':
        converted_num = num * 39.37
    elif froM == 'Meters' and tO == 'Foot':
        converted_num = num * 3.28
    elif froM == 'Inches' and tO == 'Meters':
        converted_num = num / 39.37
    elif froM == 'Inches' and tO == 'Foot':
        converted_num = num / 12
    elif froM == 'Foot' and tO == 'Meters':
        converted_num = num / 3.28
    elif froM == 'Foot' and tO == 'Inches':
        converted_num = num * 12
    else:
        converted_num = num

    conv_numL = Label(App, text=round(converted_num, 2), width=10)
    conv_numL.grid(row=1, column=4, pady=5)


# Convert button
conB = Button(App, text='Convert', command=num_con)
conB.grid(row=2, column=0, pady=5)

App.mainloop()