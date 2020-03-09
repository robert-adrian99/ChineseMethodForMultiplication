from tkinter import*
from turtle import*
import array as arr
from math import*

x4=0
y4=0 

fereastra=Tk()

display1=IntVar()
display2=IntVar()

canvas = Canvas(master=fereastra,width = 500, height = 500,bg="aqua")

frame=Frame(fereastra,width=500, height=500, borderwidth=4, bd=4, bg="powderblue")

label1=Label(frame,width=50,text=0, height=1, bg="powderblue")
label1.pack(side=BOTTOM,expand=YES,anchor=CENTER)

label2=Label(frame,width=50, text='The Result is: ', height=1, bg="powderblue")
label2.pack(side=BOTTOM,expand=YES,anchor=CENTER)

intrare1=Entry(frame, relief=RIDGE, textvariable=display1, justify="right", bd=10, bg="deepskyblue")
intrare1.pack(side=LEFT,expand=NO,anchor=NE)

intrare2=Entry(frame, relief=RIDGE, textvariable=display2, justify="right", bd=10, bg="deepskyblue")
intrare2.pack(side=RIGHT,expand=NO,anchor=NE)

rezultat=0

def invers(numar):
    numarnou=0
    while numar > 0:
        cifra = numar % 10
        numarnou=numarnou*10+cifra
        numar = numar //10
    return numarnou

def nrcif(numar):
    nr=0
    while numar>0:
        cifra=numar%10
        nr=nr+1
        numar=numar//10
    return nr

class Desen:

    global display1,display2,canvas
    def line_intersection(line1, line2):
                xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
                ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

                def det(a, b):
                    return a[0] * b[1] - a[1] * b[0]

                div = det(xdiff, ydiff)
                if div == 0:
                   raise Exception('lines do not intersect')

                d = (det(*line1), det(*line2))
                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                return x, y

    nr1punct=invers(display1.get())
    nr2punct=display2.get()
    x1=-250
    y1=40
    while nr1punct>0:
        while nr1punct%10>0:
            x2=800*(0.939692620785908)+x1
            y2=800*(0.342020143325669)+y1
            A=(x1,y1)
            B=(x2,y2)
            x3=400
            y3=-180
            while nr2punct>0:
                while nr2punct%10>0:
                    x4=800*(-0.766044443118978)+x3
                    y4=800*(0.642787609686539)+y3
                    C=(x3,y3)
                    D=(x4,y4)
                    px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
                    py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
                    canvas.create_oval(px,py,px,py,fill='red')
                    x3-=20
                x3-=80
                nr2punct=nr2punct//10
            y1-=20
        y1-=60
        nr1punct=nr1punct//10

class app(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Chinese Method for Multiplication")

    global display1
    global display2
    global frame
    global intrare1
    global intrare2
    global rezultat
    global canvas
    global x4,y4

    frame.pack(side=TOP,fill=BOTH, expand=YES)
    canvas.pack(fill=BOTH)

    def leftClick():
           nrnormal=IntVar()
           nrnormal=display1.get()
          
           numar2=IntVar()
           numar2=display2.get()

           size=nrcif(nrnormal)+nrcif(numar2)
           vector=[0]*size
           cifre1=[0]*nrcif(nrnormal)
           index=0
           dimensiune=nrcif(nrnormal)

           x=-500
           y=50
           turtle_screen = TurtleScreen(canvas)
           turtle_screen.bgcolor("aqua")
           broscuta=RawTurtle(turtle_screen)
           broscuta._rotate(20)
           
           nr1=IntVar()
           nr1=invers(nrnormal)

           while nrnormal > 0:
               cifre1[index]=nrnormal%10
               nrnormal=nrnormal//10
               index=index+1
              
           
           while nr1 > 0:
               cifra=nr1%10
               while cifra > 0:
                    broscuta.penup()
                    broscuta.goto((x,y))
                    broscuta.pendown()
                    broscuta.forward(800)
                    y=y-10
                    cifra=cifra-1
               nr1=nr1//10
               index=index-1
               y=y-80
           nr=0
           x=400
           y=-180
           broscuta._rotate(120)
           while numar2 > 0:
               cifra=numar2%10
               trans=0
               for i in range(0,dimensiune):
                   count=cifre1[i]*cifra
                   vector[i+nr]=vector[i+nr]+count%10+trans
                   trans=count//10
                   if nrcif(vector[i+nr]) > 1:
                       trans=trans+1
                       vector[i+nr]=vector[i+nr]%10

               while cifra > 0:
                    broscuta.penup()
                    broscuta.goto((x,y))
                    broscuta.pendown()
                    broscuta.forward(700)
                    x=x-20
                    cifra=cifra-1
               numar2=numar2//10
               nr=nr+1
               x=x-80

           broscuta.hideturtle()
           rezultat=0
           p=1
           for i in range(1,size):
              vector[i]=vector[i]+vector[i-1]//10
              rezultat=rezultat+vector[i-1]*p
              p=p*10
           rezultat=rezultat+vector[size-1]*p
           label1.config(text=str(rezultat))
           
    buton=Button(frame, text="MULTIPLY", command=leftClick, bd=8, bg="springgreen")
    buton.pack(side=LEFT, expand=YES, anchor=N)
    
    def clearClick():
        canvas.delete("all")
        display1=0;
        intrare1.delete(0,END)
        intrare1.insert(0,'0')
        display2=0;
        intrare2.delete(0,END)
        intrare2.insert(0,'0')
        label1.config(text=0)

    butonClr=Button(frame, text="CLEAR", command=clearClick, bd=8, bg="red")
    butonClr.pack(side=RIGHT, expand=YES, anchor=N)

app()
fereastra.mainloop()