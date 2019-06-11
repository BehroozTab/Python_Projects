import tkinter as tk
win = tk.Tk()
win.title("Calculator")

con1 = tk.IntVar()
opr = ''
num1 = tk.IntVar()

#win.resizable(100,20)
frame = tk.Frame(win)
frame.grid(row=2, column=5)

def addnum(k):
  global con1
  v = con1.get()
  con1.set(v*10+k)

def savenum(op):
  global con1
  global num1
  global opr
  opr = op
  num1 = con1.get()
  con1.set(0)

def calc():
  global con1
  global num1
  global opr
  n1 = num1
  n2 = con1.get()
  if opr=='+':
    con1.set(n1+n2)
  if opr=='*':
    con1.set(n1*n2)

l1 = tk.Label(frame,width=15, height=2,bg = "white",textvariable = con1)
l1.grid(row=0, column=1)
#l1.pack(side="right")
l2 = tk.Label(frame, text = "Exp :")
l2.grid(row=0, column=0)


b1 = tk.Button(frame, text = "  1  ",width=15,height=2,command=(lambda n=1: addnum(n)))
b1.grid(row=2, column=2)
b2 = tk.Button(frame, text = "  2  ",width=15,height=2,command=(lambda n=2: addnum(n)))
b2.grid(row=2, column=1)
b3 = tk.Button(frame, text = "  3  ",width=15,height=2,command=(lambda n=3: addnum(n)))
b3.grid(row=2, column=0)
b4 = tk.Button(frame, text = "  4  ",width=15,height=2,command=(lambda n=4: addnum(n)))
b4.grid(row=3, column=2)
b5 = tk.Button(frame, text = "  5  ",width=15,height=2,command=(lambda n=5: addnum(n)))
b5.grid(row=3, column=1)
b6 = tk.Button(frame, text = "  6  ",width=15,height=2,command=(lambda n=6: addnum(n)))
b6.grid(row=3, column=0)
b7 = tk.Button(frame, text = "  7  ",width=15,height=2,command=(lambda n=7: addnum(n)))
b7.grid(row=4, column=2)
b8 = tk.Button(frame, text = "  8  ",width=15,height=2,command=(lambda n=8: addnum(n)))
b8.grid(row=4, column=1)
b9 = tk.Button(frame, text = "  9  ",width=15,height=2,command=(lambda n=9: addnum(n)))
b9.grid(row=4, column=0)

bq = tk.Button(frame, text = "  Close  ",width=15,height=2,command = quit)
bq.grid(row=5, column=0)
badd = tk.Button(frame, text = "  +  ",width=15,height=2,command=(lambda op='+' : savenum(op)))
badd.grid(row=2, column=3)
badd = tk.Button(frame, text = "  *  ",width=15,height=2,command=(lambda op='*' : savenum(op)))
badd.grid(row=3, column=3)
bequ = tk.Button(frame, text = "  =  ",width=15,height=2,command=calc)
bequ.grid(row=4, column=3)

win.mainloop()
