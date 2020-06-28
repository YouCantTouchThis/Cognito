import tkinter as tk
import smtplib, ssl
from dotenv import load_dotenv
import os
from email.message import EmailMessage

def getUserEmail():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
    canvas1.pack()

    label1 = tk.Label(root, text='Cognito')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    label2 = tk.Label(root, text='Enter Your Email:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)

    label3 = tk.Label(root, text='You will get an email confirming your submission.\nIf you don\'t receive one, manually write your email in the email.txt file.')
    label3.config(font=('helvetica', 8))
    canvas1.create_window(200, 140, window=label3)

    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 180, window=entry1)

    def getEmail ():
        
        x1 = entry1.get()
        with open('email.txt', 'w') as f:
            f.write(x1)
            
        root.destroy()
        
    button1 = tk.Button(text='Submit', command=getEmail, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 220, window=button1)

    root.mainloop()

def confirmUserEmail():
    load_dotenv()

    user_email = None
    with open('email.txt') as f:
        user_email = f.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Next, log in to the server
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login("cognito.confirm@gmail.com", os.getenv("PASSWORD"))

    #Send the mail
    msg = EmailMessage()
    
    msg.set_content("""
    Hey there!
    Cognito has confirmed your email. We will keep you updated on any health concerns.
    Thanks,
    The Cognito Team
    """)
    msg["Subject"] = "Cognito Email Confirm"
    msg["From"] = 'cognito.confirm@gmail.com'
    msg['To'] = user_email

    


    server.send_message(msg)
    server.quit()

def send_p():
    load_dotenv()

    user_email = None
    with open('email.txt') as f:
        user_email = f.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login("cognito.confirm@gmail.com", os.getenv("PASSWORD"))

    msg = EmailMessage()
    
    msg.set_content("""
    Hey!
    Our analysis
    The Cognito Team
    """)
    msg["Subject"] = "Cognito Email Confirm"
    msg["From"] = 'cognito.confirm@gmail.com'
    msg['To'] = user_email