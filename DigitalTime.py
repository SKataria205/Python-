from tkinter import*
#from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *

class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Analog Clock",font=("times new roman",50, "bold"),
        bg="#04444a",fg="white")
        self.lbl=Label(self.root,bg="white",bd=20,relief=GROOVE)
        self.lbl=Place()#x=450, y=150,height=400,width=400)
        # self.clock_image()
        self.working()

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=Image.Draw(clock)
#For clock image
        bg=Image.open(clock.png)
        bg=bg.resize((300,300), Image.ANTIALIAS)
        clock.paste(bg,(50,50))
#For Hour Line image
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr)),250,200),fill="red",width=3)
        #For Min Line image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_)),280,210),fill="darkblue",width=3)
        #For Sec Line image
        draw.line((origin,200+80*sin(radians(sec_)),200-100*cos(radians(sec_)),300,200),fill="black",width=3)
        draw.ellipes((195,195,210,210),fill="black")
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        print(h,m,s)
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img.ImageTK.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)





root=Tk()
obj=Clock(root)
root=mainloop()