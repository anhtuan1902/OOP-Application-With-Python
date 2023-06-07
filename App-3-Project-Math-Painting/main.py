from Canvas import Canvas
from Shape import Rectangle, Square

canvas_w = int(input("Enter canvas width: "))
canvas_h = int(input("Enter canvas height: "))

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter canvas color: ")

canvas = Canvas(height=canvas_h, width=canvas_w, color=colors[canvas_color])

while True:
    shape_type = input("What do you want draw? Enter quite to quite. ")

    if shape_type.lower() == 'quite':
        break
