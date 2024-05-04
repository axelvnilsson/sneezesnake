import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_dot(ax, x, y):
    global x_scale, y_scale
    ax.clear()  # Clear previous drawings
    # Set up the plot with axes in the center
    ax.spines['left'].set_position('center')
    ax.spines['left'].set_color('gray')
    ax.spines['left'].set_linewidth(0.25)
    ax.spines['bottom'].set_position('center')
    ax.spines['bottom'].set_color('gray')
    ax.spines['bottom'].set_linewidth(0.25)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.plot(x, y, marker='o', color='black', markersize=3)  # Draw dot
    ax.text(x + 0.4, y + 0.4, f"({x:.1f}, {y:.1f})", fontsize=5, color='gray')  # Label the point
    ax.set_xlim(-20, 20)  # Set x limits
    ax.set_ylim(-20, 20)  # Set y limits

    # Customize the tick labels
    ax.tick_params(axis='both', which='major', labelsize=4, colors='gray', width=0.25)  # Set the font size and color of the axis ticks

    canvas.draw_idle()

def update_plot_from_sliders(val):
    global x_scale, y_scale
    x = x_scale.get()
    y = y_scale.get()
    x_entry.delete(0, tk.END)
    x_entry.insert(0, f"{x:.1f}")
    y_entry.delete(0, tk.END)
    y_entry.insert(0, f"{y:.1f}")
    plot_dot(ax, x, y)

def update_plot_from_entries(event=None):
    global x_scale, y_scale
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_scale.set(x)
    y_scale.set(y)
    plot_dot(ax, x, y)

root = tk.Tk()
root.title("Single Dot Plotter")
root.geometry("800x800")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, columnspan=4, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure([0, 1], weight=1)

# Initialize and place all widgets
x_entry = ttk.Entry(root, width=7)
x_entry.insert(0, '0')
x_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

y_entry = ttk.Entry(root, width=7)
y_entry.insert(0, '0')
y_scale = ttk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, command=update_plot_from_sliders)

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
