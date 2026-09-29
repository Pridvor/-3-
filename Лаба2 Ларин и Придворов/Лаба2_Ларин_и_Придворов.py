from tkinter import *
from tkinter import filedialog

def cda(x1, y1, x2, y2, cv, color):
    l = max(abs(x2 - x1), abs(y2 - y1))
    if l == 0:
        cv.create_rectangle(x1, y1, x1+1, y1+1, outline=color, fill=color)
        return
    dx = (x2 - x1) / l
    dy = (y2 - y1) / l
    x, y = x1, y1
    for i in range(int(l) + 1):
        cv.create_rectangle(int(x), int(y), int(x)+1, int(y)+1,
                            outline=color, fill=color)
        x += dx
        y += dy

def brezf(x1, y1, x2, y2, cv, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x, y = x1, y1
    f = 0
    if dy > dx:
        dx, dy = dy, dx
        f = 1
    e = dy / dx - 0.5 if dx != 0 else 0
    for i in range(int(dx) + 1):
        cv.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)
        if e >= 0:
            if f == 1: x += sx
            else: y += sy
            e -= 1
        if f == 1: y += sy
        else: x += sx
        e += dy / dx if dx != 0 else 0

def brezi(x1, y1, x2, y2, cv, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x, y = x1, y1
    f = 0
    if dy > dx:
        dx, dy = dy, dx
        f = 1
    e = 2 * dy - dx
    for i in range(dx + 1):
        cv.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)
        if e >= 0:
            if f == 1: x += sx
            else: y += sy
            e -= 2 * dx
        if f == 1: y += sy
        else: x += sx
        e += 2 * dy

def create():
    cv.delete("all")

    x1, y1 = int(e1.get()), int(e2.get())
    x2, y2 = int(e3.get()), int(e4.get())
    x3, y3 = int(e5.get()), int(e6.get())
    x4, y4 = int(e7.get()), int(e8.get())

    minx = min(x1, x2, x3, x4)
    miny = min(y1, y2, y3, y4)
    x1 -= minx - 20; y1 -= miny - 20
    x2 -= minx - 20; y2 -= miny - 20
    x3 -= minx - 20; y3 -= miny - 20
    x4 -= minx - 20; y4 -= miny - 20

    for (a, b, c, e) in [(x1, y1, x2, y2),
                          (x2, y2, x3, y3),
                          (x3, y3, x4, y4)]:
        cda  (a, b + 0, c, e + 0, cv, "#7F7FFF")
        brezf(a, b + 2, c, e + 2, cv, "#FF7F7F")
        brezi(a, b + 4, c, e + 4, cv, "#7FFF7F")
        cv.create_line(a, b + 6, c, e + 6, fill="#7F7F7F")

def save():
    f = filedialog.asksaveasfilename(defaultextension=".ps",
                                     filetypes=[("PostScript", "*.ps")])
    if f:
        cv.postscript(file=f)

root = Tk()
root.title("Лаба 3 — Полилиния")

f = Frame(root); f.pack(pady=10)

Label(f, text="x1").grid(row=0, column=0)
e1 = Entry(f, width=5); e1.insert(0, "50");  e1.grid(row=0, column=1)
Label(f, text="y1").grid(row=0, column=2)
e2 = Entry(f, width=5); e2.insert(0, "50");  e2.grid(row=0, column=3)

Label(f, text="x2").grid(row=0, column=4)
e3 = Entry(f, width=5); e3.insert(0, "200"); e3.grid(row=0, column=5)
Label(f, text="y2").grid(row=0, column=6)
e4 = Entry(f, width=5); e4.insert(0, "80");  e4.grid(row=0, column=7)

Label(f, text="x3").grid(row=1, column=0)
e5 = Entry(f, width=5); e5.insert(0, "150"); e5.grid(row=1, column=1)
Label(f, text="y3").grid(row=1, column=2)
e6 = Entry(f, width=5); e6.insert(0, "200"); e6.grid(row=1, column=3)

Label(f, text="x4").grid(row=1, column=4)
e7 = Entry(f, width=5); e7.insert(0, "60");  e7.grid(row=1, column=5)
Label(f, text="y4").grid(row=1, column=6)
e8 = Entry(f, width=5); e8.insert(0, "250"); e8.grid(row=1, column=7)

Button(f, text="Создать",   command=create).grid(row=0, column=8, padx=10)
Button(f, text="Сохранить", command=save).grid(row=1, column=8, padx=10)

cv = Canvas(root, width=800, height=600, bg="white")
cv.pack(pady=10)

root.mainloop()