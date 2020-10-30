

from tkinter import *
from PIL import Image, ImageTk 
root = Tk()

root.geometry("400x400")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="grey", borderwidth=9, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="")
l.pack(pady=42)

l = Label(f2, text="Jarvis Desktop Assistant", font="Helvetica 16 bold", fg="red")
l.pack()

photo = PhotoImage(file="AI.photo")

moto_label = Label(image=photo)
moto_label.pack()

         
        
def hello():
    print("hello everyone")


frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")


b1 = Button(frame, fg="red", text="start", command=hello)
b1.pack()

counter = 0 
def counter_label(label):
    counter=0
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000, count)
        count()
        
        

root.title("counting seconds")
label = Label(root, fg="dark green")
label.pack()
counter_label(label)
button = Button(root, text="stop", width=25, command=root.destroy)
button.pack()
root.mainloop()

root.mainloop()
