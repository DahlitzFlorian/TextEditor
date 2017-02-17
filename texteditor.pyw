import sys

# global variables
v = sys.version

# loading default GUI
if "2.7" in v:
    from Tkinter import *
    import tkFileDialog as filedialog
elif "3.3" in v or "3.4" in v:
    from tkinter import *
    from tkinter import filedialog


# save-button functionality
def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()


# "Helvetics"-font
def font_helvetica():
    global text
    text.config(font="Helvetica")


# "Courier"-font
def font_courier():
    global text
    text.config(font="Courier")


# setting up layout
root = Tk("Text Editor")
root.title("Text Editor")

# adding text field
text = Text(root)
text.grid()

# adding save-button
button = Button(root, text="Save", command=save_as)
button.grid()

# adding font choicer
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=font_courier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=font_helvetica)

# run GUI
root.mainloop()
