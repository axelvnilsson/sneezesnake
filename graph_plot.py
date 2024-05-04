import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def clear_axes(ax):
    ax.clear()
    ax.spines['left'].set_position('center')
    ax.spines['left'].set_color('gray')
    ax.spines['left'].set_linewidth(0.25)
    ax.spines['bottom'].set_position('center')
    ax.spines['bottom'].set_color('gray')
    ax.spines['bottom'].set_linewidth(0.25)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def draw_grid(ax, grid_scale):
    ax.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.25)
    ax.set_xlim(-20 * grid_scale, 20 * grid_scale)
    ax.set_ylim(-20 * grid_scale, 20 * grid_scale)
    ax.tick_params(axis='both', which='major', labelsize=4, colors='gray', width=0.25)

def plot_dot(ax, x, y):
    clear_axes(ax)
    draw_grid(ax, grid_scale.get())
    ax.plot(x, y, marker='o', color='black', markersize=3)
    ax.text(x + 0.4, y + 0.4, f"({x:.1f}, {y:.1f})", fontsize=5, color='gray')

def update_plot_from_sliders(val):
    x = x_scale.get()
    y = y_scale.get()
    x_entry.delete(0, tk.END)
    x_entry.insert(0, f"{x:.1f}")
    y_entry.delete(0, tk.END)
    y_entry.insert(0, f"{y:.1f}")
    plot_dot(ax, x, y)
    canvas.draw()  # Update canvas

def update_plot_from_entries(event=None):
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_scale.set(x)
    y_scale.set(y)
    plot_dot(ax, x, y)
    canvas.draw()  # Update canvas

def update_entry(entry, increment):
    value = float(entry.get())
    value += increment
    entry.delete(0, tk.END)
    entry.insert(0, f"{value:.1f}")
    update_plot_from_entries()

def increment_x():
    update_entry(x_entry, 0.1)

def decrement_x():
    update_entry(x_entry, -0.1)

def increment_y():
    update_entry(y_entry, 0.1)

def decrement_y():
    update_entry(y_entry, -0.1)

def update_grid_scale(val):
    plot_dot(ax, x_scale.get(), y_scale.get())
    canvas.draw()  # Update canvas

root = tk.Tk()
root.title("Single Dot Plotter")
root.geometry("800x800")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=4, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure([0, 1], weight=1)

x_entry = ttk.Entry(root, width=5)  # Adjusted width
x_entry.insert(0, '0')
x_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

y_entry = ttk.Entry(root, width=5)  # Adjusted width
y_entry.insert(0, '0')
y_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

grid_scale = ttk.Scale(root, from_=0.1, to=2, orient=tk.HORIZONTAL, command=update_grid_scale)

ttk.Label(root, text="X:").grid(row=1, column=0, sticky='w')
x_entry.grid(row=1, column=1, sticky='ew')
x_entry.bind("<FocusOut>", update_plot_from_entries)

ttk.Button(root, text="↑", command=increment_x).grid(row=1, column=2, sticky='ew')
ttk.Button(root, text="↓", command=decrement_x).grid(row=1, column=3, sticky='ew')

x_scale.grid(row=2, column=0, columnspan=4, sticky='ew')
x_scale.set(0)

ttk.Label(root, text="Y:").grid(row=3, column=0, sticky='w')
y_entry.grid(row=3, column=1, sticky='ew')
y_entry.bind("<FocusOut>", update_plot_from_entries)

ttk.Button(root, text="↑", command=increment_y).grid(row=3, column=2, sticky='ew')
ttk.Button(root, text="↓", command=decrement_y).grid(row=3, column=3, sticky='ew')

y_scale.grid(row=4, column=0, columnspan=4, sticky='ew')
y_scale.set(0)

ttk.Label(root, text="Grid Scale:").grid(row=5, column=0, sticky='w')
grid_scale.grid(row=5, column=1, columnspan=3, sticky='ew')
grid_scale.set(1)

ttk.Button(root, text="Update from Entries", command=update_plot_from_entries).grid(row=6, column=0, columnspan=4, sticky='ew')

update_plot_from_entries()  # Initial plot update

root.mainloop()
