from tkinter import Tk, Canvas # using the tkinter library for graphics
from Constants import WIDTH, HEIGHT

class Root(Tk):
    canvas = objects = None

    def __init__(self):
        super(Root, self).__init__()
        
        self.title("Pi Collisions Approximator")
        self.minsize(WIDTH, HEIGHT)
        self.resizable(False, False)

        # Create canvas
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.configure(bg="black", highlightthickness=0)
        self.objects = [] # tracks items on screen to clear & re-draw each frame

    # helper functions for drawing on the screen
    def draw_circle(self, x, y, r, fill="#ffbb00"): 
        self.objects.append(self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill))

    def draw_line(self, x0, y0, x1, y1, fill="ffffff"): 
        self.objects.append(self.canvas.create_line(x0, y0, x1, y1, fill=fill))

    def draw_text(self, x, y, txt, fill="white", font=("Arial", 25)): 
        self.objects.append(self.canvas.create_text(x, y, text=txt, fill=fill, font=font))

    def draw_rectangle(self, x0, y0, x1, y1, fill="white"): 
        self.objects.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=""))

    def clear_objects(self): 
        for obj in self.objects: 
            self.canvas.delete(obj)
        self.objects.clear()

    def draw_blocks(self, blocks, coll):
        self.clear_objects()
        self.draw_text(WIDTH / 2, 150, str(coll))
        
        for block in blocks: 
            half_side = block.w / 2
            self.draw_text(block.x, block.y - block.w / 2 - 25, str(round(block.v * 10000, 4)), font=("Arial", 16)) # draw vel, * 1000 to make numbers more readable
            self.draw_text(block.x, block.y + block.w / 2 + 25, "{:,}".format(block.m) + " kg", font=("Arial", 18)) # draw mass
            self.draw_rectangle(block.x - half_side, block.y - half_side, block.x + half_side, block.y + half_side)
        
    def draw_menu(self, selected): 
        self.clear_objects()

        margin = 200
        x = margin

        self.draw_text(WIDTH / 2, 250, "How many digits?")
        for i in range(1, 7): # 6 possible selections
            self.draw_text(x, HEIGHT / 2, str(i), "#fffb21" if selected == i else "white")
            x += ((WIDTH - (margin)) / 6)