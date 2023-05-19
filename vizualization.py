import math
import queue
import tkinter as tk
import threading
from logger import Logger
from sh import tail
from config import get_filename


ray_statuses = {True: 'Убрать лучи', False: 'Показать лучи'}
orient_statuses = {True: 'Убрать ориентацию в пространстве', False: 'Показать ориентацию в пространстве'}


class Window:

    def __init__(self, local_map, name='Карта', padding=20):
        self.window = tk.Tk()
        self.window.configure(bg='white')
        self.window.title(name)

        self.logger = Logger.get_instance()

        self.padding = padding

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        width, height = 1000, 500
        array_length = len(local_map)

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

        width_grid, height_grid = height, height
        width_control, height_control = width - width_grid, height
        self.cell_size = height_grid // array_length - self.padding

        self.grid_frame = tk.Frame(self.window, height=height_grid, width=width_grid, bg='white')
        self.control_frame = tk.Frame(self.window, height=height_control, width=width_control, bg='white')

        self.grid_frame.grid(row=0, column=0, sticky='nsew')
        self.control_frame.grid(row=0, column=1, sticky='nsew')

        self.__create_grid_frame(local_map, width_grid, height_grid)
        self.__create_control_frame(width_control, height_control)
        self.window.update_idletasks()
        self.window.grid_columnconfigure(0, weight=0)
        self.window.grid_columnconfigure(1, weight=1)

        self.logger.info('Application starts')

    def run(self):
        self.window.mainloop()

    def __draw_map(self, local_map, label_size):
        size = len(local_map)
        for y in range(size):
            for x in range(size):
                if local_map[y][x] == 1:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(x * self.cell_size + self.padding + label_size,
                                             y * self.cell_size + self.padding,
                                             (x + 1) * self.cell_size + self.padding + label_size,
                                             (y + 1) * self.cell_size + self.padding,
                                             fill=color)

    def __create_grid_frame(self, local_map, width_grid, height_grid):
        size = len(local_map)
        label_size = 1
        self.canvas = tk.Canvas(self.grid_frame, width=width_grid, height=height_grid, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.__draw_map(local_map, label_size)

        for i in range(size):
            y_coordinate = self.cell_size * i + self.cell_size // 2
            self.__draw_axis_label(str(i), label_size, self.padding // 2,
                                   y_coordinate + self.padding)

        for i in range(size):
            x_coordinate = self.cell_size * i + self.cell_size // 2 + self.padding
            self.__draw_axis_label(str(i), label_size, x_coordinate, size * self.cell_size + self.padding + label_size)

    def __draw_axis_label(self, text, size, x, y):
        label = tk.Label(self.grid_frame, text=text, width=size, height=size)
        label.place(x=x, y=y, anchor='n')

    def __create_buttons(self):
        self.button_next = tk.Button(self.top_control_frame, text="Следующая позиция", bg="white", wraplength=180)
        self.button_show_rays = tk.Button(self.top_control_frame, text="Убрать лучи", bg="white", wraplength=180)
        self.button_show_normal = tk.Button(self.top_control_frame, text="Убрать ориентацию в пространстве", bg="white",
                                            wraplength=180)

        self.button_next.pack(side=tk.TOP, pady=10)
        self.button_show_rays.pack(side=tk.TOP, pady=10)
        self.button_show_normal.pack(side=tk.TOP, pady=10)

    def __create_control_frame(self, width_control, height_control):
        self.window.grid_columnconfigure(0, weight=2)
        self.window.grid_columnconfigure(1, weight=1)

        height_top = height_control // 2
        height_bottom = height_control - height_top

        self.top_control_frame = tk.Frame(self.control_frame, width=width_control, height=height_top, bg='white')
        self.top_control_frame.pack(fill='both')

        self.bottom_control_frame = tk.Frame(self.control_frame, width=width_control, height=height_bottom, bg='white')
        self.bottom_control_frame.pack(fill='both')

        self.__create_buttons()

        self.__create_log(width_control)

    def __create_log(self, width_control):
        scrollbar = tk.Scrollbar(self.bottom_control_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text = tk.Text(self.bottom_control_frame,
                                width=width_control,
                                yscrollcommand=scrollbar.set)
        self.log_text.pack(fill=tk.BOTH, expand=1)
        scrollbar.config(command=self.log_text.yview)

        self.log_lines = queue.Queue()
        self.thread = threading.Thread(target=self.__update_log_widget)
        self.thread.daemon = True
        self.thread.start()
        self.__log_bind()

    def on_next_robots_button_click(self, scans, positions, robot_viz):
        robot_viz.clear_robots(self)
        x, y, orientation = next(positions)
        scan = next(scans)
        RobotsVis.current_scan = scan
        robot = Robot(self, x, y, orientation, scan)
        robot_viz.add_robot(robot)

    def on_show_rays_button_click(self, robot_viz):
        robot_viz.change_ray_status()
        status = robot_viz.get_ray_status()
        self.button_show_rays.config(text=ray_statuses[status])
        if status:
            for robot in robot_viz.robots:
                robot.show_rays(self)
        else:
            for robot in robot_viz.robots:
                robot.hide_rays(self)

    def on_show_normal_button_click(self, robot_viz):
        robot_viz.change_orient_status()
        status = robot_viz.get_orient_status()
        self.button_show_normal.config(text=orient_statuses[status])
        if status:
            for robot in robot_viz.robots:
                robot.show_orientation(self)
        else:
            for robot in robot_viz.robots:
                robot.hide_orientation(self)

    def add_buttons(self, scans_generator, positions_generator, robot_viz):
        self.button_next.config(
            command=lambda: self.on_next_robots_button_click(scans_generator,
                                                             positions_generator,
                                                             robot_viz))
        self.button_show_rays.config(command=lambda:
                self.on_show_rays_button_click(robot_viz))
        self.button_show_normal.config(command=lambda:
                self.on_show_normal_button_click(robot_viz))

    def log_widget_config(self):
        self.log_text.config(state='disabled')
        self.log_text.tag_config("INFO", foreground="black")
        self.log_text.tag_config("DEBUG", foreground="grey")
        self.log_text.tag_config("WARNING", foreground="orange")
        self.log_text.tag_config("ERROR", foreground="red")
        self.log_text.tag_config("CRITICAL", foreground="red", underline=1)

    def __update_log_widget(self):
        filename = get_filename()
        for line in tail("-F", " -c 1", filename, _iter=True):
            self.log_lines.put(line)
            self.window.event_generate('<<LogUpdate>>')

    def __update_log(self):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, self.log_lines.get())
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

    def __log_bind(self):
        self.window.bind('<<LogUpdate>>', lambda e: self.__update_log())


class Robot:

    def __init__(self, window, x, y, orientation, scan):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.rays = []
        self.__create_robot(window, scan)
        self.logger = Logger.get_instance()
        self.logger.info("New robot position {}".format(self))
        print("New robot position {}".format(self))

    def __str__(self):
        return 'x: {}, y: {}, angle: {}'.format(self.x, self.y, self.orientation)

    def __create_robot(self, window, scan):
        self.circle_coords = (
            self.x * window.cell_size + window.padding,
            self.y * window.cell_size + window.padding)

        self.circle = window.canvas.create_oval(self.circle_coords[0] - window.cell_size // 4,
                                                self.circle_coords[1] - window.cell_size // 4,
                                                self.circle_coords[0] + window.cell_size // 4,
                                                self.circle_coords[1] + window.cell_size // 4,
                                                fill='red', outline='black')

        self.draw_orientation(window)
        self.draw_rays(window, scan)
        if not RobotsVis.orient_status:
            self.hide_orientation(window)
        if not RobotsVis.ray_status:
            self.hide_rays(window)

    @staticmethod
    def convert_to_map_coords(window, x, y):
        return x * window.cell_size + window.padding, y * window.cell_size + window.padding

    def draw_rays(self, window, scan):
        radius = 3
        for angle in scan:
            x, y = self.convert_to_map_coords(window, *scan[angle])
            self.rays.append(window.canvas.create_line(*self.circle_coords, x, y, fill='blue'))
            self.rays.append(window.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius, fill='red'))

    def delete_rays(self, window):
        for ray in self.rays:
            window.canvas.delete(ray)

    def draw_orientation(self, window):
        main_line_coords, dashed_line_coords, angle_text_coords = self.calculate_line_orientation_coords(
            self.orientation,
            window.cell_size,
            self.circle_coords)
        self.main_line = window.canvas.create_line(*main_line_coords, fill='black')
        self.dashed_line = window.canvas.create_line(*dashed_line_coords, fill='black', dash=(4, 4))
        self.angle_text = window.canvas.create_text(*angle_text_coords, text=f"{self.orientation}°",
                                                    font=('Arial', 10),
                                                    anchor='nw')

    def delete_orientation(self, window):
        window.canvas.delete(self.main_line)
        window.canvas.delete(self.dashed_line)
        window.canvas.delete(self.angle_text)
        self.main_line = False
        self.dashed_line = False
        self.angle_text = False

    def delete_robot(self, window):
        window.canvas.delete(self.circle)
        if RobotsVis.orient_status:
            self.delete_orientation(window)
        if RobotsVis.ray_status:
            self.delete_rays(window)

    def show_rays(self, window):
        for ray in self.rays:
            window.canvas.itemconfigure(ray, state='normal')

    def hide_rays(self, window):
        for ray in self.rays:
            window.canvas.itemconfigure(ray, state='hidden')

    def show_orientation(self, window):
        window.canvas.itemconfigure(self.main_line, state='normal')
        window.canvas.itemconfigure(self.dashed_line, state='normal')
        window.canvas.itemconfigure(self.angle_text, state='normal')

    def hide_orientation(self, window):
        window.canvas.itemconfigure(self.main_line, state='hidden')
        window.canvas.itemconfigure(self.dashed_line, state='hidden')
        window.canvas.itemconfigure(self.angle_text, state='hidden')

    @staticmethod
    def calculate_line_orientation_coords(orientation, cell_size, circle_coords):
        rad = math.radians(orientation - 90)
        line_length = cell_size // 2

        x_start, y_start = circle_coords
        x_orientation, y_orientation = x_start - line_length * math.sin(rad), y_start - line_length * math.cos(rad)

        x_dashed = x_start + line_length

        angle_text_x, angle_text_y = x_start + 4, y_start - line_length // 2

        return (x_start, y_start, x_orientation, y_orientation), (x_start, y_start, x_dashed, y_start), (
        angle_text_x, angle_text_y)


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

    def clear_robots(self, window):
        for robot in self.robots:
            robot.delete_robot(window)
        self.robots = []

