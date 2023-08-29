import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import random
import time



root = tk.Tk()

root.geometry("900x800")
root.title()

type_list = tk.StringVar()
type_list.set("Scramble No_Vowels Group Odd_One_Out")

c = {}

class Word:
    def __init__(self,wo,tag_list):
        self.word = wo
        self.tags = tag_list
        
    def Has_Tag(self,tag):
        return tag in self.tags

vowel_list = ["a","e","i","o","u"]

lb = tk.Listbox(root, listvariable = type_list)

def show_choices():
    lb.grid(column = 1 , row = 2)
    
def openfile():
    global c
    filename = filedialog.askopenfilename()
    f = open(filename)
    con = f.read()
    words_list = con.split("\n")
    for w in words_list:
        if "," in w:
            w = w.split(",")
            for ww in w:
                ww = ww.lstrip().rstrip()
            word = Word(w.pop(0),w)
        else:
            w = w.lstrip().rstrip()
            word = Word(w,list())
        c[word.word] = word
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
    l = list(word)
    random.shuffle(l)
    scrambled_word = "".join(l)
    hint.configure(text = scrambled_word)
    hint.grid(column = 3, row = 2)
    entry.grid(column = 3, row = 3)

group_positions = {}
word_groups = {}

def make_groups(c):
    # make a list of tags
    tag_counts, c_reversed = get_tags_and_c_reversed(c)
    #for t in tag_counts:
    #    print(t + ": " + str(tag_counts[t]))

    # select 3-5 tags with at least 2 words
    group_list = []
    num_groups = random.randint(3,5)
    while len(group_list) < num_groups:
        g = random.choice(list(tag_counts.keys()))
        if tag_counts[g] >= 2 and g not in group_list:
            group_list.append(g)

    #for g in group_list:
    #    print(g)

    #get 2-6 words for each group, don't worry about
    # words in multiple groups
    #word_groups = {}
    for g in group_list:
        word_groups[g] = list()
        #print(g)
        num_words = random.randint(2,\
                    min(len(c_reversed[g]),6))
        #print(c_reversed[g])
        random.shuffle(c_reversed[g])
        #print(c_reversed[g])
        for n in range(num_words):
            #print(c_reversed[g][n])
            word_groups[g].append(c_reversed[g][n])
            
    for x in word_groups:
        print(x)
        for w in word_groups[x]:
            print("\t" +w)
    
    # return a dictionary which has the tag for
    # key and a list of words for the value
    return word_groups


def show_groups(groups):
    global group_positions
    # make the labels using the keys
    #make draggable word labels
    word_list = []
    for g in groups:
        for w in groups[g]:
            word_list.append(w)
    print(word_list)
    random.shuffle(word_list)
    print(word_list)
    x = 0
    #label = tk.LabelFrame(root, text = list(groups.keys())[0])
    #label.grid(column = 4, row = 4)
    for g in groups:
        label = tk.Button(root, text = g,state = tk.DISABLED, padx = 8)
        label.grid(column = 4 + x, row = 4)#,padx = 6,pady=2)
        label.update_idletasks()
        group_positions[g] = [label.winfo_x(),label.winfo_y()]
        print(group_positions)
        x += 1
    x = 0
    y = 0
    for x in range(len(groups.keys())):
        for y in range(8):
            label = tk.Label(root, text = "     ")
            label.grid(column = 4 + x, row = 5+y)
            y+=1
        x+=1
        y = 0

    x = 0
    y = 0
    for w in word_list:
        label = tk.Label(root, text = w)
        label.grid(column = 4 + x, row = 8+y)
        make_draggable(label)
        x += 1
        if x > 4:
            x = 0
            y += 1
