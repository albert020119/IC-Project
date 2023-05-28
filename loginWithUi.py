from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import exceptions
import subprocess
import window
import registerWithUi
from utils.Utils import calculate_md5_hash

def run(): 
    db = firestore.client()

    def login():
        email = email_field.get()
        password = password_field.get()

        # Access the Firestore database
        db = firestore.client()

        # Query the 'users' collection for the entered email
        query = db.collection('users').where('email', '==', email).limit(1)
        result = query.get()

        # Check if the query result contains any documents
        if len(result) > 0:
            # Get the first document from the result
            account = result[0].to_dict()

            # Check if the entered password matches the password in the account document
            if account['password'] == calculate_md5_hash(password):
                root.destroy()
                window.build_ui()
            else:
                messagebox.showerror("Invalid Password", "Invalid password")
        else:
            messagebox.showerror("Invalid Email", "Invalid email")


    def on_enterEmail(e):
        email_field.delete(0,'end')

    def on_leaveEmail(e):
        name=email_field.get()
        if name=='':
            email_field.insert(0,'please enter email...')

    def on_enterPassword(e):
        password_field.delete(0,'end')
        password_field.config(show="*")

    def on_leavePassword(e):
        name=password_field.get()
        if name=='':
            password_field.insert(0,'please enter password...')
            password_field.config(show="")

    def register():
        root.destroy()
        registerWithUi.run()

    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = ImageTk.PhotoImage(Image.open('transparentLogo.png'))
    Label(root,image=img,bg='white',highlightthickness=0).place(x=50,y=50)


    frame = Frame(root,width=350,height=350,bg='white')
    frame.place(x=570,y=70)

    heading = Label(frame,text='Sign in',fg='#ff0000',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=120,y=0)

    email_field = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    email_field.place(x=30,y=80)
    email_field.insert(0,'please enter email...')

    email_field.bind('<FocusIn>',on_enterEmail)
    email_field.bind('<FocusOut>',on_leaveEmail)

    Frame(frame,width=270,height=2,bg='black').place(x=25,y=107)

    ###########################################

    password_field = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    password_field.place(x=30,y=150)
    password_field.insert(0,'please enter password...')
    password_field.bind('<FocusIn>',on_enterPassword)
    password_field.bind('<FocusOut>',on_leavePassword)
    Frame(frame,width=270,height=2,bg='black').place(x=25,y=177)

    ##########################################

    Button(frame,width=20,pady=7,text='Log in',bg="#ff0000",fg='white',border=0,command=login).place(x=24,y=204)
    label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)


    register=Button(frame,width=6,text="Register",border=0,bg='white',cursor='hand2',fg='#ff0000',command=register)
    register.place(x=215,y=271)




    root.mainloop()

if __name__=="__main__":
    cred = credentials.Certificate('csgocheat-8b8e1-firebase-adminsdk-8ujyb-7c8cf2c466.json')  # Replace with the path to your service account key JSON file
    firebase_admin.initialize_app(cred) 
    run()