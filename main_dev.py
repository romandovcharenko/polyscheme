import pygame
from copy import deepcopy
import numpy as np
#import numba
#from numba import njit

color = 1
tile = 15
fps = 0

black = "#000000"
gray  = "#333333"
white = "#ffffff"
blue  = "#4466ff"
red   = "#ff44aa"
green = "#337755"
yellow= "#ffbb44"
brown = "#aa9944"

res = width, height = 900, 900
w, h = width // tile, height // tile
pygame.init()
surface = pygame.display.set_mode(res)
w, h = 60, 60
clock = pygame.time.Clock()
next_field = np.zeros((w, h))
current_field = np.zeros((w, h))
next_field_b = np.zeros((w, h))
current_field_b = np.zeros((w, h))
extra_x, extra_y = 0, 0
start = False
back_side = False

#@njit(fastmath=True)
def check_cell(current_field, current_field_b, x, y):
    count = 0
    is_wired = False
    count_c1, count_c2 = 0, 0
    if current_field[y, x] == 2: return 3
    elif current_field[y, x] == 3: return 1
    elif current_field[y, x] == 1:
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j, i] == 2: count += 1
                if current_field[j, i] == 4: is_wired = True
        if(count == 1 or count == 2 or is_wired): return 2
        return 1
    elif current_field[y, x] == 4: return 4
    elif current_field[y, x] == 5:
        for c in range(1, 4):
            if(current_field[y-1, x-c] == 3 or current_field[y-1, x-c] == 2): count_c1 = 1
            if(current_field[y+1, x-c] == 3 or current_field[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 == 2):
            if(current_field[y, x+2] != 0 or current_field[y, x+1] != 4): current_field[y, x+2] = 2
        return 5
    elif current_field[y, x] == 6:
        for c in range(1, 4):
            if(current_field[y-1, x-c] == 3 or current_field[y-1, x-c] == 2): count_c1 = 1
            if(current_field[y+1, x-c] == 3 or current_field[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 >= 1):
            if(current_field[y, x+2] != 0 or current_field[y, x+1] != 4): current_field[y, x+2] = 2
        return 6
    elif current_field[y, x] == 6:
        for c in range(1, 4):
            if(current_field[y-1, x-c] == 3 or current_field[y-1, x-c] == 2): count_c1 = 1
            if(current_field[y+1, x-c] == 3 or current_field[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 >= 1):
            if(current_field[y, x+2] != 0 or current_field[y, x+1] != 4): current_field[y, x+2] = 2
        return 6
    elif current_field[y, x] == 7:
        for c in range(1, 4):
            if(current_field[y-1, x-c] == 3 or current_field[y-1, x-c] == 2): count_c1 = 1
            if(current_field[y+1, x-c] == 3 or current_field[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 == 1):
            if(current_field[y, x+2] != 0 or current_field[y, x+1] != 4): current_field[y, x+2] = 2
        return 7
    elif current_field[y, x] == 9:
        for c in range(1, 4):
            if(current_field[y, x-c] == 3 or current_field[y, x-c] == 3): count_c1 = 1
        if(count_c1 == 0):
            if(current_field[y, x+2] != 0 or current_field[y, x+1] != 4): current_field[y, x+2] = 2
        return 9
    if current_field[y, x] == 8:
        global next_field
        if(current_field_b[y, x] == 8):
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field_b[j, i] == 2:
                        for k in range(y - 1, y + 2):
                            for c in range(x - 1, x + 2):
                                if(current_field[k, c] == 1):
                                    next_field[k, c] = 2
                                    current_field[k, c] = 2
        return 8

#@njit(fastmath=True)
def check_cell_b(current_field_b, current_field, x, y):
    count = 0
    is_wired = False
    count_c1, count_c2 = 0, 0
    if current_field_b[y, x] == 2: return 3
    elif current_field_b[y, x] == 3: return 1
    elif current_field_b[y, x] == 1:
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field_b[j, i] == 2: count += 1
                if current_field_b[j, i] == 4: is_wired = True
        if(count == 1 or count == 2 or is_wired): return 2
        return 1
    elif current_field_b[y, x] == 4: return 4
    elif current_field_b[y, x] == 5:
        for c in range(1, 4):
            if(current_field_b[y-1, x-c] == 3 or current_field_b[y-1, x-c] == 2): count_c1 = 1
            if(current_field_b[y+1, x-c] == 3 or current_field_b[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 == 2):
            if(current_field_b[y, x+2] != 0 or current_field_b[y, x+1] != 4): current_field_b[y, x+2] = 2
        return 5
    elif current_field_b[y, x] == 6:
        for c in range(1, 4):
            if(current_field_b[y-1, x-c] == 3 or current_field_b[y-1, x-c] == 2): count_c1 = 1
            if(current_field_b[y+1, x-c] == 3 or current_field_b[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 >= 1):
            if(current_field_b[y, x+2] != 0 or current_field_b[y, x+1] != 4): current_field_b[y, x+2] = 2
        return 6
    elif current_field_b[y, x] == 6:
        for c in range(1, 4):
            if(current_field_b[y-1, x-c] == 3 or current_field_b[y-1, x-c] == 2): count_c1 = 1
            if(current_field_b[y+1, x-c] == 3 or current_field_b[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 >= 1):
            if(current_field_b[y, x+2] != 0 or current_field_b[y, x+1] != 4): current_field_b[y, x+2] = 2
        return 6
    elif current_field_b[y, x] == 7:
        for c in range(1, 4):
            if(current_field_b[y-1, x-c] == 3 or current_field_b[y-1, x-c] == 2): count_c1 = 1
            if(current_field_b[y+1, x-c] == 3 or current_field_b[y+1, x-c] == 2): count_c2 = 1
        if(count_c1 + count_c2 == 1):
            if(current_field_b[y, x+2] != 0 or current_field_b[y, x+1] != 4): current_field_b[y, x+2] = 2
        return 7
    elif current_field_b[y, x] == 9:
        for c in range(1, 4):
            if(current_field_b[y, x-c] == 3 or current_field_b[y, x-c] == 2): count_c1 = 1
        if(count_c1 == 0):
            if(current_field_b[y, x+2] != 0 or current_field_b[y, x+1] != 4): current_field_b[y, x+2] = 2
        return 9
    elif current_field_b[y, x] == 8:
        global next_field_b
        if(current_field[y, x] == 8):
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j, i] == 2:
                        for k in range(y - 1, y + 2):
                            for c in range(x - 1, x + 2):
                                if(current_field_b[k, c] == 1):
                                    next_field_b[k, c] = 2
                                    current_field_b[k, c] = 2
        return 8

def draw_cells():
    for x in range(1, w-1):
        for y in range(1, h-1):
            if current_field[y, x] == 1:
                if not(back_side): pygame.draw.rect(surface, white, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 2:
                if not(back_side): pygame.draw.rect(surface, blue, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 3:
                if not(back_side): pygame.draw.rect(surface, red, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 4:
                if not(back_side): pygame.draw.rect(surface, black, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 5:
                if not(back_side): pygame.draw.rect(surface, blue, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 6:
                if not(back_side): pygame.draw.rect(surface, yellow, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 7:
                if not(back_side): pygame.draw.rect(surface, black, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 9:
                if not(back_side): pygame.draw.rect(surface, red, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if not(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)
            elif current_field[y, x] == 8:
                if not(back_side): pygame.draw.rect(surface, yellow, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field[y, x] = check_cell(current_field, current_field_b, x, y)

def draw_cells_b():
    for x in range(1, w-1):
        for y in range(1, h-1):
            if current_field_b[y, x] == 1:
                if(back_side): pygame.draw.rect(surface, white, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 2:
                if(back_side): pygame.draw.rect(surface, blue, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 3:
                if(back_side): pygame.draw.rect(surface, red, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 4:
                if(back_side): pygame.draw.rect(surface, black, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 5:
                if(back_side): pygame.draw.rect(surface, blue, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 6:
                if(back_side): pygame.draw.rect(surface, yellow, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 7:
                if(back_side): pygame.draw.rect(surface, black, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y-1)*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x)*tile+extra_x, (y+1)*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 9:
                if(back_side): pygame.draw.rect(surface, red, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(back_side): pygame.draw.rect(surface, yellow, ((x+1)*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)
            elif current_field_b[y, x] == 8:
                if(back_side): pygame.draw.rect(surface, yellow, (x*tile+extra_x, y*tile+extra_y, tile, tile))
                if(start): next_field_b[y, x] = check_cell_b(current_field_b, current_field, x, y)

def draw_grid():
    for x in range(w):
        for y in range(h):
            c_c = ((x*tile)+extra_x+tile//2), ((y*tile)+extra_y+tile//2)
            if(c_c[0] > 0 and c_c[1] > 0):
                pygame.draw.circle(surface, white, c_c, tile//15)

while True:
    surface.fill(gray)
    mouse_click = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = mouse_pos[0] - extra_x, mouse_pos[1] - extra_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(start): start=False
                else: start=True
            elif event.key == pygame.K_g and start == False:
                for j in range(w):
                    for i in range(h):
                        if (current_field[i, j] == 2 or current_field[i,j] == 3): current_field[i, j] = 1
                        if (current_field_b[i, j] == 2 or current_field_b[i,j] == 3): current_field_b[i, j] = 1
            elif event.key == pygame.K_b:
                if(back_side): back_side = False
                else: back_side = True
            elif event.key == pygame.K_UP: extra_y += 50
            elif event.key == pygame.K_DOWN: extra_y -= 50
            elif event.key == pygame.K_RIGHT: extra_x -= 50
            elif event.key == pygame.K_LEFT: extra_x += 50
            elif event.key == pygame.K_1: color = 4
            elif event.key == pygame.K_2: color = 1
            elif event.key == pygame.K_3: color = 5
            elif event.key == pygame.K_4: color = 6
            elif event.key == pygame.K_5: color = 7
            elif event.key == pygame.K_6: color = 8
            elif event.key == pygame.K_7: color = 9
            elif event.key == pygame.K_o:
                op_cell_m, op_cell_m_b = [], []
                f_to_s = open("save.txt", "r")
                read_c = f_to_s.readlines()
                for str_f in read_c:
                    index_map = (read_c.index(str_f))
                    str_f = str_f[2:]
                    str_f = str_f[:-3]
                    str_f = (list(map(str, str_f.split("], ["))))
                    for elem in str_f:
                        if(index_map == 0):
                            op_cell_m.append(list(map(int, elem.split(", "))))
                        else:
                            op_cell_m_b.append(list(map(int, elem.split(", "))))
                current_field = np.array(op_cell_m)
                current_field_b = np.array(op_cell_m_b)
                next_field = np.array(op_cell_m)
                next_field_b = np.array(op_cell_m_b)

    if(back_side): pygame.draw.rect(surface, brown, (extra_x, extra_y, w*tile, h*tile))
    else: pygame.draw.rect(surface, green, (extra_x, extra_y, w*tile, h*tile))
    pygame.draw.rect(surface, white, (extra_x, extra_y, w*tile, h*tile), 2)
    draw_grid()
    draw_cells_b()
    draw_cells()

    if(start):
        current_field = deepcopy(next_field)
        current_field_b = deepcopy(next_field_b)
    if(mouse_pos[0] < w*tile+extra_x and mouse_pos[1] < h*tile+extra_y and mouse_pos[0] > 0 and mouse_pos[1] > 0):
        if(back_side):
            if(mouse_pos[0] < width and mouse_pos[1] < height):
                if(mouse_click[0]): current_field_b[mouse_pos[1]//tile, mouse_pos[0]//tile] = color
                if(mouse_click[2]):
                    current_field_b[mouse_pos[1]//tile, mouse_pos[0]//tile] = 0
                    next_field_b[mouse_pos[1]//tile, mouse_pos[0]//tile] = 0
        else:
            if(mouse_pos[0] < width and mouse_pos[1] < height):
                if(mouse_click[0]): current_field[mouse_pos[1]//tile, mouse_pos[0]//tile] = color
                if(mouse_click[2]):
                    current_field[mouse_pos[1]//tile, mouse_pos[0]//tile] = 0
                    next_field[mouse_pos[1]//tile, mouse_pos[0]//tile] = 0

    pygame.display.set_caption(str(round(clock.get_fps()))+", start="+str(start)+", back="+str(back_side))
    pygame.display.update()
    clock.tick(fps)
