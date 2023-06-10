from math import cos, sin, sqrt, pi


import numpy as np

laser_scans_example = np.asarray([[4, 1, 1, 4], [2, 3, 3, 3],
                                  [3, 1, 2, 4], [1, 4, 5, 1],
                                  [1, 1, 3, 5], [2, 2, 3, 1],
                                  [1, 4, 2, 2], [3, 1, 3, 4], ])


def get_example_map():
    return np.asarray([
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0]])





def check_map(x, y, axis, simple_map, value):
    len_to_occup_cell = get_params_occupied_cell(x, y, axis, simple_map)
    return value == len_to_occup_cell


def main():
    simple_map = get_example_map()
    results = []
    scan = {0: 0, 1: 90, 2: 180, 3: 270}
    rotations_count = 4

    for scan_number, laser_scan in enumerate(laser_scans_example):
        for rotation in range(rotations_count):
            # print('scan number: {}'.format(scan_number))
            for y, row in enumerate(simple_map):
                for x, cell_value in enumerate(row):
                    # for alpha in range(0, 360, 90):
                    fit = 0
                    for axis in range(len(laser_scan)):
                        value = laser_scan[(axis - rotation) % len(laser_scan)]
                        if check_map(x, y, axis, simple_map, value):
                            fit += 1
                    if fit == len(scan):
                        results.append(
                            ('x: {}, y: {}, rotation: {}, laser scan: {}'.format(x, y, scan[rotation], laser_scan)))

    for number, result in enumerate(results):
        print('#{}'.format(number), result)


# main()


