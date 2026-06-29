import pygame as pgm
pgm.init()

COLOR_INACTIVE = pgm.Color('gray')
COLOR_ACTIVE = pgm.Color('white')
font = pgm.font.Font("font.ttf", 24)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pgm.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pgm.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pgm.KEYDOWN:
            if self.active:
                if event.key == pgm.K_RETURN:
                    global drw_op_file_b, filename, cell_m, cell_m_b
                    filename = self.text
                    if(filename == "1"):
                        filename = "halfadder.txt"
                    elif(filename == "2"):
                        filename = "1bitadder.txt"
                    elif(filename == "3"):
                        filename = "4bitadder.txt"
                    elif(filename == "4"):
                        filename = "4bitadder_w_negation.txt"
                    elif(filename == "5"):
                        filename = "rs_trigger.txt"
                    elif(filename == "6"):
                        filename = "d_trigger.txt"
                    elif(filename == "7"):
                        filename = "d_trigger_dynamic.txt"
                    elif(filename == "8"):
                        filename = "1bitadder.txt"
                    elif(filename == "9"):
                        filename = "4bitadder.txt"
                    elif(filename == "10"):
                        filename = "alu.txt"
                    self.text = ''
                    try:
                        op_cell_m, op_cell_m_b = [], []
                        f_to_s = open(filename, "r")
                        read_c = f_to_s.readlines()
                        for str_f in read_c:
                            index_map = (read_c.index(str_f))
                            str_f = str_f[2:]
                            str_f = str_f[:-3]
                            str_f = (list(map(str, str_f.split("], ["))))
                            for elem in str_f:
                                if(index_map == 0):
                                    op_cell_m.append(list(map(int,
                                                          elem.split(", "))))
                                else:
                                    op_cell_m_b.append(list(map(int,
                                                            elem.split(", "))))
                        cell_m = op_cell_m
                        cell_m_b = op_cell_m_b
                        self.active = False
                        drw_op_file_b = False
                    except:
                        self.active = False
                        drw_op_file_b = False
                elif event.key == pgm.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self, sc):
        sc.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pgm.draw.rect(sc, self.color, self.rect, 2)

def drw_op_file():
    pgm.draw.rect(sc, gray_c, (0, 0, win_w, dis_h))
    for box in input_boxes:
        box.update()
    for box in input_boxes:
        box.draw(sc)
def drw_wms(txt):
    txt_w, txt_h = font.size(txt)
    pgm.draw.rect(sc, white_c, (ms_x, ms_y-txt_h-5, txt_w+10, txt_h))
    pgm.draw.rect(sc, black_c, (ms_x, ms_y-txt_h-5, txt_w+10, txt_h), 1)
    draw_text(black_c, txt, (ms_x+5, ms_y-txt_h-5), 24)
