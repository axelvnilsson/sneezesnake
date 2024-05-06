import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def draw_two_dots_and_a_line(ax, x1, y1, x2, y2, grid_scale):
    ax.plot([x1, x2], [y1, y2], marker='o', color='black', markersize=2, linewidth=0.5)  # Draw line with dots at ends
    ax.text(x1 + 0.4 * grid_scale, y1 + 0.4 * grid_scale, f"({x1:.1f}, {y1:.1f})", fontsize=5, color='gray')  # Label point 1
    ax.text(x2 + 0.4 * grid_scale, y2 + 0.4 * grid_scale, f"({x2:.1f}, {y2:.1f})", fontsize=5, color='gray')  # Label point 2
    # ax.set_xlim(min(x1, x2) - 10, max(x1, x2) + 10)  # Set x limits
    # ax.set_ylim(min(y1, y2) - 10, max(y1, y2) + 10)  # Set y limits

def update_plot(ax, x1, y1, x2, y2):
    reset_axes(ax)
    draw_grid(ax, grid_scale.get())
    draw_two_dots_and_a_line(ax, x1, y1, x2, y2, grid_scale.get())
    canvas.draw_idle()

def update_plot_from_sliders(val):
    x1 = x1_scale.get()
    y1 = y1_scale.get()
    x2 = x2_scale.get()
    y2 = y2_scale.get()
    x1_entry.delete(0, tk.END)
    x1_entry.insert(0, f"{x1:.1f}")
    y1_entry.delete(0, tk.END)
    y1_entry.insert(0, f"{y1:.1f}")
    x2_entry.delete(0, tk.END)
    x2_entry.insert(0, f"{x2:.1f}")
    y2_entry.delete(0, tk.END)
    y2_entry.insert(0, f"{y2:.1f}")
    update_plot(ax, x1, y1, x2, y2)

def update_plot_from_entries():
    x1 = float(x1_entry.get())
    y1 = float(y1_entry.get())
    x2 = float(x2_entry.get())
    y2 = float(y2_entry.get())
    x1_scale.set(x1)
    y1_scale.set(y1)
    x2_scale.set(x2)
    y2_scale.set(y2)
    update_plot(ax, x1, y1, x2, y2)

root = tk.Tk()
root.title("Two Dots and a Line Plotter")
root.geometry("800x800")  # Set initial size of the window

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Configure the grid behavior
root.grid_rowconfigure(0, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Create sliders, labels, and entry widgets
entries = []
scales = []
labels = ['X1', 'Y1', 'X2', 'Y2']
default_values = [-5, -5, 5, 5]
for i in range(4):
    ttk.Label(root, text=labels[i]).grid(row=1, column=i, sticky='ew')
    entry = ttk.Entry(root, width=2)
    entry.grid(row=2, column=i, sticky='ew')
    entry.insert(0, str(default_values[i]))
    entries.append(entry)
    grid_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)
    grid_scale.grid(row=3, column=i, sticky='ew')
    grid_scale.set(default_values[i])
    scales.append(grid_scale)

x1_entry, y1_entry, x2_entry, y2_entry = entries
x1_scale, y1_scale, x2_scale, y2_scale = scales

ttk.Button(root, text="Update from Entries", command=update_plot_from_entries).grid(row=4, column=0, columnspan=4, sticky='ew')

update_plot_from_entries()  # Initial plot update

root.mainloop()
