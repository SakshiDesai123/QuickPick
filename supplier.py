from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk ,messagebox
import sqlite3 
import re
import pyttsx3
class supplierClass :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Quick Pick      | Devloped by Sakshi "  )
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=============================================
        
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        
        #==============All Variable============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_supp_id=StringVar()
        self.var_supp_name=StringVar()
        self.var_supp_contact=StringVar()
        self.var_supp_Address=StringVar()
        self.var_supp_email=StringVar()
        self.var_supp_gst=StringVar()
        
        
        #=======self.root======
        SearchFrame=LabelFrame(self.root,text="Search Supplier" ,  font= ("goudy old style  ", 10, "bold" ),bg="white", relief=RIDGE, bd=3)
        SearchFrame.place(x=600,y=60,width=450,height=55)
    
        
        #==========option==========
        cmb_search=ttk.Combobox (SearchFrame,textvariable=self.var_searchby, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",12),values=("Select","Supp_Id", " Supp_Name", " Supp_Contact"))
        cmb_search.place(x=10,y=0.6,width=150)
        cmb_search.current(0)
        
        
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=("goudy old style ", 15 ), bg="lightyellow")
        txt_search.place(x=170,y=0.6, width=120)
        
        btn_search=Button(SearchFrame, text="Search",command=self.search,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=300,y=0.6,width=90, height=27)
        
        
        
        #======================title===============
        self.icon_title=PhotoImage(file="image/supplier.png")
        title=Label(self.root, text= "Supplier Details",image=self.icon_title,compound=LEFT,font=("goudy old style", 30, "bold"), bg="#0f4d7d", padx=20,fg="white")
        title.place(x=50,y=10,width=1000, height=50)
        
        
        #=========content===================
        
        #==============row1=========
        lbl_suppinvoce=Label(self.root, text= "Supp - ID",font=("goudy old style", 15), bg="white")
        lbl_suppinvoce.place(x=80,y=80)
        txt_suppinvoce=Entry(self.root, textvariable=self.var_supp_id,font=("goudy old style", 15), bg="lightyellow")
        txt_suppinvoce.place(x=180,y=80,width=180)
        
        lbl_name=Label(self.root, text= "Name",font=("goudy old style", 15), bg="white")
        lbl_name.place(x=80,y=120)
        txt_name=Entry(self.root, textvariable=self.var_supp_name,font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=180,y=120,width=180)
        
        lbl_contact=Label(self.root, text= "Contact-No",font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=80,y=160)
        txt_contact=Entry(self.root, textvariable=self.var_supp_contact,font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=180,y=160,width=180)
        
        
        
        
        lbl_email=Label(self.root, text= "Email-Id",font=("goudy old style", 15), bg="white")
        lbl_email.place(x=80,y=200)
        txt_email=Entry(self.root, textvariable=self.var_supp_email,font=("goudy old style", 15), bg="lightyellow")
        txt_email.place(x=180,y=200,width=180)
        
        lbl_gst=Label(self.root, text= "GST_Id",font=("goudy old style", 15), bg="white")
        lbl_gst.place(x=80,y=240)
        txt_gst=Entry(self.root, textvariable=self.var_supp_gst,font=("goudy old style", 15), bg="lightyellow")
        txt_gst.place(x=180,y=240,width=180)
        
        
        #validate_id=self.root.register(self.checkid)
        #txt_suppinvoce.config(validate='key',validatecommand=(validate_id,'%P'))
        
        
       
       
        #validate_contact=self.root.register(self.checkcontact)
        #txt_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
        
        
       
        lbl_desc=Label(self.root, text="Address",font=("goudy old style", 15), bg="white")
        lbl_desc.place(x=80,y=280)
        
        self.txt_desc=Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180,y=280,width=180,height=30)
        
       
        
       
        
        
        #==================================BUTTON=======================
        
        btn_update=Button(self.root, text="Update",command=self.update ,  font=("goudy old style ", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_update.place(x=70,y=360,width=110, height=35)
        
        btn_add=Button(self.root, text="Save",command=self.add , font=("goudy old style ", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_add.place(x=185,y=360,width=110, height=35)
        
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_delete.place(x=300,y=360,width=110, height=35)
        
        btn_clear=Button(self.root, text="Clear",command=self.clear , font=("goudy old style ", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=415,y=360,width=110, height=35)
        
        
        
        #==============================supp details============
        
        supp_frame=Frame(self.root,bd=3, relief=RIDGE)
        supp_frame.place(x=540,y=120, width=550, height=350)
        
        scrolly=Scrollbar(supp_frame, orient=VERTICAL)
        scrollx=Scrollbar(supp_frame, orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(supp_frame,columns=("Supp_Id","Supp_Name", "Supp_Contact", "Supp_Email","Supp_Gst_id","Supp_Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("Supp_Id",text="Supp-ID")
        self.SupplierTable.heading("Supp_Name", text="Supp_Name")
        self.SupplierTable.heading("Supp_Contact",text="Contact")
        self.SupplierTable.heading("Supp_Email",text="email")
        self.SupplierTable.heading("Supp_Gst_id",text="gst_id")
        self.SupplierTable.heading("Supp_Address",text="Address")
        
        self.SupplierTable["show"]="headings"
        
       
        
        self.SupplierTable.column("Supp_Id",width=100)
        self.SupplierTable.column("Supp_Name", width=100)
        self.SupplierTable.column("Supp_Contact", width=100)
        
        self.SupplierTable.column("Supp_Email",width=100)
        self.SupplierTable.column("Supp_Gst_id",width=100)
        self.SupplierTable.column("Supp_Address",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
#================================================main=========================================


    def add(self):
        try:
         conn = sqlite3.connect('employee.db')
         cur = conn.cursor()

        # Check for Supplier ID
         if self.var_supp_id.get() == "" or len(self.var_supp_id.get()) == 0 or not self.var_supp_id.get().isdigit():
            self.engine.say('Supplier Id is required' if self.var_supp_id.get() == "" else 'Invalid Entry of Supplier Id, it should contain only digits')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Supplier Id is required." if self.var_supp_id.get() == "" else 'Invalid Entry of Supplier Id \n It should contain only digits', parent=self.root)
            return False
        
        # Check for Supplier Name
         elif self.var_supp_name.get() == "":
            self.engine.say('Please enter the Name.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the Name.", parent=self.root)
            return False
        
        # Check for numeric characters in the Supplier Name
         elif any(char.isdigit() for char in self.var_supp_name.get()):
            self.engine.say('Name cannot contain numeric characters.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Name cannot contain numeric characters.", parent=self.root)
            return False
        
        # Check for valid email format
         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
         if not re.match(email_pattern, self.var_supp_email.get()):
            self.engine.say('Invalid email format.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid email format. Eg:- sakshidesai123@gamil.com", parent=self.root)
            return False

        # Check for valid gst_id format
         gst_pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}Z[0-9]{1}$'
         if not re.match(gst_pattern, self.var_supp_gst.get()):
            self.engine.say('Invalid gst_id format.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid gst_id format.", parent=self.root)
            return False

        # Check for Supplier Contact
         elif self.var_supp_contact.get() == "" or len(self.var_supp_contact.get()) != 10 or not self.var_supp_contact.get().isdigit() or not self.var_supp_contact.get().startswith(("7", "8", "9")):
            self.engine.say('Please enter a valid 10-digit Contact number. Contact no should start with 7,8,9.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter a valid 10-digit Contact number. contact no should start with 7, 8, 9.", parent=self.root)
            return False

         else:
            cur.execute("INSERT INTO supplier(Supp_Id, Supp_Name, Supp_Contact, Supp_Email, Supp_Gst_id, Supp_Address) VALUES (?, ?, ?, ?, ?, ?)", (
                self.var_supp_id.get(),
                self.var_supp_name.get(),
                self.var_supp_contact.get(),
                self.var_supp_email.get(),
                self.var_supp_gst.get(),
                self.txt_desc.get('1.0', 'end')
            ))
            conn.commit()
            self.engine.say('Supplier Added Successfully')
            self.engine.runAndWait()
            messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
            self.show()
    
        except Exception as ex:
          messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):        
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            cur.execute("Select *  from supplier ")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))             
        row=content['values']
        #print(row)
        self.var_supp_id.set(row[0])
        self.var_supp_name.set(row[1])
        self.var_supp_contact.set(row[2])
        self.var_supp_email.set(row[3])
        self.var_supp_gst.set(row[4])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[5]),
        
        
        
        
    def update(self):
     try:
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        # Supplier ID validation
        if self.var_supp_id.get() == "" or not self.var_supp_id.get().isdigit():
            self.engine.say('Supplier ID is required and should be digits only.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Supplier ID is required and should contain only digits.", parent=self.root)
            return

        # Name validation
        name = self.var_supp_name.get().strip()
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

        # Email validation
        email = self.var_supp_email.get().strip()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            self.engine.say('Invalid email format.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid email format.", parent=self.root)
            return

        # GST ID validation
        gst = self.var_supp_gst.get().strip()
        gst_pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}Z[0-9]{1}$'
        if not re.match(gst_pattern, gst):
            self.engine.say('Invalid GST ID format.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid GST ID format.", parent=self.root)
            return

        # Contact validation
        contact = self.var_supp_contact.get().strip()
        if contact == "" or len(contact) != 10 or not contact.isdigit() or not contact.startswith(("7", "8", "9")):
            self.engine.say('Please enter a valid 10-digit Contact number starting with 7, 8, or 9.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Contact must be 10 digits and start with 7, 8, or 9.", parent=self.root)
            return

        # All validations passed, update the record
        cur.execute("""UPDATE supplier 
                       SET Supp_Name=?, Supp_Contact=?, Supp_Email=?, Supp_Gst_id=?, Supp_Address=? 
                       WHERE Supp_Id=?""", (
            name,
            contact,
            email,
            gst,
            self.txt_desc.get('1.0', END).strip(),
            self.var_supp_id.get()
        ))
        conn.commit()
        self.engine.say('Supplier Updated Successfully.')
        self.engine.runAndWait()
        messagebox.showinfo("Success", "Supplier Updated Successfully.", parent=self.root)
        self.show()

     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

            
    
    
    def delete(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try:
            if self.var_supp_id.get()=="":
                self.engine.say('Supplier Id Must Be Required')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Supplier Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Supp_Id=?",(self.var_supp_id.get(),))  
                row=cur.fetchone()
                if row==None:
                    self.engine.say('Invaild Suppliere ID')
                    self.engine.runAndWait()
                    messagebox.showerror("Error","Invaild Suppliere ID",parent=self.root)
                else:
                    self.engine.say('Are You Sure ,That You Want To Delete The Information?')
                    self.engine.runAndWait()
                    op=messagebox.askyesno("Confirm","Are You Sure ,That You Want To Delete The Information?",parent=self.root)
                    if op==True:
                     cur.execute("delete from supplier where Supp_Id=?",(self.var_supp_id.get(),))
                     conn.commit()
                     self.engine.say('Information Successfully Deleted')
                     self.engine.runAndWait()
                     messagebox.showinfo("Deleted","Information Successfully Deleted",parent=self.root)
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                
    def clear(self):
        self.var_supp_id.set("")
        self.var_supp_name.set("")
        self.var_supp_contact.set("")
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
    
    
    def search(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            if self.var_searchby.get()=="Select":
                self.engine.say('Select Search By Option.')
                self.engine.runAndWait()
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                self.engine.say('Search input should be required.')
                self.engine.runAndWait()
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select *  from supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                for row in rows:
                    self.SupplierTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
if __name__=="__main__":    
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()