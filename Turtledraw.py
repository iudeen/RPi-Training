import turtle

def draw_square(sqa):
    count = 0 
    while (count < 4):
        sqa.forward(100)
        sqa.right(90)
        count = count+1
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()
    
