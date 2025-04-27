"""URL Shortener App using Tkinter and Pyshorteners."""

from tkinter import Button, Entry, Label, PhotoImage, StringVar, Tk

import pyperclip
import pyshorteners as ps


class App:
    """A simple URL Shortener application using Tkinter and pyshorteners."""

    def __init__(self):
        """Initializes the main window and application components."""
        self.root = Tk()
        self.root.title("URL Shortener")
        self.w, self.h = 500, 120
        self.root.geometry(f"{self.w}x{self.h}")
        self.root.bind("<Escape>", self.quit)
        self.root.resizable(False, False)

        # Set the application icon
        self.icon = PhotoImage(file="images/icon.png")
        self.root.iconphoto(False, self.icon)

        # Variables
        self.url_var = StringVar()
        self.error_var = StringVar()

        # Layout
        Label(
            self.root,
            text="Enter link to shorten:",
            font=("calibre", 10, "normal"),
        ).place(x=150, y=20)
        Entry(
            self.root,
            textvariable=self.url_var,
            font=("calibre", 10, "normal"),
            width=50,
        ).place(x=40, y=40)
        Button(
            self.root, text="Shorten", command=self.shorten, bg="yellow"
        ).place(x=410, y=35)
        Button(self.root, text="Copy", command=self.copy_to_clipboard).place(
            x=100, y=70
        )
        Button(self.root, text="Paste", command=self.paste_to_clipboard).place(
            x=200, y=70
        )
        Button(self.root, text="Clear", command=self.clear).place(x=300, y=70)

        self.response_label = Label(
            self.root, text="", font=("calibre", 10, "normal")
        )
        self.response_label.place(x=150, y=100)

        self.root.mainloop()

    def quit(self, event):
        """Exits the application when the Escape key is pressed."""
        self.root.quit()

    def shorten(self):
        """Shortens the URL entered by the user and updates the label with success \
        or error message."""
        try:
            url = str(self.url_var.get())
            if not url:
                raise ValueError("Please enter a URL.")
            shorten = ps.Shortener()
            shorten_url = shorten.tinyurl.short(url)
            self.url_var.set(shorten_url)
            self.response_label.config(
                text="Successfully shortened!", fg="green"
            )
        except ValueError as ve:
            self.response_label.config(text=str(ve), fg="red")
        except ps.exceptions.BadURLException:
            self.response_label.config(text="URL is not valid", fg="red")
        except ps.exceptions.ShorteningErrorException:
            self.response_label.config(
                text="Error shortening the URL", fg="red"
            )

    def copy_to_clipboard(self):
        """Copies the shortened URL to the clipboard."""
        if self.url_var.get():
            pyperclip.copy(self.url_var.get())
            self.response_label.config(
                text="URL copied to clipboard", fg="green"
            )
        else:
            self.response_label.config(text="No URL to copy", fg="red")

    def paste_to_clipboard(self):
        """Pastes a URL from the clipboard to the URL entry field."""
        paste_data = pyperclip.paste()
        self.url_var.set(paste_data)
        self.response_label.config(text="URL pasted", fg="green")

    def clear(self):
        """Clears the URL entry field and the response label."""
        self.url_var.set("")
        self.response_label.config(text="", fg="black")


if __name__ == "__main__":
    app = App()
