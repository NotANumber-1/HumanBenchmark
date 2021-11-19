import tkinter as tk
import tkinter.ttk as ttk
import time, random
root = tk.Tk()
root.title("Aim")
root.iconbitmap("app.ico")
root.geometry("800x600+10+10")
root.resizable(False, False)
clicks = 0
running = False
stttime = 0
nowtime = 0
tempbtn = 0
timelbl = 0
cps = 0
cpslbl = 0
nd = False
def clicked():
    global clicks, tempbtn, cpslbl, cps, nowtime, stttime
    nowtime = time.time()
    timelbl["text"] = "Time elapsed: " + str(round(nowtime - stttime, 3)) + "s"
    root.update()
    clicks += 1
    pgbar["value"] += 5
    cps = round(clicks / (nowtime - stttime), 3)
    cpslbl["text"] = "Clicks per second: " + str(cps)
    root.update()
    tempbtn.destroy()
    btnrangen()

def btnrangen():
    global tempbtn, nowtime, stttime, startbtn, cpslbl, timelbl, nd
    if pgbar["value"] != 100:
        tempbtn = tk.Button(text="[!]", bg="black", fg="white", font=("Arial", 16), command=clicked)
        tempbtn.pack()
        tempbtn.place(x=random.randint(0, 700), y=random.randint(0, 500))
    else:
        nowtime = time.time()
        timelbl["text"] = "Time elapsed: " + str(round(nowtime - stttime, 3)) + "s"
        # startbtn = tk.Button(text="[!]", bg="black", fg="white", font=("Arial", 16), command=start)
        # startbtn.pack()
        # startbtn.place(x=10, y=150)
        nd = True
        root.update()

def start():
    global running, clicks, stttime, nowtime, timelbl, cpslbl, nd
    running = True
    clicks = 0
    startbtn.destroy()
    if nd:
        timelbl.destroy()
        cpslbl.destroy()
    timelbl = tk.Label(text="Time elapsed: --.---s", font=("Arial", 20))
    timelbl.pack()
    timelbl.place(x=10, y=50)
    cpslbl = tk.Label(text="Clicks per second: --.---", font=("Arial", 20))
    cpslbl.pack()
    cpslbl.place(x=10, y=100)
    stttime = time.time()
    btnrangen()

pgbar = ttk.Progressbar(orient=tk.HORIZONTAL, length=600, mode="determinate")
pgbar.pack()
pgbar.place(x=10, y=10)
startbtn = tk.Button(text="[!]", bg="black", fg="white", font=("Arial", 16), command=start)
startbtn.pack()
startbtn.place(x=10, y=50)
root.mainloop()
