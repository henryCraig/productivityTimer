import time
from tkinter import *
from tkinter import ttk

root = Tk()

#we are going to make two buttons change, using just one function

def callback():
    print(button1)

def switchCall(buttonSelf):
    if buttonSelf['text'] == 'Start':
        buttonSelf.config(text = 'Pause')
    else:
        buttonSelf.config(text = 'Start')



button1 = ttk.Button(root, text = 'Start', command = lambda: switchCall(button1))
button1.pack()
button2 = ttk.Button(root, text = 'Start', command = lambda: switchCall(button2))
button2.pack()


root.mainloop()


list1 = [1,2,3,4]
print('list1')
print(eval('list1'))
