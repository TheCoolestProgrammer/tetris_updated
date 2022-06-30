import pygame, random,copy
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
process_running = True
fps = 360

class Shape():
    def __init__(self,x,y,coords):
        self.x = x
        self.y = y
        self.coords = coords
        r = random.randint(40,255)
        g = random.randint(40,255)
        b = random.randint(40,255)
        self.color = (r,g,b)
    # def show_on_field(self,field):
    def draw(self,field):
        c = field.cell_size
        l = field.indent_left
        b = field.indent_bottom
        h = field.height
        for cords in self.coords:
            pygame.draw.rect(screen,self.color,(l+cords[0]*c,screen_height-(h-cords[1])*c-b,c,c))
    @staticmethod
    def shape1(x,y):

        #  @@@@@@
        #    @@

        return Shape(x,y,[(x,y),(x-1,y),(x+1,y),(x,y+1)])

    @staticmethod
    def shape2(x, y):

        #  @@@@@@@@

        return Shape(x, y, [(x,y),(x - 1, y), (x + 1, y), (x+2, y)])

    @staticmethod
    def shape3(x, y):

        #    @@@@
        #  @@@@

        return Shape(x, y, [(x,y),(x + 1, y), (x, y+1), (x-1, y+1)])

    @staticmethod
    def shape4(x, y):
        #  @@@@
        #    @@@@
        return Shape(x, y, [(x,y),(x - 1, y), (x, y+1), (x + 1, y+1)])

    @staticmethod
    def shape5(x, y):
        #  @@@@
        #  @@@@
        return Shape(x, y, [(x,y),(x + 1, y), (x, y + 1), (x + 1, y + 1)])


    @staticmethod
    def shape6(x, y):
        #  @@@@@@
        #      @@
        return Shape(x, y, [(x,y),(x - 1, y), (x+1, y ), (x + 1, y + 1)])

    @staticmethod
    def shape7(x, y):
        #  @@@@@@
        #  @@
        return Shape(x, y, [(x,y),(x - 1, y), (x+1, y ), (x - 1, y + 1)])

class Future_field():
    def __init__(self):
        self.width = 6
        self.height = 2
        self.future_field = [[0] * self.width for i in range(self.height)]
        self.cell_size = 35
        self.indent_right = 600
        self.indent_above = 100

        self.line_color = (180, 180, 180)
        self.line_size = 1
        self.line_color_border = (255, 255, 255)
        self.line_size_border = 5
    def draw(self,coords):
        y1 = self.indent_above
        y2 = self.indent_above + self.cell_size*self.height

        x1 = screen_width -(self.width * self.cell_size)-self.indent_right
        x2 = x1+self.cell_size*self.width

        for x in range(x1,x2,  self.cell_size):
            pygame.draw.line(screen, self.line_color, (x, y1), (x, y2), self.line_size)

        # vertical field lines
        for y in range(y1, y2, self.cell_size):
            pygame.draw.line(screen, self.line_color, (x1, y), (x2, y), self.line_size)

        pygame.draw.rect(screen,self.line_color_border,(x1,y1,self.cell_size*self.width,self.cell_size*self.height),self.line_size_border)


        for i in coords:
            pygame.draw.rect(screen, (random.randint(50,255),random.randint(50,255),random.randint(50,255)), (x1+self.cell_size*(i[0]-1),y1+self.cell_size*i[1],self.cell_size,self.cell_size))
