import pygame as py
py.init()

screen_width = 1800
screen_height = 900

screen = py.display.set_mode((screen_width,screen_height))

clock = py.time.Clock()
fps = 75
py.display.set_caption('Wizard Game')

class Player():
    def __init__(self,speed,x,y):
        img = py.image.load('img/player.png')
        self.image = py.transform.scale(img,(50,90))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = y
        self.rect.x = x
        self.y_velocity = 0
        self.jumped = False

    def update(self):
        #movement
        delta_x = 0
        delta_y = 0


        key = py.key.get_pressed()
        if key[py.K_a]:
            delta_x -= self.speed
            
        if key[py.K_d]:
            delta_x += self.speed
        
        #Jumping
        if key[py.K_SPACE] and self.jumped == False:
            self.y_velocity = -25
            self.jumped = True
        if key[py.K_SPACE] == False:
            self.jumped = False
        

        ### JUMPING
        self.y_velocity += 1
        if self.y_velocity > 10:
            self.y_velocity = 10
        
        
        delta_y += self.y_velocity
         
        self.rect.x += delta_x
        self.rect.y += delta_y

        #temp check
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            delta_y = 0

        screen.blit(self.image,(player.rect.x, player.rect.y))


tile_size = 100
#background stuff
sky = py.image.load('img/Sky.jpg')
sky = py.transform.scale(sky,(screen_width,screen_height))

level = [[0 for _ in range(18)] for _ in range(7)]
level.append([2 for _ in range(18)])
level.append([1 for _ in range(18)])

player = Player(5,100,100)
player_sprites = py.sprite.Group()

wood = py.transform.scale(py.image.load('img/wood.jpg'),(100,100))
leaves = py.transform.scale(py.image.load('img/leaves.jpg'),(100,100))

tiles = ['',wood, leaves]
#World
def draw_world(board):
    for q in range(len(board)):
        for p in range(len(level[q])):
            if board[q][p] != 0:
                value = board[q][p]
                if 0 <= value <= 2:
                    screen.blit(tiles[value], (p * tile_size, q * tile_size))





level_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]





run = True
while run:
    #screen background
    screen.blit(sky, (0,0))
    draw_world(level_1)
    player.update()
    for i in py.event.get():
        if i.type == py.QUIT:
            run = False

    py.display.flip()
    clock.tick(fps)

py.quit()
