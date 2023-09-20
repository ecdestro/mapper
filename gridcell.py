# gridcell.py

class GridCell:
    def __init__(self, canvas, row, col, cell_width, cell_height):
        self.row = row
        self.col = col
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.state = 0  # 0 for off, 1 for on
        self.canvas = canvas  # Store the canvas
        self.draw()

    def draw(self):
        x0 = self.col * self.cell_width
        y0 = self.row * self.cell_height
        x1 = x0 + self.cell_width
        y1 = y0 + self.cell_height

        if self.state == 0:
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")  # Draw a black border for off cells
        else:
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="gray")  # Fill with gray for on cells

    def toggle_state(self):
        self.state = 1 - self.state  # Toggle between 0 and 1

    def on_click(self, event):
        self.toggle_state()  # Toggle the state when clicked
        self.draw()  # Update the canvas
        print(f"Cell ({self.row}, {self.col}) - State: {self.state}")

    def on_motion(self, event):
        x0 = self.col * self.cell_width
        y0 = self.row * self.cell_height
        x1 = x0 + self.cell_width
        y1 = y0 + self.cell_height

        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            if self.state == 0:
                # Cell is off, change the state to 1 (on) on hover
                self.state = 1
                self.draw()  # Update the canvas
                print(f"Hover over Cell ({self.row}, {self.col}) - State: {self.state}")
        else:
            if self.state == 1:
                # Cell is on, change the state to 0 (off) on leave
                self.state = 0
                self.draw()  # Update the canvas
                print(f"Leave Cell ({self.row}, {self.col}) - State: {self.state}")
