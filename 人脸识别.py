import turtle


def draw_square():
    window = turtle.Screen()
    brad = turtle.Turtle()

    for _ in range(4):
        brad.forward(100)
        brad.right(90)

    window.mainloop()


if __name__ == "__main__":
    draw_square()
