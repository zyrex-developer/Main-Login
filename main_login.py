import tkinter as tk

window = tk.Tk()
window.title("Main")
window.geometry("400x300")
window.config(bg="#2e2e2e")


frame = tk.Frame(window, bg="#2b2b2b" , padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame, text=("Login Account"), font=("Arical" , 18, "bold"), fg="white" , bg="#2b2b2b")
title.grid(row=0 , column=0 , columnspan=2 , pady=10)


tk.Label(frame, text="Username:" , fg="white", bg="#2b2b2b")\
    .grid(row=1 , column=0 , sticky="w" , pady=10 )
    
username = tk.Entry(frame, bg="#7d7d7d" ,fg="white",  insertbackground="white")
username.grid(row=1 , column=1 , pady=5)



tk.Label(frame, text="Password:" , fg="white", bg="#2b2b2b")\
    .grid(row=2 , column=0 , sticky="w", pady=10)
    
password = tk.Entry(frame, bg="#7d7d7d" , fg="white", insertbackground="white", show="*")
password.grid(row=2, column=1 , pady=5)


message = tk.Label(frame, text="", fg="lightgreen", bg="#2b2b2b")
message.grid(row=4 , column=0 , columnspan=2 , pady=10 )

def login():
    user = username.get().strip()
    pwd = password.get().strip()
    
    try:
        if not user or pwd == "":            
            message.config(text="Invaild input. Please enter again. ❌" , fg="red")
        # elif                 
        else:
            message.config(text="Login Succes ✅  " , fg="lightgreen")
    except ValueError:
        print("Try Again!")
    
    
    print("Username: " , user)
    print("Password: " , pwd)
    
    
btn = tk.Button(frame, text="Login", bg="#2fcb1b" , fg="white",command=login ,padx=10)    
btn.grid(row=3 , column=0, columnspan=2 , pady=10 )




window.mainloop()