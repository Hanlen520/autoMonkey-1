from tkinter import *
from tkinter import ttk
from util import run_monkey, stop_monkey


root = Tk()
root.title("autoMonkey")
root.minsize(200, 200)
root.maxsize(200, 200)

mainframe = ttk.Frame(root, padding="15 15 15 15").pack()

ttk.Button(mainframe, text="RUN MONKEY", command=run_monkey, padding="30").pack()
ttk.Button(mainframe, text="STOP MONKEY", command=stop_monkey, padding="30").pack()

root.mainloop()
