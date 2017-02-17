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


def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()


# setting up layout
root = Tk("Text Editor")
root.title("Text Editor")

text = Text(root)
text.grid()

button = Button(root, text="Save", command = save_as)
button.grid()

# run GUI
root.mainloop()
