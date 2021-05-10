import pyshorteners as ps
from tkinter import *
import pyperclip

class App:
    def __init__(self):
        #! Initialization 
        self.root = Tk()
        self.root.title('URL shortener')
        self.w, self.h = 300, 200
        self.root.geometry("%dx%d" % (self.w, self.h))
        self.root.bind("<Escape>", self.quit)
        self.root.resizable(False,False)
        
        self.url_var = StringVar()
        
        self.url_label = Label(self.root, text = "Enter link to shorten: " , font=('calibre',10,'normal')).place(x = 90,y = 20)  
        self.url_entry = Entry(self.root,textvariable = self.url_var, font=('calibre',10,'normal'), width=30).place(x = 40,y = 40)  
        self.url_btn =Button(self.root, text ="Shorten", command = self.shorten).place(x = 40,y = 70) 
        self.copy_btn =Button(self.root, text ="Copy", command = self.copy_to_clipboard).place(x = 100,y = 70) 
        self.paste_btn =Button(self.root, text ="Paste", command = self.paste_to_clipboard).place(x = 150,y = 70) 
        self.clear_btn =Button(self.root, text ="Clear", command = self.clear).place(x = 200,y = 70) 
        

        #! Mainloop
        self.root.mainloop()
        
    
    def quit(self, event):
        self.root.quit()
    
    def shorten(self):
        url = str(self.url_var.get())
        shorten = ps.Shortener()
        shorten_url = shorten.tinyurl.short(url)
        # print(url)
        # print(shorten)
        # print(shorten_url)
        self.url_var.set(str(shorten_url))
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.url_var.get())
        
    def paste_to_clipboard(self):
        self.url_var.set(pyperclip.waitForPaste()) 
        
    def clear(self):
        self.url_var.set("") 

if __name__ == '__main__':
    app = App()  