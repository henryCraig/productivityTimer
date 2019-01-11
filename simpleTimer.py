from tkinter import *
from tkinter import ttk

root = Tk()



def updateWatch():
    if state == True:
        seconds = int(entry.get())
        if seconds > 0:
            entry.delete(0, END)
            seconds -= 1
            entry.insert(0, seconds)
    root.after(1000, updateWatch)


def start():
    global state
    state = True

def pause():
    global state
    state = False

state = False

entry = ttk.Entry(root)
entry.pack()
startButton = ttk.Button(root, text = 'Start', command = start)
startButton.pack()
pauseButton = ttk.Button(root, text = 'Pause', command = pause)
pauseButton.pack()






updateWatch()
root.mainloop()
