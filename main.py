from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=PINK)

# Canvas
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Labels
timer_label = Label(text="TIMER", bg=PINK, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

check_label = Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

# Buttons
start_img = PhotoImage(file="start.png")
start_button = Button(image=start_img, bg=PINK, border=0, activebackground=PINK, command=start_timer)
start_button.grid(row=2, column=0)

reset_img = PhotoImage(file="reset.png")
reset_button = Button(image=reset_img, bg=PINK, border=0, activebackground=PINK, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
