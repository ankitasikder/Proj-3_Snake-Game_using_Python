from tkinter import *
from tkinter.font import Font
from snake_game import gameStart
master = Tk()
frame = Frame(master,relief=SUNKEN)
master.title("HS")
photo = PhotoImage(file = "icon.png")
master.iconphoto(False, photo)
master.geometry("250x310")
master.resizable(width=0,height=0)
w=Canvas(master,width=275,height=310,bg="cyan")
master.configure(bg='yellow')
# Create text widget and specify size.
T = Text(master, height=11, width=50,bg="yellow")
# Create label
l = Label(master, text="HUNGRY SNAKE",bg="black",width=30,fg="white")
l.config(font=("Courier", 14))

Fact = """This snake game is a computer action game, whose goal is to control a snake to move and collect food in a black screen.
This is created by python pygame module and tkinter package is used to create this small  graphical user interface.
------------------------------Please the speed of the snake:------------------------------"""
l.pack()
T.pack()
EntryLabel = Label(master,text='SNAKE SPEED :',font=('arial',12,'italic bold'),bg='yellow')
EntryLabel.place(x=10,y=216)
# Insert The Fact.
T.insert(END, Fact)
s = Spinbox(master, from_ = 1, to = 20,increment=2,width=5,font=Font(family='Helvetica', size=14, weight='bold'))
speed=0
def disp(event):
    global speed
    speed=int(s.get())
    print(f'Snake Speed: {speed}')


s.bind('<Button-1>', disp)
s.place(x=150,y=215)

B = Button(master, text ="Start Game",width=12,height=2,bg="black",fg="white",font = Font(size = 12),command=lambda:[gameStart(speed)])
B.place(x=65,y=250)

master.mainloop()