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


        #------------------------------------------------------------------- employee div ---------------------------------------------------------------------------------
        empdiv=Label(frame.root,background='#636e72',fg="#ffffff")
        empdiv.place(x=205, y=55,height=500,width=300)
        
        # employee list title
        empdivtitle=Label(frame.root,background='#636e72',text="Employees",fg="#ffffff")
        empdivtitle.place(x=300, y=60,height=20,width=100)
        
        # employee list 
        emplist = Listbox(empdiv, background="#b2bec3")
        emplist.insert(1,"Safa Anil Atasoy")  
        emplist.insert(2, "Ata Demirkiran")  
        emplist.insert(3, "Tolga gobel")  
        emplist.insert(4, "Cristiano Ronaldo")  
        emplist.pack()  
        emplist.pack()  
        emplist.place(x=5, y=40,height=300,width=290)
        
        #employee div buttons
        # add Button
        empdiv.add_button = Button(frame.root,background='#27ae60',compound=CENTER,padx=5,anchor="w", text="Add",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        empdiv.add_button.place(x=215, y=430,height=40,width=135)
        # Delete Button
        empdiv.delete_button = Button(frame.root,background='#d63031',compound=CENTER,padx=5,anchor="w", text="Delete",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        empdiv.delete_button.place(x=360, y=430,height=40,width=135)
        
        
        # ----------------------------------------------------------- supplier div ---------------------------------------------------------------------------------------------
        spdiv=Label(frame.root,background='#636e72',fg="#ffffff")
        spdiv.place(x=515, y=55,height=500,width=300)
        
        # supplier list title
        supplierdivtitle=Label(frame.root,background='#636e72',text="Suppliers",fg="#ffffff")
        supplierdivtitle.place(x=610, y=60,height=20,width=100)
        
        #supplier div list
        splist= Listbox(spdiv,background="#b2bec3")
        splist.insert(1,"Apple INC")  
        splist.insert(2, "Koc Holding")  
        splist.insert(3, "Borusan A.Ş")  
        splist.insert(4, "ASELSAN")  
        splist.pack()  
        splist.pack()  
        splist.place(x=5, y=40,height=300,width=290)
       
        
        #supplier div buttons
        # add Button
        spdiv.add_button = Button(frame.root,background='#27ae60',compound=CENTER,padx=5,anchor="w", text="Add",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        spdiv.add_button.place(x=525, y=430,height=40,width=135)
        # Delete Button
        spdiv.delete_button = Button(frame.root,background='#d63031',compound=CENTER,padx=5,anchor="w", text="Delete",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        spdiv.delete_button.place(x=670, y=430,height=40,width=135)
        
        #  ----------------------------------------------------------- Category Div  -------------------------------------------------------------------------------------------
        ctdiv=Label(frame.root,background='#636e72',fg="#ffffff")
        ctdiv.place(x=825, y=55,height=200,width=515)
        
        # Category title
        supplierdivtitle=Label(frame.root,background='#636e72',text="Categories",fg="#ffffff")
        supplierdivtitle.place(x=825, y=60,height=20,width=100)
        
        # Category div list
        ctlist = Listbox(ctdiv,background="#b2bec3")
        ctlist.insert(1,"Electronic")  
        ctlist.insert(2, "Furniture")  
        ctlist.insert(3, "Book")  
        ctlist.insert(4, "Hobby")
        ctlist.insert(5, "Car")
        ctlist.insert(5, "Best Sellers")
        ctlist.pack()  
        ctlist.pack()  
        ctlist.place(x=5, y=30,height=160,width=200)
        
        #Category div buttons
        # add Button
        ctdiv.add_button = Button(ctdiv,background='#27ae60',compound=CENTER,padx=5,anchor="w", text="Add",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        ctdiv.add_button.place(x=215, y=30,height=40,width=135)
        # Delete Button
        ctdiv.delete_button = Button(ctdiv,background='#d63031',compound=CENTER,padx=5,anchor="w", text="Delete",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        ctdiv.delete_button.place(x=215, y=80,height=40,width=135)
        
        #  ----------------------------------------------------------- Products Div  --------------------------------------------------------------------------------------------
        ptdiv=Label(frame.root,background='#636e72',fg="#ffffff")
        ptdiv.place(x=825, y=260,height=200,width=515)
        
        # Product title
        supplierdivtitle=Label(frame.root,background='#636e72',text="Products",fg="#ffffff")
        supplierdivtitle.place(x=825, y=265,height=20,width=100)
        
        # Category div list
        ptlist = Listbox(ptdiv,background="#b2bec3")
        ptlist.insert(1,"Hp 15-DW3055NT Intel Core İ5-1135G7 8GB Ram 512GB SSD")  
        ptlist.insert(2, "Asus X415EA-EK977W Intel 11.nesil Core I5 11135G7 8GB")  
        ptlist.insert(3, "iPhone 11 128 GB")  
        ptlist.insert(4, "iPhone 7 Plus 32 GB")
        ptlist.insert(5, "Lg S3-W12JA2AA (S12ETK) 12.000 Btu Dualcool")
        ptlist.insert(5, "Mitsubishi Heavy SRK35ZSP-W(S) Silver Serisi A++")
        ptlist.pack()  
        ptlist.pack()  
        ptlist.place(x=5, y=30,height=160,width=200)
        
        #Category div buttons
        # add Button
        ptdiv.add_button = Button(ptdiv,background='#27ae60',compound=CENTER,padx=5,anchor="w", text="Add",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        ptdiv.add_button.place(x=215, y=30,height=40,width=135)
        # Delete Button
        ptdiv.delete_button = Button(ptdiv,background='#d63031',compound=CENTER,padx=5,anchor="w", text="Delete",font=("calibri",10),bd=3,cursor="hand2", fg="#ffffff")
        ptdiv.delete_button.place(x=215, y=80,height=40,width=135)
root = Tk()
obj = IMS(root)
root.mainloop()
