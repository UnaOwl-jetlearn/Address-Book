from tkinter import *

window = Tk()

window.geometry("1000x750")
window.title("Address Book")
window.config(background="lightgreen")

title = Label(window, text="Address Book", font=("arial",30),bg="lightgreen")
title.place(x=300,y=30)

open_button = Button(window,text="Open",font=("arial",15))
open_button.place(x=650,y=80)

save_button = Button(window,text="Save",font=("arial",15))
save_button.place(x=740,y=80)

textbox = Listbox(window, width=65,height=25)
textbox.place(x=80,y=85)

name_title = Label(window,text="Name:",font=("arial",20),bg="lightgreen")
name_title.place(x=500,y=150)

birthday_title = Label(window,text="Birthday:",font=("arial",20),bg="lightgreen")
birthday_title.place(x=500,y=200)

address_title = Label(window,text="Address:",font=("arial",20),bg="lightgreen")
address_title.place(x=500,y=250)

phone_title = Label(window,text="Phone:",font=("arial",20),bg="lightgreen")
phone_title.place(x=500,y=300)

gender_title = Label(window,text="Gender:",font=("arial",20),bg="lightgreen")
gender_title.place(x=500,y=350)

name_entry = Entry(window, font=("arial",20))
name_entry.place(x=615,y=150)

birthday_entry = Entry(window, font=("arial",20))
birthday_entry.place(x=615,y=200)

address_entry = Entry(window, font=("arial",20))
address_entry.place(x=615,y=250)

phone_entry = Entry(window, font=("arial",20))
phone_entry.place(x=615,y=300)

gender = StringVar()
gender.set("F")

gender_f = Radiobutton(window,text="F",variable=gender,value="F",width=3,height=1,font=("arial",17))
gender_m =Radiobutton(window,text="M",variable=gender,value="M",width=3,height=1,font=("arial",17))

gender_f.place(x=615,y=350)
gender_m.place(x=720,y=350)

window.mainloop()