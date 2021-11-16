from tkinter import *
root = Tk()
root.geometry("400x620")
root.title("Calculator")
root.wm_iconbitmap("cal.PNG")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Syntax error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font ="lucida 30 bold")
screen.pack(fill=X, ipadx=20, pady=10,padx=10)

f = Frame(root, bg="Gray")
b = Button(f, text="9", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="8", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="7", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="/", font="lucida 26 bold",padx=10,pady=10, bg="white")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="Gray")
b = Button(f, text="6", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="5", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="4", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="*", font="lucida 26 bold",padx=8,pady=10, bg="white")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="Gray")
b = Button(f, text="3", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="2", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="1", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="-", font="lucida 26 bold",padx=9,pady=10, bg="white")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root, bg="Gray")
b = Button(f, text="%", font="lucida 26 bold",padx=4,pady=10)
b.pack(side=LEFT,padx=8.5,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="0", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="^", font="lucida 26 bold",padx=9,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="+", font="lucida 26 bold",padx=5,pady=10, bg="white")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="Gray")
b = Button(f, text=".", font="lucida 26 bold",padx=14,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="C", font="lucida 26 bold",padx=7,pady=10)
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="=", font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=7,pady=8)
b.bind("<Button-1>",click)
b = Button(f, text="()", font="lucida 26 bold",padx=5,pady=10, bg="white")
b.pack(side=LEFT,padx=7,pady=8)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()