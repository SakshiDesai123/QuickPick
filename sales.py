from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk ,messagebox 
import sqlite3
import pyttsx3
import os
class salesClass :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Grocery Shopping Managment System     | Devloped by Sakshi  "  )
        self.root.config(bg="white")
        self.root.focus_force()
        
        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty('voice',self.voices[0].id)
        
        
        #================vari============
        self.bill_list=[]
        self.var_invoice=StringVar()
        
        #============title====================
        self.icon_title=PhotoImage(file="image/scales.png")
        lbl_title=Label(self.root, text="Customer Bill ",image=self.icon_title,compound=LEFT,padx=20,font=("goudy old style", 35), bd=3, relief=RIDGE,bg ="#0f4d7d", fg="white")
        lbl_title.pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name=Label(self.root, text= "Invoice no",font=("goudy old style", 20),bg="white")
        lbl_name.place(x=50,y=100)
        
        txt_name=Entry(self.root, textvariable=self.var_invoice,font=("goudy old style", 25),bd=3,bg="lightyellow")
        txt_name.place(x=180,y=100,width=200)
        
        #================btn==================
        
        btn_search=Button(self.root, text="Search",command=self.search, font=("goudy old style ", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_search.place(x=400,y=100,width=130, height=35)
        
        btn_clear=Button(self.root, text="Clear",command=self.clear,font=("goudy old style ", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_clear.place(x=550,y=100,width=130, height=35)
        
        #===================bill list===========================
        
        sales_Frame=Frame(self.root, bd=4, relief=RIDGE)
        sales_Frame.place(x=50,y=160,width=200,height=330)
        
        scrolly=Scrollbar(sales_Frame, orient=VERTICAL)
        
        self.Sales_List=Listbox(sales_Frame,font=("goudy old style", 15), bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        
        #=====================bill Area=======================
        bill_Frame=Frame(self.root, bd=4, relief=RIDGE)
        bill_Frame.place(x=280,y=160,width=420,height=330)
        
        
        lbl_name=Label(bill_Frame, text= "Customer sales Area",font=("goudy old style", 20),bg="orange")
        lbl_name.pack(side=TOP,fill=BOTH)
        
        scrolly2=Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area=Text(bill_Frame, bg="lightyellow",yscrollcommand=scrolly.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        #========================================================
        
        self.im3=PhotoImage(file="image/bill2.png")
        self.lbl_im3=Label(self.root , image=self.im3  )
        self.lbl_im3.place(x=770, y=190)
        
        self.show()
#============================================================================================================
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        #print(os.listdir('../sakshi')) 
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0]) 
                
    def get_data(self,evs):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
        
    def search(self):
        if self.var_invoice.get()=="":
            self.engine.say('Invoice No Is Required.')
            self.engine.runAndWait()
            messagebox.showerror("Error","Invoice No Is Required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                     self.bill_area.insert(END,i)
                fp.close()
            else:
                self.engine.say('Invalid Invoice No... Please Enter Correct Invoice No .')
                self.engine.runAndWait()
                messagebox.showerror("Error", "Invalid Invoice No... Please Enter Correct Invoice No ")
                
            
            
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
            
        
        
        
        
        
        
if __name__=="__main__":    
      root=Tk()
      obj=salesClass(root)
      root.mainloop()