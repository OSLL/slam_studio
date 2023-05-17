import numpy as np


def get_simple_map():
    return np.asarray([
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1]])


def generate_sparse_matrix(size, density=0.1):
    matrix = np.random.choice([0, 1], size=(size, size), p=[1 - density, density])
    return matrix


class Map:
    def __init__(self, debug=False, size=7, density=0.1, cell_size=1):
        if debug:
            self.array = get_simple_map()
        else:
            self.array = generate_sparse_matrix(size, density)
        self.cell_size = cell_size

    def __len__(self):
        return self.array.__len__()

    def get_random_zero_coordinates(self):
        zero_indices = np.argwhere(self.array == 0)
        random_index = np.random.randint(zero_indices.shape[0])
        x, y = zero_indices[random_index]
        return y + self.cell_size / 2, x + self.cell_size / 2

    def check_wall(self, x, y):
        return 0 == x or x == len(self) - 1 or 0 == y or y == len(self) - 1

    def get_coord_in_real_world(self, y):
        return len(self) - y

    def get_coord_in_reflected_array(self, y):
        return len(self) - y - 1

    def is_cell_occupied_in_real_world(self, x, y):
        return self.array[len(self) - y - 1, x] == 1

    def get_walls_in_real_world(self, x, y):
        walls = []
        if self.check_wall(x, y):
            if y == 0:
                walls.append((x, y, x + self.cell_size, y))
            if y == len(self) - 1:
                walls.append((x, y+1, x + self.cell_size, y+1))
            if x == 0:
                walls.append((x, y, x, y + self.cell_size))
            if  x == len(self) - 1:
                walls.append((x+1, y, x+1, y + self.cell_size))
        return walls

    def get_obstacle_boundaries_in_real_world(self, x, y):
        return [(x, y, x + 1, y), (x + 1, y, x + 1, y + 1),
                (x, y, x, y + 1), (x, y + 1, x + 1, y + 1)]

    def get_limits_for_finding_obstacle_in_array(self, alpha, x, y):
        if alpha < 90:
            limit_x, limit_y = (0, int(x)+1), (0, int(y)+1)
        elif alpha < 180:
            limit_x, limit_y = (0, int(x)+1), (int(y), len(self.array))
        elif alpha < 270:
            limit_x, limit_y = (int(x), len(self.array)), (int(y), len(self.array))
        else:
            limit_x, limit_y = (int(x), len(self.array)), (0, int(y) + 1)
        return limit_x, limit_y

    def get_limits_for_finding_obstacle_in_real_world(self, alpha, x, y):
        if alpha < 90:
            limit_x, limit_y = (0, x), (0, y)
        elif alpha < 180:
            limit_x, limit_y = (0, x), (y, len(self.array))
        elif alpha < 270:
            limit_x, limit_y = (x, len(self.array)), (y, len(self.array))
        else:
            limit_x, limit_y = (x, len(self.array)), (0, y)
        return limit_x, limit_y

    def get_free_positions(self):
        positions = []
        for j, row in enumerate(self.array):
            for i, value in enumerate(row):
                if value != 1:
                    positions.append((i + 0.5 * self.cell_size, j + 0.5 * self.cell_size, 0))
        return positions