class Field():
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.field = [[0]*self.width for i in range(self.height)]
        self.cell_size = 35

        self.indent_bottom = 20
        self.indent_left = 20

        self.line_color = (180,180,180)
        self.line_size = 1
        self.line_color_border = (255,255,255)
        self.line_size_border = 5

        self.has_fallen_objects=False
    def draw(self):
        #horisontal field lines
        y1 = screen_height-(self.cell_size*self.height)-self.indent_bottom
        y2 = screen_height-self.indent_bottom
        for x in range(self.indent_left,self.width*self.cell_size+self.indent_left,self.cell_size):
            pygame.draw.line(screen,self.line_color,(x,y1),(x,y2),self.line_size)

        #vertical field lines
        x1 = self.indent_left
        x2 = self.indent_left+self.cell_size*self.width
        for y in range(y1,y2,self.cell_size):
            pygame.draw.line(screen, self.line_color, (x1, y), (x2, y), self.line_size)

        #fallen bricks
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] != 0 and self.field[i][j] !=1:
                    c = self.cell_size
                    l = self.indent_left
                    b = self.indent_bottom
                    h = self.height
                    pygame.draw.rect(screen, self.field[i][j],(l + j * c, screen_height - (h - i) * c - b, c, c))
        # stroke
        pygame.draw.rect(screen, self.line_color_border,
                         (self.indent_left, y1, self.cell_size * self.width, self.cell_size * self.height),
                         self.line_size_border)

    def rotating(self,shape):
        # for cord in shape.coords:
        #     self.field[cord[1]][cord[0]] =0

        cords_copy = copy.deepcopy(shape.coords)
        flag = False
        for i in range(len(shape.coords)):
            # print(shape.x,shape.y, shape.coords[i][1])
            new_x = shape.x + shape.y - shape.coords[i][1]
            new_y = shape.coords[i][0] + shape.y - shape.x
            if len(self.field[0]) > new_x >=0 and new_y < len(self.field) and (self.field[new_y][new_x] ==0 or self.field[new_y][new_x] ==1) :
                shape.coords[i] = (new_x,new_y)
            else:
                flag = True
                break
        if flag:
            shape.coords=cords_copy
        for i in cords_copy:
            self.field[i[1]][i[0]] = 0
        for i in shape.coords:
            self.field[i[1]][i[0]] = 1
    def has_obstacle(self,direction,shape):
        if direction == "down":
            for cords in shape.coords:
                if cords[1] == len(self.field)-1:
                    return True
            for cords in shape.coords:
                if self.field[cords[1]+1][cords[0]] != 0 and self.field[cords[1]+1][cords[0]] != 1:
                    return True
            return False
        elif direction == "right":
            for cords in shape.coords:
                if cords[0] == len(self.field[0])-1 or(self.field[cords[1]][cords[0]+1] != 0 and self.field[cords[1]][cords[0]+1] != 1):
                    return True
            return False
        elif direction == "left":
            for cords in shape.coords:
                if cords[0] == 0 or (self.field[cords[1]][cords[0]-1] != 0 and self.field[cords[1]][cords[0]-1] != 1):
                    return True
            return False


    def move(self,direction,shape):
        if direction == "down":
            if not self.has_obstacle(direction,shape):
                i = 0
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] =0
                    shape.coords[i] = (shape.coords[i][0],shape.coords[i][1]+1)
                    i+=1
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = 1
                shape.y+=1
            else:
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = shape.color
                self.has_fallen_objects = False
                shape.coords = []
                self.check_tetris()

        elif direction == "right":
            if not self.has_obstacle(direction, shape):
                i = 0
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = 0
                    shape.coords[i] = (shape.coords[i][0]+1, shape.coords[i][1])
                    i += 1
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = 1
                shape.x +=1
        elif direction == "left":
            if not self.has_obstacle(direction, shape):
                i = 0
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = 0
                    shape.coords[i] = (shape.coords[i][0]-1, shape.coords[i][1])
                    i += 1
                for cords in shape.coords:
                    self.field[cords[1]][cords[0]] = 1
                shape.x-=1
    def delete_rows(self,rows_to_delete):
        for i in rows_to_delete:
            self.field[i] = [0]*self.width

    def fall_rows(self,deleted_rows):
        if len(deleted_rows)>0:
            lowest_deep = max(deleted_rows)
            # deleted_rows = sorted(deleted_rows,reverse=True)
            for i in range(lowest_deep-1,-1,-1):
            # for i in deleted_rows:
                if i in deleted_rows:
                    continue
                self.field[i+1] = self.field[i]
                self.field[i] = [0]*self.width

    def check_tetris(self):
        rows_to_delete=[]
        for i in range(len(self.field)-1,-1,-1):
            flag = False
            for j in range(len(self.field[i])):
                if self.field[i][j]==0:
                    flag = True
                    break
            if not flag:
                self.has_fallen_objects = False
                rows_to_delete.append(i)
        self.delete_rows(rows_to_delete)
        self.fall_rows(rows_to_delete)

def drawing(field,shape,future_field,future_shape):
    screen.fill((0, 0, 0))
    shape.draw(field)
    field.draw()
    future_field.draw(future_shape.coords)
    pygame.display.update()
    # for sprite in sprites:
        # print(coordinates_changer(sprite.x, sprite.y))
        # screen.blit(sprite.image, coordinates_changer2(sprite.x, sprite.y))

def add_shape_on_field(field):
    x=field.width//2-1
    y = 0
    shape = Shape(0,0,[])
    choise = random.randint(1,7)
    if choise == 1:
        shape = shape.shape1(x,y)
    elif choise == 2:
        shape = shape.shape2(x,y)
    elif choise == 3:
        shape = shape.shape3(x,y)
    elif choise == 4:
        shape = shape.shape4(x,y)
    elif choise == 5:
        shape = shape.shape5(x,y)
    elif choise == 6:
        shape = shape.shape6(x,y)
    elif choise == 7:
        shape = shape.shape7(x,y)
    return(shape)
def events_check(field,shape):
    global process_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_a:
                field.move("left",shape)
            elif event.key == pygame.K_d:
                field.move("right",shape)
            elif event.key == pygame.K_e:
                field.rotating(shape)

def mainloop():
    field = Field(8,18)
    future_field = Future_field()
    future_shape = add_shape_on_field(field)
    while process_running:

        if not field.has_fallen_objects:
            shape = future_shape
            future_shape = add_shape_on_field(field)
            field.has_fallen_objects = True
            # field.move(shape)
            # shape.show_on_field(field)
            events_check(field,shape)
        else:
            events_check(field, shape)
            field.move("down",shape)
        # for i in field.field:
        #     for j in i:
        #         if j != 0 and j != 1:
        #             print(1, end="")
        #         else:
        #             print(j, end="")
        #     print()
        # print("________")
        # field.check_tetris()
        drawing(field, shape,future_field,future_shape)
        pygame.time.delay(fps)


if __name__ == '__main__':
    mainloop()
