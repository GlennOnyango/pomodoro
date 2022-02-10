import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = 1
time_counter = ""
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Concentration")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="TIMER", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_count_down = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def reset():
    global check
    window.after_cancel(time_counter)
    canvas.itemconfig(timer_count_down, text="00:00")
    timer.config(text="TIMER", fg=GREEN)
    check_item.config(text="")
    check = 1


def count(number):
    minutes = math.floor(number / 60)
    seconds = number % 60
    global check
    global time_counter
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_count_down, text=f"{minutes}:{seconds}")
    if number > 0:
        time_counter = window.after(1000, count, number - 1)
    elif number == 0:
        start_timer()
        mark = ""
        for _ in range(int(check/2)):
            mark += "✔"

        check_item.config(text=mark)


def start_timer():
    global check
    if check % 2 == 0 and check != 8:
        count(SHORT_BREAK_MIN * 60)
        timer.config(text="SHORT BREAK", fg=YELLOW)
        check += 1
    elif check % 2 != 0:
        count(WORK_MIN * 60)
        timer.config(text="WORK", fg=RED)
        check += 1
    else:
        count(LONG_BREAK_MIN * 60)

        timer.config(text="LONG BREAK BREAK", fg=GREEN)
        check += 1


btn_start = Button(text="Start", command=start_timer)
btn_start.grid(row=2, column=0)

btn_start = Button(text="Reset", command=reset)
btn_start.grid(row=2, column=2)

check_item = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
check_item.grid(row=3, column=1)


window.mainloop()
