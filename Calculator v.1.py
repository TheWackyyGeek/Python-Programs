from tkinter import *

def click(event):
    #i want to capture the value from screen
    text =  event.widget.cget("text") #extract text from widget
    # now mujhe 3 diff value input digit, ops, c so different operations
    print(text)
    
    
    if text == "=":
        if scvalue.get().isdigit():
             value = int(scvalue.get())
        else:
             value = eval(screen.get())  # string ko evaluate karta hai
        
        scvalue.set(value)
        screen.update
    elif text == "C":
      scvalue.set("")
      screen.update
    else:
      scvalue.set(scvalue.get() + text)
      screen.update

# def deleteFunc():
#   lenght = len(screen.get())
#   screen.delete(lenght-1,'end')
  
    
root = Tk()
root.geometry("260x340")
root.resizable(False,False)
root.configure(background="#FEFEFE")
root.title("Calculator")
# root.wm_iconbitmap("calc.ico")
photo = PhotoImage(file="calc.png")
root.iconphoto(False, photo)
# root.configure(background="grey")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 ", bg="#EFEFEE", bd=2)
screen.pack(fill=X, ipadx=4, pady=10, padx=24)

f = Frame(root, bg="white")
b = Button(f, text="7",pady=2, padx=8, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="8",pady=2, padx=6, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="9",pady=2, padx=6, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="C",pady=1, padx=4.8, font= "lucida 18 bold", bg= "#55C612", fg="white")
b.pack(side = LEFT, pady= 1, padx=4)
b.bind("<Button-1>", click)
f.pack()
#---------------
f = Frame(root, bg="white")
b = Button(f, text="4",pady=2, padx=7, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="5",pady=2, padx=6, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="6",pady=2, padx=7, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="+",pady=0.8, padx=6, font= "lucida 18 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)
f.pack()
#-----------------------
f = Frame(root, bg="white")
b = Button(f, text="1",pady=2, padx=8, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="2",pady=2, padx=6.5, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="3",pady=0.7, padx=5.5, font= "lucida 18 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="-",pady=2, padx=8, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)
f.pack()
#-----------------------
f = Frame(root, bg="white")
b = Button(f, text="0",pady=2, padx=7, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=3)
b.bind("<Button-1>", click)

b = Button(f, text=".",pady=2, padx=10, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="%",pady=2, padx=5, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

b = Button(f, text="/",pady=2, padx=10.5, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)
f.pack()


#----------------------------
f = Frame(root, bg="white")
b = Button(f, text="*",pady=2, padx=8, font= "lucida 17 bold")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)

# b = Button(f, text="Del",pady=2, padx=12, font= "lucida 15 bold", bg="Blue",fg="white",command=deleteFunc)
b.pack(side = LEFT, pady= 2, padx=3)
b.bind("<Button-1>", click)

b = Button(f, text="=",pady=2, padx=62, font= "lucida 18 bold", bg="#FFC300",fg="white")
b.pack(side = LEFT, pady= 2, padx=4)
b.bind("<Button-1>", click)


f.pack()

#photoimage use karte digits ko icon se replace kar sakte hai


#multiple frames ke ander buttons pack kar diya
root.mainloop()
