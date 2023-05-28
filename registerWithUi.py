from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import exceptions
import subprocess
import loginWithUi
from utils.Utils import calculate_md5_hash

def run():
    db = firestore.client()

    def register():
        email = email_field.get()
        password = password_field.get()
        
        # Create a new document with the email as the document ID
        doc_ref = db.collection('users').document(email)
        
        try:
            # Set the data for the document
            doc_ref.create({
                'email': email,
                'password': calculate_md5_hash(password)
            })
            messagebox.showinfo("Registration Successful", "User registered successfully.")
        except Exception as e:
            messagebox.showerror("Registration Error", "Email already registered, please log in")


    def on_enterEmail(e):
        email_field.delete(0,'end')

    def on_leaveEmail(e):
        name=email_field.get()
        if name=='':
            email_field.insert(0,'email...')

    #

    def on_enterPassword(e):
        password_field.delete(0,'end')
        password_field.config(show="*")

    def on_leavePassword(e):
        name=password_field.get()
        if name=='':
            password_field.insert(0,'password...')
            password_field.config(show="")

    def login():
        window.destroy()
        loginWithUi.run()

    window=Tk()
    window.title("Register")
    window.geometry('925x500+300+200')
    window.resizable(False,False)
    window.configure(bg="#fff")

    img = ImageTk.PhotoImage(Image.open('registerTransparent.png'))
    Label(window,image=img,bg='white',highlightthickness=0).place(x=50,y=50)

    frame = Frame(window,width=350,height=350,bg='white')
    frame.place(x=570,y=70)


    heading = Label(frame,text='Sign Up',fg='#d8e305',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=120,y=0)

    #####################-------------------------------------

    email_field = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    email_field.place(x=30,y=80)
    email_field.insert(0,'email...')

    email_field.bind('<FocusIn>',on_enterEmail)
    email_field.bind('<FocusOut>',on_leaveEmail)

    Frame(frame,width=270,height=2,bg='black').place(x=25,y=107)

    ###########################################

    password_field = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    password_field.place(x=30,y=150)
    password_field.insert(0,'password...')
    password_field.bind('<FocusIn>',on_enterPassword)
    password_field.bind('<FocusOut>',on_leavePassword)
    Frame(frame,width=270,height=2,bg='black').place(x=25,y=177)


    Button(frame,width=20,pady=7,text='Register',bg="#d8e305",fg='white',border=0,command=register).place(x=100,y=224)
    label=Label(frame,text="I have an account",fg="black",bg="white",font=('Microsoft YaHei UI Light',9))
    label.place(x=100,y=270)


    signin = Button(frame,width=6,text="Log in", border=0, bg='white',cursor='hand2',fg='#d8e305',command=login)
    signin.place(x=200,y=271)
    window.mainloop()