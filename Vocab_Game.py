import tkinter as tk
from tkinter import filedialog
from random import shuffle




root = tk.Tk()

root.geometry("900x800")
root.title()

type_list = tk.StringVar()
type_list.set("Scramble No_Vowels")

c =""

vowel_list = ["a","e","i","o","u"]

def openfile():
    global c
    filename = filedialog.askopenfilename()
    f = open(filename)
    c = f.read()
    f.close()
    #print(c)

open_btn = tk.Button(root, text = "Open",command = openfile)
open_btn.grid(column = 1, row = 1)

lb = tk.Listbox(root, listvariable = type_list)
lb.grid(column = 1 , row = 2)

def on_select(event):
    print(event.widget.get(int(event.widget.curselection()[0])))

lb.bind("<<ListboxSelect>>", on_select)

def show_no_vowel_word(word):
    no_vowel_word = ""
    for l in word:
        if l not in vowel_list:
            no_vowel_word.append(l)

def show_scrambled_word(word):
    scrambled_word = shuffle(word)

root.mainloop()
