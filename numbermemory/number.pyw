import tkinter as tk
import tkinter.messagebox as mbox
root = tk.Tk()
root.title("Number Memory")
root.iconbitmap("app.ico")
root.geometry("800x400")
root.resizable(False, False)
mbox.showerror("Number Memory", "This function is not implemented yet. ")
root.after(1000, root.destroy())
root.mainloop()
