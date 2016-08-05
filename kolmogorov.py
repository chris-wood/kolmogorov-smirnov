import math

def calc_empirical_distribution(Xs):
    Fx = []
    total = float(len(Xs))
    for x in Xs:
        subset = filter(lambda y : y <= x, Xs)
        count = len(subset)
        Fx.append((x, float(count) / total))
    return Fx

def distribution_supremum(F0, Fk):
    delta = map(lambda ((x1, y1), (x2, y2)) : abs(y2 - y1), zip(F0, Fk))
    support = filter(lambda x : x > 0.0, delta)
    return max(support)

def kolmogorov_smirnov_statistic(F0, Fk):
    '''
    Compute the statistic according to:
      https://onlinecourses.science.psu.edu/stat414/node/322
    '''
    return distribution_supremum(F0, Fk)

_kolmogorov_smirnov_table = {
        (1, 0.2) : 0.900,
        (2, 0.2) : 0.684,
        (3, 0.2) : 0.565,
        (4, 0.2) : 0.494,
        # ...
        (10, 0.05) : 0.410,
        # ...
        (100, 0.05) : (1.36 / math.sqrt(100))
        # ...
}

def kolmogorov_smirnov_test(F0, Fk, alpha):
    n = len(Fk)
    statistic = kolmogorov_smirnov_statistic(F0, Fk)
    threshold = _kolmogorov_smirnov_table[(n, alpha)]
    if statistic > threshold:
        return False
    return True

def generate_uniform_sample(Xs, low, high):
    F0 = []
    for x in Xs:
        if x < low:
            F0.append((x, 0.0))
        elif x > high:
            F0.append((x, 1.0))
        else:
            F0.append((x, float(x) / float(low + high)))
    return F0

def exponential_cdf(l, x):
    return 1 - math.exp(-1 * l * x)

def generate_exponential_sample(Xs, l):
    F0 = []
    for x in Xs:
        F0.append((x, exponential_cdf(l, x)))
    return F0
