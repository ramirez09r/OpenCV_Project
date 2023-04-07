import tkinter as tk
from tkinter import ttk
import findScore

root = tk.Tk()
root.title("Blackjack Detector")


main = ttk.Frame(root, padding=(30, 15))
main.grid()

start_button = ttk.Button(main, text='Start', command=findScore.app)
start_button.grid(column=1, row=1)

start_button = ttk.Button(main, text='WEBCAM', command=findScore.app_webcam)
start_button.grid(column=0, row=1)

root.mainloop()
