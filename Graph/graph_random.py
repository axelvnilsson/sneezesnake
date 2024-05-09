import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def reset_axes(ax):
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
    ax.set_xlim(-10 * grid_scale, 10 * grid_scale)
    ax.set_ylim(-10 * grid_scale, 10 * grid_scale)
    ax.tick_params(axis='both', which='major', labelsize=4, colors='gray', width=0.25)

def draw_dots(ax, num_dots, dots, grid_scale_value, lines=True, labels=True):
    ax.clear()
    reset_axes(ax)
    draw_grid(ax, grid_scale_value)
    for i in range(num_dots):
        ax.plot(dots[i][0], dots[i][1], marker='o', color='black', markersize=2, linewidth=0.5)
        if labels:
            ax.text(dots[i][0] + 0.4 * grid_scale_value, dots[i][1] + 0.4 * grid_scale_value, f"({dots[i][0]:.1f}, {dots[i][1]:.1f})", fontsize=5, color='gray')
    if lines:
        for i in range(num_dots - 1):
            ax.plot([dots[i][0], dots[i + 1][0]], [dots[i][1], dots[i + 1][1]], color='black', linewidth=0.5)
    ax.set_title('Busy Life of the Dot', fontsize=10, color='gray')  # Add title
    canvas.draw_idle()

def toggle_labels():
    global labels
    labels = not labels
    update_plot()

def toggle_lines():
    global lines
    lines = not lines
    update_plot()

def update_coordinates():
    global num_dots, dots

    for i in range(num_dots):
        # Generate random increments for x and y coordinates of each dot
        dots[i][0] += random.randint(-5, 5)
        dots[i][1] += random.randint(-5, 5)

    draw_dots(ax, num_dots, dots, grid_scale.get(), lines, labels)
    root.after(100, update_coordinates)  # Update every 0.1 second

def update_plot():
    initialize_plot()

def update_plot_from_sliders(val):
    update_plot()

def initialize_plot():
    global num_dots, dots

    num_dots = int(dots_scale.get())  # Convert to int
    dots = [[random.randint(-10, 10), random.randint(-10, 10)] for _ in range(num_dots)]

    draw_dots(ax, num_dots, dots, grid_scale.get(), lines, labels)

root = tk.Tk()
root.title("Life on the Graph")
root.geometry("800x850")  # Set initial size of the window

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Configure the grid behavior
root.grid_rowconfigure(0, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Create a scale for grid_scale
grid_scale = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)
grid_scale.grid(row=1, column=0, columnspan=4, sticky='ew')
grid_scale.set((grid_scale['from'] + grid_scale['to']) / 2)  # Set initial value to the midpoint

# Create a scale for dots_scale
dots_scale = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)
dots_scale.grid(row=2, column=0, columnspan=4, sticky='ew')
dots_scale.set(5)  # Set initial value to 5

lines = True
labels = True

# Create checkbuttons for toggling labels and lines
labels_var = tk.BooleanVar(value=True)
labels_checkbutton = ttk.Checkbutton(root, text="Show Labels", command=toggle_labels, variable=labels_var)
labels_checkbutton.grid(row=3, column=0, columnspan=2, sticky='ew')

lines_var = tk.BooleanVar(value=True)
lines_checkbutton = ttk.Checkbutton(root, text="Show Lines", command=toggle_lines, variable=lines_var)
lines_checkbutton.grid(row=3, column=2, columnspan=2, sticky='ew')

initialize_plot()  # Initialize the plot

root.after(100, update_coordinates)  # Update coordinates continuously

root.mainloop()