def drw_button(c, txt_w, txt_h, h_pos, num, v, color_pen):
    butstpos = txt_w+20+num*(txt_h+15)
    pgm.draw.rect(sc, c, (butstpos, h_pos-5, txt_h+10, txt_h+10))
    if(v == 1):
        pgm.draw.rect(sc, blue_c, (butstpos+5, h_pos, txt_h//2, txt_h))
        pgm.draw.circle(sc,blue_c,(butstpos+5+txt_h//2,h_pos+txt_h//2),txt_h//2)
    elif(v == 2):
        pgm.draw.rect(sc, yellow_c, (butstpos+5, h_pos, txt_h//2, txt_h))
        yl_c = yellow_c
        pgm.draw.circle(sc,yl_c,(butstpos+5+txt_h//2,h_pos+txt_h//2),txt_h//2)
        pgm.draw.circle(sc,c,(butstpos+5,h_pos+txt_h//2),txt_h//2)
    elif(v == 3):
        pgm.draw.rect(sc,gray_c, (butstpos+5, h_pos, txt_h//2, txt_h))
        pgm.draw.circle(sc,gray_c,(butstpos+5+txt_h//2,h_pos+txt_h//2),txt_h//2)
        pgm.draw.circle(sc,c,(butstpos+7,h_pos+txt_h//2),txt_h//2)
        pgm.draw.circle(sc,gray_c,(butstpos+5-1,h_pos+txt_h//2),txt_h//2-1)
        pgm.draw.circle(sc,c,(butstpos+5-4,h_pos+txt_h//2),txt_h//2)
    elif(v == 4):
        pgm.draw.polygon(sc,red_c,((butstpos+5,h_pos),
                         (butstpos+5+txt_h-2,h_pos+txt_h//2),
                         (butstpos+5, h_pos+txt_h)))
        pgm.draw.circle(sc,red_c,(butstpos+5+txt_h-3,h_pos+txt_h//2),4)
    if(color_pen == 1 and num == 0):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 4 and num == 1):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 5 and num == 2):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 6 and num == 3):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 7 and num == 4):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 9 and num == 5):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 8 and num == 6):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    elif(color_pen == 10 and num == 7):
        pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
        pgm.draw.rect(sc, black_c, (butstpos-2, h_pos-7, txt_h+14, txt_h+14), 1)
    else: pgm.draw.rect(sc, black_c, (butstpos, h_pos-5, txt_h+10, txt_h+10), 1)
    global mss_b, start_ticks, mss_b2, mss_b3, seconds, ms_num
    if(ms_x > butstpos and ms_y > h_pos-5 and
       ms_x < txt_h+10+butstpos and ms_y < txt_h+10+h_pos-5):
        if(mss_b == False and mss_b2 == False): mss_b = True
        if(mss_b3 == True):
            seconds=(pgm.time.get_ticks()-start_ticks)/1000
        else:
            mss_b3 = True
            seconds = 0
        ms_num = num+1
        if(pgm.mouse.get_pressed()[0]):
            if(num == 0): color_pen = 1
            elif(num == 1): color_pen = 4
            elif(num == 2): color_pen = 5
            elif(num == 3): color_pen = 6
            elif(num == 4): color_pen = 7
            elif(num == 5): color_pen = 9
            elif(num == 6): color_pen = 8
            elif(num == 7): color_pen = 10
    if(num == 7): return color_pen, butstpos+txt_h+10, seconds
    else: return color_pen, seconds
def drw_bar(color_pen):
    global drw_dox_b
    if(st_game_b): txt = "Stop"
    else: txt = u"Start"
    txt_w, txt_h = font.size(txt)
    h_pos = dis_h+((bar_s//2)-(txt_h//2))
    pgm.draw.rect(sc, white_c, (0, dis_h, win_w, bar_s))
    pgm.draw.rect(sc, black_c, (5, h_pos-5, txt_w+10, txt_h+10), 1)
    sb_p1, sb_p2, sb_p3, sb_p4 = 5, h_pos-5, txt_w+15, txt_h+h_pos+5
    draw_text(black_c, txt, (10, h_pos), 24)
    color_pen,s = drw_button(white_c, txt_w, txt_h, h_pos, 4, 3, color_pen)
    color_pen,s = drw_button(white_c, txt_w, txt_h, h_pos, 3, 2, color_pen)
    color_pen,s = drw_button(white_c, txt_w, txt_h, h_pos, 2, 1, color_pen)
    color_pen,s = drw_button(gray_c, txt_w, txt_h, h_pos, 1, None, color_pen)
    color_pen,s = drw_button(white_c, txt_w, txt_h, h_pos, 0, None, color_pen)
    color_pen,s = drw_button(white_c, txt_w, txt_h, h_pos, 5, 4, color_pen)
    color_pen,s = drw_button(yellow_c, txt_w, txt_h, h_pos, 6, None, color_pen)
    color_pen,bts,s=drw_button(violet_c,txt_w,txt_h,h_pos,7,None,color_pen)
    txt = "Help"
    txt_w, txt_h = font.size(txt)
    if(bts < win_w-txt_w-15):
        pgm.draw.rect(sc,black_c,(win_w-txt_w-15,h_pos-5,txt_w+10,txt_h+10),1)
        draw_text(black_c, txt, (win_w-txt_w-10, h_pos), 24)
        if(pgm.mouse.get_pressed()[0] and drw_op_file_b == False):
            if(ms_x > win_w-txt_w-15 and ms_x < win_w-txt_w-15+txt_w+10 and 
               ms_y > h_pos-5 and ms_y < h_pos-5+txt_h+10):
                drw_dox_b = True
    else:
        pgm.draw.rect(sc,black_c,(bts+5,h_pos-5,txt_w+10,txt_h+10),1)
        draw_text(black_c, txt, (bts+10, h_pos), 24)
    if(s > 0.5):
        if(ms_num == 1): drw_wms("Conductor")
        elif(ms_num == 2): drw_wms("Electron generator")
        elif(ms_num == 3): drw_wms("AND logic gate")
        elif(ms_num == 4): drw_wms("OR logic gate")
        elif(ms_num == 5): drw_wms("XOR logic gate")
        elif(ms_num == 6): drw_wms("Inverter")
        elif(ms_num == 7): drw_wms("Transfer the signal")
        elif(ms_num == 8): drw_wms("Display")
    return sb_p1, sb_p2, sb_p3, sb_p4, color_pen
def draw_num(x, y, numpos, num):
    numpos = numpos * 5
    if(num == 2 or num == 3 or num == 5 or num == 6 or num == 7 or num == 8 or
       num == 9 or num == 0):
        rect=((x+2+numpos)*cell_s+e_x,(y+2)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+3+numpos)*cell_s+e_x,(y+2)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 1 or num ==  2 or num == 3 or num == 4 or num == 7 or num == 8 or
       num == 9 or num == 0):
        rect=((x+4+numpos)*cell_s+e_x,(y+3)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+4+numpos)*cell_s+e_x,(y+4)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 4 or num == 5 or num == 6 or num == 8 or num == 9 or num == 0):
        rect=((x+1+numpos)*cell_s+e_x,(y+3)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+1+numpos)*cell_s+e_x,(y+4)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 or
       num == 9):
        rect=((x+2+numpos)*cell_s+e_x,(y+5)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+3+numpos)*cell_s+e_x,(y+5)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 2 or num == 6 or num == 8 or num == 0):
        rect=((x+1+numpos)*cell_s+e_x,(y+6)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+1+numpos)*cell_s+e_x,(y+7)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 2 or num == 3 or num == 5 or num == 6 or num == 8 or num == 9 or
       num == 0):
        rect=((x+2+numpos)*cell_s+e_x,(y+8)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+3+numpos)*cell_s+e_x,(y+8)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
    if(num == 1 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or
       num == 8 or num == 9 or num == 0):
        rect=((x+4+numpos)*cell_s+e_x,(y+6)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
        rect=((x+4+numpos)*cell_s+e_x,(y+7)*cell_s+e_y,cell_s,cell_s)
        pgm.draw.rect(sc, violet_c, rect)
def drw_map(bin_num):
    m_wpx, m_hpx = m_w * cell_s, m_h * cell_s
    if(cell_m_side): pgm.draw.rect(sc, green_c, (e_x, e_y, m_wpx, m_hpx))
    else: pgm.draw.rect(sc, brown_c, (e_x, e_y, m_wpx, m_hpx))
    if not(chngm_b): pgm.draw.rect(sc, white_c, (e_x, e_y, m_wpx, m_hpx), 2)
    drw_grid()
    if(cell_m_side):
        for x in range(len(cell_m[0])):
            for y in range(len(cell_m)):
                if(x < (win_w-e_x)//cell_s+1 and y < (win_h-e_y)//cell_s+1 and
                   x > -e_x//cell_s-1 and y > -e_y//cell_s-1):
                    if(cell_m[y][x] == 1):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, white_c, rect)
                    elif(cell_m[y][x] == 2):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, pink_c, rect)
                    elif(cell_m[y][x] == 3):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, violet_c, rect)
                    elif(cell_m[y][x] == 4):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, gray_c, rect)
                        for_gen,tc,t2,t3=check_neighbors(y,x,cell_m,cell_m_b)
                        if(for_gen): txt = "1"
                        else: txt = "0"
                        font = pgm.font.Font("font.ttf", cell_s)
                        tw, th = font.size(txt)
                        rctg1 = rect[0] + ((cell_s//2)-(tw//2))
                        rctg2 = rect[1] + ((cell_s//2)-(th//2))
                        draw_text(white_c,txt,(rctg1,rctg2),cell_s)
                    elif(cell_m[y][x] == 5):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, blue_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x,y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x,y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m[y][x] == 6):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m[y][x] == 7):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, gray_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m[y][x] == 8):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m[y][x] == 9):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, red_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m[y][x] == 10):
                        rect=(x*cell_s+e_x,(y+1)*cell_s+e_y,cell_s*16,cell_s*9)
                        pgm.draw.rect(sc, white_c, rect)
                        dec_num = str(int(bin_num, 2))
                        try: 
                            for i in range(1, 4):
                                if(dec_num[-1*i]==str(0)): draw_num(x,y,3-i,0)
                                if(dec_num[-1*i]==str(1)): draw_num(x,y,3-i,1)
                                if(dec_num[-1*i]==str(2)): draw_num(x,y,3-i,2)
                                if(dec_num[-1*i]==str(3)): draw_num(x,y,3-i,3)
                                if(dec_num[-1*i]==str(4)): draw_num(x,y,3-i,4)
                                if(dec_num[-1*i]==str(5)): draw_num(x,y,3-i,5)
                                if(dec_num[-1*i]==str(6)): draw_num(x,y,3-i,6)
                                if(dec_num[-1*i]==str(7)): draw_num(x,y,3-i,7)
                                if(dec_num[-1*i]==str(8)): draw_num(x,y,3-i,8)
                                if(dec_num[-1*i]==str(9)): draw_num(x,y,3-i,9)
                        except: pass
                        rect=(x*cell_s+e_x,y*cell_s+e_y,cell_s,cell_s)
                        for k in range(0, 10, 9):
                            for i in range(0, 8, 2):
                                rectp1 = (x+k)*cell_s+e_x+cell_s*i
                                rect = (rectp1, rect[1], rect[2], rect[3])
                                pgm.draw.rect(sc, yellow_c, rect)
    else:
        for x in range(len(cell_m_b[0])):
            for y in range(len(cell_m_b)):
                if(x < (win_w-e_x)//cell_s+1 and y < (win_h-e_y)//cell_s+1 and
                   x > -e_x//cell_s-1 and y > -e_y//cell_s-1):
                    if(cell_m_b[y][x] == 1):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, white_c, rect)
                    elif(cell_m_b[y][x] == 2):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, pink_c, rect)
                    elif(cell_m_b[y][x] == 3):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, violet_c, rect)
                    elif(cell_m_b[y][x] == 4):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, gray_c, rect)
                    elif(cell_m_b[y][x] == 5):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, blue_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x,y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x,y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m_b[y][x] == 6):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m_b[y][x] == 7):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, gray_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y+cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                        rect=(x*cell_s+e_x, y*cell_s+e_y-cell_s, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m_b[y][x] == 8):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
                    elif(cell_m_b[y][x] == 9):
                        rect = (x*cell_s+e_x, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, red_c, rect)
                        rect=(x*cell_s+e_x+cell_s, y*cell_s+e_y, cell_s, cell_s)
                        pgm.draw.rect(sc, yellow_c, rect)
def ms_motion(b):
    if(mnpl_b_1 == False and mnpl_b == False):
        if(cell_m_side):
            if(b == 1 or b == 3):
                xy = ev.pos
                x, y = round(xy[0]-e_x)//cell_s, round(xy[1]-e_y)//cell_s
                if(x < m_w and y < m_h and y >= 0 and x >= 0):
                    try:
                        if(b == 1): cell_m[y][x] = color_pen
                        else: cell_m[y][x] = 0
                    except: pass
        else:
            if(b == 1 or b == 3):
                xy = ev.pos
                x, y = round(xy[0]-e_x)//cell_s, round(xy[1]-e_y)//cell_s
                if(x < m_w and y < m_h and y >= 0 and x >= 0):
                    if(b == 1): cell_m_b[y][x] = color_pen
                    else: cell_m_b[y][x] = 0
def drw_grid():
    for x in range(m_w):
        for y in range(m_h):
            c_c = ((x*cell_s)+e_x+cell_s//2, (y*cell_s)+e_y+cell_s//2)
            if(c_c[0] > 0 and c_c[1] > 0):
                pgm.draw.circle(sc, white_c, c_c, cell_s//15)
def chng_maps():
    ce_x, ce_y = (ms_x-e_x)//cell_s*cell_s, (ms_y-e_y)//cell_s*cell_s
    pgm.draw.rect(sc, white_c, (e_x, e_y, ce_x+cell_s, ce_y+cell_s), 1)
    return (ms_x-e_x)//cell_s, (ms_y-e_y)//cell_s
def drw_m_s():
    if(ns_w < 1 or ns_h < 1): txt = str(round(0))+"x"+str(round(0))
    else: txt = str(round(ns_w+1))+"x"+str(round(ns_h+1))
    txt_w, txt_h = font.size(txt)
    pgm.draw.rect(sc, white_c, (10, 10, txt_w+10, txt_h+10))
    draw_text(black_c, txt, (15, 15), 24)
def draw_text(c, txt, rect, size):
    font = pgm.font.Font("font.ttf", size)
    img = font.render(txt, True, c)
    sc.blit(img, rect)
def check_neighbors(i, j, cell_m2, cell_m_b2):
    neighbors_list=[[0,-1],[1,0],[0,1],[-1,0]]
    tail_count = 0
    tl2,tl3 = False, False
    for_gen = False
    for k in range(len(neighbors_list)):
        wan = neighbors_list[k][0]
        tu = neighbors_list[k][1]
        try:
            if(cell_m2[i+wan][j+tu] == 1 or
               cell_m2[i+wan][j+tu] == 2 or
               cell_m2[i+wan][j+tu] == 3): for_gen = True
            if(cell_m2[i+wan][j+tu] == 3): tail_count += 1
            if(cell_m2[i+wan][j+tu] == 4): tl2 = True
            if(cell_m2[i+wan][j+tu] == 3 or cell_m_b2[i+wan][j+tu] == 3):
                tl3 = True
        except: pass
    if(tail_count == 1 or tail_count == 2): return for_gen, True, tl2, tl3
    else: return for_gen, False, tl2, tl3
def v_ch(i, j, cell_m2):
    tail_count = 0
    v_and, v_or, v_xor, v_inv = False, False, False, False
    for k in range(1, 4):
        try:
            if(cell_m2[i-1][j-k] == 3): tail_count += 1
            if(cell_m2[i+1][j-k] == 3): tail_count += 1
            if(cell_m2[i][j-k] == 3): v_inv = True
        except: pass
    if(tail_count == 2): v_and = True
    else: v_and = False
    if(tail_count == 1): v_xor = True
    else: v_xor = False
    if(tail_count >= 1): v_or = True
    else: v_or = False
    return v_and, v_or, v_xor, v_inv
def st_game():
        cell_m2 = list(map(list, cell_m))
        cell_m_b2 = list(map(list, cell_m_b))
        for i in range(len(cell_m)):
            for j in range(len(cell_m[i])):
                if(cell_m2[i][j] == 2): cell_m[i][j] = 1
                if(cell_m2[i][j] == 3): cell_m[i][j] = 2
                fg,tail_count,tl2,tl3 = check_neighbors(i,j, cell_m2, cell_m_b2)
                if(cell_m2[i][j]==1 and tail_count):cell_m[i][j]=3
                if(cell_m2[i][j]==1 and tl2):cell_m[i][j]=3
                v_and, v_or, v_xor, v_inv = v_ch(i, j, cell_m2)
                if(cell_m2[i][j] == 5 and v_and): cell_m[i][j+2]=3
                if(cell_m2[i][j] == 6 and v_or): cell_m[i][j+2]=3
                if(cell_m2[i][j] == 7 and v_xor): cell_m[i][j+2]=3
                if(cell_m2[i][j] == 8 and tl3):
                    for k in range(len(neighbors_list)):
                        wan = neighbors_list[k][0]
                        tu = neighbors_list[k][1]
                        try:
                            if(cell_m2[i+wan][j+tu] == 1):
                                cell_m[i+wan][j+tu] = 3
                        except: pass
                if(cell_m2[i][j] == 9): 
                    if not(v_inv): cell_m[i][j+2]=3
                if(cell_m2[i][j] == 10): 
                    bin_num = "0"
                    try:
                        for c in range(0, 10, 9):
                            for k in range(0, 8, 2):
                                if(cell_m2[i-1][j+k+c] == 3): bin_num+="1"
                                elif(cell_m2[i-2][j+k+c] == 3): bin_num+="1"
                                elif(cell_m2[i-3][j+k+c] == 3): bin_num+="1"
                                else: bin_num+="0"
                    except: pass
        for i in range(len(cell_m_b)):
            for j in range(len(cell_m_b[i])):
                if(cell_m_b2[i][j] == 2): cell_m_b[i][j] = 1
                if(cell_m_b2[i][j] == 3): cell_m_b[i][j] = 2
                fg,tail_count,tl2,tl3 = check_neighbors(i,j, cell_m_b2, cell_m2)
                if(cell_m_b2[i][j]==1 and tail_count): cell_m_b[i][j]=3
                if(cell_m_b2[i][j]==1 and tl2):cell_m_b[i][j]=3
                v_and, v_or, v_xor, v_inv = v_ch(i, j, cell_m_b2)
                if(cell_m_b2[i][j] == 5 and v_and): cell_m_b[i][j+2]=3
                if(cell_m_b2[i][j] == 6 and v_or): cell_m_b[i][j+2]=3
                if(cell_m_b2[i][j] == 7 and v_xor): cell_m_b[i][j+2]=3
                if(cell_m_b2[i][j] == 8 and tl3):
                    for k in range(len(neighbors_list)):
                        wan = neighbors_list[k][0]
                        tu = neighbors_list[k][1]
                        try:
                            if(cell_m_b2[i+wan][j+tu] == 1):
                                cell_m_b[i+wan][j+tu] = 3
                        except: pass
                if(cell_m_b2[i][j] == 9): 
                    if not(v_inv): cell_m_b[i][j+2]=3
        try: return bin_num
        except: return "0"
def blit_text(surface, text, pos, font, img):
    global max_d
    color = white_c
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    max_width, max_height = max_width - 10, max_height - 10
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height
    if(max_d < y): max_d = y
    if(img != None):
        sc.blit(img, ((win_w//2)-(img.get_size()[0]//2),y+10))
def draw_dox():
    with open("text.txt", encoding="utf-8") as f_to_s:
        read = f_to_s.read()
    blit_text(sc, read, (10, y_text), font, img_halfadder)
    global drw_dox_b
    pgm.draw.rect(sc, white_c, (0, dis_h, win_w, bar_s))
    txt = "Exit"
    txt_w, txt_h = font.size(txt)
    h_pos = dis_h+((bar_s//2)-(txt_h//2))
    pgm.draw.rect(sc,black_c,(5, h_pos-5,txt_w+10,txt_h+10),1)
    draw_text(black_c, txt, (10, h_pos), 24)
    if(pgm.mouse.get_pressed()[0]):
        if(ms_x > 5 and ms_x < 5+txt_w+10 and 
           ms_y > h_pos-5 and ms_y < h_pos-5+txt_h+10):
            drw_dox_b = False

white_c = "#ffffff"
green_c = "#337755"
brown_c = "#aa9944"
blue_c  = "#4466ff"
red_c   = "#ff44aa"
pink_c  = "#ff55ff"
violet_c= "#5555ff"
yellow_c= "#ffbb44"
gray_c  = "#333333"
lgray_c = "#555555"
black_c = "#000000"

img_halfadder = pgm.image.load("img_halfadder.jpg")

sb_p1, sb_p2, sb_p3, sb_p4 = 0, 0, 0, 0
bin_num = "0"
y_text = 10
max_d = 0
page = 0
start_ticks, seconds, ms_num = 0, 0, 0
filename = ""

color_pen = 1
neighbors_list=[[0,-1],[1,0],[0,1],[-1,0]]
sc = pgm.display.set_mode((500, 500), pgm.RESIZABLE)
#from pygame.locals import *
#flags = DOUBLEBUF
#sc = pgm.display.set_mode((500, 500), flags)
sc.set_alpha(None)
pgm.display.set_caption("Polygon of Logical Schemes	O for opening a file")
bar_s = 40
cell_s = 30
m_w, m_h = 10, 10
m_wpx, m_hpx = m_w * cell_s, m_h * cell_s
win_w, win_h = sc.get_size()
dis_h = win_h - bar_s
e_x, e_y = (win_w//2)-(m_wpx//2), (dis_h//2)-(m_hpx//2)
cell_m = [[0] * m_w for i in range(m_h)]
cell_m_b = [[0] * m_w for i in range(m_h)]
cell_m_side = True
mnpl_b = False
mnpl_b_1 = False
chngm_b = False
st_game_b = False
hide_bar = False
drw_dox_b = False
mss_b, mss_b2, mss_b3 = False, False, False
drw_op_file_b = False
run = True
input_box1 = InputBox((win_w-100)//2-50, (win_h-30)//2-15, 100, 30)
input_boxes = [input_box1]
#num_pic = 0
while run:
    #num_pic += 1
    old_win_w, old_win_h = win_w, win_h
    win_w, win_h = sc.get_size()
    if(old_win_w != win_w or old_win_h != win_h):
        input_box1 = InputBox((win_w-100)//2-50, (win_h-30)//2-15, 100, 30)
        input_boxes = [input_box1]
    dis_h = win_h - bar_s
    m_w, m_h = len(cell_m[0]), len(cell_m)
    m_wpx, m_hpx = m_w * cell_s, m_h * cell_s
    ms_x, ms_y = pgm.mouse.get_pos()
    for ev in pgm.event.get():
        for box in input_boxes:
            box.handle_event(ev)
        if(ev.type == pgm.QUIT):
            run = False
            exit()
        if(hide_bar and drw_dox_b == False): stop_line = win_h
        else: stop_line = dis_h
        if(ev.type == pgm.MOUSEBUTTONDOWN and drw_dox_b == False and 
           drw_op_file_b == False):
            if(ms_x>sb_p1 and ms_y>sb_p2 and ms_x<sb_p3 and ms_y<sb_p4 and
               hide_bar == False):
                if(st_game_b): st_game_b = False
                else: st_game_b = True
        if(ev.type == pgm.MOUSEMOTION):
            mss_b2 = False
            mss_b3 = False
        if(ms_y < stop_line and drw_dox_b == False and drw_op_file_b == False):
            if(ev.type == pgm.MOUSEBUTTONDOWN):
                ev_b = ev.button
                if(chngm_b and ev_b == 1):
                    chngm_b = False
                    if(ns_w > 0 and ns_h > 0):
                        d_w, d_h = round(ns_w-m_w)+1, round(ns_h-m_h)+1
                        for k in range(abs(d_h)):
                            if(d_h > 0):
                                cell_m.append([0 for i in range(m_w)])
                                cell_m_b.append([0 for i in range(m_w)])
                            elif(d_h < 0):
                                cell_m.pop(-1)
                                cell_m_b.pop(-1)
                        for k in range(abs(d_w)):
                            if(d_w > 0):
                                for i in range(m_h+d_h):
                                    cell_m[i].append(0)
                                    cell_m_b[i].append(0)
                            if(d_w < 0):
                                for i in range(m_h+d_h):
                                    cell_m[i].pop(-1)
                                    cell_m_b[i].pop(-1)
                else:
                    if not(mnpl_b):ms_motion(ev_b)
                if(ev_b == 1):
                    if(chngm_b):
                        st_rctx = ms_x//cell_s*cell_s
                        st_rcty = ms_y//cell_s*cell_s
                    if(mnpl_b):
                        mnpl_b = False
                        mnpl_b_1 = True
                        st_p2d, st_p1d = 0, 0
                        test_l=list(zip(*([x[st_p1:en_p1+1] for x in cell_m])))
                        out_list = []
                        for row in test_l:
                            out_list.append(list(row)[st_p2:en_p2+1])
            if(ev.type == pgm.MOUSEMOTION and drw_dox_b == False):
                ev_b = ev.buttons
                if 1 in ev_b: ms_motion(ev_b.index(1)+1)
                if(ev_b[1]):
                    ev_rel = ev.rel
                    e_x, e_y = e_x + ev_rel[0], e_y + ev_rel[1] 
            if(ev.type==pgm.MOUSEWHEEL and mnpl_b==False and mnpl_b_1==False
               and drw_dox_b == False):
                ev_y = ev.y
                sign = ev_y // abs(ev_y)
                x, y = ms_x - e_x, ms_y - e_y
                size_old_x = len(cell_m[0]) * cell_s
                size_old_y = len(cell_m) * cell_s
                mins = min(size_old_x, size_old_y)
                plus_y = round(abs(ev_y*mins)/(len(cell_m)*50))+1
                if(cell_s + 50 < 150 and cell_s - 5 > 1):
                    cell_s += plus_y * sign
                elif(sign == -1 and cell_s - 5 > 1):
                    cell_s += plus_y * sign
                elif(sign == 1 and cell_s + 50 < 150):
                    cell_s += plus_y * sign
                size_new_x = len(cell_m[0]) * cell_s
                size_new_y = len(cell_m) * cell_s
                size_dop_x = abs(size_new_x - size_old_x)
                size_dop_y = abs(size_new_y - size_old_y)
                proc_x, proc_y = x/size_old_x*100, y/size_old_y*100
                e_x -= sign * (size_dop_x/100)*proc_x
                e_y -= sign * (size_dop_y/100)*proc_y
        if(ev.type == pgm.KEYDOWN and drw_op_file_b == False):
            ev_key = ev.key
            if(ev_key == pgm.K_a):
                if(drw_dox_b): drw_dox_b = False
                else: drw_dox_b = True
        #if(ev.type == pgm.KEYDOWN and drw_dox_b and drw_op_file_b == False):
        #    if(ev_key == pgm.K_RIGHT): page += 1
        #    if(ev_key == pgm.K_LEFT): page -= 1
        #    print(page)
        if(ev.type==pgm.KEYDOWN and drw_dox_b==False and drw_op_file_b==False):
            ev_key = ev.key
            if(ev_key == pgm.K_BACKSPACE and mnpl_b_1):
                for i in range(st_p1, en_p1+1):
                    for j in range(st_p2, en_p2+1):
                        try:
                            cell_m[j][i] = 0
                            cell_m_b[j][i] = 0
                        except: pass
                mnpl_b_1 = False
            if(ev_key == pgm.K_UP and mnpl_b_1): st_p2d -= 1
            if(ev_key == pgm.K_DOWN and mnpl_b_1): st_p2d += 1
            if(ev_key == pgm.K_LEFT and mnpl_b_1): st_p1d -= 1
            if(ev_key == pgm.K_RIGHT and mnpl_b_1): st_p1d += 1
            if(ev_key == pgm.K_RETURN and mnpl_b_1):
                cell_m2 = list(map(list, cell_m))
                cell_m_b2 = list(map(list, cell_m_b))
                for i in range(st_p1, en_p1+1):
                    for j in range(st_p2, en_p2+1):
                        try:
                            cell_m[j+st_p2d][i+st_p1d] = cell_m2[j][i]
                            cell_m_b[j+st_p2d][i+st_p1d] = cell_m_b2[j][i]
                        except: pass
                mnpl_b_1 = False
            if(ev_key == pgm.K_g):
                bin_num = "0"
                for i in range(m_w):
                    for j in range(m_h):
                        if(cell_m[j][i] == 2 or cell_m[j][i] == 3):
                            cell_m[j][i] = 1
                        if(cell_m_b[j][i] == 2 or cell_m_b[j][i] == 3):
                            cell_m_b[j][i] = 1
            if(ev_key == pgm.K_b):
                if(cell_m_side): cell_m_side = False
                else: cell_m_side = True
            if(ev_key == pgm.K_o):
                drw_op_file_b = True
            if(ev_key == pgm.K_t):
                pgm.image.save(sc,"screenshot.jpg")
            if(ev_key == pgm.K_s):
                open("save.txt", 'w').close()
                file_to_save = open("save.txt", "a")
                file_to_save.write(str(cell_m)+"\n")
                file_to_save.write(str(cell_m_b)+"\n")
                file_to_save.close()
            if(ev_key == pgm.K_r):
                chngm_b = True
            if(ev_key == pgm.K_h):
                if(hide_bar): hide_bar = False
                else: hide_bar = True
            elif(ev_key == pgm.K_c):
                if not(hide_bar):
                    e_x, e_y = (win_w//2)-(m_wpx//2), (dis_h//2)-(m_hpx//2)
                else:
                    e_x, e_y = (win_w//2)-(m_wpx//2), (win_h//2)-(m_hpx//2)
            elif(ev_key == pgm.K_m and mnpl_b_1 == False):
                mnpl_b = True
                st_pos1 = (ms_x-e_x)//cell_s*cell_s
                st_pos2 = (ms_y-e_y)//cell_s*cell_s
            elif(ev_key == pgm.K_1):
                color_pen = 1
            elif(ev_key == pgm.K_2):
                color_pen = 4
            elif(ev_key == pgm.K_3):
                color_pen = 5
            elif(ev_key == pgm.K_4):
                color_pen = 6
            elif(ev_key == pgm.K_5):
                color_pen = 7
            elif(ev_key == pgm.K_6):
                color_pen = 9
            elif(ev_key == pgm.K_7):
                color_pen = 8
            elif(ev_key == pgm.K_8):
                color_pen = 10
            elif(ev_key == pgm.K_SPACE):
                if(st_game_b):st_game_b = False
                else: st_game_b = True
        if(ev.type==pgm.MOUSEWHEEL and drw_dox_b):
            y_text += ev.y*2
    ms_x_old, ms_y_old = ms_x, ms_y
    if(drw_dox_b):
        if(y_text > 10): y_text = 10
        #if(max_d != 0):
        #    if(abs(y_text) > max_d):
        #        y_text = -max_d
        keys=pgm.key.get_pressed()
        if keys[pgm.K_UP]:
            y_text += 20
        elif keys[pgm.K_DOWN]:
            y_text -= 20
        elif keys[pgm.K_c]:
            y_text = 10
    sc.fill(gray_c)
    if(drw_dox_b == False):
        drw_map(bin_num)
        if not(hide_bar):sb_p1,sb_p2,sb_p3,sb_p4,color_pen=drw_bar(color_pen)
        if(chngm_b):
            ns_w, ns_h = chng_maps()
            drw_m_s()
        if(mnpl_b):
            end_pos1 = (ms_x-st_pos1-e_x)//cell_s*cell_s+cell_s
            end_pos2 = (ms_y-st_pos2-e_y)//cell_s*cell_s+cell_s
            pgm.draw.rect(sc,white_c,(st_pos1+e_x,st_pos2+e_y,end_pos1,
                                      end_pos2),1)
            st_p1 = round(st_pos1//cell_s)
            st_p2 = round(st_pos2//cell_s)
            en_p1 = round(end_pos1//cell_s-1+st_p1)
            en_p2 = round(end_pos2//cell_s-1+st_p2)
        if(mnpl_b_1):
            pgm.draw.rect(sc,white_c,(st_pos1+e_x+(st_p1d*cell_s),
                                    st_pos2+e_y+(st_p2d*cell_s),
                                    end_pos1,end_pos2),1)
        if(st_game_b): bin_num = st_game()
    else:
        draw_dox()
    if(mss_b):
        start_ticks=pgm.time.get_ticks()
        mss_b, mss_b2 = False, True
    if(drw_op_file_b): drw_op_file()
    #pgm.image.save(sc,"vid/"+str(num_pic)+".jpg")
    pgm.display.update()
    pgm.time.Clock().tick(60)
