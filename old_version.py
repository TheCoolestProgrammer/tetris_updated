# this version was made at 4th  October 2021

# shape 1 =  ##
#          ######
#
# shape 2 = ########
#
# shape 3 = ####
#             ####
#
# shape 4 =   ####
#           ####
#
# shape 5 = ####
#           ####
#
# shape 6 = ####
#             ##
#             ##
#
# shape 7 = ####
#           ##
#           ##



import pygame
import random
pygame.init()

screen_width = 10
screen_height = 20


field = [list(0 for i in range(screen_width)) for j in range(screen_height)]
field.append([2]*screen_width)

len_block = 30
screen = pygame.display.set_mode((screen_width*len_block,screen_height*len_block))



shapes = False

speed = 1
speed2 = 250

def painting(shape,x,y, value,pos):
    if shape == 1:
        if pos == 1:
            field[y][x + 1] = value
            field[y][x - 1] = value
            field[y][x] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
        elif pos == 2:
            field[y][x] = value
            field[y+1][x] = value
            field[y][x+1] = value
            if y - 1 >= 0:
                field[y-1][x] = value
        elif pos == 3:
            field[y][x + 1] = value
            field[y][x - 1] = value
            field[y][x] = value
            field[y + 1][x] = value
        elif pos == 4:
            field[y][x] = value
            field[y + 1][x] = value
            field[y][x - 1] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
    if shape == 2:
        if pos == 1:
            field[y][x] = value
            field[y][x + 1] = value
            field[y][x + 2] = value
            field[y][x - 1] = value
        elif pos == 2:
            field[y][x] = value
            if y - 1 >= 0:
                field[y-1][x] = value
            field[y+1][x] = value
            field[y+2][x] = value
    if shape == 3:
        if pos == 1:
            field[y][x] = value
            field[y][x - 1] = value
            field[y + 1][x] = value
            field[y + 1][x + 1] = value
        elif pos == 2:
            field[y][x] = value
            field[y][x - 1] = value
            field[y + 1][x-1] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
    if shape == 4:
        if pos == 1:
            field[y][x] = value
            field[y][x + 1] = value
            field[y + 1][x] = value
            field[y + 1][x - 1] = value
        elif pos ==2:
            field[y][x] = value
            field[y][x + 1] = value
            field[y + 1][x+1] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
    if shape == 5:
        field[y][x] = value
        field[y][x + 1] = value
        field[y + 1][x + 1] = value
        field[y + 1][x] = value
    if shape == 6:
        if pos == 1:
            field[y][x] = value
            field[y][x - 1] = value
            field[y + 1][x] = value
            field[y + 2][x] = value
        elif pos == 2:
            field[y][x] = value
            field[y][x - 1] = value
            field[y][x - 2] = value
            if y - 1 >= 0:
                field[y -1][x] = value
        elif pos == 3:
            field[y][x] = value
            field[y][x + 1] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
            if y - 2 >= 0:
                field[y - 2][x] = value
        elif pos == 4:
            field[y][x] = value
            field[y][x + 1] = value
            field[y][x + 2] = value
            field[y + 1][x] = value
    if shape == 7:
        if pos == 1:
            field[y][x] = value
            field[y][x + 1] = value
            field[y + 1][x]= value
            field[y + 2][x] = value
        elif pos == 2:
            field[y][x] = value
            field[y][x - 1] = value
            field[y][x - 2] = value
            field[y + 1][x] = value
        elif pos == 3:
            field[y][x] = value
            field[y][x - 1] = value
            if y - 1 >= 0:
                field[y - 1][x] = value
            if y - 2 >= 0:
                field[y - 2][x] = value
        elif pos == 4:
            field[y][x] = value
            field[y][x + 1] = value
            field[y][x + 2] = value
            if y - 1 >= 0:
                field[y - 1][x] = value

