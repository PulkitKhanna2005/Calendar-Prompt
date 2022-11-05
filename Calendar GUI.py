from tkinter import *
import calendar
def showcalendar():
    gui = Tk()
    gui.config(background='cyan')
    gui.title("Calendar For The Year")
    gui.geometry("550x585")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font='Consolas 10 bold')
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop
    
if __name__=='__main__':
    new = Tk()
    new.config(background='pink')
    new.title("CALENDAR GUI")
    new.geometry("300x200")
    cal = Label(new, text="CALENDAR",bg='light grey',font=("times", 25, "bold"))
    year = Label(new, text="Enter year", bg='dark grey', font=("times", 15))
    year_field=Entry(new)
    button = Button(new, text='Show calendar',fg='Black',bg='Orange', font=("times", 10),command=showcalendar)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()
                    
