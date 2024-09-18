import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Analog Clock")

# Create the turtle for drawing the clock
clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)
clock.pensize(3)

# Draw the clock face
clock.penup()
clock.goto(0, 200)
clock.setheading(180)
clock.pendown()
clock.circle(200)

# Draw the hour marks
clock.penup()
clock.goto(0, 0)
clock.setheading(90)
for i in range(12):
    clock.penup()
    clock.forward(170)
    clock.pendown()
    clock.forward(20)
    clock.penup()
    clock.goto(0, 0)
    clock.right(30)

# Create the hour hand turtle
hour_hand = turtle.Turtle()
hour_hand.hideturtle()
hour_hand.speed(0)
hour_hand.pensize(5)
hour_hand.color("blue")

# Create the minute hand turtle
minute_hand = turtle.Turtle()
minute_hand.hideturtle()
minute_hand.speed(0)
minute_hand.pensize(3)
minute_hand.color("green")

# Create the second hand turtle
second_hand = turtle.Turtle()
second_hand.hideturtle()
second_hand.speed(0)
second_hand.pensize(1)
second_hand.color("red")

# Update the clock hands
def update():
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate the angles for the clock hands
    hour_angle = (hour % 12) * 30 + minute / 2
    minute_angle = minute * 6
    second_angle = second * 6

    # Set the angles for the clock hands
    hour_hand.setheading(-hour_angle + 90)
    minute_hand.setheading(-minute_angle + 90)
    second_hand.setheading(-second_angle + 90)

    # Draw the clock hands
    hour_hand.clear()
    hour_hand.penup()
    hour_hand.goto(0, 0)
    hour_hand.pendown()
    hour_hand.forward(100)
    minute_hand.clear()
    minute_hand.penup()
    minute_hand.goto(0, 0)
    minute_hand.pendown()
    minute_hand.forward(150)
    second_hand.clear()
    second_hand.penup()
    second_hand.goto(0, 0)
    second_hand.pendown()
    second_hand.forward(180)

    # Schedule the next update
    turtle.ontimer(update, 1000)

# Start the clock
update()

# Start the turtle event loop
turtle.done()
