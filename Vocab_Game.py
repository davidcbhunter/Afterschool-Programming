import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import random
import time



root = tk.Tk()

root.geometry("900x800")
root.title()

type_list = tk.StringVar()
type_list.set("Scramble No_Vowels Group Odd_One_Out Opposites")

c = {}

class Word:
    def __init__(self,wo,tag_list, oppo = ""):
        self.word = wo
        self.opposite = oppo
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
        # update this so that you take off the
        # opposite term first (if it exists)
        if ";" in w:
            #print("has opposite")
            w_list = w.split(";")
            wo = w_list.pop(0)
            #print(wo)
            w_list = str(w_list[0])
            #print(w_list)
            if "," in w_list:
                #print("has tags")
                w_list_two = w_list.split(",")
                opp = w_list_two.pop(0)
                #print(opp)
                for ww in w_list_two:
                    ww = ww.lstrip().rstrip()
                #print(w_list_two)
                word = Word(wo,w_list_two,opp)
            else:
                #print("no tags")
                opp = w_list.pop(0)
                word = Word(w,list(),opp)
        else:
            #print("no opposite")
            if "," in w:
                w_list = w.split(",")
                wo = w_list.pop(0)
                #print(wo)
                for ww in w_list:
                    ww = ww.lstrip().rstrip()
                word = Word(wo,w_list)
            else:
                wo = w
                word = Word(wo,list())
        c[word.word] = word
    f.close()
#    for w in c:
#        print(c[w].word)
#        print(c[w].opposite)
#        print(c[w].tags)
#        print("\n")
    show_choices()
    #print(c)

#write function to split line into word?

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
    #print(word_list)
    random.shuffle(word_list)
    #print(word_list)
    x = 0
    #label = tk.LabelFrame(root, text = list(groups.keys())[0])
    #label.grid(column = 4, row = 4)
    for g in groups:
        label = tk.Button(root, text = g,state = tk.DISABLED, padx = 8)
        label.grid(column = 4 + x, row = 4)#,padx = 6,pady=2)
        label.update_idletasks()
        group_positions[g] = [label.winfo_x(),\
                              label.winfo_y(),\
                              label.winfo_width()]
        #print(group_positions)
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
        label.place(x = 40 + (x*50), y = 300+(y*30))
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

def get_opposites(c):
    max_opposite = 7
    word_dict = {}
    for wo in c:
        if c[wo].opposite != "" and \
           len(word_dict) < max_opposite:
            word_dict[wo] = c[wo].opposite
    print(word_dict)
    return list(word_dict.keys()), list(word_dict.values())

canvas = tk.Canvas(root, width=500, height=300, bg = "white")

def show_opposites(word_list,opposite_list):
    canvas.place(x = 100, y = 75)
    for w in word_list:
        canvas.create_text(110,85+(
            word_list.index(w) * 35),text = w)
    random.shuffle(opposite_list)
    for w in opposite_list:
        canvas.create_text(350,85+(
            opposite_list.index(w) * 35),text = w)
    root.bind("<Button-1>",on_draw_line_start)
    root.bind("<B1-Motion>",on_draw_line_motion)
    root.bind("<ButtonRelease-1>",on_draw_line_finish)



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
    #do this first to get accurate positions
    lb.grid_forget()
    lb.update_idletasks()
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
    elif sel == "Opposites":
        words, opposites = get_opposites(c)
        show_opposites(words,opposites)
    

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
line_id = 0
reset = False

def on_draw_line_start(event):
    global original_pos_x
    global original_pos_y
    global line_id
    original_pos_x = event.x
    original_pos_y = event.y
    if line_id == 0 or reset:
        line_id = canvas.create_line(original_pos_x,\
                                 original_pos_y,\
                                 original_pos_x,\
                                 original_pos_y, width = 5)
    else:
        canvas.itemconfigure(line_id, state = tk.NORMAL)
        canvas.coords(line_id, original_pos_x,\
                                 original_pos_y,\
                                 original_pos_x,\
                                 original_pos_y)
            

def on_draw_line_motion(event):
    canvas.coords(line_id,original_pos_x,\
                  original_pos_y,\
                  event.x, event.y)
# write code to draw lines between two points

#when the mouse button is released, check if
#it is correct
def on_draw_line_finish(event):
    #check the position
    global reset
    start_id = canvas.find_closest(original_pos_x,\
                                   original_pos_y,\
                                   halo = 5, start = line_id)
    end_id = canvas.find_closest(event.x,\
                                   event.y,\
                                   halo = 5, start = line_id)
    #print(line_id)
    #print(start_id)
    #print(end_id)

    if all(start_id):
        if "text" in canvas.itemconfigure(start_id):
            s = canvas.itemcget(start_id,"text")
            if all(end_id):
                if "text" in canvas.itemconfigure(end_id):
                    e = canvas.itemcget(end_id,"text")
                    if c[s].opposite != e:
                        canvas.itemconfigure(line_id, state = tk.HIDDEN)
                        reset = False
                    else:
                        reset = True
                else:
                    canvas.itemconfigure(line_id, state = tk.HIDDEN)
                    reset = False
            else:
                canvas.itemconfigure(line_id, state = tk.HIDDEN)
                reset = False
        else:
            canvas.itemconfigure(line_id, state = tk.HIDDEN)
            reset = False
    else:
        canvas.itemconfigure(line_id, state = tk.HIDDEN)
        reset = False
    

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
    #print(widget.winfo_x())
    #print(widget.winfo_y())
    selected_word = widget.cget("text")
    group = ""
    for g in word_groups:
        if selected_word in word_groups[g] \
        and widget.winfo_x() <= group_positions[g][0] + \
        group_positions[g][2]/2.0 + 5\
        and widget.winfo_x() > group_positions[g][0] - \
        group_positions[g][2]/2.0 - 5:
            group = g
            break
    if group != "":
        #print(group)
        #print(group_positions[g])
        widget.unbind("<Button-1>")
        widget.unbind("<B1-Motion>")
        widget.unbind("<ButtonRelease-1>")
    else:
        widget.place(x=original_pos_x,y=original_pos_y)
root.mainloop()
