import math
from display import *

size = 500
radius = 100
xc = 250
yc = 250


def dont(x, y):
    if x < 0 or size < x:
        return 1
    if y < 0 or size < y:
        return 1
    return 0


def draw_line(x0, y0, x1, y1, screen, color):
    # setup
    if x1 > x0:
        s0 = x0
        t0 = y0
        s1 = x1
        t1 = y1
    # 3rd, 4th, 5th, 6th octants
    else:
        s0 = x1
        t0 = y1
        s1 = x0
        t1 = y0
    x = s0
    y = t0
    A = (t1 - t0)
    B = -(s1 - s0)
    # 0 <= -B always true
    # 1st octant
    if 0 <= A and A <= -B:
        d = 2 * A + B
        while x <= s1:
            if dont(x, y) == 0:
                plot(screen, color, x, y)
            x += 1
            d += 2 * A
            if d >= 0:
                y += 1
                d += 2 * B
    # 2nd octant
    elif 0 <= A and -B <= A:
        d = A + 2 * B
        while y <= t1:
            if dont(x, y) == 0:
                plot(screen, color, x, y)
            y += 1
            d += 2 * B
            if d <= 0:
                x += 1
                d += 2 * A
    # 7th octant
    elif A <= 0 and A <= B:
        d = A + -2 * B
        while y >= t1:
            if dont(x, y) == 0:
                plot(screen, color, x, y)
            y += -1
            d += -2 * B
            if d >= 0:
                x += 1
                d += 2 * A
    # 8th octant
    elif A <= 0 and B <= A:
        d = 2 * A + -B
        while x <= s1:
            if dont(x, y) == 0:
                plot(screen, color, x, y)
            x += 1
            d += 2 * A
            if d <= 0:
                y += -1
                d += -2 * B
    else:
        print("invalid\n")


def draw_function(A, B, C, screen, color):
    if A == 0 and B == 0:
        print("no line\n")
        return
    if A == 0:
        b = int(-C / B)
        draw_line(0, b, size, b, screen, color)
        return
    if B == 0:
        b = int(-C / A)
        draw_line(b, 0, b, size, screen, color)
        return
    # normal line
    m = -A / B
    b = int(-C / B)
    x0 = 0
    y0 = b
    x1 = size
    y1 = int(size * (-A / B) + (-C / B))
    draw_line(x0, y0, x1, y1, screen, color)


def draw_theta(d, screen, color):
    if d == math.pi:
        draw_function(1, 0, -(xc - radius), screen, color)
        return
    if d == 2 * math.pi:
        draw_function(1, 0, -(xc + radius), screen, color)
        return
    A = radius * math.cos(d)
    B = radius * math.sin(d)
    C = -A * (xc + A) - B * (yc + B)
    draw_function(A, B, C, screen, color)
