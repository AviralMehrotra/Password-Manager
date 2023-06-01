from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
import sys

file_path = "dat.json"

# ======== Check Master Password ========#

def check_password():
    entered_master_password = master_password_entry.get()
    if entered_master_password == '123':  # Replace 'password123' with your desired password
        pass_window.destroy()
    else:
        messagebox.showerror("Incorrect Password", "Incorrect password. You cannot access the password manager.")
        sys.exit()

# ======== Password Prompt UI ========#

pass_window = Tk()
pass_window.title("Password Prompt")
pass_window.resizable(False, False)
pass_window.config(padx=50, pady=60)

def on_close():
        sys.exit()  # Terminate the program if the password prompt window is closed

pass_window.protocol("WM_DELETE_WINDOW", on_close)

master_password_label = Label(pass_window, text="Enter password:")
master_password_label.grid(row=0, column=1)
master_password_entry = Entry(pass_window, show="*", width=30)
master_password_entry.grid(row=1, column=1, pady=5, padx=15)
master_password_entry.focus()

master_password_button = Button(pass_window, text="Submit", command=check_password)
master_password_button.grid(row=1, column=2)

master_password_entry.bind("<Return>", lambda event: check_password())

pass_window.mainloop()

# ======== Password Generator ========#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ======== Search Password ========#

def search_password():
    global file_path
    website_name = website_detail_input.get()
    if len(website_name) == 0:
        messagebox.showinfo(
            title="Oops", message="Please, Enter a website name to search!")
    else:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(
                title="Error", message="No Data File Found!")
        else:
            if website_name in data:
                found_email = data[website_name]["Email"]
                found_password = data[website_name]["Password"]
                messagebox.showinfo(
                    title=website_name, message=f"Email: {found_email}\nPassword: {found_password}")
            else:
                messagebox.showinfo(
                    title="Error", message=f"No details for {website_name} exists.")

# ======== Saving Password ========#

def add_to_file():
    global file_path
    website = website_detail_input.get()
    email = email_input.get()
    password = password_input.get()
    content_to_add = {
        website: {
            "Email": email,
            "Password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)  # reading old data
        except FileNotFoundError:
            with open(file_path, "w") as file:
                # saving updated data
                json.dump(content_to_add, file, indent=4)
        else:
            data.update(content_to_add)  # updating old data with new data

            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)  # saving updated data
        finally:
            website_detail_input.delete(0, END)
            password_input.delete(0, END)

# ======== Password Manager UI ========#

window = Toplevel()
window.title("Password Manager")
window.config(padx=30, pady=30)
window.resizable(False, False)
window.withdraw()

canvas= Canvas(width=210, height=200)
logo_img= PhotoImage(file="passlock.png")
canvas.create_image(105, 105, image=logo_img)

canvas.grid(row= 0,column=1)

website_detail_label= Label(text="Website:", font=("Arial", 10))
website_detail_label.grid(row=1,column=0)
website_detail_input= Entry(width=37, font=("Arial", 10))
website_detail_input.grid(row=1,column=1, pady=5)
search_button= Button(text="Search", width=8, pady=-1.5, font=("Arial", 10), command=search_password)
search_button.grid(row=1,column=2)

email_label= Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(row=2,column=0)
email_input= Entry(width=50, font=("Arial", 10))
email_input.grid(row=2,column=1, padx=10, pady=5, columnspan=2)
email_input.insert(0, "aviralmehrotra@gmail.com")

password_label= Label(text="Password:", font=("Arial", 10))
password_label.grid(row=3,column=0)
password_input= Entry(width=37, font=("Arial", 10))
password_input.grid(row=3,column=1, pady=5)
generate_button= Button(text="Generate", width=8, pady=-1.5, font=("Arial", 10), command=generate_password)
generate_button.grid(row=3,column=2)

add_btn= Button(text="Add", width=8, padx=8, pady=-2, font=("Arial", 10), command=add_to_file)
add_btn.grid(row=4,column=1)


window.mainloop()
