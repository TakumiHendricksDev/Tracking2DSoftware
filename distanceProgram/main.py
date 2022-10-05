from tkinter import *
from tkinter import ttk

offset = 100


def update():
    distance = slider.get()
    c.delete("all")
    c.create_rectangle(2.5, 2.5, 400, 400, fill='white', width=5)
    c.create_text(200, 180, text=distance.__str__() + ' cm', fill="black", font=('Helvetica 15 bold'))
    drawLine(distance)


def drawLine(distance):
    firstXPos = 200 * (1 - ((distance / 2) / (offset / 2)))
    secondXPos = (200 * ((distance / 2) / (offset / 2))) + 200
    if distance <= offset:
        line = c.create_line(firstXPos, 200, secondXPos, 200, fill='blue', width=5)
        point(firstXPos, 200, 5)
        point(secondXPos, 200, 5)
    else:
        line = c.create_line(0, 200, 400, 200, fill='blue', width=5)
        point(0, 200, 5)
        point(400, 200, 5)


def point(x, y, size):
    c.create_oval(x, y, x, y, width=size)


def drawScreen():
    global c
    global slider

    root = Tk()

    root.geometry("1080x1920")

    c = Canvas(root, width=400, height=400)
    c.pack()

    c.create_rectangle(2.5, 2.5, 400, 400, fill='white', width=5)
    c.create_text(200, 180, text='0 cm', fill="black", font=('Helvetica 15 bold'))
    drawLine(1)

    slider = Scale(root, from_=0, to=offset, orient=HORIZONTAL)
    slider.set(1)
    slider.pack()
    Button(root, text="update", command=update).pack()

    root.mainloop()


def main():
    drawScreen()


if __name__ == '__main__':
    main()
