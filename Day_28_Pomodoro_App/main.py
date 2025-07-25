from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(timer)  
  canvas.itemconfig(timer_text, text="00:00")   # timer_text 00:00
  title_label.config(text="Timer")              # title_label "Timer 
  check_button_label.config(text="")            # reset check_marks
  global reps
  reps= 0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps 
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 8 == 0:  # If it's the 8th rep:
    count_down(long_break_sec)
    title_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:  # If it's 2nd/4th/6th rep:
    count_down(short_break_sec)
    title_label.config(text="Break", fg=PINK)
  else: # If it's the 1st/3rd/5th/7th rep:
    count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  # print(count)
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    marks = "" 
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✔"
    check_button_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\Hi\Documents\Python_Practice\Day_28_Pomodoro_App\tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# check_button_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_button_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_button_label.grid(column=1, row=3)


window.mainloop()