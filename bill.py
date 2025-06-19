from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk ,messagebox
import sqlite3
import time
import os
import pyttsx3
import tempfile
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Quick Pick   |   Devloped by Sakshi "  )
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
        
        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        #===========title=========================
        #self.icon_title=PhotoImage(file="image/main.png")
        title=Label(self.root,text="Quick Pick " , compound=LEFT, 
                   font=("goudy old style" , 40 ,"bold") , bg="#010c48" , fg="white", anchor="w" ,padx=20).place(x=0, y=0 , relwidth= 1, height= 70)
        
        
        
        #========btn_logout========================
        btn_logout=Button(self.root , text="Logout" ,command=self.logout, font=("goudy old style", 15 ,"bold"), bg="yellow" , cursor= "hand2")
        btn_logout.place(x=1100, y=10 , width= 150, height= 50)
        
        
        #=========clock=============================
        self.lbl_clock=Label(self.root,text=" Welcome to Quick Pick  \t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS ",  
                             font=("goudy old style" ,15) , bg="#4d636d" , fg="white")
        self.lbl_clock.place(x=0, y=70 , relwidth= 1, height= 30)
        
        #============== Product frame=========================
        
        ProductFrame1=Frame(self.root, bd=4, bg="white",relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=560)
        
        title=Label(ProductFrame1, text= "All Product",font=("goudy old style", 20,"bold"), bg="black", fg="white")
        title.pack(side=TOP,fill=X)
        #======================= Product Search frame===========================
        self.var_search=StringVar()
        
        ProductFrame2=Frame(ProductFrame1, bd=4, bg="white",relief=RIDGE)
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2, text= "Search product | By  Name",font=("goudy old style", 15,"bold"), bg="white", fg="green")
        lbl_search.place(x=2,y=5)
        
        lbl_name=Label(ProductFrame2, text= "Product  Name",font=("goudy old style", 15,"bold"), bg="white")
        lbl_name.place(x=5,y=45)
        
        txt_search=Entry(ProductFrame2, textvariable=self.var_search,font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=135,y=47,width=150,height=22)
        
        btn_search=Button(ProductFrame2 , text="Search",command=self.search,font=(" goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=290,y=45,width=90, height=25)
        
        btn_show_all=Button(ProductFrame2 , text="Show All",command=self.show,font=("goudy old style", 15), bg="#0f4d7d", fg="white", cursor="hand2")
        btn_show_all.place(x=290,y=10,width=90, height=25)
        
        
        #==================== Product details====================
        
        ProductFrame3=Frame(ProductFrame1,bd=3, relief=RIDGE)
        ProductFrame3.place(x=2,y=140, width=398, height=385)
        
        scrolly=Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3, orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("Pro_Id","Pro_Name","Pro_Price", "Pro_Quantity","Pro_Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("Pro_Id",text="Prod-Id")
        self.product_Table.heading("Pro_Name",text="Name")
        self.product_Table.heading("Pro_Price", text="Price")
        self.product_Table.heading("Pro_Quantity", text="Quantity")
        self.product_Table.heading("Pro_Status",text="Status")
        
        self.product_Table["show"]="headings"
        
       
        self.product_Table.column("Pro_Id",width=30)
        self.product_Table.column("Pro_Name",width=90)
        self.product_Table.column("Pro_Price", width=50)
        self.product_Table.column("Pro_Quantity", width=60)
        self.product_Table.column("Pro_Status",width=50)
    
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        #self.show()
        
        
        lbl_note=Label(ProductFrame1, text= "Note : Enter 0 Quantity to remove product from the Cart ",font=("goudy old style", 13,"bold")
                       , bg="white", fg="red")
        lbl_note.pack(side=BOTTOM,fill=X)
        
#==================================  Customer frame ========================================   
        self.var_cname=StringVar()
        self.var_contact =StringVar()
        
        CustomerFrame=Frame(self.root,bd=3, relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110, width=530, height=70)
       
        ctitle=Label(CustomerFrame, text= "Customer Details",font=("goudy old style", 15), bg="lightgrey", fg="black")
        ctitle.pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame, text= "Name",font=("goudy old style", 15), bg="white")
        lbl_name.place(x=5,y=35)
        txt_name=Entry(CustomerFrame, textvariable=self.var_cname,font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=80,y=35,width=140)
        
        lbl_name=Label(CustomerFrame, text= "Contact-No",font=("goudy old style", 15), bg="white")
        lbl_name.place(x=240,y=35)
        txt_name=Entry(CustomerFrame, textvariable=self.var_contact,font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=360,y=35,width=150)
        validate_contact=self.root.register(self.checkcontact)
        txt_name.config(validate='key',validatecommand=(validate_contact,'%P'))
        
#===============================================cal_cart========================
       
        Cal_Cart_Frame=Frame(self.root,bd=3, relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190, width=530, height=360) 
 #========================================cal cart frame==================================       
        self.var_cal_input=StringVar()
        
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9, relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=4, width=268, height=345) 
        
        
        self.txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,"bold"), justify="right",state="readonly",width=21,bd=10,relief=GROOVE)
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text="7",font=('arial',15,"bold"),command=lambda:self.get_input(7),width=4,pady=12,cursor="hand2",bd=5).grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=('arial',15,"bold"),command=lambda:self.get_input(8),width=4,pady=12,cursor="hand2",bd=5).grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=('arial',15,"bold"),command=lambda:self.get_input(9),width=4,pady=12,cursor="hand2",bd=5).grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font=('arial',15,"bold"),command=lambda:self.get_input("+"),width=4,pady=12,cursor="hand2",bd=5).grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text="4",font=('arial',15,"bold"),command=lambda:self.get_input(4),width=4,pady=12,cursor="hand2",bd=5).grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=('arial',15,"bold"),command=lambda:self.get_input(5),width=4,pady=12,cursor="hand2",bd=5).grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=('arial',15,"bold"),command=lambda:self.get_input(6),width=4,pady=12,cursor="hand2",bd=5).grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=('arial',15,"bold"),command=lambda:self.get_input("-"),width=4,pady=12,cursor="hand2",bd=5).grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text="1",font=('arial',15,"bold"),command=lambda:self.get_input(1),width=4,pady=12,cursor="hand2",bd=5).grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=('arial',15,"bold"),command=lambda:self.get_input(2),width=4,pady=12,cursor="hand2",bd=5).grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=('arial',15,"bold"),command=lambda:self.get_input(3),width=4,pady=12,cursor="hand2",bd=5).grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=('arial',15,"bold"),command=lambda:self.get_input("*"),width=4,pady=12,cursor="hand2",bd=5).grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text="0",font=('arial',15,"bold"),command=lambda:self.get_input(0),width=4,pady=12,cursor="hand2",bd=5).grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text="c",font=('arial',15,"bold"),command=self.clear_cal,width=4,pady=12,cursor="hand2",bd=5).grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font=('arial',15,"bold"),command=self.perform_cal,width=4,pady=12,cursor="hand2",bd=5).grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=('arial',15,"bold"),command=lambda:self.get_input("/"),width=4,pady=12,cursor="hand2",bd=5).grid(row=4,column=3)
        
        
#=====================  cart frame===============      
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3, relief=RIDGE)
        Cart_Frame.place(x=275,y=4, width=245, height=345)
        
        self.ctitle=Label(Cart_Frame, text= "Cart \t Total Product: [0]",font=("goudy old style", 15), bg="lightgrey", fg="black")
        self.ctitle.pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(Cart_Frame, orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame, orient=HORIZONTAL)
        
        self.CartTable=ttk.Treeview(Cart_Frame,columns=("Pro_Id","Pro_Name","Pro_Price", "Pro_Quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("Pro_Id",text="Prod-Id")
        self.CartTable.heading("Pro_Name",text="Name")
        self.CartTable.heading("Pro_Price", text="Price")
        self.CartTable.heading("Pro_Quantity", text="Quantity")
        
        
        self.CartTable["show"]="headings"
        
       
        self.CartTable.column("Pro_Id",width=60)
        self.CartTable.column("Pro_Name",width=60)
        self.CartTable.column("Pro_Price", width=60)
        self.CartTable.column("Pro_Quantity", width=60)
        
    
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
       
       
       
       
       
#==============================add cart widgets frame======================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_stock=StringVar()
        
          
        Add_CartWidgetsFrame=Frame(self.root,bd=3, relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550, width=530, height=120) 
        
        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name", font=("goudy old style", 15),bg="white")
        lbl_p_name.place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname, font=("goudy old style", 15) ,bg='lightyellow',state="readonly")
        txt_p_name.place(x=5,y=35,width=160,height=22)
        
        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty", font=("goudy old style", 15),bg="white")
        lbl_p_price.place(x=180,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price, font=("goudy old style", 15) ,bg='lightyellow',state="readonly")
        txt_p_price.place(x=180,y=35,width=150,height=22)
        
        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity", font=("goudy old style", 15),bg="white")
        lbl_p_qty.place(x=350,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_quantity, font=("goudy old style", 15) ,bg='lightyellow')
        txt_p_qty.place(x=350,y=35,width=150,height=22)
        
        self.lbl_instock=Label(Add_CartWidgetsFrame,text="In Stock ", font=("goudy old style", 15),bg="white")
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear=Button(Add_CartWidgetsFrame, text="Clear",command=self.clear_cart,font=("goudy old style ", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=180,y=70,width=150, height=30)
        
        btn_add=Button(Add_CartWidgetsFrame, text="Add | Update Cart",command=self.add_update_cart,font=("goudy old style ", 15), bg="orange", fg="white", cursor="hand2")
        btn_add.place(x=340,y=70,width=180, height=30)
 
 
     #========================bill area===========
    
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410) 
        
        bill_title=Label(billFrame, text= "Customer Bill Area",font=("goudy old style", 20,"bold"), bg="#262626", fg="white")
        bill_title.pack(side=TOP,fill=X)   
        
        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #============================bill button=====================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=150)
        
        self.lbl_amt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style ", 15), bg="#C1CDCD", fg="black")
        self.lbl_amt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billMenuFrame,text="Discount \n[5%]",font=("goudy old style ", 15), bg="#76EEC6", fg="black")
        self.lbl_discount.place(x=126,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style ", 15), bg="#EE6A50", fg="black")
        self.lbl_net_pay.place(x=250,y=5,width=150,height=70)
        
        
        btn_print=Button(billMenuFrame, text="Print",command=self.print_bill,font=("goudy old style ", 15), bg="#00BFFF", fg="black", cursor="hand2")
        btn_print.place(x=2,y=80,width=120, height=50)
        
        btn_clear_all=Button(billMenuFrame, text="Clear All",command=self.clear_all,font=("goudy old style ", 15), bg="#BCD22E", fg="black", cursor="hand2")
        btn_clear_all.place(x=126,y=80,width=120, height=50)
        
        btn_generate=Button(billMenuFrame, text="Generate Bill",command=self.generate_bill,font=("goudy old style ", 15), bg="#8968CD", fg="black", cursor="hand2")
        btn_generate.place(x=250,y=80,width=150, height=50)
 #======================FOOTER=======================
 
        lbl_footer=Label(self.root,text="Quick Pick | Sakshi and Sushma \n Any technical issue contact use ",  
                             font=("goudy old style " ,10) , bg="#4d636d" , fg="white")  
        lbl_footer.pack(side=BOTTOM,fill=BOTH)
 
        self.show()
        #self.bill_top()
        self.update_date_time()
        
        
        
        
#==============================All Function==================

#=============calculator======
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set("")
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
        
#======================

    def show(self):        
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            #self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","Name","Price", "Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("Select Pro_Id  ,Pro_Name , Pro_Price,Pro_Quantity,Pro_Status from product where Pro_Status='Active'  ")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
        
    def search(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            
            if self.var_search.get()=="":
                self.engine.say('Search input should be required..')
                self.engine.runAndWait()
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select Pro_Id ,Pro_Name , Pro_Price,Pro_Quantity,Pro_Status from product  where Pro_Name LIKE '%"+self.var_search.get()+"%' and Pro_Status='Active' ")
                rows=cur.fetchall()
                if len(rows)!=0:
                   self.product_Table.delete(*self.product_Table.get_children())
                   for row in rows:
                    self.product_Table.insert('',END,values=row)
                else:
                    self.engine.say('No Result Found!!!..')
                    self.engine.runAndWait()
                    messagebox.showerror("Error","No Result Found!!!", parent=self.root)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   
       
       
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))             
        row=content['values']
        #print(row) pid  ,Name , Price,Quantity,Status
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set('1')
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        
        
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))             
        row=content['values']
        #print(row) pid  ,Name , Price,Quantity,Status
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
       
       
    def add_update_cart(self):
        if self.var_pid.get()=="":
                self.engine.say('Please Select The Product From List..')
                self.engine.runAndWait()
                messagebox.showerror("Error","Please Select The Product From List",parent=self.root)  
        elif self.var_quantity.get()=="":
                self.engine.say('Quantity is Required..')
                self.engine.runAndWait()  
                messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif int(self.var_quantity.get()) > int(self.var_stock.get()):
                self.engine.say('Product is not in stock !!!')
                self.engine.runAndWait()  
                messagebox.showerror("Error","Product is not in stock !!!",parent=self.root)
        else:  
                #price_cal=(int(self.var_quantity.get())*float(self.var_price.get()))
                #price_cal=float(price_cal)
                price_cal=self.var_price.get()
                #pid  ,Name , Price,Quantity,Status
                cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_quantity.get(),self.var_stock.get()]
                #print(self.cart_list)
                
                #=======update cart=========
                present="no"
                index_=0
                for row in self.cart_list:
                      if self.var_pid.get()==row[0]:
        
                          present="yes"
                          break
                      index_+=1
                if present=="yes":
                    self.engine.say('Product is already present ... So do you want to Update  or Remove it From cart list?')
                    self.engine.runAndWait()
                    op=messagebox.askyesno("Confirm", "Product is already present ... So do you want to Update  or Remove it From cart list? ",parent=self.root)
                    if op==True:
                        if self.var_quantity.get()=="0":
                            self.cart_list.pop(index_)
                        else:
                            #pid  ,Name , Price,Quantity,Status
                            #self.cart_list[index_][2]=price_cal#price
                            self.cart_list[index_][3]=self.var_quantity.get()#qty
                            
                else:
                      self.cart_list.append(cart_data)
                self.show_cart()
                self.bill_update()
    
    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discoumt=0
        for row in self.cart_list:
            #pid  ,Name , Price,Quantity,Status
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discoumt=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discoumt
        self.lbl_amt.config( text=f"Bill Amount \n[{str(self.bill_amnt)}]")
        self.lbl_net_pay.config( text=f"Net Pay\n[{str(self.net_pay)}]")
        self.ctitle.config(text= f"Cart \t Total Product: [{str(len(self.cart_list))}]")
    
    
    def show_cart(self):
        try: 
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
                    
    
    
    def generate_bill(self):
        if self.var_cname.get()==''or self.var_contact.get()=='' or len(self.var_contact.get())!=10 or not self.var_contact.get().isdigit() or not self.var_contact.get().startswith(("7", "8", "9")):
            self.engine.say('Please enter your valid Contact number and Name.. Contact no should start with 7,8,9 ')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter your valid Contact number and Name. Contact no should start with 7,8,9 ",parent=self.root)
        
               
        else:
            #==========Bill Top====================
            self.bill_top()
            #==========Bill middle====================
            self.bill_middle()
            #==========Bill bottom====================
            self.bill_bottom()
             
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            self.engine.say('Your Bill Has been Generated.')
            self.engine.runAndWait()
            messagebox.showinfo('Saved','Your Bill Has Been Generated ',parent=self.root) 
            self.chk_print=1
            
            
            
            
            
            
            
            
            
                  
                
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y")) 
        bill_top_temp=f'''
\t\tHare Krishna General Store
\t Mr.Jalaram Narayanlal Medatiya
\t Phone Number:- 88287928**,Thane-400608
{str("="*47)}  
 Customer Name:- {self.var_cname.get()}
 Phone Name:- {self.var_contact.get()}
 Bill Number:- {str(self.invoice)}\t\t  Date:- {str(time.strftime("%d/%m/%Y"))} 
{str("="*47)}
  Product Name\t\t\tQuantity\t\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)        
                
    
    
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\tRs.{self.bill_amnt}
 Discount\t\t\tRs.{self.discoumt}
 Net Pay\t\t\tRs.{self.net_pay}
{str("="*47)}\n           
        '''        
        self.txt_bill_area.insert(END,bill_bottom_temp)          
                
                
    def bill_middle(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
           for row in self.cart_list:
            
            Pro_Id=row[0]
            Name=row[1]
            Pro_Quantity=(int(row[4])-int(row[3]))
            if int(row[3])==int(row[4]):
                Pro_Status='Inactive'
            if int(row[3])!=int(row[4]):
                Pro_Status='Active'
            Price=float(row[2])*int(row[3])
            Price=str(Price)
            self.txt_bill_area.insert(END,"\n"+Name+"\t\t\t"+row[3]+"\tRs."+Price)
            #================update qty in product table====================
            cur.execute('Update Product set Pro_Quantity=?, Pro_Status=? where Pro_Id=?',(
                Pro_Quantity,
                Pro_Status,
                Pro_Id
            )) 
            conn.commit()  
            conn.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)             
                
    def clear_cart(self):    
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.lbl_instock.config(text=f"In Stock ")
        self.var_stock.set('')
              
                
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.ctitle.config(text= f"Cart \t Total Product: [0]")
        self.clear_cart()
        self.show()
        self.show_cart()
                   
                
    def update_date_time(self): 
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Quick Pick  \t\t Date: {str(date_)}\t\t Time: {str(time_)} ")          
        self.lbl_clock.after(200,self.update_date_time)      
                
    def print_bill(self):
        if self.chk_print==1:
            self.engine.say('Please wait will printing..')
            self.engine.runAndWait()
            messagebox.showinfo('Print','Please wait will printing',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))    
            os.startfile(new_file,'print')
        else: 
            self.engine.say('Please generate bill to print..')
            self.engine.runAndWait()           
            messagebox.showerror('Print','Please generate bill to print',parent=self.root)  
            
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")   
              
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            self.engine.say('Invalid Entry')
            self.engine.runAndWait()
            messagebox.showerror('Invalid','Invalid Entry')
            return False
if __name__=="__main__":    
           root=Tk()
           obj=BillClass(root)
           root.mainloop()