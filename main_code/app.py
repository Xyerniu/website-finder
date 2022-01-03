# frontend , remove print lines later
import threading
import tkinter as tk
import url as bc

numbs = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]
numbs2 = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]

bool1 = False
bool2 = False
bool3 = False
bool4 = False
num = 0
num2 = 0
end1 = ".com"
url = "https://"
run = True
x1 = False



def get1num(event):
    global num
    num = drop.get()


def get2num(event):
    global num2
    num2 = drop2.get()


def set_bool():
    global bool1, bool2, bool3, bool4
    if v1.get() == 1:
        bool1 = True
    if v1.get() == 0:
        bool1 = False
    if v2.get() == 1:
        bool2 = True
    if v2.get() == 0:
        bool2 = False
    if v3.get() == 1:
        bool3 = True
    if v3.get() == 0:
        bool3 = False
    if v4.get() == 1:
        bool4 = True
    if v4.get() == 0:
        bool4 = False


def get_end(value):
    global end1
    end1 = value


def geturl(value):
    global url
    url = value


def start1():
    global x1
    if num2 > 0:
        v5 = True
    else:
        v5 = False
    bc.main_loop(v5, url, num2, num, end1, bool1, bool2, bool3, bool4)


def stop():
    bc.stop()


root = tk.Tk()
# non variable gui stuff


canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg='#332541')
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.85, anchor='n')

label1 = tk.Label(frame, text="number of random characters", fg="green", bg="#263D42")
label1.place(relx=0.5, relwidth=0.5, relheight=0.07, rely=0.12)

label3 = tk.Label(frame, text="number of random words", fg="green", bg="#263D42")
label3.place(relx=0, relwidth=0.5, relheight=0.07, rely=0.12)

# variable gui stuff
drop = tk.IntVar()
drop.set(numbs[0])

drop1 = tk.OptionMenu(frame, drop, *numbs, command=get1num)  #
drop1.place(relx=0.5, relwidth=0.5, relheight=0.07, rely=0.2)

drop2 = tk.IntVar()
drop2.set(numbs2[0])

drop3 = tk.OptionMenu(frame, drop2, *numbs2, command=get2num)  #
drop3.place(relx=0, relwidth=0.5, relheight=0.07, rely=0.2)

end = tk.StringVar()  # ending of the url
start = tk.StringVar()  # start of the url
t1 = tk.IntVar()  # if random words are enabled just say if num of random words if more than 0
# booleans for the random string
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()

# url starts

button1 = tk.Radiobutton(frame, text="youtube url", fg="green", bg="#263D42", variable=start,
                         value="https://www.youtube.com/results?search_query=",
                         command=lambda: geturl(start.get()))
button1.place(relx=0.75, relwidth=0.25, relheight=0.07, rely=0.3)
button2 = tk.Radiobutton(frame, text="normal url", fg="green", bg="#263D42", variable=start, value="https://",
                         command=lambda: geturl(start.get()))
button2.place(relx=0.5, relwidth=0.25, relheight=0.07, rely=0.3)
button3 = tk.Radiobutton(frame, text="google sites url", fg="green", bg="#263D42", variable=start,
                         value="https://sites.google.com/view/",
                         command=lambda: geturl(start.get()))
button3.place(relx=0.25, relwidth=0.25, relheight=0.07, rely=0.3)
button4 = tk.Radiobutton(frame, text="reddit url", fg="green", bg="#263D42", variable=start,
                         value="https://www.reddit.com/r/",
                         command=lambda: geturl(start.get()))
button4.place(relx=0, relwidth=0.25, relheight=0.07, rely=0.3)

# url ending buttons
button01 = tk.Radiobutton(frame, text=".gov", fg="green", bg="#263D42", variable=end, value=".gov",
                          command=lambda: get_end(end.get()))
button01.place(relx=0.75, relwidth=0.25, relheight=0.07, rely=0.5)
button02 = tk.Radiobutton(frame, text=".com", fg="green", bg="#263D42", variable=end, value=".com",
                          command=lambda: get_end(end.get()))
button02.place(relx=0.5, relwidth=0.25, relheight=0.07, rely=0.5)
button03 = tk.Radiobutton(frame, text=".org", fg="green", bg="#263D42", variable=end, value=".org",
                          command=lambda: get_end(end.get()))
button03.place(relx=0.25, relwidth=0.25, relheight=0.07, rely=0.5)
button04 = tk.Radiobutton(frame, text=".lt", fg="green", bg="#263D42", variable=end, value=".lt",
                          command=lambda: get_end(end.get()))
button04.place(relx=0, relwidth=0.25, relheight=0.07, rely=0.5)

# bool1-4  buttons
check2 = tk.Checkbutton(frame, text="rng upper letters", fg="green", bg="#263D42", variable=v1,
                        command=lambda: set_bool())
check2.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.075)

check3 = tk.Checkbutton(frame, text="rng lower letters", fg="green", bg="#263D42", variable=v2,
                        command=lambda: set_bool())
check3.place(relx=0.50, rely=0.6, relwidth=0.25, relheight=0.075)

check4 = tk.Checkbutton(frame, text="rng numbers", fg="green", bg="#263D42", variable=v3, command=lambda: set_bool())
check4.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.075)

check5 = tk.Checkbutton(frame, text="rng symbols", fg="green", bg="#263D42", variable=v4,
                        command=lambda: set_bool())
check5.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.075)

# start button
button = tk.Button(frame, text="start", fg="green", bg="#263D42",
                   command=lambda: threading.Thread(target=start1).start())
button.place(rely=0.8, relheight=0.1, relwidth=1, )

button = tk.Button(frame, text="stop", fg="green", bg="#263D42",
                   command=lambda: stop())
button.place(rely=0.9, relheight=0.1, relwidth=1, )
root.mainloop()
