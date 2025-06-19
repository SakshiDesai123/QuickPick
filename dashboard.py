from tkinter import*
#from PIL import ImageTk,Image#pip install pillow
import sqlite3
import time
import os

from tkinter import ttk, messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from bill import BillClass


class IMS :
    def __init__(self,root):
        self.root=root
        self.root.title("Grocery Shop Login | Developed By Sakshi")
        self.root.geometry("1350x700+0+0")
        self.root.title("Quick Pick  " )
        self.root.config(bg="white")
        
      
        
        #===========title==========
        
    


        #self.icon_image=ImageTk.PhotoImage(file="image/main.png")
        title=Label(self.root,text=" Quick Pick" ,   compound=LEFT,
                   font=("goudy old style" , 40 ,"bold") , bg="#010c48" , fg="white", anchor="w" ,pady=250).place(x=0, y=0 , relwidth= 1, height= 70)
        
        
        
        
        
        #========btn_logout========
        btn_logout=Button(self.root , text="Logout" , command=self.logout,font=("goudy old style", 15 ,"bold"), bg="yellow" , cursor= "hand2")
        btn_logout.place(x=1100, y=10 , width= 150, height= 50)
        
        
        
        
        #=========clock===========
        self.lbl_clock=Label(self.root,text=" Welcome to Quick Pick \t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS ",  
                             font=("goudy old style" ,15) , bg="#4d636d" , fg="white")
        self.lbl_clock.place(x=0, y=70 , relwidth= 1, height= 30)
        
        
        
        
        #========Left Menu =======
        self.MenuLogo=PhotoImage(file="image/ims2.png")
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0, y=100 , width= 200, height=598)
        
        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        
        
        
        
        #======MENU======
        lbl_menu=Label(LeftMenu , text="Menu" , font=("goudy old style", 20 ) ,bg="#009688")
        lbl_menu.pack(side=TOP , fill=X)

        self.icon_side=PhotoImage(file="image/side.png")
        
        btn_emplyoee=Button(LeftMenu , text="Employee" , command = self.employee , image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_emplyoee.pack(side=TOP , fill=X)
        
        btn_supplier=Button(LeftMenu , text="Supplier" , command= self.supplier, image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_supplier.pack(side=TOP , fill=X)
        
        btn_category=Button(LeftMenu , text="Category" , command= self.category,image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_category.pack(side=TOP , fill=X)
        
        btn_product=Button(LeftMenu , text="Product" , command= self.product,image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_product.pack(side=TOP , fill=X)
        
        btn_sales=Button(LeftMenu , text="Sales" ,command= self.sales,image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_sales.pack(side=TOP , fill=X)
        
        btn_bill_generate=Button(LeftMenu , text="Billing" , command= self.bill,image=self.icon_side, compound=LEFT , padx=5,font=("goudy old style", 20)  , bg="white",bd=3 , cursor= "hand2",anchor="w")
        btn_bill_generate.pack(side=TOP , fill=X)
        
        
        
        #======content======
        
        self.lbl_employee=Label(self.root,text="Total Employee \n [0]", bd=9, relief= RIDGE, bg="#ff5722", fg="black",font=("goudy old style", 25 ,"bold"))
        self.lbl_employee.place(x=300,y=120, height=150, width =300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier \n [0]", bd=9, relief= RIDGE, bg="#33bbf9", fg="black",font=("goudy old style", 25 ,"bold"))
        self.lbl_supplier.place(x=650,y=120, height=150, width =300)
        
        self.lbl_category=Label(self.root,text="Total Category \n [0]", bd=9, relief= RIDGE, bg="#009688", fg="black",font=("goudy old style", 25 ,"bold"))
        self.lbl_category.place(x=1000,y=120, height=150, width =300)
        
        self.lbl_product=Label(self.root,text="Total Product \n [0]", bd=9, relief= RIDGE, bg="#ffc107", fg="black",font=("goudy old style", 25 ,"bold"))
        self.lbl_product.place(x=300,y=300, height=150, width =300)
        
        self.lbl_sales=Label(self.root,text="Total Sales \n [0]", bd=9, relief= RIDGE, bg="#607d8b", fg="black",font=("goudy old style", 25 ,"bold"))
        self.lbl_sales.place(x=650,y=300, height=150, width =300)
        
        
        
        
        
        #=========footer===========
        lbl_footer=Label(self.root,text="Quick Pick",  
                             font=("goudy old style" ,10) , bg="#4d636d" , fg="white")  
        lbl_footer.place(x=200,y=660, height=40, width=1200)
        
        
        
        self.update_content()
        
#====================================================================================================================================================================================
  
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
    def bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
        
        
    #==================================
    
    
        
    def update_content(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try:
            cur.execute("select * from  product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product \n [{str(len(product))}]')
            
            cur.execute("select * from  supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier \n [{str(len(supplier))}]')
            
            cur.execute("select * from  category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category \n [{str(len(category))}]')
            
            cur.execute("select * from  employe")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee \n [{str(len(employee))}]')
            bill=str(len(os.listdir('bill')))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')
            
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Quick Pick \t\t Date: {str(date_)}\t\t Time: {str(time_)} ")          
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")        
            
            
            
            
if __name__=="__main__":    
           root=Tk()
           obj=IMS(root)
           root.mainloop()