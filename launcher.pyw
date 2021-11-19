import tkinter as tk
import tkinter.messagebox as mbox
import os, sys
root = tk.Tk()
root.title("Game Launcher")
root.iconbitmap("app.ico")
root.geometry("800x400")
root.resizable(False, False)
title = tk.Label(text="Game Laucher", font=("Arial", 24))
title.pack()
title.place(x=10, y=10)
selected_game = "Select Game"
def set_cursel(sel):
    global selected_game
    selected_game = sel
def change_window():
    root.attributes("-toolwindow", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.8)
    root.geometry("200x60")
    title["text"] = "Launched"

def launch_game():
    global selected_game
    if selected_game == "Select Game":
        mbox.showerror("Game Launcher", "Please select a game.")
    else:
        root.destroy()
        
games = ["Select Game", "Number Memory", "Reaction", "Aim"]
var = tk.StringVar()
var.set(games[0])
game_dropdown = tk.OptionMenu(root, var, *games, command=set_cursel)
game_dropdown.pack()
game_dropdown.place(x=10, y=70)
# Launch button
launch_button = tk.Button(text="Launch", font=("Arial", 12), command=launch_game)
launch_button.pack()
launch_button.place(x=10, y=100)
root.mainloop()

if selected_game == "Number Memory":
    os.system("python .\\numbermemory\\number.pyw")
    os.system(f"python {os.path.basename(__file__)}")
elif selected_game == "Reaction":
    os.system("python .\\reaction\\reaction.pyw")
    os.system(f"python {os.path.basename(__file__)}")
elif selected_game == "Aim":
    os.system("python .\\aim\\aim.pyw")
    os.system(f"python {os.path.basename(__file__)}")
