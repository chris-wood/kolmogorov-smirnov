import math
import random

def generate_points(N, M):
    x_coords = [random.randint(0, M) for i in range(N)]
    y_coords = [random.randint(0, M) for i in range(N)]
    return [(x, y) for (x, y) in zip(x_coords, y_coords)]

def distance(p1, p2):
    x_delta_sqr = (p2[0] - p1[0]) ** 2
    y_delta_sqr = (p2[1] - p1[1]) ** 2
    return math.sqrt(x_delta_sqr + y_delta_sqr)

def find_pair_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j and points[i] != points[j]:
                d = distance(points[i], points[j])
                distances.append(d)
    return distances

def minimum_distance(N, M):
    points = generate_points(N, M)
    distances = find_pair_distances(points)
    return min(distances)

def minimum_distance_test(T = 10, N = 800, M = 1000):
    min_distances = [minimum_distance(N, M) for t in range(T)]
    return min_distances

min_distances = minimum_distance_test()
min_distances.sort()

from kolmogorov import *

# mean = \lambda^{-1} for the exponential distribution
F0 = generate_exponential_sample(min_distances, 0.995 ** -1) 
Fk = calc_empirical_distribution(min_distances)

print kolmogorov_smirnov_test(F0, Fk, 0.05)
