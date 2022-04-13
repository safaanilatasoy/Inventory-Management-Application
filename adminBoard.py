from tkinter import *
from PIL import  Image,ImageTk #pip install pillow

class IMS:
    def __init__(frame,root):
        frame.root=root
        # This is frame size 
        frame.root.geometry("1350x700+0+0")
        # Title of the frame
        frame.root.title("Inventory Management Application")
        # Frame background color
        root.configure(background='#ecf0f1')
        
        
        # Title of the page
        frame.icon_title = PhotoImage(file="images\inventory.png")
        title=Label(frame.root,background='#1e90ff', text="Inventory Management Application",image=frame.icon_title,compound=LEFT,font=("calibri",15,"bold"), fg="#ffffff")
        title.place(x=0, y=0, relwidth=1,height=50)
        
        # This is a left Navbar
        LeftNavbar=Label(frame.root,background='#2f3542', fg="#ffffff")
        LeftNavbar.place(x=0, y=50,height=1350,width=200) 
        
        # Date 
        LeftNavbar.date_label = Label(frame.root,background='#383F4F', text="DD-MM-YYYY \t   HH:MM:SS",font=("calibri",8), fg="#ffffff")
        LeftNavbar.date_label.place(x=0, y=50,height=30,width=200)
        
        # Left Navbar Employee button
        LeftNavbar.emp_button = Button(frame.root,background='#383F4F',compound=LEFT,padx=5,anchor="w", text="Employee",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        LeftNavbar.emp_button.place(x=0, y=80,height=40,width=200)
        
        # Left Navbar Supplier button
        LeftNavbar.supplier_button = Button(frame.root,background='#383F4F',compound=LEFT,padx=5,anchor="w", text="Supplier",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        LeftNavbar.supplier_button.place(x=0, y=120,height=40,width=200)
        
        # Left Navbar Category button
        LeftNavbar.category_button = Button(frame.root,background='#383F4F',compound=LEFT,padx=5,anchor="w", text="Category",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        LeftNavbar.category_button.place(x=0, y=160,height=40,width=200)
        
        # Left Navbar Products button
        LeftNavbar.products_button = Button(frame.root,background='#383F4F',compound=LEFT,padx=5,anchor="w", text="Products",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        LeftNavbar.products_button.place(x=0, y=200,height=40,width=200)
        
         # Left Navbar Quit button
        LeftNavbar.quit_button = Button(frame.root,background='#383F4F',compound=LEFT,padx=5,anchor="w", text="Quit",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        LeftNavbar.quit_button.place(x=0, y=240,height=40,width=200)
        
        
        
    
root = Tk()
obj = IMS(root)
root.mainloop()
