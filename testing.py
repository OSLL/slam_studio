from data import get_iterator
from generator import generate_scans
from map_model import Map
from vizualization import Robot, RobotsVis, Window
from data import get_iterator


def main():
    local_map = Map(debug=False, density=0.61)
    robot_viz = RobotsVis()
    window = Window(local_map.array)
    positions = local_map.get_free_positions()
    scans = []
    for x_robot, y_robot, orientation in positions:
        scans.append(generate_scans(x_robot, y_robot, local_map, alpha_diff=10))
    scan_it = get_iterator(scans)
    scan = next(scan_it)

    positions = local_map.get_free_positions()
    positions_it = get_iterator(positions)
    x_robot, y_robot, orientation = next(positions_it)

    robot = Robot(window, x_robot, y_robot, orientation, scan)
    robot_viz.add_robot(robot)

    window.add_buttons(scan_it, positions_it, robot_viz)

    window.run()


main()