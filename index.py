from tkinter import*
from PIL import ImageTk#======pillow library it is used for add jpg image
from tkinter import messagebox
import sqlite3
class index:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Library Management")

        #bg image
        self.bg=ImageTk.PhotoImage(file="image/1 (7).jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        f1=Frame(self.root,bg="#FFFFE0",relief=GROOVE,bd=3)
        f1.place(x=250,y=50,width=900,height=600)

        l1=Label(f1,text="LIBRARY MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="#FFFFE0",fg="#FF8C00")
        l1.place(x=40,y=50)

        self.bg=ImageTk.PhotoImage(file="image/1 (10).jpg")
        self.bg_image=Label(f1,image=self.bg).place(x=400,y=200,width=400,height=300)

        btn=Button(f1,text="ADMIN LOGIN",command=self.admin,width=20,font="arial 15 bold", bg="#FFF0F5",fg="#FF8C00")
        btn.place(x=80,y=250)

        btn=Button(f1,text="LIBRARIAN LOGIN",command=self.register,width=20,font="arial 15 bold", bg="#FFF0F5",fg="#FF8C00")
        btn.place(x=80,y=400)

    def admin(self):
        self.root.destroy()
        import home
    def register(self):
        self.root.destroy()
        import librarian
root=Tk()
obj=index(root)
root.mainloop()