while True:
    screen.fill((0, 0, 0))

    pygame.time.delay(speed2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.QUIT:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                # for i in range(len(field)):
                #     for j in range(len(field[i])):
                #         print(field[i][j], end="")
                #     print()
                painting(shape, x, y, 0, pos)
                x -= speed
                # for i in range(len(field)):
                #     for j in range(len(field[i])):
                #         print(field[i][j], end="")
                #     print()
                # print("____________________________________________")
            if event.key == pygame.K_RIGHT:
                painting(shape, x, y, 0, pos)
                x += speed
            if event.key == pygame.K_DOWN:
                painting(shape, x, y, 0, pos)
                y += speed
            if event.key == pygame.K_e:
                if shape == 1 or shape == 6 or shape == 7:
                    painting(shape, x, y, 0, pos)
                    pos += 1
                    if pos > 4:
                        pos = 1
                elif shape == 5:
                    pass
                else:
                    painting(shape, x, y, 0, pos)
                    pos +=1
                    if pos > 2:
                        pos = 1
            # print(x,y)
            # print(speed)

    if not shapes:
        shape = random.randint(1,7)
        y = 0
        x = 3
        pos = 1
        #painting(shape,x,y,1,pos)
        shapes = True
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        #continue

    for i in range(len(field)):
        if field[i] == [1]*screen_width:
            for j in range(i,0,-1):
                field[j] = field[j-1]

    painting(shape, x, y, 0, pos)
    y += 1
    painting(shape, x, y, 1, pos)


    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                pygame.draw.rect(screen,(color),(j*len_block, i*len_block, len_block,len_block))
            if field[i][j] == 2:
                pygame.draw.rect(screen,(color),(j*len_block, i*len_block, len_block,len_block))
    #pressed = pygame.key.get_pressed()



    if shape == 1:
        if pos == 1:
            if field[y+1][x] == 1 or field[y+1][x - 1] == 1 or field[y+1][x + 1] == 2 or field[y+1][x] == 2 or field[y+1][x - 1] == 2 or field[y+1][x + 1] == 2:
                shapes = False
                continue
        elif pos == 2:
            if field[y+2][x] == 1 or field[y+1][x+1] == 1 or field[y+2][x] == 2 or field[y+1][x+1] == 2:
                shapes = False
                continue
        elif pos == 3:
            if field[y+1][x - 1] == 1 or field[y+1][x + 1] == 1 or field[y+2][x] or field[y+1][x - 1] == 2 or field[y+1][x + 1] == 2 or field[y+2][x] == 2:
                shapes = False
                continue
        elif pos == 4:
            if field[y+2][x] == 1 or field[y+1][x-1] == 1 or field[y+2][x] == 2 or field[y+1][x - 1] == 2:
                shapes = False
                continue
    elif shape == 2:
        if pos == 1:
            if field[y+1][x-1] == 1 or field[y+1][x]== y or field[y+1][x+1] == 1 or field[y+1][x+2] == 1 or field[y+1][x-1] == 2 or field[y+1][x]== y or field[y+1][x+1] == 2 or field[y+1][x+2] == 2:
                shapes = False
                continue
        elif field[y+3][x] == 1 or field[y+3][x] == 2 :
            shapes = False
            continue
    elif shape == 3:
        if pos == 1:
            if field[y+1][x-1] == 1 or field[y+2][x] == 1 or field[y+2][x+1] == 1 or field[y+1][x-1] == 2 or field[y+2][x] == 2 or field[y+2][x+1] == 2:
                shapes = False
                continue
        if pos == 2:
            if field[y+1][x] == 1 or field[y+2][x-1] == 1 or  field[y+1][x] == 2 or field[y+2][x-1] == 2:
                shapes = False
                continue
    elif shape == 4:
        if pos == 1:
            if field[y+1][x+1] == 1 or field[y+2][x] == 1 or field[y+2][x-1] == 1 or field[y+1][x+1] == 2 or field[y+2][x] == 2 or field[y+2][x-1] == 2:
                shapes = False
                continue
        elif pos == 2:
            if field[y+1][x] == 1 or field[y+2][x+1] == 1 or field[y+1][x] == 2 or field[y+2][x+1] == 2:
                shapes = False
                continue
    elif shape == 5:
        if field[y+2][x]==1 or field[y+2][x+1] == 1 or field[y+2][x]==2 or field[y+2][x+1] == 2:
            shapes = False
            continue
    elif shape == 6:
        if pos == 1:
            if field[y+3][x] == 1 or field[y+1][x-1] == 1 or field[y+3][x] == 2 or field[y+1][x-1] == 2:
                shapes = False
                continue
        elif pos == 2:
            if field[y+1][x] == 1 or field[y+1][x-1] == 1 or field[y+1][x-2] == 1 or field[y+1][x] == 2 or field[y+1][x-1] == 2 or field[y+1][x-2] == 2:
                shapes = False
                continue
        elif pos == 3:
            if field[y+1][x] ==1 or field[y+1][x+1] == 1 or field[y+1][x] ==2 or field[y+1][x+1] == 2:
                shapes = False
                continue
        elif pos == 4:
            if field[y+2][x] == 1 or field[y+1][x+1]==1 or field[y+1][x+2] == 1 or field[y+2][x] == 2 or field[y+1][x+1]==2 or field[y+1][x+2] == 2:
                shapes = False
                continue
    elif shape == 7:
        if pos == 1:
            if field[y+1][x+1] == 1 or field[y+3][x] == 1 or field[y+1][x+1] == 2 or field[y+3][x] == 2:
                shapes = False
                continue
        elif pos == 2:
            if field[y+2][x] == 1 or field[y+1][x - 1] == 1 or field[y+1][x - 2] == 1 or field[y+2][x] == 2 or field[y+1][x - 1] == 2 or field[y+1][x - 2] == 2:
                shapes = False
                continue
        elif pos == 3:

            if field[y+1][x] == 1 or field[y+1][x - 1] == 1 or field[y+1][x] == 2 or field[y+1][x - 1] == 2:
                shapes = False
                continue
        elif pos == 4:
            if field[y+1][x] == 1 or field[y+1][x+1]==1 or field[y+1][x+2] == 1 or field[y+1][x] == 2 or field[y+1][x+1]==2 or field[y+1][x+2] == 2:

                shapes = False
                continue
    #TODO добавить условий для проверки не соприкоснулась ли крайняя клетка фигуры другой фигуры

    # for i in range(len(field)):
    #     for j in range(len(field[i])):
    #         print(field[i][j], end="")
    #     print()
    pygame.display.update()