# \Users\vrish\Downloads\pomodoro-start
from tkinter import *
import time
#constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#93C572"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer_count = None

#timer reset

def reset_timer():
    global reps
    window.after_cancel(timer_count)
    time.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

#timer mechanism
def start_countdown():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        time.config(text="Long Break", font=("Courier", 30, "bold"),bg=YELLOW, fg=RED, borderwidth=10, highlightthickness=0)
    elif reps % 2 ==0:
        time.config(text="Short Break", font=("Courier", 30, "bold"),bg=YELLOW, fg=PINK, borderwidth=10, highlightthickness=0)
        countdown(short_break_sec)
    else:
        countdown(work_sec)
        time.config(text="Work", font=("Courier", 30, "bold"),bg=YELLOW, fg=GREEN, borderwidth=10, highlightthickness=0)

#countdown
import math
def countdown(count):
    global timer_count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        print(count)
        timer_count = window.after(1000, countdown, count - 1)

    else:
        start_countdown()
        marks = ""
        work_sesh = math.floor(reps/2)
        for i in range(work_sesh):
            marks += "✔"
        check_mark.config(text=marks)
#UI
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="<insert background image file path (preferably a tomato :))>")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 30, "bold"))
canvas.grid(column=2, row=2)

time = Label(text="Timer", font=("Courier", 30, "bold"),bg=YELLOW, fg=GREEN, borderwidth=10, highlightthickness=0)
time.grid(column=2, row=1)

reset_b = Button(text="Reset", command=reset_timer, highlightthickness=0, bg=RED, font=FONT)
reset_b.grid(column=3, row=4)

start_b = Button(text="Start", command=start_countdown, highlightthickness=0, bg=GREEN, font=FONT)
start_b.grid(column=1, row=4)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)



window.mainloop()

