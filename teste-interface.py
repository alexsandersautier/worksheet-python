from tkinter import *
from datetime import datetime
import app

window = Tk()

window.title("Registration of Job Vacancies")
window.config(padx=10, pady=100)

# field company
lbl_company = Label(text="Company:")
lbl_company.grid(row=2,column=0)
ent_company = Entry(width=35)
ent_company.grid(row=2,column=1, columnspan=2)

# field vacancy
lbl_vacancy = Label(text="Vacancy:")
lbl_vacancy.grid(row=3,column=0)
ent_vacancy = Entry(width=35)
ent_vacancy.grid(row=3,column=1, columnspan=2)

# field Application Date
lbl_date = Label(text="Application Date:")
lbl_date.grid(row=4,column=0)
ent_date = Entry(width=20)
ent_date.grid(row=4,column=1,columnspan=2)

# field Register Other?
lbl_register = Label(text="Register other?")
lbl_register.grid(row=5,column=0)
ent_register = Entry(width=35)
ent_register.grid(row=5,column=1,columnspan=2)

def delete():
    ent_company.delete(0,'end')
    ent_vacancy.delete(0,'end')
    ent_date.delete(0,'end')
    ent_register.delete(0,'end')
    ent_company.focus()

def date():
    company = ent_company.get()
    vacancy = ent_vacancy.get()
    date_reg = ent_date.get()
    continues = ent_register.get()
    print(company, vacancy, date_reg, continues)
    app.criar__planilha(company, vacancy, date_reg, continues)
    delete()

def exit():
    window.destroy()

# btn save
btn_save = Button(text="Save",width=15,command=date)
btn_save.grid(row=6,column=0)

btn_delete = Button(text="Delete",width=15,command=delete)
btn_delete.grid(row=6,column=2)

btn_exit = Button(text="Exit",width=15,command=exit)
btn_exit.grid(row=7,column=1)


window.mainloop()