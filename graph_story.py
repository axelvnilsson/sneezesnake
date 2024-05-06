import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

class Story:
    def __init__(self):
        # Initialize the chapters with 'type' and plotting data
        self.chapters = [
            {'title': 'Chapter 1', 'message': 'Welcome to the beginning.', 'x': 5, 'y': 10, 'lines': True, 'labels': False, 'type': 'line'},
            {'title': 'Chapter 2', 'message': 'Things get interesting.', 'x': 15, 'y': 20, 'lines': False, 'labels': True, 'type': 'bar'},
            {'title': 'Chapter 3', 'message': 'The plot thickens.', 'x': 25, 'y': 30, 'lines': True, 'labels': True, 'type': 'scatter'},
            {'title': 'Chapter 4', 'message': 'Approaching the climax.', 'x': 35, 'y': 40, 'lines': False, 'labels': False, 'type': 'bar'},
            {'title': 'Chapter 5', 'message': 'The end is here.', 'x': 45, 'y': 50, 'lines': True, 'labels': True, 'type': 'line'}
        ]
        self.current_chapter = 0

    def get_current_chapter(self):
        return self.chapters[self.current_chapter]

    def next_chapter(self):
        if self.current_chapter < len(self.chapters) - 1:
            self.current_chapter += 1
            return True
        else:
            return False

def display_chapter(chapter):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    axcolor = 'lightgoldenrodyellow'
    
    if chapter['type'] == 'scatter':
        sc = ax.scatter([chapter['x']], [chapter['y']], c='blue')
    elif chapter['type'] == 'line':
        ln, = ax.plot([chapter['x']-5, chapter['x']], [chapter['y']-5, chapter['y']], 'r-')
    elif chapter['type'] == 'bar':
        bars = ax.bar([chapter['x']], [chapter['y']], width=5)

    ax_slider_x = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_slider_y = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

    slider_x = Slider(ax_slider_x, 'X', 0.1, 100.0, valinit=chapter['x'])
    slider_y = Slider(ax_slider_y, 'Y', 0.1, 100.0, valinit=chapter['y'])

    def update(val):
        x = slider_x.val
        y = slider_y.val
        if chapter['type'] == 'scatter':
            sc.set_offsets([[x, y]])
        elif chapter['type'] == 'line':
            ln.set_xdata([x-5, x])
            ln.set_ydata([y-5, y])
        elif chapter['type'] == 'bar':
            bars[0].set_height(y)
            bars[0].set_x(x)
        fig.canvas.draw_idle()

    slider_x.on_changed(update)
    slider_y.on_changed(update)

    plt.show()

def main():
    story = Story()
    while True:
        current_chapter = story.get_current_chapter()
        display_chapter(current_chapter)
        input("Press Enter to continue to the next chapter or close the plot window...")
        if not story.next_chapter():
            print("End of story.")
            break

if __name__ == "__main__":
    main()
