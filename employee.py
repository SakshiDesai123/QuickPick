
from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import datetime
import sqlite3
import pyttsx3
import re

#import pyttsx3
class employeeClass :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Grocery Shopping Managment System   | Devloped by Sakshi"  )
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=============================================
        
        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        
        
        #==============All Variable============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_salary=StringVar()
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_pass=StringVar()
        self.var_emp_utype=StringVar()
        self.check_var=IntVar()
              
        
        #=======searchframe=========
        SearchFrame=LabelFrame(self.root,text="Search Employee" ,  font= ("goudy old style  ", 10, "bold" ),bg="white", relief=RIDGE, bd=3)
        SearchFrame.place(x=250,y=1,width=600,height=70)
        
        
        
        #==========option==========
        cmb_search=ttk.Combobox (SearchFrame,textvariable=self.var_searchby, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",12),values=("Select","Emp_Id", " Emp_Name", " Emp_Contact", "Emp_Email"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=("goudy old style ", 15 ), bg="lightyellow")
        txt_search.place(x=200,y=10)
        
        btn_search=Button(SearchFrame, text="Search", command=self.search, font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=430,y=9,width=130, height=27)
        
        
        
        #======================title===============
        self.icon_title=PhotoImage(file="image/emp2.png")
        title=Label(self.root, text= "Employee Details",image=self.icon_title,compound=LEFT,font=("goudy old style", 30),bd=2, bg="#0f4d7d", fg="white", padx=20)
        title.place(x=50,y=80,width=1000)
        
        
        #=========content===================
        
        
        #==============row1=========
        lbl_empid=Label(self.root, text= "Emp-ID",font=("goudy old style", 15), bg="white")
        lbl_empid.place(x=50,y=150)
        lbl_name=Label(self.root, text= "Employee Name",font=("goudy old style", 15),bd=4, bg="white")
        lbl_name.place(x=350,y=150)
        lbl_contact=Label(self.root, text= "Contact-No",font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=750,y=150)
        
        txt_empid=Entry(self.root, textvariable=self.var_emp_id,font=("goudy old style", 15), bg="lightyellow")
        txt_empid.place(x=150,y=150,width=180)
        #validate_id=self.root.register(self.checkid)
        #txt_empid.config(validate='key',validatecommand=(validate_id,'%P'))
        
        txt_name=Entry(self.root, textvariable=self.var_emp_name,font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=500,y=150,width=180)
        # bind  validation register
        
        
        txt_contact=Entry(self.root, textvariable=self.var_emp_contact,font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=850,y=150,width=180)
        # bind  validation register
        #validate_contact=self.root.register(self.checkcontact)
        #txt_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
        
        
        #==================row2=================
        lbl_email=Label(self.root, text= "Email-ID",font=("goudy old style", 15), bg="white")
        lbl_email.place(x=50,y=190)
        
        lbl_gender=Label(self.root, text= "Gender",font=("goudy old style", 15), bg="white")
        lbl_gender.place(x=350,y=190)
        lbl_dob=Label(self.root, text= "D.O.B",font=("goudy old style", 15), bg="white")
        lbl_dob.place(x=750,y=190)
        
        txt_email=Entry(self.root, textvariable=self.var_emp_email,font=("goudy old style", 15), bg="lightyellow")
        txt_email.place(x=150,y=190,width=180)
        
        
        txt_gender=Entry(self.root, textvariable=self.var_emp_gender,font=("goudy old style", 15), bg="lightyellow")
        txt_gender.place(x=500,y=190,width=180)
        cmb_gender=ttk.Combobox (self.root,textvariable=self.var_emp_gender, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",15),values=("","Male", "Female", "Other"))
        cmb_gender.place(x=500,y=190,width=180)
        cmb_gender.current(0)
        txt_dob=Entry(self.root, textvariable=self.var_emp_dob,font=("goudy old style", 15), bg="lightyellow")
        txt_dob.place(x=850,y=190,width=180)
        
        
        #=================row3====================
        lbl_pass=Label(self.root, text= "Password",font=("goudy old style", 15), bg="white")
        lbl_pass.place(x=50,y=230)
        lbl_doj=Label(self.root, text= "D.O.J",font=("goudy old style", 15), bg="white")
        lbl_doj.place(x=350,y=230)
        lbl_utype=Label(self.root, text= "User Type",font=("goudy old style", 15), bg="white")
        lbl_utype.place(x=750,y=230)
        
        txt_pass=Entry(self.root, textvariable=self.var_emp_pass,font=("goudy old style", 15), bg="lightyellow")
        txt_pass.place(x=150,y=230,width=180)
        
       
        
        
        txt_doj=Entry(self.root, textvariable=self.var_emp_doj,font=("goudy old style", 15), bg="lightyellow")
        txt_doj.place(x=500,y=230,width=180)
         # Binding validation register
        
        
        
        txt_utype=Entry(self.root, textvariable=self.var_emp_utype,font=("goudy old style", 15), bg="lightyellow")
        txt_utype.place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox (self.root,textvariable=self.var_emp_utype, state='readonly', justify=CENTER, 
                                 font= ("goudy old style ",15),values=("","Admin","Employee", ))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
        
        #=====================row4======================
        
        lbl_salary=Label(self.root, text= "Salary",font=("goudy old style", 15), bg="white")
        lbl_salary.place(x=50,y=270)
        lbl_address=Label(self.root, text= "Address",font=("goudy old style", 15), bg="white")
        lbl_address.place(x=350,y=270)
        
        txt_salary=Entry(self.root, textvariable=self.var_emp_salary,font=("goudy old style", 15), bg="lightyellow")
        txt_salary.place(x=150,y=270,width=180)
        # Binding validation register
        
        self.txt_address=Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=450,y=270,width=350,height=60)
        
        
         #===========Checkbutton================
        check_frame=Frame(self.root)
        check_frame.place(x=70,y=310,width=300,height=80)

        
        check_btn=Checkbutton(check_frame,text="Above detail are totally correct. ", variable=self.check_var, font=("goudy old style", 15),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        
        self.check_lbl=Label(check_frame, text= "",font=("goudy old style", 15), fg="red")
        self.check_lbl.grid(row =1,column=0,padx=10,sticky=W)

        
       
        
        #==================================BUTTON=======================
        
        btn_update=Button(self.root, text="Update",command=self.update,font=("goudy old style ", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_update.place(x=500,y=340,width=110, height=28)
        
        btn_add=Button(self.root, text="Save", command=self.add,font=("goudy old style ", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_add.place(x=620,y=340,width=110, height=28)
        
        btn_delete=Button(self.root, text="Delete",command=self.delete,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_delete.place(x=740,y=340,width=110, height=28)
        
        btn_clear=Button(self.root, text="Clear",command=self.clear,font=("goudy old style ", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=860,y=340,width=110, height=28)
        
        
        
        #==============================emp details============
        
        emp_frame=Frame(self.root,bd=3, relief=RIDGE)
        emp_frame.place(x=0,y=380, relwidth=1, height=120)
        
        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("Emp_Id","Emp_Name", "Emp_Contact", "Emp_Email","Emp_Gender","Emp_DOB","Emp_Password","Emp_DOJ","Emp_Utype","Emp_Salary","Emp_Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("Emp_Id",text="Emp-ID")
        self.EmployeeTable.heading("Emp_Name", text="Emp_Name")
        self.EmployeeTable.heading("Emp_Contact", text="Emp_Contact")
        self.EmployeeTable.heading("Emp_Email",text="Emp_Email")
        self.EmployeeTable.heading("Emp_Gender",text="Emp_Gender")
        self.EmployeeTable.heading("Emp_DOB", text="D.O.B")
        self.EmployeeTable.heading("Emp_Password",text="Emp_Password")
        self.EmployeeTable.heading("Emp_DOJ",text="D.O.J")
        self.EmployeeTable.heading("Emp_Utype" ,text="Utype")
        self.EmployeeTable.heading("Emp_Salary",text="Salary")
        self.EmployeeTable.heading("Emp_Address",text="Address")
        
        
        self.EmployeeTable["show"]="headings"
        
       
        self.EmployeeTable.column("Emp_Id",width=60)
        self.EmployeeTable.column("Emp_Name", width=100)
        self.EmployeeTable.column("Emp_Contact", width=100)
        self.EmployeeTable.column("Emp_Email",width=100)
        self.EmployeeTable.column("Emp_Gender",width=100)
        self.EmployeeTable.column("Emp_DOB", width=100)
        self.EmployeeTable.column("Emp_Password",width=100)
        self.EmployeeTable.column("Emp_DOJ",width=100)
        self.EmployeeTable.column("Emp_Utype" ,width=100)
        self.EmployeeTable.column("Emp_Salary",width=100)
        self.EmployeeTable.column("Emp_Address",width=200)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
    #==================validation==============================
   #call back fun 
    
        
    
    #def checkcontact(self,contact):
        
        
    
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
               return True
            else:
                self.engine.say('Enter valid password.Password should contain special character,number,alphabet,starting should be a capital letter \n(Example:Sakshi@05)')
                self.engine.runAndWait()
                messagebox.showerror('Invalid','Enter valid password.\nPassword should contain special character,number,alphabet,starting should be a capital letter \n(Example:Sakshi@05)')
                return False
        else:
             self.engine.say('Length try to exceed')
             self.engine.runAndWait()
             messagebox.showerror('Invalid','Length try to exceed')
             return False
         
         
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
               return True
            else:
                self.engine.say('Invalid Email Please Enter valid email (Example:sakshidesai05@gmail.com)')
                self.engine.runAndWait()
                messagebox.showerror('Alert',' Invalid Email Please Enter valid email .\n\n(Example:sakshidesai05@gmail.com)')
                
                return False
        else:
             self.engine.say('Email Length is too small.\n\n(Example:sakshidesai05@gmail.com)')
             self.engine.runAndWait()
             messagebox.showerror('Invalid',' Email Length is too small.\n\n(Example:sakshidesai05@gmail.com)')
             return False
    
    

    
       
    
       
        
        
   #========================== main ===============================
    def add(self):
            x = y = 0
            
    
    # Validating Employee ID
            if self.var_emp_id.get() == "" or len(self.var_emp_id.get()) == 0 or not self.var_emp_id.get().isdigit():
                self.engine.say('Employee Id is required' if self.var_emp_id.get() == "" else 'Invalid Entry of Employee Id it should contain only digits')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Employee Id is required." if self.var_emp_id.get() == "" else 'Invalid Entry of Employee Id \n It should contain only digits', parent=self.root)
            
            
            
            elif self.var_emp_name.get()=="":
                self.engine.say('Please enter the Name.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter the Name. ",parent=self.root)
            
            elif any(char.isdigit() for char in self.var_emp_name.get()):
                    self.engine.say('Name cannot contain numeric characters .')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Name cannot contain numeric characters .", parent=self.root)
                
            elif self.var_emp_contact.get() == "" or len(self.var_emp_contact.get()) != 10 or not self.var_emp_contact.get().isdigit() or not self.var_emp_contact.get().startswith(("7", "8", "9")):
                self.engine.say('Please enter a valid 10-digit Contact number. contact no should stsrt with 7,8,9')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter a valid 10-digit Contact number. contact no should start with 7,8,9", parent=self.root)
           
            elif self.var_emp_email.get()=="":
                self.engine.say('Please enter your Email..')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your Email. ",parent=self.root)
                
            
            elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_emp_email.get()):
              self.engine.say('Invalid email format.')
              self.engine.runAndWait()
              messagebox.showerror("Error", "Invalid email format. Eg:- sakshidesai123@gamil.com", parent=self.root)
              return False

            elif self.var_emp_gender.get()=="" or self.var_emp_gender.get()=="Select your Gender ":
                self.engine.say('Please select proper Gender.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select proper Gender. ",parent=self.root)
                
                
                
            elif self.var_emp_dob.get() == "" or len(self.var_emp_dob.get()) != 10:
                self.engine.say('Please enter your DOB in the correct format.\nDate, month, and year should be in digits.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your DOB in dd/mm/yyyy format.\nDate, month, and year should be in digits.", parent=self.root)
            else:
                dob_parts = self.var_emp_dob.get().split('/')
                
                if len(dob_parts) != 3:
                           self.engine.say('Please enter your DOB in correct format.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Invalid DOB format.", parent=self.root)
                else:
                         day, month, year = dob_parts[0], dob_parts[1], dob_parts[2]

                if not (day.isdigit() and month.isdigit() and year.isdigit()):
                           self.engine.say('Please enter your DOJ in digits.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Date, month, and year should be in digits.", parent=self.root)
                else:   
                    day = int(day)
                    month = int(month)
                    year = int(year)
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2025):
                       self.engine.say('Invalid date, month, or year')
                       self.engine.runAndWait()
                       messagebox.showerror("Error", "Invalid date, month, or year.", parent=self.root)
                       
                       self.show()                 

        
            
            
# Check for password
            elif self.var_emp_pass.get() == "":
                self.engine.say('Please enter your password.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your password.", parent=self.root)
            
            elif not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])", self.var_emp_pass.get()):
                self.engine.say('Enter a valid password. Password should contain at least one digit, one lowercase and one uppercase letter, and one special character.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Enter a valid password. Password should contain at least one digit, one lowercase and one uppercase letter, and one special character.", parent=self.root)
            
            elif self.var_emp_doj.get()== "" or len(self.var_emp_doj.get()) != 10:
                    self.engine.say('Please enter your DOJ in the correct format.\nDate, month, and year should be in digits.')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please enter your DOJ in dd/mm/yyyy format.\nDate, month, and year should be in digits.", parent=self.root)
            else:
                # Split the entered DOJ into day, month, and year
                    doj_parts = self.var_emp_doj.get().split('/')
                    
                    if len(doj_parts) != 3:
                           self.engine.say('Please enter your DOJ in correct format.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Invalid DOJ format.", parent=self.root)
                    else:

                    
                         day, month, year = doj_parts[0], doj_parts[1], doj_parts[2]

                    if not (day.isdigit() and month.isdigit() and year.isdigit()):
                           self.engine.say('Please enter your DOJ in digits.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Date, month, and year should be in digits.", parent=self.root)
                   
                    else:   
                       day = int(day)
                       month = int(month)
                       year = int(year)
                    if not (1 <= day <= 31 and 1 <= month <= 12 ):
                       self.engine.say('Invalid date, month')
                       self.engine.runAndWait()
                       messagebox.showerror("Error", "Invalid date, month, or year.", parent=self.root)      
                    
                    else:
                        current_date = datetime.date.today()
                        
            entered_date = datetime.date(year, month, day)
            if entered_date > current_date:
                           self.engine.say('DOJ cannot be in the future.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "DOJ cannot be in the future.", parent=self.root)
          
              
            
                
            elif self.var_emp_utype.get()=="" or self.var_emp_utype.get()=="Select your User Type ":
                self.engine.say('Please select proper user type')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select proper user type. ",parent=self.root)
            
           

            
            salary_input = self.var_emp_salary.get().strip()

            if not salary_input.isdigit():
                error_message = "Salary should be a positive number and in digits."
            elif int(salary_input) > 15000:
                error_message = "Please enter the salary properly. Salary cannot be more than 15000."
            else:
                error_message = None

            if error_message:
                self.engine.say(error_message)
                self.engine.runAndWait()
                messagebox.showerror("Error", error_message, parent=self.root)
                return False

            elif self.var_emp_email.get()!=None and self.var_emp_pass.get()!=None:
                x=self.checkemail(self.var_emp_email.get())
                y=self.checkpassword(self.var_emp_pass.get())
                if (x == True) and (y == True):
                  if self.check_var.get()==0:
                    self.engine.say('Please agree the condition.')
                    self.engine.runAndWait()
                    self.check_lbl.config(text=" Please agree the condition",fg="red")
                    
                  else:
                    self.engine.say('checked.')
                    self.engine.runAndWait()
                    self.check_lbl.config(text='checked',fg="green")
                    try:
                        conn=sqlite3.connect('employee.db')
                        cur=conn.cursor()
                        cur.execute("Insert into employe(Emp_Id,Emp_Name,Emp_Contact,Emp_Email,Emp_Gender,Emp_DOB,Emp_Password,Emp_DOJ,Emp_Utype,Emp_Salary,Emp_Address) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                       self.var_emp_id.get(),
                                       self.var_emp_name.get(),
                                       self.var_emp_contact.get(),
                                       self.var_emp_email.get(),
                                       self.var_emp_gender.get(),
                                       self.var_emp_dob.get(),
                                       self.var_emp_pass.get(),
                                       self.var_emp_doj.get(),
                                       self.var_emp_utype.get(),
                                       self.var_emp_salary.get(),
                                       self.txt_address.get('1.0',END),
                                       
                                       
                        ))    
                        conn.commit()
                        self.engine.say('Employee Added Successfully.')
                        self.engine.runAndWait()       
                        messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                        self.show()
                    except Exception as ex:
                         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   

                    
    def show(self):        
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            cur.execute("Select *  from employe ")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            self.engine.say(f"Error due to: {str(ex)}")
            self.engine.runAndWait()
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))             
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_contact.set(row[2])
        self.var_emp_email.set(row[3])
        self.var_emp_gender.set(row[4])
        self.var_emp_dob.set(row[5])
        self.var_emp_pass.set(row[6])
        self.var_emp_doj.set(row[7])
        self.var_emp_utype.set(row[8])
        self.var_emp_salary.set(row[9])
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[10]),
        
        
        
        
        
    def update(self):
            x=y=0
             
            # Validating Employee ID
            if self.var_emp_id.get() == "" or len(self.var_emp_id.get()) == 0 or not self.var_emp_id.get().isdigit():
                self.engine.say('Employee Id is required' if self.var_emp_id.get() == "" else 'Invalid Entry of Employee Id it should contain only digits')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Employee Id is required." if self.var_emp_id.get() == "" else 'Invalid Entry of Employee Id \n It should contain only digits', parent=self.root)
            
            
            
            elif self.var_emp_name.get()=="":
                self.engine.say('Please enter the Name.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter the Name. ",parent=self.root)
            elif any(char.isdigit() for char in self.var_emp_name.get()):
                    self.engine.say('Name cannot contain numeric characters .')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Name cannot contain numeric characters .", parent=self.root)
                
            elif self.var_emp_contact.get() == "" or len(self.var_emp_contact.get()) != 10 or not self.var_emp_contact.get().isdigit() or not self.var_emp_contact.get().startswith(("7", "8", "9")):
                self.engine.say('Please enter a valid 10-digit Contact number. contact no should stsrt with 7,8,9')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter a valid 10-digit Contact number. contact no should start with 7,8,9", parent=self.root)
                return False
           
            elif self.var_emp_email.get()=="":
                self.engine.say('Please enter your Email..')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your Email. ",parent=self.root)
                
            elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_emp_email.get()):
              self.engine.say('Invalid email format.')
              self.engine.runAndWait()
              messagebox.showerror("Error", "Invalid email format. Eg:- sakshidesai123@gamil.com", parent=self.root)
              return False

                
            elif self.var_emp_gender.get()=="" or self.var_emp_gender.get()=="Select your Gender ":
                self.engine.say('Please select proper Gender.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select proper Gender. ",parent=self.root)
                
                
                
            elif self.var_emp_dob.get() == "" or len(self.var_emp_dob.get()) != 10:
                self.engine.say('Please enter your DOB in the correct format.\nDate, month, and year should be in digits.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your DOB in dd/mm/yyyy format.\nDate, month, and year should be in digits.", parent=self.root)
            else:
                dob_parts = self.var_emp_dob.get().split('/')
                
                if len(dob_parts) != 3:
                           self.engine.say('Please enter your DOB in correct format.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Invalid DOB format.", parent=self.root)
                else:
                         day, month, year = dob_parts[0], dob_parts[1], dob_parts[2]

                if not (day.isdigit() and month.isdigit() and year.isdigit()):
                           self.engine.say('Please enter your DOJ in digits.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Date, month, and year should be in digits.", parent=self.root)
                else:   
                    day = int(day)
                    month = int(month)
                    year = int(year)
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024):
                       self.engine.say('Invalid date, month, or year')
                       self.engine.runAndWait()
                       messagebox.showerror("Error", "Invalid date, month, or year.", parent=self.root)
                       
                       self.show()
            
                
            
# Check for password
            elif self.var_emp_pass.get() == "":
                self.engine.say('Please enter your password.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter your password.", parent=self.root)
            elif not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])", self.var_emp_pass.get()):
                 self.engine.say('Enter a valid password. Password should contain at least one digit, one lowercase and one uppercase letter, and one special character.')
                 messagebox.showerror('Enter a valid password. Password should contain at least one digit, one lowercase and one uppercase letter, and one special character.')
            elif self.var_emp_doj.get()== "" or len(self.var_emp_doj.get()) != 10:
                    self.engine.say('Please enter your DOJ in the correct format.\nDate, month, and year should be in digits.')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please enter your DOJ in dd/mm/yyyy format.\nDate, month, and year should be in digits.", parent=self.root)
            else:
                # Split the entered DOJ into day, month, and year
                    doj_parts = self.var_emp_doj.get().split('/')
                    
                    if len(doj_parts) != 3:
                           self.engine.say('Please enter your DOJ in correct format.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Invalid DOJ format.", parent=self.root)
                    else:

                    
                         day, month, year = doj_parts[0], doj_parts[1], doj_parts[2]

                    if not (day.isdigit() and month.isdigit() and year.isdigit()):
                           self.engine.say('Please enter your DOJ in digits.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "Date, month, and year should be in digits.", parent=self.root)
                   
                    else:   
                       day = int(day)
                       month = int(month)
                       year = int(year)
                    if not (1 <= day <= 31 and 1 <= month <= 12 ):
                       self.engine.say('Invalid date, month')
                       self.engine.runAndWait()
                       messagebox.showerror("Error", "Invalid date, month, or year.", parent=self.root)      
                    
                    else:
                        current_date = datetime.date.today()
                        
            entered_date = datetime.date(year, month, day)
            if entered_date > current_date:
                           self.engine.say('DOJ cannot be in the future.')
                           self.engine.runAndWait()
                           messagebox.showerror("Error", "DOJ cannot be in the future.", parent=self.root)
          
              
            
                
            elif self.var_emp_utype.get()=="" or self.var_emp_utype.get()=="Select your User Type ":
                self.engine.say('Please select proper user type')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please select proper user type. ",parent=self.root)
            
           

            
            elif self.var_emp_salary.get() == "" or int(self.var_emp_salary.get()) > 15000 or not (self.var_emp_salary.get().isdigit() and int(self.var_emp_salary.get()) >= 0): 
                error_message =(
                         'Please enter the salary properly. Salary cannot be more than 15000.'
                         if self.var_emp_salary.get() == "" or int(self.var_emp_salary.get()) > 15000
                         else 'Salary should be a positive number and in digits.'
                          )
                self.engine.say(error_message)
                self.engine.runAndWait()
                messagebox.showerror("Error", error_message, parent=self.root)
                return False
            
 
                
            elif self.var_emp_email.get()!=None and self.var_emp_pass.get()!=None:
                x=self.checkemail(self.var_emp_email.get())
                y=self.checkpassword(self.var_emp_pass.get())
            if (x == True) and (y == True):
                if self.check_var.get()==0:
                    self.engine.say('Please agree the condition.')
                    self.engine.runAndWait()
                    self.check_lbl.config(text=" Please agree the condition",fg="red")
                    
                else:
                    self.engine.say('checked.')
                    self.engine.runAndWait()
                    self.check_lbl.config(text='checked',fg="green")
            
                
                    try:
                        conn=sqlite3.connect('employee.db')
                        cur=conn.cursor()
                        cur.execute("Update  employe set Emp_Name=?, Emp_Contact=?, Emp_Email=?,Emp_Gender=?,Emp_DOB=?,Emp_Password=?,Emp_DOJ=?,Emp_Utype=?,Emp_Salary=?,Emp_Address=? where Emp_Id=?",(
                        
                        self.var_emp_name.get(),
                        self.var_emp_contact.get(),
                        self.var_emp_email.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_pass.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_utype.get(),
                        self.var_emp_salary.get(),
                        self.txt_address.get('1.0',END),
                        self.var_emp_id.get(),
                          
                        )) 
                        conn.commit() 
                        self.engine.say('Employee Updated Successfully.')
                        self.engine.runAndWait()      
                        messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                        self.show()
                    except Exception as ex:
                           messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    
    def delete(self):
     try:
        if self.var_emp_id.get() == "":
            self.engine.say('Employee Id Must Be Required.')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Employee Id Must Be Required", parent=self.root)
            return

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM employe WHERE Emp_Id=?", (self.var_emp_id.get(),))
        row = cur.fetchone()

        if row is None:
            self.engine.say('Invalid Employee ID')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
        else:
            self.engine.say('Are you sure you want to delete the information?')
            self.engine.runAndWait()
            op = messagebox.askyesno("Confirm", "Are you sure you want to delete the information?", parent=self.root)
            if op:
                cur.execute("DELETE FROM employe WHERE Emp_Id=?", (self.var_emp_id.get(),))
                conn.commit()
                self.engine.say('Information successfully deleted.')
                self.engine.runAndWait()
                messagebox.showinfo("Deleted", "Information successfully deleted", parent=self.root)
                self.clear()

     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

                
    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_contact.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_dob.set("")
        self.var_emp_pass.set("")
        self.var_emp_doj.set("")
        self.var_emp_utype.set("Admin")
        self.var_emp_salary.set("")
        self.txt_address.delete('1.0',END),
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
                cur.execute("Select *  from employe where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
            
            

       
         
            

        

        
        
if __name__=="__main__":    
       root=Tk()
       obj=employeeClass(root)
       root.mainloop()