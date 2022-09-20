from tkinter import Label, Tk
import time
app_obj=Tk()
app_obj.geometry("200x73")
app_obj.title("Digital Clock")
app_obj.resizable(0,0)   # fixed window

tfont=("Calibri",40,'bold')


unit=Label(app_obj, font=tfont,bg="white",fg="red")
unit.grid(row=0,column=0,padx=2)

def clock():
    time_live=time.strftime("%H:%M:%S")
    
    unit.config(text=time_live)
    unit.after(200,clock)


clock()
app_obj.mainloop()