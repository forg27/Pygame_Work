import pygame as py
py.init()

screen_width = 1200
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.y_velocity = 0
        self.jumped = False

    def update(self):
        #movement
        delta_x = 0
        delta_y = 0

        key = py.key.get_pressed()
        if key[py.K_SPACE] and self.jumped == False:
            self.y_velocity = -17
            self.jumped = True
        if key[py.K_SPACE] == True:
            self.jumped = True

        
        if key[py.K_a]:
            delta_x -= self.speed
            
        if key[py.K_d]:
            delta_x += self.speed
        
        ### JUMPING
        self.y_velocity += 1

        if self.y_velocity > 10:
            self.y_velocity = 10
        delta_y += self.y_velocity
        

        #level collision
        for tile in world.tile_list:
            # x collision
            if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                delta_x = 0
                
            
            # y collision
            if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                #check if below block
                if self.y_velocity < 0:
                    delta_y = tile[1].bottom - self.rect.top
                    self.y_velocity = 0
                elif self.y_velocity >= 0:
                    delta_y = tile[1].top - self.rect.bottom
                    self.y_velocity = 0
                    self.jumped = False
            
        self.rect.x += delta_x
        self.rect.y += delta_y

        #temp check
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.jumped = False
            delta_y = 0

        screen.blit(self.image,(player.rect.x, player.rect.y))


tile_size = 62
#background stuff
sky = py.image.load('img/Sky.jpg')
sky = py.transform.scale(sky,(screen_width,screen_height))

player = Player(5,100,100)
player_sprites = py.sprite.Group()

#World


class World():
    def __init__(self, data):
        self.tile_list = []
        wood = py.image.load('img/wood.jpg')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    wood = py.transform.scale(wood, (tile_size, tile_size))
                    wood_rect = wood.get_rect()
                    wood_rect.x = col_count * tile_size
                    wood_rect.y = row_count * tile_size
                    tile = (wood, wood_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    leaves = py.transform.scale(py.image.load('img/leaves.jpg'),(tile_size,tile_size))
                    leaves_rect = wood.get_rect()
                    leaves_rect.x = col_count * tile_size
                    leaves_rect.x = row_count * tile_size
                    tile = (leaves, leaves_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    
    def draw_world(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

## test level will update!
level_1 =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
             [1, 0, 0, 0, 1, 1, 0, 1, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
                 , [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 1], 
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 0, 0, 0, 1], 
                 [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                   [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                     [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]]
world = World(level_1)

run = True
while run:
    #screen background
    screen.blit(sky, (0,0))
    world.draw_world()
    player.update()
    for i in py.event.get():
        if i.type == py.QUIT:
            run = False

    py.display.flip()
    clock.tick(fps)

py.quit()
