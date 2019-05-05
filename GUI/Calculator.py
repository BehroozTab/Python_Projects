import tkinter as tk
win = tk.Tk()
win.title("Hello")

con1 = tk.IntVar()
opr = tk.StringVar()
num1=tk.IntVar()
frame = tk.Frame(win)
frame.grid(row=2, column=5)

def addnum(k):
  global con1
  v = con1.get()
  con1.set(v*10+k)

def savenum():
  global con1
  global num1
  num1 = con1.get()
  con1.set(0)

l1 = tk.Label(frame,width=20,textvariable = con1)
l1.grid(row=0, column=1)
l2 = tk.Label(frame, text = "Exp :")
l2.grid(row=0, column=0)

b1 = tk.Button(frame, text = "  1  ",width=15,height=2,command=(lambda con1=1: addnum(con1)))
b1.grid(row=2, column=1)
b2 = tk.Button(frame, text = "  2  ",width=15,height=2,command=(lambda con1=2: addnum(con1)))
b2.grid(row=2, column=0)
bq = tk.Button(frame, text = "  Close  ",width=15,height=2,command = quit)
bq.grid(row=3, column=0)
badd = tk.Button(frame, text = "  +  ",width=15,height=2,command=(lambda opr='+': savenum()))
badd.grid(row=2, column=2)

win.mainloop()

