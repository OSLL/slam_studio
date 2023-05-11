import math
import tkinter as tk

ray_statuses = {True: 'Убрать лучи', False: 'Показать лучи'}
orient_statuses = {True: 'Убрать ориентацию в пространстве', False: 'Показать ориентацию в пространстве'}


def change_window_geometry(window, window_width, window_height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def create_window(size, cell_size, name='Карта', coordinate_padding=20):
    window = tk.Tk()
    window.title(name)

    grid = tk.Frame(window)
    control_frame = tk.Frame(window, bg="white", width=200)

    grid.grid(row=0, column=0, sticky="nsew", padx=coordinate_padding)
    control_frame.grid(row=0, column=1, sticky="nsew")

    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)

    canvas = tk.Canvas(grid, width=size * cell_size, height=(size * cell_size), bg="white")
    canvas.grid(row=0, column=0, sticky="nsew")

    for i in range(size):
        y_coordinate = cell_size * i + cell_size // 2
        label = tk.Label(window, text=str(i))
        label.place(x=coordinate_padding // 3, y=y_coordinate + coordinate_padding, anchor='w')

    for i in range(size):
        x_coordinate = cell_size * i + cell_size // 2
        label = tk.Label(grid, text=str(i))
        label.place(x=x_coordinate, y=size * cell_size + 2, anchor='n')

    window.update_idletasks()
    window_width = grid.winfo_width() + control_frame.winfo_width() + 100 + coordinate_padding
    window_height = max(grid.winfo_height(), control_frame.winfo_height()) + coordinate_padding
    change_window_geometry(window, window_width, window_height)

    return window, canvas, control_frame, grid


def run_window(window):
    window.mainloop()


def create_map(canvas, simple_map, cell_size=100):
    size = len(simple_map)
    cells = [[None for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for x in range(size):
            if simple_map[y][x] == 1:
                color = "black"
            else:
                color = "white"
            cell = canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size,
                                           fill=color)
            cells[y][x] = cell

    return cells


class Robot:
    cell_size = 100

    def __init__(self, canvas, x, y, orientation, scan):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.orientation = orientation
        self.rays = []
        self.create_robot(scan)

    def create_robot(self, scan):
        self.circle_coords = (
            self.x * Robot.cell_size, self.y * Robot.cell_size)

        self.circle = self.canvas.create_oval(self.circle_coords[0] - Robot.cell_size // 4,
                                              self.circle_coords[1] - Robot.cell_size // 4,
                                              self.circle_coords[0] + Robot.cell_size // 4,
                                              self.circle_coords[1] + Robot.cell_size // 4,
                                              fill='red', outline='black')
        if RobotsVis.orient_status:
            self.draw_orientation()
        if RobotsVis.ray_status:
            self.draw_rays(scan)

    def convert_to_map_coords(self, x, y):
        return x * Robot.cell_size, y * Robot.cell_size

    def draw_rays(self, scan):
        radius = 3
        for angle in scan:
            x, y = self.convert_to_map_coords(*scan[angle])
            self.rays.append(self.canvas.create_line(*self.circle_coords, x, y, fill='blue'))
            self.rays.append(self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red'))

    def delete_rays(self):
        for ray in self.rays:
            self.canvas.delete(ray)

    def draw_orientation(self):
        main_line_coords, dashed_line_coords, angle_text_coords = self.calculate_line_orientation_coords(
            self.orientation,
            Robot.cell_size,
            self.circle_coords)
        self.main_line = self.canvas.create_line(*main_line_coords, fill='black')
        self.dashed_line = self.canvas.create_line(*dashed_line_coords, fill='black', dash=(4, 4))
        self.angle_text = self.canvas.create_text(*angle_text_coords, text=f"{self.orientation}°", font=('Arial', 10),
                                                  anchor='nw')

    def delete_orientation(self):
        self.canvas.delete(self.main_line)
        self.canvas.delete(self.dashed_line)
        self.canvas.delete(self.angle_text)
        self.main_line = False
        self.dashed_line = False
        self.angle_text = False

    def delete_robot(self):
        self.canvas.delete(self.circle)
        if RobotsVis.orient_status:
            self.delete_orientation()
        if RobotsVis.ray_status:
            self.delete_rays()

    def show_rays(self):
        for ray in self.rays:
            self.canvas.itemconfigure(ray, state='normal')

    def hide_rays(self):
        for ray in self.rays:
            self.canvas.itemconfigure(ray, state='hidden')

    def show_orientation(self):
        self.canvas.itemconfigure(self.main_line, state='normal')
        self.canvas.itemconfigure(self.dashed_line, state='normal')
        self.canvas.itemconfigure(self.angle_text, state='normal')

    def hide_orientation(self):
        self.canvas.itemconfigure(self.main_line, state='hidden')
        self.canvas.itemconfigure(self.dashed_line, state='hidden')
        self.canvas.itemconfigure(self.angle_text, state='hidden')

    @staticmethod
    def calculate_line_orientation_coords(orientation, cell_size, circle_coords):
        rad = math.radians(orientation-90)
        line_length = cell_size // 2

        x_start, y_start = circle_coords
        x_orientation, y_orientation = x_start - line_length * math.sin(rad), y_start - line_length * math.cos(rad)

        x_dashed = x_start + line_length

        angle_text_x, angle_text_y = x_start + 4, y_start - line_length // 2

        return (x_start, y_start, x_orientation, y_orientation), (x_start, y_start, x_dashed, y_start), (angle_text_x, angle_text_y)


class RobotsVis:
    orient_status = True
    ray_status = True
    current_scan = False

    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def get_orient_status(self):
        return RobotsVis.orient_status

    def change_orient_status(self):
        RobotsVis.orient_status = not RobotsVis.orient_status

    def get_ray_status(self):
        return RobotsVis.ray_status

    def change_ray_status(self):
        RobotsVis.ray_status = not RobotsVis.ray_status

    def clear_robots(self):
        for robot in self.robots:
            robot.delete_robot()
        self.robots = []


def on_next_robots_button_click(canvas, scans, positions, robot_viz):
    robot_viz.clear_robots()
    x, y, orientation = next(positions)
    scan = next(scans)
    RobotsVis.current_scan = scan
    robot = Robot(canvas, x, y, orientation, scan)
    robot_viz.add_robot(robot)
    print('Новая позиция: {}, {}, {}'.format(x, y, orientation))
    print('Скан: {}'.format(scan))


def on_show_rays_button_click(button_show_rays, robot_viz):
    robot_viz.change_ray_status()
    status = robot_viz.get_ray_status()
    button_show_rays.config(text=ray_statuses[status])
    if status:
        for robot in robot_viz.robots:
            robot.show_rays()
    else:
        for robot in robot_viz.robots:
            robot.hide_rays()


def on_show_normal_button_click(button_show_normal, robot_viz):
    robot_viz.change_orient_status()
    status = robot_viz.get_orient_status()
    button_show_normal.config(text=orient_statuses[status])
    if status:
        for robot in robot_viz.robots:
            robot.show_orientation()
    else:
        for robot in robot_viz.robots:
            robot.hide_orientation()


def add_text(label, text):
    label.config(text=text)


def create_control_frame(control_frame):
    button_next = tk.Button(control_frame, text="Следующая позиция", bg="white", wraplength=180)
    button_show_rays = tk.Button(control_frame, text="Убрать лучи", bg="white", wraplength=180)
    button_show_normal = tk.Button(control_frame, text="Убрать ориентацию в пространстве", bg="white", wraplength=180)

    button_next.pack(side=tk.TOP, pady=10)
    button_show_rays.pack(side=tk.TOP, pady=10)
    button_show_normal.pack(side=tk.TOP, pady=10)
    return button_next, button_show_rays, button_show_normal
