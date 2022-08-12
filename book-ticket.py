from tkinter import *
from tkinter.ttk import OptionMenu
from tkinter.messagebox import askyesno
root=Tk()
root.geometry("980x700+0+0")
root.title("Cyber Security")
root.configure(bg="sky blue")

Tops = Frame(root,bg="light blue",width = 980,height=150,relief=SUNKEN)
Tops.pack(side=TOP)


#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Ticket Booking",fg="steel blue",bg="light green")
lblinfo.grid(row=1,column=1)
lbl = Label(Tops,bg="light blue",bd='50')
lbl.grid(row=0,column=2)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=2,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=3,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=4,column=0)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Movies:",bd='15',fg="steel blue",bg="light blue")
lbl.grid(row=5,column=0)
ml=["Select","RRR","KGF","Sitaramam"]
c1=StringVar()
d1=OptionMenu(Tops,c1,*ml)
d1.grid(column=1,row=5)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Tickets",bd='15',fg="steel blue",bg="light blue")
lbl.grid(row=6,column=0)
tl=["Select",1,2,3,4,5]
c2=IntVar()
d2=OptionMenu(Tops,c2,*tl)
d2.grid(column=1,row=6)



#-----------------Submit Button Calling Function------------
def call():
    ans=askyesno("confirm?","movie:"+c1.get()+"\nTickets:"+str(c2.get()))
    if ans:
        if c1.get()=="Sitaramam":
            total=350*c2.get()
            messagebox.showinfo("bill",total)
        else:
            total=120*c2.get()
            messagebox.showinfo("bill",total)
        
btn=Button(Tops,text="Book",font=('ariel' ,16,'bold'),command=call)
btn.grid(column=1,row=14)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=16,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=17,column=0)

#-----------------main loop------------
root.mainloop()
