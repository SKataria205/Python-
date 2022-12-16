
#from tkinter import *
#import tkinter
from tkinter import filedialog, Text, Tk
import os

root = Tk()
#root = tkinter.TkVersion()
apps = []

if os.path.isfile('save.txt'):
   with open('save.txt', 'r') as f:
       tempApps = f.read()
       tempApps = tempApps.split(',')
       apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename) 
    for app in apps:
        label =Tk.label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)


canvas = root.Canvas(root, height=700, width=700, bg="green")
canvas.pack()

frame = root.Frame(root,bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = root.Button(root, text="open File", padx=10,
pady=5, fg="white", bg="pink", command=addApp)
openFile.pack()

runApps = root.Button(root, text="Run Apps", padx=10,
pady=5, fg="white", bg="pink")
runApps.pack()

for app in apps:
    label = Tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.text', 'w') as f:
    for app in apps:
        f.write(app + ',')