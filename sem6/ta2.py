from random import randint
from tkinter import Tk, Canvas


def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'


WIDTH = 600
HEIGHT = 400


class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.R = randint(10, 50)
        self.x = x
        self.y = y
        self.dx, self.dy = 5, 5
        self.color = rand_color()
        self.ball_id = canvas.create_oval(
            self.x - self.R, self.y - self.R,
            self.x + self.R, self.y + self.R,
            fill=self.color
        )

    def move(self):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w <= 1:
            w = WIDTH
        if h <= 1:
            h = HEIGHT

        self.x += self.dx
        self.y += self.dy

        if self.x + self.R > w:
            self.x = w - self.R
            self.dx = -self.dx
        elif self.x - self.R < 0:
            self.x = self.R
            self.dx = -self.dx

        if self.y + self.R > h:
            self.y = h - self.R
            self.dy = -self.dy
        elif self.y - self.R < 0:
            self.y = self.R
            self.dy = -self.dy

    def show(self):
        self.canvas.coords(
            self.ball_id,
            self.x - self.R, self.y - self.R,
            self.x + self.R, self.y + self.R
        )


def click_handler(event):
    balls.append(Ball(canvas, event.x, event.y))


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(20, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack(fill='both', expand=True)

canvas.bind('<Button-1>', click_handler)

balls = [Ball(canvas, randint(50, WIDTH - 50), randint(50, HEIGHT - 50))
         for _ in range(3)]

tick()
root.mainloop()
