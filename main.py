import turtle
import random

# Set up the screen ============================================================
screen = turtle.Screen()
screen.title("Turtle race")
screen.setup(width=600, height=400)
screen.bgcolor("black")
user_in = screen.textinput("question", "Who will win the race ? enter a color :")


# Create race finish line object ================================================
finish_line = turtle.Turtle()
finish_line.speed(0)
finish_line.shape("square")
finish_line.shapesize(stretch_len=0.5, stretch_wid=18)
finish_line.color("gold")
finish_line.penup()
finish_line.goto(290, 0)

# Create a turtles object =======================================================
# tim_p turtle : purple turtle
tim_p = turtle.Turtle()
tim_p.speed(random.randint(0, 10))
tim_p.color("purple")
tim_p.shape("turtle")
tim_p.showturtle()
tim_p.penup()
tim_p.goto(-280,0)

# tim_b turtle : blue turtle
tim_b = turtle.Turtle()
tim_b.speed(random.randint(0, 10))
tim_b.color("blue")
tim_b.shape("turtle")
tim_b.showturtle()
tim_b.penup()
tim_b.goto(-280,30)

# tim_g turtle : green turtle
tim_g = turtle.Turtle()
tim_g.speed(random.randint(0, 10))
tim_g.color("green")
tim_g.shape("turtle")
tim_g.showturtle()
tim_g.penup()
tim_g.goto(-280,60)

# tim_r turtle : red turtle
tim_r = turtle.Turtle()
tim_r.speed(random.randint(0, 10))
tim_r.color("red")
tim_r.shape("turtle")
tim_r.showturtle()
tim_r.penup()
tim_r.goto(-280,-30)

# tim_s turtle : gold turtle
tim_s = turtle.Turtle()
tim_s.speed(random.randint(0, 10))
tim_s.color("silver")
tim_s.shape("turtle")
tim_s.showturtle()
tim_s.penup()
tim_s.goto(-280,-60)

# All turtles :
all_turtles = [tim_p, tim_b, tim_g, tim_r, tim_s]

# Turtle movement ====================================================
while user_in:
    for turtle in all_turtles:      
        if turtle.xcor() > 280:
            user_in = False
            winning_color = turtle.pencolor()
            if winning_color == user_in:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance) 
    


screen.exitonclick()