import tkinter as tk
from tkinter import filedialog
from random import shuffle,choice




root = tk.Tk()

root.geometry("900x800")
root.title()

type_list = tk.StringVar()
type_list.set("Scramble No_Vowels")

c = []

vowel_list = ["a","e","i","o","u"]

lb = tk.Listbox(root, listvariable = type_list)

def show_choices():
    lb.grid(column = 1 , row = 2)
    
def openfile():
    global c
    filename = filedialog.askopenfilename()
    f = open(filename)
    con = f.read()
    c = con.split("\n")
    f.close()
    show_choices()
    #print(c)

open_btn = tk.Button(root, text = "Open",command = openfile)
open_btn.grid(column = 1, row = 1)

def show_no_vowel_word(word,hint):
    no_vowel_word = ""
    for l in word:
        if l not in vowel_list:
            no_vowel_word += l
    hint.configure(text = no_vowel_word)
    hint.grid(column = 3, row = 2)
    entry.grid(column = 3, row = 3)

def show_scrambled_word(word,hint):
    scrambled_word = shuffle(word)
    hint.configure(text = scrambled_word)
    hint.grid(column = 3, row = 2)
    entry.grid(column = 3, row = 3)
    

hint = tk.Label()

def on_select(event):
    selection = event.widget.get(int(event.widget.curselection()[0]))
    word = choice(c)
    if selection == "Scramble":    
        show_scrambled_word(word,hint)
    elif selection == "No_Vowels":
        show_no_vowel_word(word,hint)
    lb.grid_forget()
    #print()

def Check(event):
    print("checking")

lb.bind("<<ListboxSelect>>", on_select)





entry = tk.Entry(root,textvariable = hint)
entry.bind("<KeyRelease-Return>",Check)


    
root.mainloop()
