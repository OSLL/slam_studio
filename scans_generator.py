from math import cos, sin, sqrt, pi
import numpy as np


def euclidean_distance(x1, x2, y1, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_point_in_direction(array, direction, limit):
    k = 0
    if direction > 0:
        for i in range(limit + 1, len(array)):
            if array[i] == 1:
                return k
            k += 1
    else:
        for i in range(limit - 1, -1, -1):
            if array[i] == 1:
                return k
            k += 1
    return k


def get_params_occupied_cell(x, y, angle, simple_map):
    x_end, y_end = x, y
    length = 0
    e = 0.00000001
    radians = pi * (angle / 180)
    cos_alpha = cos(radians)
    cos_alpha = 0 if abs(cos_alpha) < e else cos_alpha
    sin_alpha = sin(radians)
    sin_alpha = 0 if abs(sin_alpha) < e else sin_alpha

    if not cos_alpha:
        direction = -1 * sin_alpha
        length = get_point_in_direction(simple_map[:, x], direction, y)
        if direction > 0:
            y_end += (length + 1)
        else:
            y_end -= (length + 1)
    elif not sin_alpha:
        direction = -1 * cos_alpha
        length = get_point_in_direction(simple_map[y], direction, x)
        if direction > 0:
            x_end += (length + 1)
        else:
            x_end -= (length + 1)
    return length, x_end, y_end


def cross(A1, B1, C1, A2, B2, C2):
    A = np.array([[A1, B1], [A2, B2]])
    C = np.array([C1, C2])
    if np.linalg.det(A) != 0:
        return np.linalg.solve(A, C)
    return None, None


def get_matrix_coefficients_for_line(b_robot, k_robot):
    if k_robot is None:
        A1 = 1
        B1 = 0
        C1 = b_robot
    else:
        A1 = -1 * k_robot
        B1 = 1
        C1 = b_robot
    return A1, B1, C1


def get_line_coefficients(**kwargs):
    e = 0.00000001
    if 'alpha' in kwargs:
        alpha, x, y = kwargs['alpha'], kwargs['x'], kwargs['y']
        radians = pi * (alpha / 180)
        cos_alpha = cos(radians)
        cos_alpha = 0 if abs(cos_alpha) < e else cos_alpha
        if not cos_alpha:
            return None, x
        k = sin(radians) / cos(radians)
        b = y - k * x
    elif 'coordinates' in kwargs:
        x1, y1, x2, y2 = kwargs['coordinates']
        k = (y2 - y1) / (x2 - x1) if x2 != x1 else None
        if k is None:
            return None, x1
        b = y1 - k * x1
    else:
        raise ValueError('Invalid arguments provided.')
    return k, b


def is_point_belongs_segment(x_cross, y_cross, segment_coordinates):
    x1, y1, x2, y2 = segment_coordinates
    return min(x1, x2) <= round(x_cross, 1) <= max(x1, x2) and min(y1, y2) <= round(y_cross, 1) <= max(y1, y2)


def is_point_belongs_area(x_cross, y_cross, limit_x, limit_y):
    return limit_x[0] <= round(x_cross, 1) <= limit_x[1] and limit_y[0] <= round(y_cross, 1) <= limit_y[1]


def get_closest_point(x_robot, y_robot, alpha, local_map):
    # y_robot_reflection = local_map.get_coord_in_reflected_array(y_robot)
    y_robot_in_real_world = local_map.get_coord_in_real_world(y_robot)
    k_robot, b_robot = get_line_coefficients(alpha=alpha, x=x_robot, y=y_robot_in_real_world)
    limit_x, limit_y = local_map.get_limits_for_finding_obstacle_in_array(alpha, x_robot, y_robot_in_real_world)
    limit_x_real, limit_y_real = local_map.get_limits_for_finding_obstacle_in_real_world(alpha, x_robot,
                                                                                         y_robot_in_real_world)

    walls = local_map.get_walls_in_real_world(int(x_robot), int(y_robot_in_real_world))
    points = {}
    crossing_points = []

    for j in range(*limit_y):
        for i in range(*limit_x):
            # if i == int(x_robot) and j == int(y_robot_in_real_world):
            #     continue
            if local_map.is_cell_occupied_in_real_world(i, j):
                coordinates = local_map.get_obstacle_boundaries_in_real_world(i, j)
                cr_points = get_crossing_points(k_robot, b_robot, coordinates, x_robot, y_robot_in_real_world)
                if cr_points:
                    crossing_points.extend(cr_points)

            else:
                # wall = wall or local_map.check_wall(i, j)  # FIXME
                if local_map.check_wall(i, j):
                    walls += local_map.get_walls_in_real_world(i, j)
    if walls:
        walls += local_map.get_walls_in_real_world(int(x_robot), int(y_robot_in_real_world))  # FIXME
        cr_points = get_crossing_points(k_robot, b_robot, walls, x_robot, y_robot_in_real_world)
        if cr_points:
            crossing_points.extend(cr_points)

    for crossing_point in crossing_points:
        len_cross, x_cross, y_cross = crossing_point
        if is_point_belongs_area(x_cross, y_cross, limit_x_real, limit_y_real):
            points.update({len_cross: (x_cross, y_cross)})

    closest_point = min(points.keys()) # FIXME
    x_result, y_result = points[closest_point]
    y_result = local_map.get_coord_in_real_world(y_result)
    return x_result, y_result


def get_crossing_points(k_robot, b_robot, coordinates, x_robot, y_robot):  # FIXME
    a1, b1, c1 = get_matrix_coefficients_for_line(b_robot, k_robot)
    result = []
    for coordinate in coordinates:
        k_segment, b_segment = get_line_coefficients(coordinates=coordinate)
        a2, b2, c2 = get_matrix_coefficients_for_line(b_segment, k_segment)
        x_cross, y_cross = cross(a1, b1, c1, a2, b2, c2)
        if x_cross is not None and is_point_belongs_segment(x_cross, y_cross, coordinate):
            length = euclidean_distance(x_robot, x_cross, y_robot, y_cross)
            result.append((length, x_cross, y_cross))
    return result

    # min_len = None
    # min_x, min_y = None, None
    #     if x_cross is not None:
    #         x_cross, y_cross = round(x_cross, 1), round(y_cross, 1)
    #         if is_point_belongs_segment(x_cross, y_cross, coordinate):
    #             length = euclidean_distance(x_robot, x_cross, y_robot, y_cross)
    #             if not min_len or length < min_len:
    #                 min_len = length
    #                 min_x, min_y = x_cross, y_cross
    # if min_len is not None:
    #     return (min_len, min_x, min_y)


def get_cell_fragments_coordinates(cell_size, i, j):
    coordinates = [(i, j, i + cell_size, j),
                   (i + cell_size, j, i + cell_size, j + cell_size),
                   (i + cell_size, j + cell_size, i, j + cell_size),
                   (i, j, i, j + cell_size)]
    return coordinates


def generate(x_robot, y_robot, local_map, alpha_diff=90, cell_size=1):
    scan = {}
    for alpha in range(0, 360, alpha_diff):
        if not alpha % 90:

            _, x_array, y_array = get_params_occupied_cell(int(x_robot), int(y_robot), alpha, local_map.array)
            k_robot, b_robot = get_line_coefficients(alpha=alpha, x=x_robot, y=y_robot)
            coordinates = get_cell_fragments_coordinates(cell_size, x_array, y_array)
            crossing_points = get_crossing_points(k_robot, b_robot, coordinates, x_robot, y_robot)

            closest_point = min(crossing_points, key=lambda x: x[0])  # FIXME
            scan.update({alpha: closest_point[1:]})
        else:
            try:
                x_array, y_array = get_closest_point(x_robot, y_robot, alpha, local_map)
                scan.update({alpha: (x_array, y_array)})
                # print(scan)
            except Exception as e:
                print('Failed! Угол:', alpha, '\nx:', x_robot, 'y:', y_robot)
                print(e)
    return scan


