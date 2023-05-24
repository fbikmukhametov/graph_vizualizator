from math import pi, sin, cos
import tkinter as tk

# количество вершин
d = int(input())


# создаем окно
root = tk.Tk()
root.title("Дерево графов")

# создаем canvas
canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# координаты центра окна
center_x = canvas_width // 2
center_y = canvas_height // 2

# радиус вершин
r = 25


# координаты вершин
vertices_coords = [(center_x + 10 * r * sin(2 * pi * i / d), center_y + 10 * r * cos(2 * pi * i / d)) for i in range(d)]

# нарисовать вершины
for i in range(d):
    canvas.create_oval(vertices_coords[i][0] - r, vertices_coords[i][1] - r, vertices_coords[i][0] + r, vertices_coords[i][1] + r, fill="purple", outline="black")
    canvas.create_text(vertices_coords[i][0], vertices_coords[i][1], text=str(i))

# нарисовать ребра
for i in range(d):
    for j in range(i + 1, d):
        canvas.create_line(vertices_coords[i][0], vertices_coords[i][1], vertices_coords[j][0], vertices_coords[j][1])

# запускаем цикл событий
root.mainloop()