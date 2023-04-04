from tkinter import*
rt=Tk()

rt.title("ASCII project")
rt.geometry("500x500")
rt.configure(background="light blue")

enter_word = Entry(rt)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

btn = Button(rt, text="DIsplay the ASCII code and encrypted value ", bg="blue" fg="black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label = Label(rt, text="Name in ASCII code :", bg="blue", fg="black")
label.place(relx=0.5,rely=0.6,anchor=CENTER)

label = Label(rt, text="Encrypted Name :", bg="blue", fg="black")
label.place(relx=0.5,rely=0.7,anchor=CENTER)


rt.mainloop()

