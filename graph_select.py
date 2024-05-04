import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotInputWidget(ttk.Frame):
    def __init__(self, master, label_text, default_value, scale_range, command):
        super().__init__(master)
        self.label_text = label_text
        self.default_value = default_value
        self.scale_range = scale_range
        self.command = command

        self.initialize_widgets()

    def initialize_widgets(self):
        self.label = ttk.Label(self, text=self.label_text)
        self.entry = ttk.Entry(self, width=7)
        self.scale = ttk.Scale(self, from_=self.scale_range[0], to=self.scale_range[1], orient=tk.HORIZONTAL, command=self.command)

        self.label.grid(row=0, column=0, sticky='w')
        self.entry.grid(row=0, column=1, sticky='ew')
        self.scale.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.entry.insert(0, str(self.default_value))
        self.scale.set(self.default_value)

    def get_value(self):
        return float(self.entry.get())

class SingleDotPlotterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Single Dot Plotter")
        self.geometry("800x800")

        self.initialize_widgets()
        self.configure_grid()
        self.update_plot_from_entries()

    def initialize_widgets(self):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.x_input = PlotInputWidget(self, "X:", 0, (-10, 10), self.update_plot_from_sliders)
        self.y_input = PlotInputWidget(self, "Y:", 0, (-10, 10), self.update_plot_from_sliders)
        self.grid_scale = ttk.Scale(self, from_=0.1, to=2, orient=tk.HORIZONTAL, command=self.update_grid_scale)

        self.x_input.grid(row=1, column=0)
        self.y_input.grid(row=2, column=0)
        self.grid_scale.grid(row=3, column=0, columnspan=2, sticky='ew')
        self.canvas_widget.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure([0, 1], weight=1)

    def configure_grid(self):
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('gray')
        self.ax.spines['left'].set_linewidth(0.25)
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('gray')
        self.ax.spines['bottom'].set_linewidth(0.25)
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.25)
        self.ax.tick_params(axis='both', which='major', labelsize=4, colors='gray', width=0.25)

    def plot_dot(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y, marker='o', color='black', markersize=3)
        self.ax.text(x + 0.4, y + 0.4, f"({x:.1f}, {y:.1f})", fontsize=5, color='gray')
        self.ax.set_xlim(-20 * self.grid_scale.get(), 20 * self.grid_scale.get())
        self.ax.set_ylim(-20 * self.grid_scale.get(), 20 * self.grid_scale.get())
        self.canvas.draw_idle()

    def update_plot_from_entries(self):
        x = self.x_input.get_value()
        y = self.y_input.get_value()
        self.plot_dot(x, y)

    def update_plot_from_sliders(self, val):
        x = self.x_input.get_value()
        y = self.y_input.get_value()
        self.plot_dot(x, y)

    def update_grid_scale(self, val):
        self.plot_dot(self.x_input.get_value(), self.y_input.get_value())

class LinePlotterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Line Plotter")
        self.geometry("800x800")

        self.initialize_widgets()
        self.configure_grid()

    def initialize_widgets(self):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.x1_input = PlotInputWidget(self, "X1:", 0, (-10, 10), self.update_plot)
        self.y1_input = PlotInputWidget(self, "Y1:", 0, (-10, 10), self.update_plot)
        self.x2_input = PlotInputWidget(self, "X2:", 0, (-10, 10), self.update_plot)
        self.y2_input = PlotInputWidget(self, "Y2:", 0, (-10, 10), self.update_plot)
        self.grid_scale = ttk.Scale(self, from_=0.1, to=2, orient=tk.HORIZONTAL, command=self.update_plot)

        self.x1_input.grid(row=1, column=0)
        self.y1_input.grid(row=2, column=0)
        self.x2_input.grid(row=3, column=0)
        self.y2_input.grid(row=4, column=0)
        self.grid_scale.grid(row=5, column=0, sticky='ew')
        self.canvas_widget.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def configure_grid(self):
        self.ax.spines['left'].set_position('center')
        self.ax.spines['left'].set_color('gray')
        self.ax.spines['left'].set_linewidth(0.25)
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['bottom'].set_color('gray')
        self.ax.spines['bottom'].set_linewidth(0.25)
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.25)
        self.ax.tick_params(axis='both', which='major', labelsize=4, colors='gray', width=0.25)

    def plot_line(self, x1, y1, x2, y2):
        self.ax.clear()
        self.ax.plot([x1, x2], [y1, y2], marker='o', color='black', markersize=3)
        self.ax.text(x1 + 0.4, y1 + 0.4, f"({x1:.1f}, {y1:.1f})", fontsize=5, color='gray')
        self.ax.text(x2 + 0.4, y2 + 0.4, f"({x2:.1f}, {y2:.1f})", fontsize=5, color='gray')
        self.ax.set_xlim(-20 * self.grid_scale.get(), 20 * self.grid_scale.get())
        self.ax.set_ylim(-20 * self.grid_scale.get(), 20 * self.grid_scale.get())
        self.canvas.draw_idle()

    def update_plot(self, val):
        x1 = self.x1_input.get_value()
        y1 = self.y1_input.get_value()
        x2 = self.x2_input.get_value()
        y2 = self.y2_input.get_value()
        self.plot_line(x1, y1, x2, y2)

def choose_application():
    choice = input("Enter '1' for Single Dot Plotter App or '2' for Line Plotter App: ")
    if choice == '1':
        app = SingleDotPlotterApp()
    elif choice == '2':
        app = LinePlotterApp()
    else:
        print("Invalid choice. Running Single Dot Plotter App by default.")
        app = SingleDotPlotterApp()
    app.mainloop()

if __name__ == "__main__":
    choose_application()
