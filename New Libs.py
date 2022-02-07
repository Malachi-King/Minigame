from tkinter import (messagebox, Tk, Entry, mainloop)
import tkinter as tk

def gui1():
    if prompt1 := messagebox.askyesno(
        title="Welcome to Mad Libs!", message="Do you want to play Mad Libs?"
    ):
        gui2()
    elif prompt2 := messagebox.askyesno(
        title="Are you sure?", message="Did you say you want to play Mad Libs?"
    ):
        gui2()
    else:
        messagebox.showinfo(title = "Fine then.", message = "Fuck you too.")
def gui2():
    if gui2prompt1 := messagebox.askyesno(
        title="Mad Libs", message="Have you ever played Mad Libs?"
    ):
        playedMadLibsTrue()
    else:
        playedMadLibsFalse()
        playedMadLibsFalse()
def playedMadLibsFalse():
    messagebox.showinfo(title = "Mad Libs Rules", message = "Let's go over the rules, then!")
    messagebox.showinfo(title = "Mad Libs Rules", message = "I have a story that's missing some words. It's your job to give me the words to fill in the blanks.")
    messagebox.showinfo(title = "Mad Libs Rules", message = "I can't show you the story until we are done.")
    messagebox.showinfo(title = "Mad Libs Rules", message = "I will ask you for a person, place, or thing. Give me a word you think can fit in to the story.")
    if ask1 := messagebox.askyesno(
        title="Mad Libs Rules", message="Are you ready?"
    ):
        playedMadLibsTrue()
def playedMadLibsTrue():
    messagebox.showinfo(title = "Mad Libs", message = "Let's get started, then!")
    tkinterUIGeneration1()

def tkinterUIGeneration1():
    master = Tk()
    master.geometry("500x200")
    master.title("Mad Libs")
    userInput1 = tk.StringVar()
    prompt1 = tk.Label(master, text = "Give me an animal: " ).pack()
    entry1 = tk.Entry(master, textvariable = userInput1).pack()
    button1 = tk.Button(master, text = "Confirm...", command=tkinterUIGeneration2).pack()

def tkinterUIGeneration2():
    messagebox.showinfo(title = "Penis", message = "penis")


def main():
    gui1()
    
if __name__ == "__main__":
    main()

mainloop()