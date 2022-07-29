from tkinter import *
import math


#CONSTANTS
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
#TIMER RESET MECH

def reset_timer():
    window.after_cancel(timer) #resets timer to None/Initial
    #reset other
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text="Timer")
    check_mark.config(text= "") 
    global reps
    reps = 0

#TIMER MECH

def start_timer():

    global reps
    reps += 1
    #Sessions mechanism
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

#COUNTDOWN MECH
def count_down(count):
    #Convert count_secs inputted to minutes and seconds seperately
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000, count_down, count - 1)#calls count_down() every 1sec
    else:
        start_timer()  #When session ends its goes to next one and starts timer again
        #marks added per work sessions
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)




#GUI SETUP
window = Tk()
window.title("POMODORO TIMER APP")
window.config(padx= 60, pady= 60, bg= YELLOW)


title_label = Label(text="TIMER", fg= GREEN, font= (FONT_NAME, 50,'bold'), bg = YELLOW) 
title_label.grid(column=1, row=0)

#canvas
canvas = Canvas(width= 210, height =230, bg= YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 115, image = tomato_image)


timer_text = canvas.create_text(100, 136, text = "00:00", fill= "white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)



#buttons
start_btn = Button(text="Start", bg= YELLOW, command= start_timer)
start_btn.grid(column=0 , row=2)

reset_btn = Button(text="Reset", bg= YELLOW, command= reset_timer)
reset_btn.grid(column=2 , row=2)

#checkmarks
check_mark = Label(bg=YELLOW, fg= GREEN, font=(FONT_NAME,20))
check_mark.grid(column=1, row=3)



window.mainloop()
