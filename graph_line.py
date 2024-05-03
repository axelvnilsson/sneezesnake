import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_line(ax, x1, y1, x2, y2):
    ax.clear()  # Clear previous drawings
    ax.plot([x1, x2], [y1, y2], marker='o', color='blue')  # Draw line with dots at ends
    ax.text(x1, y1, f"({x1:.1f}, {y1:.1f})", fontsize=12, color='red')  # Label point 1
    ax.text(x2, y2, f"({x2:.1f}, {y2:.1f})", fontsize=12, color='red')  # Label point 2
    ax.set_xlim(min(x1, x2) - 10, max(x1, x2) + 10)  # Set x limits
    ax.set_ylim(min(y1, y2) - 10, max(y1, y2) + 10)  # Set y limits
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
    plot_line(ax, x1, y1, x2, y2)

def update_plot_from_entries():
    x1 = float(x1_entry.get())
    y1 = float(y1_entry.get())
    x2 = float(x2_entry.get())
    y2 = float(y2_entry.get())
    x1_scale.set(x1)
    y1_scale.set(y1)
    x2_scale.set(x2)
    y2_scale.set(y2)
    plot_line(ax, x1, y1, x2, y2)

root = tk.Tk()
root.title("Interactive Line Plotter")
root.geometry("800x600")  # Set initial size of the window

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
default_values = [1, 1, 5, 5]
for i in range(4):
    ttk.Label(root, text=labels[i]).grid(row=1, column=i, sticky='ew')
    entry = ttk.Entry(root, width=5)
    entry.grid(row=2, column=i, sticky='ew')
    entry.insert(0, str(default_values[i]))
    entries.append(entry)
    scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)
    scale.grid(row=3, column=i, sticky='ew')
    scale.set(default_values[i])
    scales.append(scale)

x1_entry, y1_entry, x2_entry, y2_entry = entries
x1_scale, y1_scale, x2_scale, y2_scale = scales

ttk.Button(root, text="Update from Entries", command=update_plot_from_entries).grid(row=4, column=0, columnspan=4, sticky='ew')

update_plot_from_entries()  # Initial plot update

root.mainloop()
