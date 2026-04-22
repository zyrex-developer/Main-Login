import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x350")
app.title("Modern Login")

# Title
title = ctk.CTkLabel(app, text="Welcome Back", font=("Arial", 22, "bold"))
title.pack(pady=20)

# Username
username = ctk.CTkEntry(app, placeholder_text="Username don't forget @ ", width=250)
username.pack(pady=10)

# Password
password = ctk.CTkEntry(app, placeholder_text="Password", show="*", width=250)
password.pack(pady=10)

# Message
message = ctk.CTkLabel(app, text="")
message.pack(pady=5)

# Show/Hide password
def toggle_password():
    if password.cget("show") == "":
        password.configure(show="*")
    else:
        password.configure(show="")

show_btn = ctk.CTkButton(app, text="Show Password", command=toggle_password, width=150)
show_btn.pack(pady=5)

# Login function
def login():
    user = username.get()
    pwd = password.get()

    if not user or not pwd:
        message.configure(text="Fill all fields ❌", text_color="red")
    else:
        message.configure(text=f"Welcome {user} ✅", text_color="green")

# Login button
login_btn = ctk.CTkButton(app, text="Login", command=login, width=200)
login_btn.pack(pady=20)

app.mainloop()