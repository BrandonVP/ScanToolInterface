import serial
import sys
import glob
import tkinter as tk
from tkinter.constants import CENTER, NONE, TRUE
from tkinter.scrolledtext import ScrolledText 

comPort = 'COM18'
WINDOW_SIZE = '700x700'

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class serialCapture(tk.Tk):
    def __init__(self):
        super().__init__()

        # Try Else
        try:
            self.uart = serial.Serial(comPort, baudrate=115200, timeout=10)
        except Exception as e:
            print(e)
        else:
            print("Unable to open port")
            app = connect()
        
        self.stop = False
        self.title("ScanTool")
        self.geometry(WINDOW_SIZE) 
        self.st = ScrolledText(self, width=50, height=10)
        self.st.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        btn1=tk.Button(self, text="Start", width=10,height=4, command=self.startCapture, bg ='grey',fg='black')
        btn1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        btn2=tk.Button(self, text="Stop", width=10,height=4, command=self.stopCapture, bg ='grey',fg='black')
        btn2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        btn3=tk.Button(self, text="Clear", width=10,height=4, command=self.clearBox, bg ='grey',fg='black')
        btn3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        btn4=tk.Button(self, text="Save", width=10,height=4, command=self.saveCapture, bg ='grey',fg='black')
        btn4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        self.st.after(1, self.update)
        
        
    def startCapture(self):
        self.stop = False

    def stopCapture(self):
        self.stop = True

    def clearBox(self):
        self.st.delete('1.0', tk.END)

    def saveCapture(self):
        captureFile = open("test.txt", "w")
        captureFile.write(self.st.get(1.0, tk.END))
        captureFile.close()

    def update(self):
        if self.stop == False:
            temp = self.uart.in_waiting
            if (temp > 0):
                fully_scrolled_down = self.st.yview()[1] == 1.0
                self.st.insert(tk.INSERT, self.uart.readline())
                if fully_scrolled_down:
                    self.st.see("end")
        self.st.after(1, self.update)

 
class connect(tk.Tk):
    def __init__(self):
        super().__init__()
        print(comPort)
        self.title("ScanTool")
        btn1=tk.Button(self, text="Serial Capture", width=14,height=2, command=self.connectSerial, bg ='grey',fg='black')
        btn1.place(x=300,y=50)
        btn2=tk.Button(self, text="Capture Files", width=14,height=2, command=NONE, bg ='grey',fg='black')
        btn2.place(x=300,y=100)
        btn3=tk.Button(self, text="Pid Scans", width=14,height=2, command=NONE, bg ='grey',fg='black')
        btn3.place(x=300,y=150)
        btn4=tk.Button(self, text="Mac Address", width=14,height=2, command=NONE, bg ='grey',fg='black')
        btn4.place(x=300,y=200)
        self.geometry(WINDOW_SIZE) 
    def connectSerial(self):
        app = serialCapture()
        self.after(1, self.destroy)
        

class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ScanTool")
        self.geometry(WINDOW_SIZE) 
        btn=tk.Button(self, text="Connect", width=14,height=2, command=self.connectTool, bg ='grey',fg='black')
        btn.place(x=300,y=100)

        self.clicked = tk.StringVar()
        options = serial_ports()
        self.clicked.set(options[0])
        drop = tk.OptionMenu( self, self.clicked , *options )
        drop.config(width=11,height=2, bg = 'grey')
        drop.place(x=300,y=200)

    def connectTool(self):
        print(self.clicked.get())
        comPort = self.clicked.get()
        print(comPort)
        app = connect()
        self.after(1, self.destroy)


if __name__ == "__main__":
    app = main()
    app.mainloop()


#Drop memus
"""
from tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
"""


#tab example
"""
import tkinter.messagebox
from tkinter import *
app=Tk() #creating the main window and storing the window object in 'win'
app.title('ScanTool') #setting title of the window
app.geometry('600x400') #setting the size of the window




def func():#function of the button
    tkinter.messagebox.showinfo("Greetings","Hello! Welcome to PythonGeeks.")
    

btn=Button(app,text="Click Me", width=10,height=4,command=func, bg ='red',fg='white')
btn.place(x=100,y=30)

lab=Label(app,text='PythonGeeks',width=50,height=30)
lab.place(x=100,y=100)


app.mainloop() #running the loop that works as a triggerrunning the loop that works as a trigger
"""

"""
from tkinter import *
from tkinter.ttk import *

root = Tk()
tabmanager = Notebook(root)
tabmanager.pack(expand=1,fill="both")

tab1 = Frame(tabmanager)
tab2 = Frame(tabmanager)

tabmanager.add(tab1,text="Home")
tabmanager.add(tab2,text="About")

root.mainloop()
"""