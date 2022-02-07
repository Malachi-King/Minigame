

from tkinter import (messagebox, Tk, Entry, mainloop)
import tkinter as tk

def tkinterUIGeneration1():
    master = Tk()
    master.geometry("500x200")
    master.title("Mad Libs")
    userInput1 = tk.StringVar()
    prompt1 = tk.Label(master, text = "Give me an animal: " ).pack()
    entry1 = tk.Entry(master, textvariable = userInput1).pack()
    button1 = tk.Button(master, text = "Confirm...", command=tkinterUIGeneration2).pack()

def tkinterUIGeneration2():
    print("penis")

def main():
    tkinterUIGeneration1()

if __name__ == "__main__":
    main()

mainloop()