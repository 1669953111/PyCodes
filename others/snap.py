import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL

def next_shape():
    global shape
    global previus_color
    global current_color

    previus_color = current_color

    c.delete(shape)
    if len(shapes)> 0:
        shape = shapes.pop()
        c.itemconfigure(shape,state=NORMAL)
        current_color = c.itemcget(shape,'fill')
        root.after(1000,next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if p1_score > p2_score:
            c.create_text(200,200,text="Winner: Player1!")
        if p1_score < p2_score:
            c.create_text(200,200,text="Winner: Player2!")
        else:
            c.create_text(200,200,text='Draw')
        c.pack()

def snap(event):
    global shape
    global p1_score
    global p2_score
    valid = False

    if previus_color == current_color:
        valid = True
    
    if valid:
        if event.char == 'q':
            p1_score = p1_score + 1
        else:
            p2_score = p2_score + 1
        shape = c.create_text(200,200,text='SNAP! You score 1 point!')
    else:
        if event_.char == 'p':
            p1_score = p1_score - 1
        else:
            p2_score = p2_score - 1
        shape = c.create_text(200,200,text='WRONG! You lose 1 point!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)

root = Tk()
root.title('snap')
c = Canvas(root, width=400, height=400)

shapes = []
# create circle
circle = c.create_oval(35,20,365,350,outline='black',fill='black',state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350,outline='red',fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350,outline='green',fill='green',state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350,outline='blue',fill='blue',state=HIDDEN)
shapes.append(circle)
# create rectangle
rectangle = c.create_rectangle(35,100,365,350,outline='black',fill='black',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,350,outline='red',fill='red',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,350,outline='green',fill='green',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35,100,365,350,outline='blue',fill='blue',state=HIDDEN)
shapes.append(rectangle)
# create square
square = c.create_rectangle(35,20,365,350,outline='black',fill='black',state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,20,365,350,outline='red',fill='red',state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,20,365,350,outline='green',fill='green',state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35,20,365,350,outline='blue',fill='blue',state=HIDDEN)
shapes.append(square)

c.pack()

random.shuffle(shapes)

shape = None
previus_color = ''
current_color = ''
p1_score = 0
p2_score = 0

root.after(3000,next_shape)
c.bind('q',snap)
c.bind('p',snap)
c.fucus_set()

root.mainloop()