import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
process_running = True
fps = 60

class Field():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.cell_size = 50

        self.indent_bottom = 20
        self.indent_left = 20

        self.line_color = (180,180,180)
        self.line_size = 1
        self.line_color_border = (255,255,255)
        self.line_size_border = 5
    def draw(self):
        #horisontal field lines
        y1 = screen_height-(self.cell_size*self.height)-self.indent_bottom
        y2 = screen_height-self.indent_bottom
        for x in range(self.indent_left,self.width*self.cell_size+self.indent_left,self.cell_size):
            pygame.draw.line(screen,self.line_color,(x,y1),(x,y2),self.line_size)
        #stroke
        pygame.draw.rect(screen,self.line_color_border,(self.indent_left,y1, self.cell_size*self.width,self.cell_size*self.height),self.line_size_border)

        #vertical field lines
        x1 = self.indent_left
        x2 = self.indent_left+self.cell_size*self.width
        for y in range(y1,y2,self.cell_size):
            pygame.draw.line(screen, self.line_color, (x1, y), (x2, y), self.line_size)

def drawing(field):
    screen.fill((0, 0, 0))

    field.draw()

    pygame.display.update()
    # for sprite in sprites:
        # print(coordinates_changer(sprite.x, sprite.y))
        # screen.blit(sprite.image, coordinates_changer2(sprite.x, sprite.y))

def events_check():
    global process_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
def mainloop():
    field = Field(6,12)
    while process_running:
        events_check()
        pygame.time.delay(fps)
        drawing(field)

if __name__ == '__main__':
    mainloop()
