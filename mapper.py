# mapper.py v0.0.1 20230920 (c)ecdestro

from tkinter import *
from tkinter import filedialog
from gridcell import GridCell

# Define the window resolution
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define default grid dimensions
DEFAULT_ROWS = 10
DEFAULT_COLS = 10
DEFAULT_CELL_WIDTH = 20
DEFAULT_CELL_HEIGHT = 20

def newFile():
    pass

def openFile():
    location = filedialog.askopenfile(title = "Open", initialdir = ".", defaultextension = "*.txt", filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
    try:
        pass
    except AttributeError:
        print("No File Selected")

def saveFile():
    location = filedialog.asksaveasfilename(title = "Save As", initialdir = ".", defaultextension = "*.txt", filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
    try:
        pass
    except FileNotFoundError:
        print("No File Selected")

if __name__ == "__main__":
    mapper = Tk()
    mapper.title("Raycast Map Editor")
    mapper.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    body = Canvas(mapper)
    body.grid()
    body.focus_set()
    
    # cols = DEFAULT_COLS
    # rows = DEFAULT_ROWS
    cell_width = DEFAULT_CELL_WIDTH
    cell_height = DEFAULT_CELL_HEIGHT

    # Create and bind the GridCell instances
    # grid_cells = [[GridCell(row, col, cell_width, cell_height) for col in range(cols)] for row in range(rows)]
    # Create a 2D list to hold GridCell objects
    grid = []

    # Define the number of rows and columns
    num_rows = 10
    num_cols = 10

    # Create the GridCell objects and add them to the grid list
    for row in range(num_rows):
        row_cells = []
        for col in range(num_cols):
            cell = GridCell(body, row, col, cell_width, cell_height)
            row_cells.append(cell)
        grid.append(row_cells)

    # Bind the mouse click event to the on_click method for each cell
    for row_cells in grid:
        for cell in row_cells:
            body.tag_bind(cell, '<Button-1>', cell.on_click)

    for row_cells in grid:
        for cell in row_cells:
            body.tag_bind(cell, '<Motion>', cell.on_motion)
    # # Bind the mouse enter (hover) event to the on_hover method for each cell
    # for row_cells in grid:
    #     for cell in row_cells:
    #         body.bind('<Enter>', cell.on_hover)

    # # Bind the mouse leave event to the on_leave method for each cell
    # for row_cells in grid:
    #     for cell in row_cells:
    #         body.bind('<Leave>', cell.on_leave)

    menuBar = Menu(mapper)

    fileMenu = Menu(menuBar, tearoff = False)
    fileMenu.add_command(label = "New Map", command = newFile)
    fileMenu.add_command(label = "Open Map...", command = openFile)
    fileMenu.add_command(label = "Save Map", command = False)
    fileMenu.add_command(label = "Save Map As...", command = saveFile)
    fileMenu.add_command(label = "Exit Editor", command = mapper.quit)
    menuBar.add_cascade(label = "File", menu = fileMenu)

    editMenu = Menu(menuBar, tearoff = False)
    editMenu.add_command(label = "Undo", command = False)
    editMenu.add_command(label = "Redo", command = False)
    editMenu.add_command(label = "Grid Size...", command = False)
    editMenu.add_command(label = "Clear Grid", command = False)
    menuBar.add_cascade(label = "Edit", menu = editMenu)

    mapper.config(menu = menuBar)
    mapper.mainloop()