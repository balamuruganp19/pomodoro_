from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
timer = None
rep = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if rep % 2 == 0:
        count_down(short_break)
        title_label.config(text="Short Break", fg="black")
    elif rep % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break", fg="Pink")
    else:
        count_down(work_sec)
        title_label.config(text="Work Section", fg="blue")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    counter_min = math.floor(count / 60)
    counter_sec = count % 60
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"
    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        if rep == 3:
            check_mark.configure(text="✅✅")
        elif rep == 5:
            check_mark.config(text="✅✅✅")
        elif rep == 7:
            check_mark.config(text="✅✅✅")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PomoDora")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", font=("Arial", 24), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)
start_button = Button(text="Start", font=("Arial", 10), highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)
end_button = Button(text="Reset", font=("Arial", 10), highlightthickness=0,command=reset)
end_button.grid(row=2, column=2)
check_mark = Label(text="✅", fg=GREEN, bg=YELLOW)
check_mark.grid(row=2, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 24))
canvas.grid(row=1, column=1)
window.mainloop()
