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
        f1=Frame(self.root,bg="#FFFFE0",relief=GROOVE,bd=3)
        f1.place(x=250,y=50,width=900,height=600)
        #self.grid(row=0,column=0)

        #lable for frame

        l1=Label(f1,text="REGISTER HERE",font=("times new roman",40,"bold"),bg="#FFFFE0",fg="#FF8C00")
        l1.place(x=90,y=30)

        #==first name feild
        firstname=Label(f1,text="First Name:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        firstname.place(x=80,y=120)
       
        self.textname=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textname.place(x=80,y=160)
       
       #==last name feild
        lastname=Label(f1,text="Last Name:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        lastname.place(x=400,y=120)
       
        self.textlname=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textlname.place(x=400,y=160)

        #email
        
        email=Label(f1,text="Email:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        email.place(x=80,y=240)
    
        self.textemail=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textemail.place(x=80,y=280)

        # phone feild
        phone=Label(f1,text="Phone No.:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        phone.place(x=400,y=240)
        
        self.textph=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textph.place(x=400,y=280)

        #password
        
        password=Label(f1,text="Pasword:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        password.place(x=80,y=360)
       
        self.textpass=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textpass.place(x=80,y=400)

       #confirm password
        cpass=Label(f1,text="Confirm Pasword:",font=("times new roman",15,"bold"),bg="#FFFFE0",fg="#2F4F4F")
        cpass.place(x=400,y=360)
       
        self.textcpass=Entry(f1,width=25,font="arial 15",bd=1,bg="#FAFAD2",fg="#808080")
        self.textcpass.place(x=400,y=400)
        
        #login button
        btn=Button(f1,text="REGISTER",command=self.login,width=10,font="arial 15 bold", bg="#FFF0F5",fg="#FF8C00")
        btn.place(x=200,y=500)
        #login button
        btn=Button(f1,text="LOGIN",command=self.abc,width=10,font="arial 15 bold", bg="#FFF0F5",fg="#FF8C00")
        btn.place(x=400,y=500)

        btn=Button(f1,text="Home",command=self.home,width=10,font="arial 10 bold",bd=0, bg="white",fg="#FF8C00")
        btn.place(x=00,y=560)
    
    def login(self):
        if self.textname.get()=="" or self.textemail.get()=="" or self.textph.get()=="" or self.textpass.get()=="" or self.textcpass.get()=="": 
           messagebox.showerror("error","all field required",parent=self.root) 
        elif self.textpass.get()!=self.textcpass.get():
            messagebox.showerror("error"," password & confirm pasword are not same",parent=self.root)
        else:
            conn= sqlite3.connect('data.db')
            c=conn.cursor()
            c.execute("select email from library where email='%s'"%self.textemail.get())
            row=c.fetchone()
            if row==None:
                c.execute("insert into library values('%s','%s','%s','%s','%s','%s')"%
                    (
                        self.textname.get(),
                        self.textlname.get(),
                        self.textemail.get(),
                        self.textph.get(),
                        self.textpass.get(),
                        self.textcpass.get()
                     )

                )
                messagebox.showinfo("sucess","Data sucessfully enter in the table",parent=self.root)

            else:
                messagebox.showerror("error","email already saved")
            c.close()
            
            conn.commit()
            conn.close()
            self.clear()

    def clear(self):
        self.textname.delete(0, END),
        self.textlname.delete(0, END),
        self.textemail.delete(0, END),
        self.textph.delete(0, END),
        self.textpass.delete(0, END),
        self.textcpass.delete(0, END)
    def abc(self):
        self.root.destroy()
        import home
    def register(self):
        self.root.destroy()
        import index
    def home(self):
        self.root.destroy()
        import index    






        #if self.f3.get()=="" or self.f5.get()=="":
        #    messagebox.showerror("error","all field required",parent=self.root)
        #elif self.f3.get()=="harjot" or self.f5.get()!="harjot1":
        #    messagebox.showerror("error2","invalid usernmae/password",parent=self.root)
        #else:
        #    messagebox.showinfo("welcome","welcome there yhooooooo!.......",parent=self.root)#


root=Tk()
obj=lib(root)
root.mainloop()