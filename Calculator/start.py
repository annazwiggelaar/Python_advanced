from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Calculator")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="Quit", command=self.exit_window)
        quit_button.place(x=0, y=0)
        button_0 = Button(self, text="0")
        button_0.place(x=200, y=450)
        button_point = Button(self, text=".")
        button_point.place(x=230, y=450)
        button_1 = Button(self, text="1")
        button_1.place(x=200, y=400)
        button_2 = Button(self, text="2")
        button_2.place(x=230, y=400)
        button_3 = Button(self, text="3")
        button_3.place(x=260, y=400)
        button_4 = Button(self, text="4")
        button_4.place(x=200, y=350)
        button_5 = Button(self, text="5")
        button_5.place(x=230, y=350)
        button_6 = Button(self, text="6")
        button_6.place(x=260, y=350)
        button_7 = Button(self, text="7")
        button_7.place(x=200, y=300)
        button_8 = Button(self, text="8")
        button_8.place(x=230, y=300)
        button_9 = Button(self, text="9")
        button_9.place(x=260, y=300)
        button_ac = Button(self, text="AC")
        button_ac.place(x=200, y=250)
        button_divide = Button(self, text="%", command=self.divide)
        button_divide.place(x=290, y=250)
        button_multiply = Button(self, text="x", command=self.multiply)
        button_multiply.place(x=290, y=300)
        button_minus = Button(self, text="-", command=self.minus)
        button_minus.place(x=290, y=350)
        button_add = Button(self, text="+", command=self.add)
        button_add.place(x=290, y=400)
        button_is = Button(self, text="=")
        button_is.place(x=290, y=450)
        w = Canvas(self, bg="grey", width=200, height=100)          # place for output
        w.pack()
        w.create_text(100, 20, fill="darkblue", text="test")        # text output


    def exit_window(self):
        exit()

    def divide(self):
        return lambda a, b: a / b

    def multiply(self):
        return lambda a, b: a * b

    def minus(self):
        return lambda a, b: a - b

    def add(self):
        return lambda a, b: a + b


root = Tk()
root.geometry("400x500")
app = Window(root)
root.mainloop()