def make_odd_one_out():
    tag_counts, c_reversed = get_tags_and_c_reversed(c)
    
    #for t in tag_counts:
    #    print(t + ": " + str(tag_counts[t]))

    # select 3-4 tags with at least 3 words
    group_list = []
    num_groups = random.randint(3,4)
    while len(group_list) < num_groups:
        g = random.choice(list(tag_counts.keys()))
        if tag_counts[g] >= 3 and g not in group_list:
            group_list.append(g)

    #for g in group_list:
    #    print(g)

    #get 3 words for each group
    word_groups = {}
    for g in group_list:
        word_groups[g] = list()
        #print(g)
        num_words = 3
        #print(c_reversed[g])
        random.shuffle(c_reversed[g])
        #print(c_reversed[g])
        for n in range(num_words):
            #print(c_reversed[g][n])
            word_groups[g].append(c_reversed[g][n])
        odd_group = random.choice(list(tag_counts.keys()))
        while odd_group == g or odd_group in word_groups:
            odd_group = random.choice(list(tag_counts.keys()))
        word_groups[g].append(random.choice(c_reversed[odd_group]))
        random.shuffle(word_groups[g])
    return word_groups

def show_odd_one_out(odd_one_out):
    pass

def get_tags_and_c_reversed(c):
    tag_counts = {}
    c_reversed = {}
    for w in c:
        #print(t)
        # count how many times each tag is used
        for t in c[w].tags:
            if t not in tag_counts:
                tag_counts[t] = 1
            else:
                tag_counts[t] += 1

            if t not in c_reversed:
                c_reversed[t] = [w]
            else:
                c_reversed[t].append(w)
    return tag_counts,c_reversed

hint = tk.Label()
message = tk.Label()
word = ""

def on_select(event):
    global selection
    selection = event.widget.get(int(event.widget.curselection()[0]))
    Selected(selection)
    #print()

def Selected(sel):
    global word
    global word_groups
    word = random.choice(list(c.keys()))
    if sel == "Scramble":    
        show_scrambled_word(word,hint)
    elif sel == "No_Vowels":
        show_no_vowel_word(word,hint)
    elif sel == "Group":
        word_groups = make_groups(c)
        show_groups(word_groups)
    elif sel == "Odd_One_Out":
        odd_one_out = make_odd_one_out()
        show_odd_one_out(odd_one_out)
    lb.grid_forget()

def Check(event):
    print("checking")
    if entry.get() == word:
        print("correct")
        message.configure(text = "Good job")
    else:
        print("incorrect")
        message.configure(text = "Nope")
    message.grid(column = 3, row = 4)
    message.update_idletasks()
    HideMessage(message)

lb.bind("<<ListboxSelect>>", on_select)




text = tk.StringVar()
entry = tk.Entry(root,textvariable = text)
entry.bind("<KeyRelease-Return>",Check)

def HideMessage(message):
    time.sleep(3)
    message.grid_forget()
    hint.configure(text = "")
    hint.update()
    text.set("")
    entry.update()
    Selected(selection)

def make_draggable(wid):
    wid.bind("<Button-1>",on_drag_start)
    wid.bind("<B1-Motion>",on_drag_motion)
    wid.bind("<ButtonRelease-1>",on_drag_finish)

original_pos_x = 0
original_pos_y = 0

def on_drag_start(event):
    global original_pos_x
    global original_pos_y
    widget = event.widget
    original_pos_x = widget.winfo_x()
    original_pos_y = widget.winfo_y()
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x,y=y)
    widget.update_idletasks()
    
def on_drag_finish(event):
    widget = event.widget
    widget.update_idletasks()
    #check the position
    print(widget.winfo_x())
    print(widget.winfo_y())
    selected_word = widget.cget("text")
    group = ""
    for g in word_groups:
        if selected_word in word_groups[g]:
            group = g
            break
    if g != "":
        print(group)
        print(group_positions[g])
    #if correct, use widget.unbind("<Button-1>")
    # widget.unbind("<B1-Motion>")
    # widget.unbind("<ButtonRelease-1>")
    # if not correct, move the widget
    # widget.place(x=original_pos_x,y=original_pos_y)
root.mainloop()
