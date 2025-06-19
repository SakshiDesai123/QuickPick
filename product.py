from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk ,messagebox
import sqlite3
import pyttsx3 
class productClass :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Quick Pick      | Devloped by Sakshi"  )
        self.root.config(bg="white")
        self.root.focus_force()
        
         #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        
        
        
         #==============All Variable============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_Pro_Id=StringVar()
        self.var_cat=StringVar()
        self.var_supplier=StringVar()
        self.cat_list=[]
        self.supplier_list=[]
        self.fetch_cat_supplier()
        self.var_product_name=StringVar()
        self.var_product_price=StringVar()
        self.var_qty=StringVar()
        self.var_product_status=StringVar()
        
        
        #===========product frame========
        productFrame=LabelFrame(self.root, bd=4, bg="white", relief=RIDGE)
        productFrame.place(x=20,y=10,width=450,height=480)
        
        #=============search frame======
        SearchFrame=LabelFrame(self.root,text="Search Product" ,  font= (" goudy old style ", 10, "bold" ),bg="white", relief=RIDGE, bd=3)
        SearchFrame.place(x=500,y=10,width=580,height=60)
        
        
        
        #==========option==========
        cmb_search=ttk.Combobox (SearchFrame,textvariable=self.var_searchby, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",12),values=("Select","Pro_Category", "Pro_Supplier", "Pro_Name"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=("goudy old style ", 15 ), bg="lightyellow")
        txt_search.place(x=200,y=10)
        
        btn_search=Button(SearchFrame, text="Search",command=self.search,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=430,y=9,width=130, height=27)
        
        #============title===============
        self.icon_title=PhotoImage(file="image/product.png")
        title=Label(productFrame, text= "Product Details",image=self.icon_title,compound=LEFT,padx=20,font=("goudy old style", 35), bg="#0f4d7d", fg="white")
        title.pack(side=TOP,fill=X)
        
        
        #===================content===========
        
        lbl_category=Label(productFrame, text= "Category",font=("goudy old style", 18), bg="white")
        lbl_category.place(x=30,y=70)
        lbl_supplier=Label(productFrame, text= "Supplier",font=("goudy old style", 18), bg="white")
        lbl_supplier.place(x=30,y=120)
        lbl_Name=Label(productFrame, text= "Name",font=("goudy old style", 18), bg="white")
        lbl_Name.place(x=30,y=170)
        lbl_Price=Label(productFrame, text= "Price",font=("goudy old style", 18), bg="white")
        lbl_Price.place(x=30,y=220)
        lbl_QTY=Label(productFrame, text= "Quantity",font=("goudy old style", 18), bg="white")
        lbl_QTY.place(x=30,y=270)
        lbl_Status=Label(productFrame, text= "Status",font=("goudy old style", 18), bg="white")
        lbl_Status.place(x=30,y=320)
        
    
        
        txt_category=Entry(productFrame, textvariable=self.var_cat,font=("goudy old style", 15), bg="lightyellow")
        txt_category.place(x=150,y=70,width=200)
        cmb_category=ttk.Combobox (productFrame,textvariable=self.var_cat, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",15),values=self.cat_list)
        cmb_category.place(x=150,y=70,width=200)
        cmb_category.current(0)
        
        txt_supplier=Entry(productFrame, textvariable=self.var_supplier,font=("goudy old style", 15), bg="lightyellow")
        txt_supplier.place(x=150,y=120,width=200)
        cmb_supplier=ttk.Combobox (productFrame,textvariable=self.var_supplier, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",15),values=self.supplier_list)
        cmb_supplier.place(x=150,y=120,width=200)
        cmb_supplier.current(0)
        
        txt_Name=Entry(productFrame, textvariable=self.var_product_name,font=("goudy old style", 15), bg="lightyellow")
        txt_Name.place(x=150,y=170,width=200)
        # bind  validation register
        
        txt_Price=Entry(productFrame, textvariable=self.var_product_price,font=("goudy old style", 15), bg="lightyellow")
        txt_Price.place(x=150,y=220,width=200)
        # bind  validation register
       # validate_p=self.root.register(self.checkprice)
        #txt_Price.config(validate='key',validatecommand=(validate_p,'%P'))
        
        
        txt_Quantity=Entry(productFrame, textvariable=self.var_qty,font=("goudy old style", 15), bg="lightyellow")
        txt_Quantity.place(x=150,y=270,width=200)
        #validate_q=self.root.register(self.checkqty)
        #txt_Quantity.config(validate='key',validatecommand=(validate_q,'%P'))
        
        txt_Status=Entry(productFrame, textvariable=self.var_product_status,font=("goudy old style", 15), bg="lightyellow")
        txt_Status.place(x=150,y=320,width=200)
        cmb_Status=ttk.Combobox (productFrame,textvariable=self.var_product_status, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",15),values=("","Active","Inactive" ))
        cmb_Status.place(x=150,y=320,width=200)
        cmb_Status.current(0)
        
        #=============btn==========================
        
        btn_update=Button(productFrame, text="Update",command=self.update,font=("goudy old style ", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_update.place(x=20,y=400,width=80, height=28)
        
        btn_add=Button(productFrame, text="Save", command=self.add ,font=("goudy old style ", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_add.place(x=110,y=400,width=80, height=28)
        
        btn_delete=Button(productFrame, text="Delete",command=self.delete,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_delete.place(x=200,y=400,width=80, height=28)
        
        btn_clear=Button(productFrame, text="Clear",command=self.clear,font=("goudy old style ", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=290,y=400,width=80, height=28)
        
        
        #=======================product ============================
        
        product_frame=Frame(self.root,bd=3, relief=RIDGE)
        product_frame.place(x=500,y=100, width=550, height=380)
        
        scrolly=Scrollbar(product_frame, orient=VERTICAL)
        scrollx=Scrollbar(product_frame, orient=HORIZONTAL)
        
        self.ProductTable=ttk.Treeview(product_frame,columns=("Pro_Id","Pro_Category","Pro_Supplier","Pro_Name", "Pro_Price", "Pro_Quantity","Pro_Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("Pro_Id",text="Prod-Id")
        self.ProductTable.heading("Pro_Category",text="Category")
        self.ProductTable.heading("Pro_Supplier", text="Supplier")
        self.ProductTable.heading("Pro_Name", text="Name") 
        self.ProductTable.heading("Pro_Price",text="Price")
        self.ProductTable.heading("Pro_Quantity",text="Quantity")
        self.ProductTable.heading("Pro_Status", text="Status")
        
        
        
        self.ProductTable["show"]="headings"
        
        self.ProductTable.column("Pro_Id",width=60)
        self.ProductTable.column("Pro_Category",width=60)
        self.ProductTable.column("Pro_Supplier", width=80)
        self.ProductTable.column("Pro_Name", width=80)
        self.ProductTable.column("Pro_Price",width=60)
        self.ProductTable.column("Pro_Quantity",width=80)
        self.ProductTable.column("Pro_Status", width=80)
        
        
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
    
      
        
   #========================== main ===============================
    def fetch_cat_supplier(self):
        self.cat_list.append("Empty")
        self.supplier_list.append("Empty")
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try:
            cur.execute("Select  Cat_Name  from category")
            cat=cur.fetchall()
           
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                   self.cat_list.append(i[0])
                
            
            
            cur.execute("Select  Supp_Name  from supplier ")
            supplier=cur.fetchall()
            if len(supplier)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in supplier:
                   self.supplier_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def add(self):
     try:
        name = self.var_product_name.get().strip()
        price = self.var_product_price.get().strip()
        qty = self.var_qty.get().strip()
        cat = self.var_cat.get().strip()
        supplier = self.var_supplier.get().strip()
        status = self.var_product_status.get().strip()

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        # Validate Name
        if name == "":
            self.engine.say('Please enter the product name.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the product name.", parent=self.root)
            return
        if any(char.isdigit() for char in name):
            self.engine.say('Name cannot contain numeric characters.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Name cannot contain numeric characters.", parent=self.root)
            return

        # Check if product already exists
        cur.execute("SELECT * FROM product WHERE Pro_Name=?", (name,))
        if cur.fetchone():
            self.engine.say('This product already exists.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "This product already exists, try another name.", parent=self.root)
            return

        # Validate Category
        if cat in ["Select", "Select your Category "]:
            self.engine.say('Please select a valid category.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a valid category.", parent=self.root)
            return

        # Validate Supplier
        if supplier in ["Select", "Select your Supplier "]:
            self.engine.say('Please select a valid supplier.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a valid supplier.", parent=self.root)
            return

        # Validate Status
        if status in ["", "Select your Status "]:
            self.engine.say('Please select a valid status.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a valid status.", parent=self.root)
            return

        # Validate Quantity
        if qty == "":
            self.engine.say('Please enter the quantity.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the quantity.", parent=self.root)
            return
        if not qty.isdigit():
            self.engine.say('Quantity should only contain digits.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Quantity should only contain digits.", parent=self.root)
            return

        # Validate Price
        if price == "":
            self.engine.say('Please enter the price.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the price.", parent=self.root)
            return
        if not price.replace('.', '', 1).isdigit():
            self.engine.say('Price should be a number.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Price should be a number.", parent=self.root)
            return
        if price.count('.') > 1:
            self.engine.say('Price can only have one decimal point.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Price can only have one decimal point.", parent=self.root)
            return

        # Insert product into database
        cur.execute("INSERT INTO product(Pro_Category, Pro_Supplier, Pro_Name, Pro_Price, Pro_Quantity, Pro_Status) VALUES (?, ?, ?, ?, ?, ?)", (
            cat, supplier, name, price, qty, status
        ))
        conn.commit()
        self.engine.say('Product added successfully.')
        self.engine.runAndWait()
        messagebox.showinfo("Success", "Product added successfully", parent=self.root)
        self.show()

     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

 
    def show(self):        
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            cur.execute("Select *  from product ")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))             
        row=content['values']
        #print(row)
        self.var_Pro_Id.set(row[0])
        self.var_cat.set(row[1])
        self.var_supplier.set(row[2])
        self.var_product_name.set(row[3])
        self.var_product_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_product_status.set(row[6])
       
    def update(self):
     try:
        # Validate product name
        name = self.var_product_name.get().strip()
        if name == "":
            self.engine.say('Please enter the Name.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the Name.", parent=self.root)
            return
        if any(char.isdigit() for char in name):
            self.engine.say('Name cannot contain numeric characters.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Name cannot contain numeric characters.", parent=self.root)
            return

        # Validate dropdowns
        if self.var_cat.get() in ["Select", "Select your Category "]:
            self.engine.say('Please select a proper category.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a proper category.", parent=self.root)
            return

        if self.var_supplier.get() in ["Select", "Select your Supplier "]:
            self.engine.say('Please select a proper supplier.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a proper supplier.", parent=self.root)
            return

        if self.var_product_status.get() in ["", "Select your Status "]:
            self.engine.say('Please select a proper status.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select a proper status.", parent=self.root)
            return

        # Validate quantity
        qty = self.var_qty.get().strip()
        if qty == "":
            self.engine.say('Please enter the Quantity.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the Quantity.", parent=self.root)
            return
        if not qty.isdigit():
            self.engine.say('Quantity should only contain digits.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Quantity should only contain digits.", parent=self.root)
            return

        # Validate price
        price = self.var_product_price.get().strip()
        if price == "":
            self.engine.say('Please enter the Price.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the Price.", parent=self.root)
            return
        if not price.replace('.', '', 1).isdigit():
            self.engine.say('Price should be a number.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Price should be a number.", parent=self.root)
            return
        if price.count('.') > 1:
            self.engine.say('Price can have only one decimal point.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Price can have only one decimal point.", parent=self.root)
            return

        # Check for duplicate product name (excluding current product)
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT Pro_Id FROM product WHERE Pro_Name=? AND Pro_Id!=?", (name, self.var_Pro_Id.get()))
        duplicate = cur.fetchone()
        if duplicate:
            self.engine.say('This product name already exists.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "This product name already exists. Try a different one.", parent=self.root)
            return

        # Update the product
        cur.execute("""
            UPDATE product 
            SET Pro_Category=?, Pro_Supplier=?, Pro_Name=?, Pro_Price=?, Pro_Quantity=?, Pro_Status=? 
            WHERE Pro_Id=?
        """, (
            self.var_cat.get(),
            self.var_supplier.get(),
            name,
            price,
            qty,
            self.var_product_status.get(),
            self.var_Pro_Id.get()
        ))
        conn.commit()
        self.engine.say('Product Updated Successfully.')
        self.engine.runAndWait()
        messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
        self.show()

     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    
    def delete(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try:
            if self.var_Pro_Id.get()=="":
                self.engine.say('Select Product from list')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Select Product from list",parent=self.root)
            else:
                cur.execute("Select * from product where Pro_Id=?",(self.var_Pro_Id.get(),))  
                row=cur.fetchone()
                if row==None:
                    self.engine.say('Invaild Product')
                    self.engine.runAndWait()
                    messagebox.showerror("Error","Invaild Product",parent=self.root)
                else:
                    self.engine.say('Are You Sure ,That You Want To Delete The Information?')
                    self.engine.runAndWait()
                    op=messagebox.askyesno("Confirm","Are You Sure ,That You Want To Delete The Information?",parent=self.root)
                    if op==True:
                     cur.execute("delete from product where Pro_Id=?",(self.var_Pro_Id.get(),))
                     conn.commit()
                     self.engine.say('Information Successfully Deleted')
                     self.engine.runAndWait()
                     messagebox.showinfo("Deleted","Information Successfully Deleted",parent=self.root)
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                
    def clear(self):
        self.var_cat.set(""),
        self.var_supplier.set(""),
        self.var_product_name.set(""),
        self.var_product_price.set(""),
        self.var_qty.set(""),
        self.var_product_status.set(""),
        self.var_Pro_Id.set(""),
                          
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
    
    
    def search(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            if self.var_searchby.get()=="Select":
                self.engine.say('Select Search By Option')
                self.engine.runAndWait()
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                self.engine.say('Search input should be required')
                self.engine.runAndWait()
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select *  from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                    self.ProductTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
        
        
    
       
   
        
    
        
if __name__=="__main__":    
    root=Tk()
    obj=productClass(root)
    root.mainloop()
    
