from tkinter import *


class IMS:
    def __init__(frame,root):
        frame.root=root
        # This is frame size 
        frame.root.geometry("1350x700+0+0")
        # Title of the frame
        frame.root.title("Inventory Management Application")
        
        
        
        # Title of the page
        frame.icon_title = PhotoImage(file=)
        title=Label(frame.root,background='#ecf0f1', text="Inventory Management Application", font=("calibri",20,"bold"), fg="#2c3e50").place(x=0, y=10, relwidth=1,height=70) 
        
        # Frame background color
        root.configure(background='#ecf0f1')
    
root = Tk()
obj = IMS(root)
root.mainloop()
