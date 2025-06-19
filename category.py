from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3 
import pyttsx3
class categoryClass :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Quick Pick      | Devloped by Sakshi  "  )
        self.root.config(bg="white")
        self.root.focus_force()
        
        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        
        
        #=======================variable===========
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        #=============title==========================
        self.icon_title=PhotoImage(file="image/cat.png")
        lbl_title=Label(self.root, text= "Manage Product Category",image=self.icon_title,compound=LEFT,padx=20,font=("goudy old style", 35), bd=3, relief=RIDGE,bg ="#0f4d7d", fg="white")
        lbl_title.place(x=50,y=10,width=1000)
        
        lbl_name=Label(self.root, text= "Category Name",font=("goudy old style", 25),bg="white")
        lbl_name.place(x=50,y=100)
        
        txt_name=Entry(self.root, textvariable=self.var_name,font=("goudy old style", 25),bd=3,bg="lightyellow")
        txt_name.place(x=300,y=100,width=300)
        
        
        #=============button=============
        btn_add=Button(self.root, text="ADD",command=self.add, font=("goudy old style ", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_add.place(x=300,y=170,width=130, height=35)
        
        btn_delete=Button(self.root, text="Delete",command=self.delete,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_delete.place(x=470,y=170,width=130, height=35)
        
        
        #================= categ details========================
        cate_frame=Frame(self.root,bd=3, relief=RIDGE)
        cate_frame.place(x=700,y=100, width=380, height=380)
        
        scrolly=Scrollbar(cate_frame, orient=VERTICAL)
        scrollx=Scrollbar(cate_frame, orient=HORIZONTAL)
        
        self.CategoryTable=ttk.Treeview(cate_frame,columns=("Cat_Id","Cat_Name", ),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        
        self.CategoryTable.heading("Cat_Id",text="Category-ID")
        self.CategoryTable.heading("Cat_Name", text="Name")
        
        self.CategoryTable["show"]="headings"
    
        self.CategoryTable.column("Cat_Id",width=80)
        self.CategoryTable.column("Cat_Name", width=100)
        
        self.CategoryTable.pack(fill=BOTH,expand=1)
        
        
        #====================img============
        
        self.im1=PhotoImage(file="image/daily.png")
        self.lbl_im1=Label(self.root , image=self.im1, bd=5)
        self.lbl_im1.place(x=50, y=240)
        
        self.im2=PhotoImage(file="image/grain2.png")
        self.lbl_im2=Label(self.root , image=self.im2, bd=5  )
        self.lbl_im2.place(x=370, y=240)
        
        
        
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        
        
   #========================== main ===============================
    def add(self):
        
        try:
            conn=sqlite3.connect('employee.db')
            cur=conn.cursor()
            if self.var_name.get()=="":
                self.engine.say('Please enter the Name.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Please enter the Name. ",parent=self.root)
            elif any(char.isdigit() for char in self.var_name.get()):
                    self.engine.say('Name cannot contain numeric characters .')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Name cannot contain numeric characters .", parent=self.root)
                        
            else:
                    cur.execute("Insert into category(Cat_Name) values(?)",(self.var_name.get(),)) 
                    conn.commit() 
                    self.engine.say(' Category Added Successfully.')
                    self.engine.runAndWait()      
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
 
    def show(self):        
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try: 
            cur.execute("Select *  from category ")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  
        
    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))             
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
        
        
        
        
        
        
    def delete(self):
        conn=sqlite3.connect('employee.db')
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="":
                self.engine.say(' Press Select category name from the list.')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Press Select category name from the list",parent=self.root)
            else:
                cur.execute("Select * from category where Cat_Id=?",(self.var_cat_id.get(),))  
                row=cur.fetchone()
                if row==None:
                    self.engine.say(' Please Try Again.')
                    self.engine.runAndWait()
                    messagebox.showerror("Error"," Please Try Again ",parent=self.root)
                    
                else:
                    self.engine.say('Are You Sure ,That You Want To Delete The Information? .')
                    self.engine.runAndWait()
                    op=messagebox.askyesno("Confirm","Are You Sure ,That You Want To Delete The Information?",parent=self.root)
                    if op==True:
                     cur.execute("delete from category where Cat_Id=?",(self.var_cat_id.get(),))
                     conn.commit()
                     self.engine.say('Information Successfully Deleted.')
                     self.engine.runAndWait()
                     messagebox.showinfo("Deleted","Information Successfully Deleted",parent=self.root)
                     self.show()
                     self.var_cat_id.set("")
                     self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                
    

        
        
        
        
        
        
        
        
        
if __name__=="__main__":    
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()