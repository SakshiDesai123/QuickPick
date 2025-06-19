import sqlite3
def create_db():
  conn=sqlite3.connect('employee.db')
  cur=conn.cursor()
  
  cur.execute("CREATE TABLE product(Pro_Id INTEGER PRIMARY KEY ,Pro_Category VARCHAR(50) ,Pro_Supplier VARCHAR(50), Pro_Name VARCHAR(50) ,Pro_Price VARCHAR(50),Pro_Quantity VARCHAR(50),Pro_Status VARCHAR(50))")
  conn.commit() 
  
  
  cur.execute("CREATE TABLE employe(Emp_Id INTEGER PRIMARY KEY  ,Emp_Name VARCHAR(50),Emp_Contact VARCHAR(50), Emp_Email VARCHAR(50),Emp_Gender VARRCHAR(50),Emp_DOB VARCHAR(50),Emp_Password VARCHAR(50),Emp_DOJ VARCHAR(50),Emp_Utype VARCHAR(50),Emp_Salary VARCHAR(50),Emp_Address VARCHAR(50))")
  conn.commit()  

  cur.execute("CREATE TABLE supplier(Supp_Id INTEGER PRIMARY KEY ,Supp_Name VARCHAR(50),Supp_Contact VARCHAR(50)  ,  Supp_Email VARCHAR(50)  , Supp_Gst_id  VARCHAR(50),Supp_Address VARCHAR(50))")
  conn.commit() 

  cur.execute("CREATE TABLE category(Cat_Id INTEGER PRIMARY KEY ,Cat_Name VARCHAR(50))")
  conn.commit()

create_db() 

  


 
   