from display import *
from draw import *

screen = new_screen()

# TESTING

# white = [255, 255, 255]
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]

# testing draw_line
# draw_line(0, 0, 500, 500, screen, white)
# draw_line(100, 0, 100, 500, screen, red)
# draw_line(0, 100, 500, 100, screen, green)
# draw_line(0, 500, 100, 100, screen, blue)
# draw_line(500, 0, 0, 300, screen, white)
# draw_line(500, 0, 0, 100, screen, red)
# draw_line(500, 500, 0, 300, screen, green)
# draw_line(500, 500, 0, 100, screen, blue)

# testing draw_function
# draw_function(0, 1, -100, screen, white)
# raw_function(1, 0, -350, screen, white)
# draw_function(5, 2, -1500, screen, white)

# testing draw_theta
# draw_theta(2*math.pi, screen, white)
# draw_theta(math.pi, screen, white)
# draw_theta(math.pi/3, screen, white)
# draw_theta(-math.pi/3, screen, white)

for i in range(1, 256):
    d = 2 * math.pi * i / 256
    c = [i, (85 + i) % 256, (170 + i) % 256]
    draw_theta(d, screen, c)

display(screen)
save_extension(screen, 'img.png')
