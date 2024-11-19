import tkinter as tk

window=tk.Tk()

window.title("TIC TAC TOE")

window.geometry("800x500")

titlr=tk.Label(window,text="** TIC TAC TOE **",font=("Consolas",35))
titlr.pack(pady=20,padx=20)

buttonframe=tk.Frame(window)
buttonframe.columnconfigure(0, weight =4)
buttonframe.columnconfigure(1, weight =4)
buttonframe.columnconfigure(2, weight =4)

def logic():

    l=[(box1,box2,box3),(box4,box5,box6),(box7,box8,box9),(box1,box4,box7),(box2,box5,box8),(box3,box6,box9),(box1,box5,box9),(box3,box5,box7)]
    for i in l:
        a,b,c=i[0],i[1],i[2]
        logicr(a,b,c)
        
def logicr(a,b,c): #checks for winner
            if a['text']== b['text']== c['text']!="___" :
                winner=a["text"]+" WON!!"
                result=tk.Label(window,text=winner,font=("Consolas",20))
                a['bg']="light green"
                b['bg']="light green"
                c['bg']="light green"
                result.pack()
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


def markr(b): #Marks the button X or O
    global n
    if n == 10:
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

buttonframe.pack()
rebutn=tk.Button(window,text="ReMatch?",bg="light yellow",font=("Arial",15),command=lambda:butnr())
rebutn.pack(pady=10)

window.mainloop()
