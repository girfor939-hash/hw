from tkinter import *
from tkinter import ttk

root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

task = StringVar()
task_entry = ttk.Entry(mainframe, width=7, textvariable=task)
task_entry.grid(column=2, row=1, sticky=(W, E))

ans = StringVar()

ttk.Label(mainframe, textvariable=ans).grid(
    column=2, row=2, sticky=(W, E), pady=(6, 0)
)

def out():
    ans.set(eval(task.get()))

ttk.Button(mainframe, text="Calculate", command=out).grid(
    column=2, row=3, sticky=(W, E), pady=(6, 0)
)

mainframe.columnconfigure(2, weight=1)

root.mainloop()
