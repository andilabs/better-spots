from geopy.distance import vincenty


def get_distance_between_points(point_a, point_b):
    return round(vincenty(point_a, point_b).kilometers, 1)
