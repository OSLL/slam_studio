from generator import get_scans
from Map import Map, get_scan
from vizualization import Robot, RobotsVis, create_window, create_map, create_control_frame, change_window_geometry, \
    run_window, on_show_rays_button_click, on_show_normal_button_click, on_next_robots_button_click


def main():
    matrix = Map(debug=False, density=0.61)
    size = len(matrix)
    robot_viz = RobotsVis()
    x_robot, y_robot, orientation = 2.5, 2.5, 0
    scan = get_scans(x_robot, y_robot, matrix, alpha_diff=60)

    window, canvas, control_frame, grid = create_window(size, Robot.cell_size)
    create_map(canvas, matrix.map, cell_size=Robot.cell_size)
    button_next, button_show_rays, button_show_normal = create_control_frame(control_frame)
    #
    positions_generator = matrix.get_positions()
    scans = []
    for x_robot, y_robot, orientation in positions_generator:
        scans.append(get_scans(x_robot, y_robot, matrix, alpha_diff=10))
    print(scans)
    scans_generator = get_scan(scans)
    scan = next(scans_generator)
    positions_generator = matrix.get_positions()
    x_robot, y_robot, orientation = next(positions_generator)

    robot = Robot(canvas, x_robot, y_robot, orientation, scan)
    robot_viz.add_robot(robot)

    button_next.config(command=lambda: on_next_robots_button_click(canvas, scans_generator, positions_generator, robot_viz))

    button_show_rays.config(command=lambda: on_show_rays_button_click(button_show_rays, robot_viz))
    button_show_normal.config(command=lambda: on_show_normal_button_click(button_show_normal, robot_viz))

    window.update_idletasks()
    window_width = grid.winfo_width() + control_frame.winfo_width() + 100
    window_height = max(grid.winfo_height(), control_frame.winfo_height())
    change_window_geometry(window, window_width, window_height)
    run_window(window)


main()