from tkinter import *  # import all
from tkinter import filedialog

root = Tk("Text Editor")
root.title("Text Editor")
text = Text(root)
text.grid() 

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

button=Button(root, text="Save", command=saveas)
button.grid()

if __name__ == "__main__":
    root.mainloop()