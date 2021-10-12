#importstatements
import turtle
import random

#gameconfiguration
turtle_color = ["indigo", "red", "blue", "pink"]
turtle_size = 4
turtle_shape = "turtle"
score = 0
font_setup = ("Arial", 25, "normal")
timer = 15
counter_interval = 1000
timer_up = False

#initializeturtle
Tim = turtle.Turtle()
Tim.fillcolor(random.choice(turtle_color))
Tim.shape(turtle_shape)
Tim.shapesize(turtle_size)
Tim.penup()

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(-150,200)
score_writer.hideturtle()

time_writer = turtle.Turtle()
time_writer.penup()
time_writer.goto(150,200)
time_writer.hideturtle()

#gamefunctions
def turtle_clicked(x,y):
    #print("Tim was clicked!!")
    global timer_up
    Tim.fillcolor(random.choice(turtle_color))
    if timer_up: #when to stop
        Tim.hideturtle()
    else: #Keep going
        update_score()
        Tim.hideturtle()
        change_position()
        Tim.showturtle()

def change_position():
    new_xpos = random.randint(-200,150)
    new_ypos = random.randint(-150,150)
    Tim.goto(new_xpos, new_ypos)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)

def countdown():
    global timer, timer_up
    time_writer.clear()
    if timer <= 0:
        time_writer.write("Time's up!", font=font_setup)
        timer_up = True
        Tim.hideturtle()
    else:
        time_writer.write("Timer:" + str(timer), font=font_setup)
        timer -= 1
        time_writer.getscreen().ontimer(countdown, counter_interval)

#events
Tim.onclick(turtle_clicked)

wn = turtle.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()