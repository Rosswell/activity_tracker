from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
import csv


# global variables
timerVar = None
afterId = None

root = Tk()
root.focus_force()
root.title("Activity Tracking")

mainframe = ttk.Frame(root, padding="4 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

task = StringVar()
task1Time = StringVar()
task2Time = StringVar()
task3Time = StringVar()
task4Time = StringVar()
task5Time = StringVar()
task6Time = StringVar()
task7Time = StringVar()
task8Time = StringVar()
task9Time = StringVar()
task10Time = StringVar()
task11Time = StringVar()

# setting default values
timerList = [task2Time, task3Time, task4Time, task5Time, task6Time,
             task7Time, task8Time, task9Time, task10Time, task11Time]
for timer1 in timerList:
    timer1.set('00:00:00')
timerDict = {k: v for k, v in zip(list(range(1, 11)), timerList)}


def startTimer(dictKey):
    global timerVar
    if not afterId:
        timerVar = timerDict[dictKey]
        update_clock()


def update_clock():
    global timerVar
    global afterId
    myTime = datetime.strptime(timerVar.get(), "%H:%M:%S")
    myTime += timedelta(seconds=1)
    timerVar.set(myTime.strftime("%H:%M:%S"))
    # afterId is for root.after_cancel(afterId) calls to cancel the after call
    afterId = root.after(1000, update_clock)

def stopTimer():
    global afterId
    root.after_cancel(afterId)
    afterId = None

# labels
ttk.Label(mainframe, text="Task").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Total Time").grid(column=2, row=1)

# row 2
ttk.Label(mainframe, text="Hamilton Dev").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=task2Time).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(1)).grid(column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=2, sticky=(W, E))

# row 3
ttk.Label(mainframe, text="LIMS Dev").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=task3Time).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(2)).grid(column=3, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=3, sticky=(W, E))

# row 4
ttk.Label(mainframe, text="LIMS Support").grid(column=1, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=task4Time).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(3)).grid(column=3, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=4, sticky=(W, E))

# row 5
ttk.Label(mainframe, text="Documentation").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=task5Time).grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(4)).grid(column=3, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=5, sticky=(W, E))

# row 6
ttk.Label(mainframe, text="NFL Algorithm").grid(column=1, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=task6Time).grid(column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(5)).grid(column=3, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=6, sticky=(W, E))

# row 7
ttk.Label(mainframe, text="PR reviews").grid(column=1, row=7, sticky=(W, E))
ttk.Label(mainframe, textvariable=task7Time).grid(column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(6)).grid(column=3, row=7, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=7, sticky=(W, E))

# row 8
ttk.Label(mainframe, text="Discussion (Slack/Email)").grid(column=1, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=task8Time).grid(column=2, row=8, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(7)).grid(column=3, row=8, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=8, sticky=(W, E))

# row 9
ttk.Label(mainframe, text="Meetings").grid(column=1, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=task9Time).grid(column=2, row=9, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(8)).grid(column=3, row=9, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=9, sticky=(W, E))

# row 10
ttk.Label(mainframe, text="HR").grid(column=1, row=10, sticky=(W, E))
ttk.Label(mainframe, textvariable=task10Time).grid(column=2, row=10, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(9)).grid(column=3, row=10, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=10, sticky=(W, E))

# row 11
ttk.Label(mainframe, text="Misc Not work").grid(column=1, row=11, sticky=(W, E))
ttk.Label(mainframe, textvariable=task11Time).grid(column=2, row=11, sticky=(W, E))
ttk.Button(mainframe, text="Start Timer", command=lambda: startTimer(10)).grid(column=3, row=11, sticky=(W, E))
ttk.Button(mainframe, text="Stop Timer", command=stopTimer).grid(column=4, row=11, sticky=(W, E))

def export():
    now = datetime.now().strftime("%m/%d/%Y")
    times = [now, task2Time.get(), task3Time.get(), task4Time.get(), task5Time.get(), task6Time.get(),
             task7Time.get(), task8Time.get(), task9Time.get(), task10Time.get(), task11Time.get()]
    try:
        with open('/Users/ross/Documents/LIMS/activityTracker.csv', 'a', newline='\n') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            writer.writerow(times)
        exportSuccess(True)
    except:
        exportSuccess(False, times)

def exportSuccess(success, times=None):
    toplevel = Toplevel()
    if success:
        label1 = Message(toplevel, text='Export Successful', width=400)
    else:
        label1 = Message(toplevel, text='Export Unsuccessful.\nManually write times:\n{}'.format(','.join(times)), width=400)
    label1.pack()
    but1 = Button(toplevel, text='OK', command=toplevel.destroy)
    but1.pack()
    centerWindow(toplevel)
    toplevel.focus_force()

def resetTimers():
    def okPress(event=None):
        for timer in timerList:
            timer.set('00:00.00')
        toplevel.destroy()
    def cancelPress():
        toplevel.destroy()
    toplevel = Toplevel()
    toplevel.bind('<KP_Enter>', okPress)
    toplevel.bind('<Return>', okPress)
    label1 = Message(toplevel, text='Are you sure you want to reset all the timers?', width=400)
    label1.pack()
    but1 = Button(toplevel, text='OK', command=okPress)
    but1.bind('<KP_Enter>', okPress)
    but1.bind('<Return>', okPress)
    but2 = Button(toplevel, text='Cancel', command=cancelPress)
    but1.pack()
    but2.pack()
    centerWindow(toplevel)
    toplevel.focus_force()

def centerWindow(window):
    root.update_idletasks()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    currentPos = int(root.geometry().split('+')[1])
    # calculate x and y coordinates for the Tk window based on the screen it's on
    if currentPos < 1680:
        x = 1680 / 2 - size[0] / 2
        y = 1050 / 2 - size[1] / 2
    elif currentPos >= 1680 and currentPos < 3600:
        x = 1680 + 1920 / 2 - size[0] / 2
        y = 1080 / 2 - size[1] / 2
    else:
        x = 1680 + 1920 + 1080 / 2 - size[0] / 2
        y = 1046 / 2 - size[1] / 2

    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

# non-timer functionality
ttk.Button(mainframe, text="Export", command=export).grid(column=4, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Clear Timers", command=resetTimers).grid(column=3, row=1, sticky=(W, E))

# configuring the window location
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
centerWindow(root)
root.mainloop()
