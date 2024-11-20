import tkinter as tk

window=tk.Tk()
window.title("TIC TAC TOE")
window.geometry("800x500")

titlr=tk.Label(window,text="** TIC TAC TOE **",font=("Consolas",35)) #Title of Game
titlr.pack(pady=20,padx=20)

xpoi,ypoi=0,0

buttonframe=tk.Frame(window)     #Frame for X and O Place holder
buttonframe.columnconfigure(0, weight =4)
buttonframe.columnconfigure(1, weight =4)
buttonframe.columnconfigure(2, weight =4)

def logic():

    l=[(box1,box2,box3),(box4,box5,box6),(box7,box8,box9),(box1,box4,box7),(box2,box5,box8),(box3,box6,box9),(box1,box5,box9),(box3,box5,box7)]
    for i in l:
        a,b,c=i[0],i[1],i[2]
        logicr(a,b,c)
        
def logicr(a,b,c): #checks for winner also Add to Score Board
            global xpoi,ypoi
            if a['text']== b['text']== c['text']!="___" :
                winner=a["text"]+" WON!!"
                if a["text"]== " X ":
                    xpoi+=1
                    xpoint['text']=xpoi
                else:
                    ypoi+=1
                    ypoint['text']=ypoi   
                result=tk.Label(window,text=winner,font=("Consolas",20))
                a['bg']="light green"
                b['bg']="light green"
                c['bg']="light green"
                result.pack()
                global n
                n=11
            else:
                pass

def butnr():  #makes buttons and hence restarts 
    global n,box1,box2,box3,box4,box5,box6,box7,box8,box9
    n=1

    box1=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box1))
    box1.grid(row=0, column=0, sticky="news")

    box2=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box2))
    box2.grid(row=0,column=1,sticky="news")

    box3=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box3))
    box3.grid(row=0,column=2,sticky="news")

    box4=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box4))
    box4.grid(row=1,column=0,sticky="news")

    box5=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box5))
    box5.grid(row=1,column=1,sticky="news")

    box6=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box6))
    box6.grid(row=1,column=2,sticky="news")

    box7=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box7))
    box7.grid(row=2,column=0,sticky="news")

    box8=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box8))
    box8.grid(row=2,column=1,sticky="news")

    box9=tk.Button(buttonframe,text="___",font=("Consolas",30 ),command=lambda:markr(box9))
    box9.grid(row=2,column=2,sticky="news")

butnr()

score=tk.Label(text="SCOREBOARD",font=("Arial",16)) #SCOREBOARD
score.place(x=70,y=100)

def resetscore():
    xpoi=0
    xpoint['text']=xpoi
    ypoi=0
    ypoint['text']=ypoi


xscore=tk.Label(text="-X:",font=("Arial",16))
xscore.place(x=70,y=130)

xpoint=tk.Button(text=xpoi,bg="light blue",font=("Arial",16),command=lambda:resetscore())
xpoint.place(x=110,y=130)

ypoint=tk.Button(text=ypoi,bg="pink",font=("Arial",16),command=lambda:resetscore())
ypoint.place(x=110,y=180)

yscore=tk.Label(text="-O:",font=("Arial",16))
yscore.place(x=70,y=180)

def markr(b): #Marks the button X or O
    global n
    if n==11:
        butnr()
    elif n == 10:
        po=tk.Label(window,text="It's a Draw",font=("Arial",15))
        po.pack(pady=5)
        butnr()
    elif b["text"] == " O " or b["text"] ==  ' X ':
        po=tk.Label(window,text="Invalid Choice",font=("Arial",12))
        po.pack(pady=5)
    else:
        if n%2==0:
            b['bg']="pink"
            b["text"]=" O "
        else:
            b['bg']="light blue"
            b["text"]=' X '
        n=n+1
    logic()

buttonframe.pack() #display Button

rebutn=tk.Button(window,text="ReMatch?",bg="light yellow",font=("Arial",15),command=lambda:butnr()) #Restart Button
rebutn.pack(pady=10)

window.mainloop()
