from tkinter import * 

window=Tk()
window.geometry("450x300")
window.title("Login Page")
window.config(background="#A4E3BC")

username=Label(window,text="Username",bg="blue",fg="white",font=("Arial",15))
username.place(x=80,y=80)

user_entry=Entry(window,width=20,bg="#A4D3E3",fg="white",font=("Arial",15))
user_entry.place(x=190,y=80)

password=Label(window,text="Password",bg="purple",fg="white",font=("Arial",15))
password.place(x=80,y=130)

pass_entry=Entry(window,width=20,show="*",bg="#D0A4E3",fg="white",font=("Arial",15))
pass_entry.place(x=190,y=130)

submit=Button(window,text="Submit",bg="#E3D6A4",fg="black",font=("Arial",15),command=window.destroy)
submit.place(x=200,y=200)



window.mainloop()