from generator import get_scans
from Map import Map, get_scan
from vizualization import Robot, RobotsVis, Window


def main():
    local_map = Map(debug=False, density=0.61)
    size = len(local_map)
    robot_viz = RobotsVis()
    x_robot, y_robot, orientation = 2.5, 2.5, 0
    scan = get_scans(x_robot, y_robot, local_map, alpha_diff=60)

    window = Window(local_map.array)
    #
    positions_generator = local_map.get_positions()
    scans = []
    for x_robot, y_robot, orientation in positions_generator:
        scans.append(get_scans(x_robot, y_robot, local_map, alpha_diff=10))
    print(scans)
    scans_generator = get_scan(scans)
    scan = next(scans_generator)
    positions_generator = local_map.get_positions()
    x_robot, y_robot, orientation = next(positions_generator)

    robot = Robot(window, x_robot, y_robot, orientation, scan)
    robot_viz.add_robot(robot)

    # button_next.config(command=lambda: on_next_robots_button_click(canvas, scans_generator, positions_generator, robot_viz))
    #
    # button_show_rays.config(command=lambda: on_show_rays_button_click(button_show_rays, robot_viz))
    # button_show_normal.config(command=lambda: on_show_normal_button_click(button_show_normal, robot_viz))
    #
    # window.update_idletasks()
    # window_width = grid.winfo_width() + control_frame.winfo_width() + 100
    # window_height = max(grid.winfo_height(), control_frame.winfo_height())
    # change_window_geometry(window, window_width, window_height)
    window.run()


main()