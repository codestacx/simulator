from pynput.keyboard import Key, Controller
import time
import tkinter as tk
from tkinter import messagebox
keyboard = Controller();
master = tk.Tk() # master instance

e1 = tk.Entry(master)   #text field
tkvarq = tk.StringVar(master) #input menu

commands = ["Key Down","Key Up","Enter","Key Right","Key Left"]
commandsList = {
    "Key Down": Key.down,
    "Key Up": Key.up,
    "Enter": Key.enter,
    "Key Right": Key.right,
    "Key Left": Key.left
}

def centerizeScreen():
    # Gets the requested values of the height and widht.
    windowWidth = master.winfo_reqwidth()
    windowHeight = master.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)
    master.geometry("+{}+{}".format(positionRight, positionDown))
 

def pressAndReleaseKey(command):
    keyboard.press(command)
    keyboard.release(command)

def processCommand(command,timeInterval):
    time.sleep(timeInterval)
    pressAndReleaseKey(commandsList[command])
    processCommand(command,timeInterval)

def startSimulation():
    command = tkvarq.get()
    if e1.get() == '':
        messagebox.showerror("Error", "Please specifiy value for time interval in seconds");
        return
        
    timeInterval = int(e1.get())
    print(timeInterval)
    if timeInterval <= 0:
        messagebox.showerror("Error", "Time Interval must be positive (seconds)")
        return
    processCommand(command,timeInterval)


def UI():
    centerizeScreen();
    tk.Label(master, 
         text="Time Interval").grid(row=0)
    
    e1.grid(row=0, column=1)
    
    tk.Label(master, 
         text="Trigger Command").grid(row=1,column=0) 
    tkvarq.set(commands[0])
    question_menu = tk.OptionMenu(master,  tkvarq, *commands)
    question_menu.grid(row=1,column=1)

    
    
    tk.Button(master, 
              text='Quit', 
              command=master.quit).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(master,
              text='Start', command=startSimulation).grid(row=3, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)

    tk.mainloop()


def main():
    UI()

if __name__ == '__main__':
    main()   


