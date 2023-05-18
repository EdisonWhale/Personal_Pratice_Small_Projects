from tkinter import *
from tkinter import messagebox
import pyqrcode
import pyperclip
from PIL import ImageTk, Image
import os
import webbrowser


class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title('QR Code Generator')
        self.root.geometry('430x530')  # Set the size of the window


        self.upper_frame = Frame(root, width=400, height=300, bg='light grey')
        self.upper_frame.pack(side=TOP, fill=BOTH)
        self.lower_frame = Frame(root, width=400, height=300, bg='light grey')
        self.lower_frame.pack(side=BOTTOM, fill=BOTH)

        self.draw_widgets()
        self.history = []
        self.history_labels = []

    def draw_widgets(self):
        app_label = Label(self.upper_frame, text="QR Code Generator", fg='black', font=('Arial', 30), bg='light grey')
        app_label.place(x=50, y=20)  # Adjust the position of the label

        name_label = Label(self.upper_frame, text="Link name", bg='light grey')
        link_label = Label(self.upper_frame, text="Link", bg='light grey')
        name_label.place(x=50, y=100)
        link_label.place(x=50, y=140)

        self.name_entry = Entry(self.upper_frame)
        self.link_entry = Entry(self.upper_frame)
        self.name_entry.place(x=120, y=100)
        self.link_entry.place(x=120, y=140)

        generate_button = Button(self.upper_frame, text="Generate QR code", command=self.generate)
        generate_button.place(x=80, y=180)

        open_button = Button(self.upper_frame, text="Open QR code", command=self.open_link)
        open_button.place(x=220, y=180)

    def generate(self):
        link_name = self.name_entry.get()
        link = self.link_entry.get()
        file_name = link_name +".png"
        try:
            url = pyqrcode.create(link)
            url.png(file_name, scale=8)
            image = Image.open(file_name)
            image = image.resize((200, 200), Image.ANTIALIAS)
            image.save(file_name)
        except Exception as e:
            messagebox.showerror("Error", "Failed to generate QR Code: " + str(e))
            return

        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(self.lower_frame, image=image, bg='light grey')
        image_label.image = image
        image_label.place(x=100, y=10)

        self.history.append((link_name, link, file_name))
        if len(self.history) > 3:  # keep only last 3 history records
            self.history.pop(0)

        # Update history
        self.display_history()

    def display_history(self):
        # Clear old history labels
        for label in self.history_labels:
            label.destroy()
        self.history_labels = []

        history_label = Label(self.upper_frame, text="Recent history: ", font=('Arial', 15), bg='light grey')
        history_label.place(x=50, y=220)
        self.history_labels.append(history_label)

        for i, (link_name, link, file_name) in enumerate(self.history[-3:], 1):
            text = f"{i}. {link_name}: {link}"
            history_entry = Label(self.upper_frame, text=text, font=('Arial', 10), bg='light grey')
            history_entry.place(x=50, y=240 + i*20)
            self.history_labels.append(history_entry)

            copy_button = Button(self.upper_frame, text="Copy Link", command=lambda link=link: self.copy_link(link))
            copy_button.place(x=280, y=240 + i*20)
            self.history_labels.append(copy_button)

    def copy_link(self, link):
        pyperclip.copy(link)
        messagebox.showinfo("Success", "Link copied to clipboard.")

    def open_link(self):
        if self.history:
            _, link, _ = self.history[-1]
            webbrowser.open(link)
        else:
            messagebox.showinfo("Info", "No QR code has been generated yet.")


if __name__ == "__main__":
    root = Tk()
    QRCodeGenerator(root)
    root.mainloop()
