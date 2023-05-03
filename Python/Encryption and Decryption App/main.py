import base64
import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

class EncryptDecryptApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("420x420")
        self.master.title("Encryption/Decryption App")
        self.master.configure(bg="#f0f0f0")

        # Set icon
        image_icon = PhotoImage(file="key.png")
        self.master.iconphoto(False, image_icon)
        
        # Add UI elements
        self.add_widgets()

    def add_widgets(self):
        style = ttk.Style()
        style.configure("TButton",
                        font=("calibri", 12),
                        background="#1089ff",
                        foreground="white",
                        bordercolor="#1089ff",
                        focusthickness=3,
                        focuscolor="black")
        style.map("TButton",
                  background=[("active", "#0096db"),
                              ("disabled", "#b3b3b3")],
                  bordercolor=[("active", "#0096db")],
                  relief=[("pressed", "groove"),
                          ("!pressed", "ridge")])

        Label(text="Enter text for encryption and decryption", bg="#f0f0f0", fg="black", font=("calibri", 13)).place(x=10, y=10)
        self.text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        self.text1.place(x=10, y=50, width=400, height=100)

        Label(text="Enter secret key for encryption and decryption", bg="#f0f0f0", fg="black", font=("calibri", 13)).place(x=10, y=170)
        self.code = StringVar()
        Entry(textvariable=self.code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

        Button(self.master, text="ENCRYPT", command=self.encrypt, bg="#ed3833", fg="white", bd=0).place(x=10, y=250, width=190, height=40)
        Button(self.master, text="DECRYPT", command=self.decrypt, bg="#00bd56", fg="white", bd=0).place(x=220, y=250, width=190, height=40)
        Button(self.master, text="RESET", command=self.reset, bg="#1089ff", fg="white", bd=0).place(x=10, y=300, width=190, height=40)
        Button(self.master, text="OPEN", command=self.open_file, bg="#1089ff", fg="white", bd=0).place(x=220, y=300, width=190, height=40)
        Button(self.master, text="SAVE", command=self.save_file, bg="#1089ff", fg="white", bd=0).place(x=10, y=350, width=190, height=40)
        
        Label(self.master, text="Created by Edison", bg="#f0f0f0", fg="black", font=("calibri", 13)).place(x=250, y=360)

    def encrypt(self):
        password = self.code.get()

        if not password:
            messagebox.showerror("Encryption", "Input Password")
        else:
            message = self.text1.get(1.0, END)
            encoded_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encoded_message)
            encrypted_text = base64_bytes.decode("ascii")
            self.text1.delete(1.0, END)
            self.text1.insert(1.0, encrypted_text)

    def decrypt(self):
        password = self.code.get()

        if not password:
            messagebox.showerror("Decryption", "Input Password")
        else:
            message = self.text1.get(1.0, END)
            decoded_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decoded_message)
            decrypted_text = base64_bytes.decode("ascii")
            self.text1.delete(1.0, END)
            self.text1.insert(1.0, decrypted_text)

    def reset(self):
        self.code.set("")
        self.text1.delete(1.0, END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
                self.text1.delete(1.0, END)
                self.text1.insert(1.0, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text1.get(1.0, END)
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(content)

def main():
    root = Tk()
    EncryptDecryptApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
