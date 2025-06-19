from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import time
import os
import pyttsx3
import re
import subprocess
import email_pass
import smtplib

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Shop Login | Developed By Sakshi")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        self.otp = ''
        
        # Text-to-speech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty('voice', self.voices[0].id)
        
        # Images
        self.phone_image = PhotoImage(file="image/lap3.png")
        self.lbl_Phone_Image = Label(self.root, image=self.phone_image, bd=0).pack()

        # Login Frame
        self.emp_id = StringVar()
        self.password = StringVar()
        
        login_frame = Frame(self.root, bd=8, relief=RIDGE, bg="white")
        login_frame.place(x=825, y=90, width=350, height=500)

        title = Label(login_frame, text="Login System", font=("goudy old style", 25, "bold"), bg="lightgrey").place(x=1, y=3, relwidth=1)

        lbl_emp_id = Label(login_frame, text="USER-ID", font=("Time roman", 20, "bold"), bg="white", fg="#767171").place(x=50, y=100)
        txt_emp_id = Entry(login_frame, textvariable=self.emp_id, font=("time roman", 20), bg="#ECECEC", bd=3).place(x=50, y=140, width=250)
        lbl_pass = Label(login_frame, text="PASSWORD", font=("time roman", 20, "bold"), bg="white", fg="#767171").place(x=50, y=200)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("time roman", 20), bg="#ECECEC", bd=3).place(x=50, y=240, width=250)

        btn_login = Button(login_frame, command=self.login, text="Log-in", font=("Arial Rounded MT Bold", 15, "bold"), bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("time roman", 15, "bold")).place(x=150, y=355)

        btn_forget = Button(login_frame, text="Forget Password?", command=self.forget_window, font=("time roman", 15, "bold"), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=390)
        
       
        
        btn_reg = Button(login_frame, text=" Admin Register", command=self.register_window, font=("time roman", 15, "bold"), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=430)

        # Registration Frame
        register_frame = Frame(self.root, bd=8, relief=RIDGE, bg="white")
        register_frame.place(x=825, y=600, width=350, height=60)

        lbl_reg = Label(register_frame, text="  Welcome to Quick Pick ", font=("time roman", 15, "bold"), bg="white", fg="#00ABA9").place(x=50, y=12)
        #btn_register = Button(register_frame, text="Register", command=self.register_window, font=("time roman", 12, "bold"), bg="#4CAF50", fg="white", bd=2, cursor="hand2").place(x=220, y=10, width=100, height=30)

        # Animation images
        self.im1 = PhotoImage(file="image/gr2.png")
        self.im2 = PhotoImage(file="image/gr1.png")
        self.im3 = PhotoImage(file="image/grain.png")
        self.im4 = PhotoImage(file="image/bakrey.png")
        
        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=347, y=190, width=478, height=300)
        
        self.animate()
        
    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im4
        self.im4 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)
   
    def login(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        try:
            if self.emp_id.get() == "" or self.password.get() == "":
                self.engine.say('All Fields are required')
                self.engine.runAndWait()
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                cur.execute("select Emp_Utype from employe where Emp_Id=? AND Emp_Password=?", (self.emp_id.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    self.engine.say('Invalid Username or Password. Try again with correct credentials')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Username or Password \n Try again with correct credentials", parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.engine.say('Admin Login Successfully')
                        self.engine.runAndWait()
                        messagebox.showinfo("Success", "Admin Login Successfully", parent=self.root) 
                        self.root.destroy()
                        subprocess.Popen(["python", "dashboard.py"])
                    else:
                        self.engine.say('Employee Login Successfully')
                        self.engine.runAndWait()
                        messagebox.showinfo("Success", "Employee Login Successfully", parent=self.root)
                        self.root.destroy()
                        os.system("python bill.py")
        except Exception as ex:
            self.engine.say('Error')
            self.engine.runAndWait()
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def register_window(self):
        self.register_win = Toplevel(self.root)
        self.register_win.title("Admin/Employee Registration")
        self.register_win.geometry('500x600+500+100')
        self.register_win.focus_force()
        self.register_win.config(bg="white")
        
        title = Label(self.register_win, text='REGISTRATION', font=("goudy old style", 20, "bold"), bg="lightgrey", fg="black").pack(side=TOP, fill=X)
        
        # Registration form fields
        lbl_emp_id = Label(self.register_win, text="Employee ID", font=("goudy old style", 15), bg="white").place(x=50, y=60)
        self.entry_emp_id = Entry(self.register_win, font=("goudy old style", 15), bg="lightyellow")
        self.entry_emp_id.place(x=200, y=60, width=250)
        
        lbl_name = Label(self.register_win, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=100)
        self.entry_name = Entry(self.register_win, font=("goudy old style", 15), bg="lightyellow")
        self.entry_name.place(x=200, y=100, width=250)
        
        lbl_email = Label(self.register_win, text="Email", font=("goudy old style", 15), bg="white").place(x=50, y=140)
        self.entry_email = Entry(self.register_win, font=("goudy old style", 15), bg="lightyellow")
        self.entry_email.place(x=200, y=140, width=250)
        
        lbl_contact = Label(self.register_win, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=180)
        self.entry_contact = Entry(self.register_win, font=("goudy old style", 15), bg="lightyellow")
        self.entry_contact.place(x=200, y=180, width=250)
        
        lbl_pass = Label(self.register_win, text="Password", font=("goudy old style", 15), bg="white").place(x=50, y=220)
        self.entry_pass = Entry(self.register_win, show="*", font=("goudy old style", 15), bg="lightyellow")
        self.entry_pass.place(x=200, y=220, width=250)
        
        lbl_cpass = Label(self.register_win, text="Confirm Password", font=("goudy old style", 15), bg="white").place(x=50, y=260)
        self.entry_cpass = Entry(self.register_win, show="*", font=("goudy old style", 15), bg="lightyellow")
        self.entry_cpass.place(x=200, y=260, width=250)
        
        lbl_utype = Label(self.register_win, text="User Type", font=("goudy old style", 15), bg="white").place(x=50, y=300)
        self.cmb_utype = ttk.Combobox(self.register_win, values=["Admin", "Employee"], font=("goudy old style", 15), state='readonly')
        self.cmb_utype.place(x=200, y=300, width=250)
        self.cmb_utype.current(1)
        
        btn_register = Button(self.register_win, text="Register", command=self.register, font=("goudy old style", 15), bg="#4CAF50", fg="white", cursor="hand2").place(x=200, y=350, width=100, height=35)
        
    def register(self):
        if self.entry_emp_id.get() == "" or self.entry_name.get() == "" or self.entry_email.get() == "" or self.entry_contact.get() == "" or self.entry_pass.get() == "" or self.entry_cpass.get() == "":
            self.engine.say('All fields are required')
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields are required", parent=self.register_win)
        elif self.cmb_utype.get() != "Admin":
            self.engine.say('Only Admin Registration is allowed')
            self.engine.runAndWait()
            messagebox.showerror("Access Denied", "Only Admin Registration is allowed", parent=self.register_win)
            

        elif self.entry_pass.get() != self.entry_cpass.get():
            self.engine.say('Password and Confirm Password must match')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Password and Confirm Password must match", parent=self.register_win)
        else:
            try:
                conn = sqlite3.connect('employee.db')
                cur = conn.cursor()
                cur.execute("INSERT INTO employe (Emp_Id, Emp_Name, Emp_Email, Emp_Contact, Emp_Password, Emp_Utype) VALUES (?, ?, ?, ?, ?, ?)",
                            (self.entry_emp_id.get(), self.entry_name.get(), self.entry_email.get(), 
                             self.entry_contact.get(), self.entry_pass.get(), self.cmb_utype.get()))
                conn.commit()
                self.engine.say('Registration successful')
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Registration successful", parent=self.register_win)
                self.register_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.register_win)
                
                
    def register(self):
        emp_id = self.entry_emp_id.get().strip()
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        contact = self.entry_contact.get().strip()
        password = self.entry_pass.get().strip()
        confirm = self.entry_cpass.get().strip()
        utype = self.cmb_utype.get().strip()

    # 1. Empty fields check
        if not all([emp_id, name, email, contact, password, confirm]):
            self.engine.say( "All fields are required",)
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields are required", parent=self.register_win)
            return

        # 2. Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.engine.say( "Invalid email format",)
            self.engine.runAndWait()
            
            messagebox.showerror("Error", "Invalid email format", parent=self.register_win)
            return

    # 3. Contact number check
        if not contact.isdigit() or len(contact) not in (10):
            self.engine.say("Contact must be numeric and 10  digits",)
            self.engine.runAndWait()
            messagebox.showerror("Error", "Contact must be numeric and 10 digits", parent=self.register_win)
            return

        # 4. Password strength check
        password_pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])"
        if not re.match(password_pattern, password):
            self.engine.say( "Password should contain at least:\n• one digit\n• one lowercase\n• one uppercase\n• one special character",)
            self.engine.runAndWait()
            messagebox.showerror(
                "Error",
                "Password should contain at least:\n• one digit\n• one lowercase\n• one uppercase\n• one special character",
                parent=self.register_win
            )
            return

        # 5. Confirm password match
        if password != confirm:
            self.engine.say( "All fields are required",)
            self.engine.runAndWait()
            messagebox.showerror("Error", "Passwords do not match", parent=self.register_win)
            return

        # 6. Admin only restriction
        if utype != "Admin":
            self.engine.say( "Only Admin registration is allowed",)
            self.engine.runAndWait()
            messagebox.showerror("Error", "Only Admin registration is allowed", parent=self.register_win)
            return

        # 7. DB Insert
        try:
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO employe (Emp_Id, Emp_Name, Emp_Email, Emp_Contact, Emp_Password, Emp_Utype) VALUES (?, ?, ?, ?, ?, ?)",
                        (emp_id, name, email, contact, password, utype))
            conn.commit()
            self.engine.say( "All fields are required",)
            self.engine.runAndWait()
            messagebox.showinfo("Success", "Admin Registered Successfully", parent=self.register_win)
            self.register_win.destroy()
        except Exception as ex:
            self.engine.say("Error", "All fields are required",)
            self.engine.runAndWait()
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.register_win)

    
    def forget_window(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        try:
            if self.emp_id.get() == "":
                self.engine.say('Employee Id Must Be Required')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Employee Id Must Be Required", parent=self.root)
            else:
                cur.execute("select Emp_email from employe where Emp_Id=?", (self.emp_id.get(),))
                email = cur.fetchone()    
                if email == None:
                    self.engine.say('Invalid Employee Id, try again')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Employee Id, try again", parent=self.root)
                else:
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    
                    chk = self.send_email(email[0])
                    if chk == 'f':
                        self.engine.say('Connection Error, try again')
                        self.engine.runAndWait()
                        messagebox.showerror("Error", "Connection Error, try again", parent=self.root)
                    else:
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry('450x400+500+100')
                        self.forget_win.focus_force()
                        self.forget_win.config(bg="white")
                        
                        title = Label(self.forget_win, text='RESET PASSWORD', font=("goudy old style", 20, "bold"), bg="lightgrey", fg="black").pack(side=TOP, fill=X)
                        
                        lbl_reset = Label(self.forget_win, text="Enter OTP Sent On Your Email Id", font=("goudy old style", 15), bg="white", fg="#767171").place(x=50, y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("goudy old style", 15), bg="#ECECEC", bd=3).place(x=50, y=90, width=250, height=30)
                        
                        self.btn_reset = Button(self.forget_win, text="SUBMIT", command=self.validate_otp, font=("goudy old style", 13), bg="#00B0F0", fg="white", cursor="hand2")
                        self.btn_reset.place(x=310, y=90, width=100, height=30)
                        
                        lbl_new_pass = Label(self.forget_win, text="New Password", font=("goudy old style", 15), bg="white", fg="#767171").place(x=50, y=150)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, show="*", font=("goudy old style", 15), bg="#ECECEC", bd=3).place(x=50, y=180, width=250, height=30)
                        
                        lbl_conf_pass = Label(self.forget_win, text="Confirm Password", font=("goudy old style", 15), bg="white", fg="#767171").place(x=50, y=230)
                        txt_conf_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, show="*", font=("goudy old style", 15), bg="#ECECEC", bd=3).place(x=50, y=260, width=250, height=30)
                        
                        self.btn_update = Button(self.forget_win, text="Update", command=self.update_password, state=DISABLED, font=("goudy old style", 15), bg="#4CAF50", fg="white", cursor="hand2")
                        self.btn_update.place(x=150, y=310, width=150, height=35)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_conf_pass.get() == "":
            self.engine.say('Password fields are required')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Password fields are required", parent=self.forget_win)
        elif self.var_new_pass.get() != self.var_conf_pass.get():
            self.engine.say('Password & Confirm Password must be same')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.forget_win)
        else:
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()
            try:
                cur.execute("UPDATE employe SET Emp_Password=? WHERE Emp_Id=?", (self.var_new_pass.get(), self.emp_id.get()))
                conn.commit()
                self.engine.say('Password Updated successfully')
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Password Updated successfully", parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
       
    def validate_otp(self):
        if int(self.otp) == int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
            self.engine.say('OTP validated. Please enter new password')
            self.engine.runAndWait()
            messagebox.showinfo("Success", "OTP validated. Please enter new password", parent=self.forget_win)
        else:
            self.engine.say('Invalid OTP, Try again')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)
            
    def send_email(self, to_):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_
        
        s.login(email_, pass_)
        
        self.otp = int(time.strftime("%H%M%S")) + int(time.strftime("%S"))
        subj = 'Grocery Shop - Reset Password OTP'
        msg = f'Dear User,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nGrocery Shop Team'
        msg = "Subject:{}\n\n{}".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk = s.ehlo()
        if chk[0] == 250:
            return 's'
        else:
            return 'f'

root = Tk()
obj = Login_System(root)
root.mainloop() 