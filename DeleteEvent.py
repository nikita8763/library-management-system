from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
# import pymysql
import config
import mysql.connector

# Add your own database name and password here to reflect in the code
mypass= config.dbPass
mydatabase=config.db

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor(buffered=True)

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteEvent():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from event where id = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Notice Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    bookInfo1.delete(0, END)
    root.destroy()
    
def deleteEventView(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Notice", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Notice ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteEvent)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()