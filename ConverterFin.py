from tkinter import *
from tkinter import ttk

#name window
window = Tk()
window.configure(bg = "steel blue")

#Converting Kgs to Lbs
def kiloConvert():
    print("Convert Success")
    pounds = float(ev1.get())*2.20462
    grams = float(ev1.get())*1000
    ounces = float(ev1.get())*35.274

#Clear text box
    t1.delete("1.0", END)
    t1.insert(END, pounds)
    t2.delete("1.0", END)
    t2.insert(END, grams)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

#Button to convert
b1 = Button(window, text = "Convert", bg = "navy", command = kiloConvert, fg = "white")
b1.grid(row = 2, column = 2)

#Button Style
def on_enter(e):
    b1.configure(bg = "slategray3")
def on_leave(e):
    b1.configure(bg = "navy")

b1.bind('<Enter>', on_enter)
b1.bind('<Leave>', on_leave)
        
#Entry Box
ev1 = StringVar()
ev1 = Entry(window, textvariable = ev1)
ev1.grid(row = 2, column = 1)

#Shows converted values
t1 = Text(window, height = 1, width = 15)
t1.grid(row = 2, column = 3)
t2 = Text(window, height = 1, width = 15)
t2.grid(row = 2, column = 4)
t3 = Text(window, height = 1, width = 15)
t3.grid(row = 2, column = 5)

#Labels above
l1= Label(window, text = "Enter Kilograms:", bg = "steel blue", fg = "white", font = ("Arial Bold", 10))
l1.grid(row = 1, column = 1)
l2= Label(window, text = "Pounds", bg = "steel blue", fg = "white", font = ("Arial Bold", 10))
l2.grid(row = 1, column = 3)
l3= Label(window, text = "Grams", bg = "steel blue", fg = "white", font = ("Arial Bold", 10))
l3.grid(row = 1, column = 4)
l3= Label(window, text = "Ounces", bg = "steel blue", fg = "white", font = ("Arial Bold", 10))
l3.grid(row = 1, column = 5)

window.mainloop()
