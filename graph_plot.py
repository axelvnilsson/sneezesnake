import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_dot(ax, x, y):
    ax.clear()  # Clear previous drawings
    ax.plot(x, y, marker='o', color='blue')  # Draw dot
    ax.text(x, y, f"({x:.1f}, {y:.1f})", fontsize=12, color='red')  # Label the point
    ax.set_xlim(-10, 10)  # Set x limits
    ax.set_ylim(-10, 10)  # Set y limits
    canvas.draw_idle()

def update_plot_from_sliders(val):
    x = x_scale.get()
    y = y_scale.get()
    x_entry.delete(0, tk.END)
    x_entry.insert(0, f"{x:.1f}")
    y_entry.delete(0, tk.END)
    y_entry.insert(0, f"{y:.1f}")
    plot_dot(ax, x, y)

def update_plot_from_entries(event=None):
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_scale.set(x)
    y_scale.set(y)
    plot_dot(ax, x, y)

root = tk.Tk()
root.title("Single Dot Plotter")
root.geometry("800x600")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=4, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure([0, 1], weight=1)

# Initialize entry and scale for X and Y before defining functions that use them
x_entry = ttk.Entry(root, width=7)
x_entry.insert(0, '0')
x_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

y_entry = ttk.Entry(root, width=7)
y_entry.insert(0, '0')
y_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

# Place widgets
ttk.Label(root, text="X:").grid(row=1, column=0, sticky='w')
x_entry.grid(row=1, column=1, sticky='ew')
x_entry.bind("<Return>", update_plot_from_entries)
x_scale.grid(row=2, column=0, columnspan=2, sticky='ew')
x_scale.set(0)

ttk.Label(root, text="Y:").grid(row=3, column=0, sticky='w')
y_entry.grid(row=3, column=1, sticky='ew')
y_entry.bind("<Return>", update_plot_from_entries)
y_scale.grid(row=4, column=0, columnspan=2, sticky='ew')
y_scale.set(0)

ttk.Button(root, text="Update from Entries", command=update_plot_from_entries).grid(row=5, column=0, columnspan=2, sticky='ew')

update_plot_from_entries()  # Initial plot update

root.mainloop()
