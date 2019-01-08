import time
from tkinter import *
from tkinter import ttk

"""
seconds = int(input("How many seconds: "))
print('you said: ', seconds, "seconds")

for i in range(seconds):
    print(seconds-i)
    time.sleep(1)

print("00")
"""


#Alright, so the basic Idea right now is to take this simple code and put it into a GUI
#so first I need to create a gui with multiple
root = Tk()

#So this gives me one entry box to Write down the Activity, one to write down the Time, and one Button to start and stop
"""
entry = ttk.Entry(root, width = 30)
entry.grid()
entry = ttk.Entry(root, width = 30)
entry.grid()
button = ttk.Button(root, text = 'Start')
button.grid()
button2 = ttk.Button(root, text = 'Start')
button2.grid()
"""

#Here I want to have the button change its text to "Pause" if at start, or "Start" if text = "Pause"
#This works, this changes the button

#FIXME I need to allow this function to take arguments, so that each button can call on the same function
#I know I've done this before, it uses the word sigma somewhere

# TODO: Make lets say 8 different frames, each with its one name-able timer

"""
def callback():
    if button['text'] == 'Start':
        button.config(text = "Pause")
    else:
        button.config(text = "Start")


button.config(command = callback)
#button2.config(command = callback)
"""

#This is a different way to keep the frame visible after
#padding = (100,100)

#
#frame1.pack_propagate(0)

frame1 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame1.grid(column = 1, row = 1)
entry = ttk.Entry(frame1, width = 20)
entry.grid()
entry = ttk.Entry(frame1, width = 20)
entry.grid()
button = ttk.Button(frame1, text = 'Start')
button.grid()


frame2 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame2.grid(column = 2, row = 1)
entry = ttk.Entry(frame2, width = 20)
entry.grid()
entry = ttk.Entry(frame2, width = 20)
entry.grid()
button = ttk.Button(frame2, text = 'Start')
button.grid()

frame3 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame3.grid(column = 3, row = 1)


frame4 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame4.grid(column = 4, row = 1)

frame5 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame5.grid(column = 1, row = 2)


frame6 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame6.grid(column = 2, row = 2)


frame7 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame7.grid(column = 3, row = 2)


frame8 = ttk.Frame(root, height = 200, width = 300, relief = SUNKEN)
frame8.grid(column = 4, row = 2)



root.mainloop()
