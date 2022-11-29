from tkinter import *
window = Tk()
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)


def calculate():
    km = round(float(input.get()) * 1.609, 2)
    num_km.config(text=km)


# Input
input = Entry(width=10)
input.grid(row=0, column=1)

# Is equal
label = Label(text="is equal to")
label.grid(row=1, column=0)

# num_km
num_km = Label(text="0")
num_km.grid(row=1, column=1)

# Calculate
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

# Miles
miles = Label(text="Miles")
miles.grid(row=0, column=2)

# Km
km = Label(text="Km")
km.grid(row=1, column=2)


window.mainloop()
