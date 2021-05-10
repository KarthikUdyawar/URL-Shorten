import pyshorteners
from tkinter import *

class App:
    def __init__(self):
        #! Initialization 
        self.root = Tk()
        self.root.title('URL shortener')
        self.w, self.h = 300, 200
        self.root.geometry("%dx%d" % (self.w, self.h))
        self.root.bind("<Escape>", self.quit)
        
        
        

        #! Mainloop
        self.root.mainloop()
        
    
    def quit(self, event):
        self.root.quit()

if __name__ == '__main__':
    app = App()  

