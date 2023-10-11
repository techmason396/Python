from tkinter import *

MILES = 1.609344

windown = Tk()
windown.title("Mile to Km Converter")
windown.minsize(width=300, height=150)

input_km = Entry()
input_km.grid(row=0, column=1)
input_km.focus()

# LABEL
miles_label = Label(text="Miles", font=('Aria', 15))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=('Aria',15))
equal_label.grid(row=1, column=0)

result_label = Label(text="Miles", font=("Aria",15))
result_label.grid(row=1, column=1)

km_lable = Label(text="Km", font=("Aria", 15))
km_lable.grid(row=1, column=2)

# BUTTON
def calculate_miles_to_Km():
    try:
        miles = int(input_km.get())
        result = miles * MILES
        result_label.config(text=result)
    except ValueError:
        print("Value not valid")
    
cal_button = Button(text='Calculate', command=calculate_miles_to_Km)
cal_button.grid(row=2, column=1)


windown.mainloop()
