import pyshorteners as ps
from tkinter import *
import pyperclip

class App:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('URL shortener')
        self.w, self.h = 500, 120
        self.root.geometry("%dx%d" % (self.w, self.h))
        self.root.bind("<Escape>", self.quit)
        self.root.resizable(False,False)
        
        self.url_var = StringVar()
        self.error_var = StringVar()
        
        self.url_label = Label(self.root, text = "Enter link to shorten: " , font=('calibre',10,'normal')).place(x = 150,y = 20)  
        self.url_entry = Entry(self.root,textvariable = self.url_var, font=('calibre',10,'normal'), width=50).place(x = 40,y = 40)  
        self.url_btn =Button(self.root, text ="Shorten", command = self.shorten, bg='yellow').place(x = 410,y = 35) 
        self.copy_btn =Button(self.root, text ="Copy", command = self.copy_to_clipboard).place(x = 100,y = 70) 
        self.paste_btn =Button(self.root, text ="Paste", command = self.paste_to_clipboard).place(x = 200,y = 70) 
        self.clear_btn =Button(self.root, text ="Clear", command = self.clear).place(x = 300,y = 70) 
        self.error_label = Label(self.root, text = "", font=('calibre',10,'normal'))
        self.error_label.place(x = 150,y = 100)  
        
        self.root.mainloop()
        
    def quit(self, event):
        self.root.quit()
    
    def shorten(self):
        try:
            url = str(self.url_var.get())
            shorten = ps.Shortener()
            shorten_url = shorten.tinyurl.short(url)
            self.url_var.set(str(shorten_url))
            self.error_label.config(text='Successful shorten',fg='green')
        except ps.exceptions.BadURLException:
            self.error_label.config(text='URL is not valid',fg='red')
        except ps.exceptions.ShorteningErrorException:
            self.error_label.config(text='It is already shorten',fg='red')
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.url_var.get())
        
    def paste_to_clipboard(self):
        self.url_var.set(pyperclip.waitForPaste()) 
        
    def clear(self):
        self.url_var.set("") 

if __name__ == '__main__':
    app = App()  