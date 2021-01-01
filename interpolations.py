def linear_interpolation(p, p1, p2):
    p[1] = p1[1] + (((p[0] - p1[0]) * (p2[1] - p1[1])) / (p2[0] - p1[0]))
    return p

#print(linear_interpolation([2,0], [3,5], [6,8]))

def quadratic_interpolation(p, p0, p1, p2):
    a = ((p[0] - p1[0]) * (p[0] - p2[0])) / ((p0[0] - p1[0]) * (p0[0] - p2[0])) * p0[1]
    b = ((p[0] - p0[0]) * (p[0] - p2[0])) / ((p1[0] - p0[0]) * (p1[0] - p2[0])) * p1[1]
    c = ((p[0] - p0[0]) * (p[0] - p1[0])) / ((p2[0] - p0[0]) * (p2[0] - p1[0])) * p2[1]
    p[1] = a + b + c
    return p

#print(quadratic_interpolation( [2,0], [4,5], [19, 2], [14,9] ))