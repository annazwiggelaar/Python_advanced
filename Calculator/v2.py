from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Calculator")
        self.pack(fill=BOTH, expand=1)
        canvas1 = Canvas(root, width=400, height=300)
        canvas1.pack()
        entry1 = Entry(root)
        canvas1.create_window(210, 100, window=entry1, height=23)
        entry2 = Entry(root)
        canvas1.create_window(210, 140, window=entry2, height=23)
        entry3 = Entry(root)
        canvas1.create_window(210, 200, window=entry3, height=23)
        label1 = Label(root, text="Enter value 1:")
        canvas1.create_window(100, 100, window=label1)
        label2 = Label(root, text="Enter value 2:")
        canvas1.create_window(100, 140, window=label2)
        label3 = Label(root, text="The result is:")
        canvas1.create_window(100, 200, window=label3)

        def divide():
            nr1 = entry1.get()
            nr2 = entry2.get()
            label4 = Label(root, text=float(nr1)/float(nr2), bg="white")
            canvas1.create_window(210, 200, window=label4)

        button_divide = Button(root, text="/", bg="darkorange", fg="white", command=divide)
        button_divide.place(x=310, y=100)

        def multiply():
            nr1 = entry1.get()
            nr2 = entry2.get()
            label5 = Label(root, text=float(nr1)*float(nr2), bg="white")
            canvas1.create_window(210, 200, window=label5)

        button_multiply = Button(root, text="x", bg="darkorange", fg="white", command=multiply)
        button_multiply.place(x=310, y=140)

        def minus():
            nr1 = entry1.get()
            nr2 = entry2.get()
            label6 = Label(root, text=float(nr1)-float(nr2), bg="white")
            canvas1.create_window(210, 200, window=label6)

        button_minus = Button(root, text="-", bg="darkorange", fg="white", command=minus)
        button_minus.place(x=350, y=100)

        def add():
            nr1 = entry1.get()
            nr2 = entry2.get()
            label7 = Label(root, text=float(nr1)+float(nr2), bg="white")
            canvas1.create_window(210, 200, window=label7)

        button_add = Button(root, text="+", bg="darkorange", fg="white", command=add)
        button_add.place(x=350, y=140)

        def exit_window():
            exit()

        quit_button = Button(root, text="Quit", command=exit_window)
        quit_button.place(x=0, y=0)


root = Tk()
app = Window(root)
root.mainloop()
