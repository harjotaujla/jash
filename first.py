from tkinter import*
import sqlite3
class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("JASH")
        #self.title=IntVar()
        title=Label(self.root,text="JASH",bd=12,relief=GROOVE,bg="blue",fg="white",font=("times new roman",30,"bold"),pady=2)
        title.pack(fill=X)
        #print(title)
        f1=LabelFrame(self.root,text="Jashan",font=("times new roman",15,"bold"),bg="blue")
        f1.place(x=0,y=80,relwidth=1)
        n=Label(f1,text="jashan",font=("times new roman",10,"bold"),bg="blue",fg="white")
        n.grid(row=0,column=1,pady=20)
        f2=LabelFrame(self.root,text="sukha",font=("times new roman",15,"bold"),bg="blue")
        f2.place(x=0,y=180,width="325",height="380")
        m=Label(f2,text="sukha",font=("times new roman",10,"bold"),bg="blue",fg="white")
        m.grid(row=0,column=1,pady=20,sticky="w")


conn= sqlite3.connect('add.db')
c=conn.cursor()
c.execute("""create table adds(
    first text
)



""")
conn.commit()
conn.close()
root=Tk()
obj=Bill(root)
root.mainloop()