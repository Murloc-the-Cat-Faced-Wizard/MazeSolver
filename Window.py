from tkinter import Tk, BOTH, Canvas 

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("MazeSolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
