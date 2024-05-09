import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def draw_fractal(canvas, ax, xmin, xmax, ymin, ymax, max_iter):
    ax.clear()
    result = mandelbrot_set(xmin, xmax, ymin, ymax, width=800, height=600, max_iter=max_iter)
    ax.imshow(result.T, extent=[xmin, xmax, ymin, ymax], origin="lower", cmap="hot")
    ax.set_title("Mandelbrot Set")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    canvas.draw_idle()

def update(val):
    draw_fractal(canvas, ax, float(xmin_scale.get()), float(xmax_scale.get()), 
                 float(ymin_scale.get()), float(ymax_scale.get()), int(max_iter_scale.get()))

root = tk.Tk()
root.title("Mandelbrot Fractal Generator")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

controls_frame = ttk.Frame(root)
controls_frame.pack(fill=tk.X, side=tk.BOTTOM)

canvas_widget.pack(fill=tk.BOTH, expand=True)

xmin_label = ttk.Label(controls_frame, text="X Min")
xmin_scale = ttk.Scale(controls_frame, from_=-2.0, to=0.5, orient=tk.HORIZONTAL, command=update)
xmax_label = ttk.Label(controls_frame, text="X Max")
xmax_scale = ttk.Scale(controls_frame, from_=-0.5, to=1.0, orient=tk.HORIZONTAL, command=update)
ymin_label = ttk.Label(controls_frame, text="Y Min")
ymin_scale = ttk.Scale(controls_frame, from_=-1.5, to=1.5, orient=tk.HORIZONTAL, command=update)
ymax_label = ttk.Label(controls_frame, text="Y Max")
ymax_scale = ttk.Scale(controls_frame, from_=-1.0, to=2.0, orient=tk.HORIZONTAL, command=update)
max_iter_label = ttk.Label(controls_frame, text="Max Iterations")
max_iter_scale = ttk.Scale(controls_frame, from_=50, to=1000, orient=tk.HORIZONTAL, command=update)

xmin_label.pack(side=tk.LEFT)
xmin_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
xmax_label.pack(side=tk.LEFT)
xmax_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
ymin_label.pack(side=tk.LEFT)
ymin_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
ymax_label.pack(side=tk.LEFT)
ymax_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
max_iter_label.pack(side=tk.LEFT)
max_iter_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)

update(None)  # Draw the initial Mandelbrot set
root.mainloop()
