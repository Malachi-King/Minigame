from tkinter import messagebox
import tkinter as tkinter

def gui1():
    if prompt1 := messagebox.askyesno(
        title="Welcome to Mad Libs!", message="Do you want to play Mad Libs?"
    ):
        print("test")
    elif prompt2 := messagebox.askyesno(
        title="Are you sure?", message="Did you say you want to play Mad Libs?"
    ):
        print("test 2")
    else:
        messagebox.showinfo(title = "Fine then.", message = "Fuck you too.")
gui1()