from tkinter import*
from PIL import ImageTk#======pillow library it is used for add jpg image
from tkinter import messagebox
import sqlite3
class lib:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Library Management")
        #bg image
        self.bg=ImageTk.PhotoImage(file="image/1 (7).jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        # frame
        f1=Frame(self.root,bg="white",relief=GROOVE,bd=3)
        f1.place(x=250,y=50,width=900,height=600)


        #lable for frame

        l1=Label(f1,text="LIBRARIAN LOGIN HERE",font=("times new roman",40,"bold"),bg="white",fg="#FF8C00")
        l1.place(x=90,y=30)

        #==username feild
        f2=Label(f1,text="Email:",font=("times new roman",20,"bold"),bg="white",fg="#2F4F44")
        f2.place(x=80,y=120)
       
        self.textemail=Entry(f1,width=40,font="arial 10",bd=1,bg="#FAFAD2",fg="#808080")
        self.textemail.place(x=80,y=180)
       
        self.bg=ImageTk.PhotoImage(file="image/library1.jpg")
        self.bg_image=Label(f1,image=self.bg).place(x=400,y=200,width=400,height=300)

        # password feild
        f4=Label(f1,text="Password:",font=("times new roman",20,"bold"),bg="white",fg="#2F4F44")
        f4.place(x=80,y=240)
        
        self.textpass=Entry(f1,width=40,font="arial 10",bd=1,bg="#FAFAD2",fg="#808080")
        self.textpass.place(x=80,y=300)
        
        # forget

        fbtn=Button(f1,text="Forget Password?",bg="white",fg="red",font=("times new roman",10),bd=0)
        fbtn.place(x=80,y=320)

        fbtn=Button(f1,text="Register",bg="white",command=self.regi,fg="red",font=("times new roman",10),bd=0)
        fbtn.place(x=80,y=340)
        
        
        #login button
        btn=Button(f1,text="LOGIN",command=self.login,width=10,font="arial 15 bold", bg="#FFF0F5",fg="#FF8C00")
        btn.place(x=130,y=420)

        btn=Button(f1,text="Home",command=self.home,width=10,font="arial 10 bold",bd=0, bg="white",fg="#FF8C00")
        btn.place(x=00,y=560)

    

    def login(self):
        if self.textemail.get()=="" or self.textpass.get()=="":
            messagebox.showerror("error","all field required",parent=self.root)
        else:
            conn= sqlite3.connect('data.db')
            c=conn.cursor()
            c.execute("select * from library where email='%s'"%self.textemail.get())
            row=c.fetchall()
            if row!=None:
                messagebox.showinfo("welcome","welcome there yhooooooo!.......",parent=self.root)
            else:
                messagebox.showerror("error","wrong email and password")
    def regi(self):
        self.root.destroy()
        import register
    def home(self):
        self.root.destroy()
        import index


root=Tk()
obj=lib(root)
root.mainloop()