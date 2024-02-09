import pygame as py
py.init()


# tutorial souce https://www.youtube.com/watch?v=7w8FiHe4ziQ
screen_width = 1240
screen_height = 720
tile_size = 90
screen = py.display.set_mode((screen_width,screen_height))

clock = py.time.Clock()
fps = 75

py.display.set_caption('Level Editor')

level = [[0 for _ in range(18)] for _ in range(7)]
level.append([2 for _ in range(18)])
level.append([1 for _ in range(18)])

#load images
sky = py.image.load('img/Sky.jpg')
sky = py.transform.scale(sky,(screen_width,screen_height))

#get dirt texture
wood = py.transform.scale(py.image.load('img/wood.jpg'),(100,100))
leaves = py.transform.scale(py.image.load('img/leaves.jpg'),(100,100))


#tiles lists -- fill in your images but keep 0 blank
tiles = ['', wood, leaves]


def draw_board(board):
    # 0 is always empty and then insert your own indexes ... example: tiles[1] = wood
    for q in range(len(board)):
        for p in range(len(level[q])):
            if board[q][p] != 0:
                value = board[q][p]
                if 0 <= value <= 2:
                    screen.blit(tiles[value], (p * tile_size, q * tile_size))
#editor loop
run = True
while run:
    clock.tick(fps)
    screen.blit(sky,(0,0))

    #draw the tiles
    draw_board(level)


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        #change tile using mouse
        if event.type == py.MOUSEBUTTONDOWN:
            coords = (py.mouse.get_pos()[0] // tile_size, py.mouse.get_pos()[1] // tile_size)
            if event.button == 1 or event.button == 4:
                #next tile change 3 for length of ur list
                if level[coords[1]][coords[0]] < 3:
                    level[coords[1]][coords[0]] += 1
                else:
                    level[coords[1]][coords[0]] = 0
            if event.button == 3 or event.button == 5:
                #previous tile
                if level[coords[1]][coords[0]] > 0:
                    level[coords[1]][coords[0]] -= 1
                else:
                    level[coords[1]][coords[0]] = 2
        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:
                board_string = "["
                for i in range(len(level)):
                    board_string += str(level[i]+ '\n')
                board_string += "]"
                print(board_string)
    py.display.flip()
py.quit()