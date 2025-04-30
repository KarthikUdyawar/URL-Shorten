"""URL Shortener App using Tkinter and Pyshorteners."""

import os
from tkinter import CENTER, Button, Entry, Frame, Label, StringVar, Tk

import pyperclip
import pyshorteners as ps
from PIL import Image, ImageTk, UnidentifiedImageError


class URLShortenerApp(Tk):
    """A URL Shortener app using Tkinter with class-based UI structure."""

    def __init__(self):
        """Initializes the main window and application components."""
        super().__init__()

        # Window setup
        self.title("URL Shortener")
        self.geometry("600x250")
        self.minsize(400, 250)
        self.configure(padx=20, pady=20)

        # Load icon
        self.set_icon()

        # State variables
        self.url_var = StringVar()

        # UI setup
        self.setup_ui()

        # Binds
        self.bind("<Escape>", self.quit)

        # Set focus
        self.url_entry.focus_set()

    def set_icon(self):
        """Attempt to load and set application icon."""
        icon_path = "images/icon.ico"
        if os.path.exists(icon_path):
            try:
                icon = ImageTk.PhotoImage(Image.open(icon_path))
                self.iconphoto(False, icon)
            except (OSError, UnidentifiedImageError) as e:
                print(f"Failed to load icon: {e}")

    def setup_ui(self):
        """Sets up all UI components."""
        main_frame = Frame(self)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.8)

        # Header
        header_frame = Frame(main_frame)
        header_frame.pack(fill="x", pady=(0, 10))

        Label(
            header_frame, text="URL Shortener", font=("Helvetica", 16, "bold")
        ).pack()

        # Input
        input_frame = Frame(main_frame)
        input_frame.pack(fill="x", pady=10)

        Label(
            input_frame,
            text="Enter link to shorten:",
            font=("Helvetica", 10),
            anchor="w",
        ).pack(fill="x")

        entry_row = Frame(input_frame)
        entry_row.pack(fill="x", pady=5)

        self.url_entry = Entry(
            entry_row, textvariable=self.url_var, font=("Helvetica", 10)
        )
        self.url_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        Button(
            entry_row,
            text="Shorten",
            command=self.shorten,
            bg="#FFEB3B",
            font=("Helvetica", 10, "bold"),
            padx=10,
        ).pack(side="right")

        # Action buttons
        buttons_frame = Frame(main_frame)
        buttons_frame.pack(fill="x", pady=10)

        btn_style = {"padx": 15, "pady": 5, "font": ("Helvetica", 10)}

        Button(
            buttons_frame,
            text="Copy",
            command=self.copy_to_clipboard,
            **btn_style,
        ).pack(side="left", padx=(0, 5))
        Button(
            buttons_frame,
            text="Paste",
            command=self.paste_to_clipboard,
            **btn_style,
        ).pack(side="left", padx=5)
        Button(
            buttons_frame, text="Clear", command=self.clear, **btn_style
        ).pack(side="left", padx=5)

        # Response
        response_frame = Frame(main_frame)
        response_frame.pack(fill="x", pady=10)

        self.response_label = Label(
            response_frame, text="", font=("Helvetica", 10), anchor="w"
        )
        self.response_label.pack(fill="x")

    # main.py:145:15: W0718: Catching too general exception Exception (broad-exception-caught)
    def shorten(self):
        """Shortens the entered URL using TinyURL and displays result."""
        try:
            self.update_idletasks()
            url = str(self.url_var.get())
            if not url:
                raise ValueError("Please enter a URL.")

            shortener = ps.Shortener()
            short_url = shortener.tinyurl.short(url)
            self.url_var.set(short_url)
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

        except Exception:  # pylint: disable=broad-except
            # Catch-all for any other unexpected errors.
            self.response_label.config(
                text="An unexpected error occurred", fg="red"
            )

    def copy_to_clipboard(self):
        """Copies the shortened URL to clipboard."""
        if self.url_var.get():
            pyperclip.copy(self.url_var.get())
            self.response_label.config(
                text="URL copied to clipboard", fg="green"
            )
        else:
            self.response_label.config(text="No URL to copy", fg="red")

    def paste_to_clipboard(self):
        """Pastes URL from clipboard to the input."""
        try:
            self.url_var.set(pyperclip.paste())
            self.response_label.config(text="URL pasted", fg="green")
        except pyperclip.PyperclipException as e:
            self.response_label.config(
                text=f"Error pasting: {str(e)}", fg="red"
            )

    def clear(self):
        """Clears the input and response label."""
        self.url_var.set("")
        self.response_label.config(text="", fg="black")

    def quit(self, event=None):
        """Quits the application."""
        self.destroy()


if __name__ == "__main__":
    app = URLShortenerApp()
    app.mainloop()
