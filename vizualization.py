import math
import tkinter as tk
import numpy as np


def print_coordinates(event):
    print("Координаты курсора: ", event.x, event.y)

class Window:
    def __init__(self, local_map, name='Карта', coordinate_padding=20):
        self.window = tk.Tk()
        self.window.configure(bg='white')
        self.window.title(name)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        width, height = 1000, 700
        array_length = len(local_map)

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

        width_grid, height_grid = height-coordinate_padding, height-coordinate_padding
        width_control, height_control = width - width_grid, height
        self.cell_size = height_grid // array_length - coordinate_padding

        self.grid_frame = tk.Frame(self.window, height=height_grid, width=width_grid, bg='white')
        self.control_frame = tk.Frame(self.window, height=height_control, width=width_control, bg='white')

        self.grid_frame.grid(row=0, column=0, sticky='nsew')
        self.control_frame.bind("<Motion>", print_coordinates)
        self.control_frame.grid(row=0, column=1, sticky='nsew')

        self.__create_grid_frame(local_map, coordinate_padding, width_grid, height_grid)
        self.__create_control_frame(width_control, height_control)
        self.window.update_idletasks()
        self.window.mainloop()

    def __create_map(self, local_map, coordinate_padding):
        size = len(local_map)
        for y in range(size):
            for x in range(size):
                if local_map[y][x] == 1:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(x * self.cell_size +coordinate_padding, y * self.cell_size, (x + 1) * self.cell_size +coordinate_padding, (y + 1) * self.cell_size,
                                           fill=color)

    def __create_grid_frame(self, local_map, coordinate_padding, width_grid, height_grid):
        size = len(local_map)
        self.canvas = tk.Canvas(self.grid_frame, width=width_grid, height=height_grid, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.__create_map(local_map, coordinate_padding)

        for i in range(size):
            y_coordinate = self.cell_size * i + self.cell_size // 2
            label = tk.Label(self.grid_frame, text=str(i))
            label.place(x=0, y=y_coordinate + coordinate_padding, anchor='w')

        for i in range(size):
            x_coordinate = self.cell_size * i + self.cell_size // 2
            label = tk.Label(self.grid_frame, text=str(i))
            label.place(x=x_coordinate, y=size * self.cell_size + 2, anchor='n')


    def __create_control_frame(self, width_control, height_control):
        self.control_frame.grid(row=0, column=1, sticky='nsew')

        self.window.grid_columnconfigure(0, weight=2)
        self.window.grid_columnconfigure(1, weight=1)

        height_top = height_control // 2
        height_bottom = height_control - height_top

        self.top_control_frame = tk.Frame(self.control_frame, width=width_control, height=height_top, bg='white')
        self.top_control_frame.pack(fill='both')

        self.bottom_control_frame = tk.Frame(self.control_frame, width=width_control, height=height_bottom, bg='white')
        self.bottom_control_frame.pack(fill='both')

        button_next = tk.Button(self.top_control_frame, text="Следующая позиция", bg="white", wraplength=180)
        button_show_rays = tk.Button(self.top_control_frame, text="Убрать лучи", bg="white", wraplength=180)
        button_show_normal = tk.Button(self.top_control_frame, text="Убрать ориентацию в пространстве", bg="white",
                                       wraplength=180)

        button_next.pack(side=tk.TOP, pady=10)
        button_show_rays.pack(side=tk.TOP, pady=10)
        button_show_normal.pack(side=tk.TOP, pady=10)

        log_text = tk.Text(self.bottom_control_frame, width=width_control // 50, height=height_bottom // 50)
        log_text.pack(fill='both')
        log_text.config(state='disabled')


def get_simple_map():
    return np.asarray([
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1]])
Window(get_simple_map())
