import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os


USER_DATA_FILE = "user_data.json"


if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "r") as file:
        data = json.load(file)
        users = data.get("users", [])
        passwords = data.get("passwords", [])
else:
    users = []
    passwords = []

def save_user_data():
    with open(USER_DATA_FILE, "w") as file:
        json.dump({"users": users, "passwords": passwords}, file)

def register_user():
    while True:
        username = simpledialog.askstring("Registreerimine", "Sisesta kasutajanimi:")
        if username:
            if username in users:
                messagebox.showerror("Viga", "Selline kasutajanimi on juba olemas!")
            else:
                password = simpledialog.askstring("Registreerimine", "Sisesta parool:", show='*')
                if password:
                    users.append(username)
                    passwords.append(password)
                    save_user_data()
                    messagebox.showinfo("Edu", "Kasutaja registreeritud!")
                    break  
        else:
            break  

def login():
    while True:
        username = simpledialog.askstring("Autoriseerimine", "Sisesta kasutajanimi:")
        if username in users:
            password = simpledialog.askstring("Autoriseerimine", "Sisesta parool:", show='*')
            if passwords[users.index(username)] == password:
                messagebox.showinfo("Edu", f"Tere tulemast, {username}!")
                break  
            else:
                messagebox.showerror("Viga", "Vale parool!")
        else:
            messagebox.showerror("Viga", "Sellist kasutajat ei leitud!")
            break  

def reset_password():
    while True:
        username = simpledialog.askstring("Parooli taastamine", "Sisesta kasutajanimi:")
        if username in users:
            old_password = simpledialog.askstring("Parooli taastamine", "Sisesta vana parool:", show='*')
            if old_password == passwords[users.index(username)]:
                new_password = simpledialog.askstring("Parooli taastamine", "Sisesta uus parool:", show='*')
                if new_password:
                    passwords[users.index(username)] = new_password
                    save_user_data()
                    messagebox.showinfo("Edu", "Parool edukalt muudetud!")
                    break  
            else:
                messagebox.showerror("Viga", "Vale vana parool!")
        else:
            messagebox.showerror("Viga", "Sellist kasutajat ei leitud!")
            break  

def change_credentials():
    while True:
        old_username = simpledialog.askstring("Kasutajanime ja/või parooli muutmine", "Sisesta vana kasutajanimi:")
        if old_username in users:
            old_password = simpledialog.askstring("Kasutajanime ja/või parooli muutmine", "Sisesta vana parool:", show='*')
            if old_password == passwords[users.index(old_username)]:
                new_username = simpledialog.askstring("Kasutajanime ja/või parooli muutmine", "Sisesta uus kasutajanimi:")
                if new_username:
                    users[users.index(old_username)] = new_username
                    save_user_data()
                    messagebox.showinfo("Edu", "Kasutajanimi edukalt muudetud!")
                new_password = simpledialog.askstring("Kasutajanime ja/või parooli muutmine", "Sisesta uus parool:", show='*')
                if new_password:
                    passwords[users.index(old_username)] = new_password
                    save_user_data()
                    messagebox.showinfo("Edu", "Parool edukalt muudetud!")
                    break  
            else:
                messagebox.showerror("Viga", "Vale parool!")
        else:
            messagebox.showerror("Viga", "Sellist kasutajat ei leitud!")
            break 


root = tk.Tk()
root.title("Kasutaja haldamine")
root.geometry("400x300")


root.configure(bg="#2c3e50")


btn_register = tk.Button(root, text="Registreerimine", command=register_user)
btn_register.pack(pady=20)

btn_login = tk.Button(root, text="Autoriseerimine", command=login)
btn_login.pack(pady=20)

btn_reset_password = tk.Button(root, text="Parooli taastamine", command=reset_password)
btn_reset_password.pack(pady=20)

btn_change_credentials = tk.Button(root, text="Kasutajanime ja/või parooli muutmine", command=change_credentials)
btn_change_credentials.pack(pady=20)

root.mainloop()

