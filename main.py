import pygame, random
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
process_running = True
fps = 60

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

        #stroke
        pygame.draw.rect(screen,self.line_color_border,(self.indent_left,y1, self.cell_size*self.width,self.cell_size*self.height),self.line_size_border)

    def has_obstacle(self,shape):
        for cords in shape.coords:
            if cords[1] == len(self.field)-1:
                return True
        return False
    def move(self,shape):
        if not self.has_obstacle(shape):
            i = 0
            for cords in shape.coords:
                self.field[cords[1]][cords[0]] =0
                shape.coords[i] = (shape.coords[i][0],shape.coords[i][1]+1)
                i+=1
            for cords in shape.coords:
                self.field[cords[1]][cords[0]] = 1
        else:
            self.has_fallen_objects = False
def drawing(field,shape):
    screen.fill((0, 0, 0))
    shape.draw(field)
    field.draw()

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
def events_check():
    global process_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
def mainloop():
    field = Field(8,18)
    while process_running:
        events_check()
        if not field.has_fallen_objects:
            shape = add_shape_on_field(field)
            field.has_fallen_objects = True
            field.move(shape)
            # shape.show_on_field(field)
        else:
            field.move(shape)
        # for i in field.field:
        #     print(i)
        # print("___________________________________")
        drawing(field,shape)
        pygame.time.delay(fps)


if __name__ == '__main__':
    mainloop()
