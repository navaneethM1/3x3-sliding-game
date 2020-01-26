import pygame
import random


#initialises the board(draws line segments for dividing screen) and where the _ is present
def board_init(game,grid,centers):
    game.fill((17,30,108))

    for i in range(1,3):
        pygame.draw.line(game,(255,255,255),(0,200*i),(600,200*i),1)
        pygame.draw.line(game,(255,255,255),(200*i,0),(200*i,600),1)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                x0 = i
                y0 = j
            d[grid[i][j]](centers[i][j])
    return x0,y0
    
#gets a random intial configuration
def get_grid():
    choicefile=open("C:\\Users\\Navaneeth M\\Desktop\\PATTERNS.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    choice=random.choice(linelist)
    a=choice.strip()
    l=[]
    d=[]
    e=[]
    grid=[]
    i=0
    l.append(int(a[i]))
    l.append(int(a[i+1]))
    l.append(int(a[i+2]))
    d.append(int(a[i+3]))
    d.append(int(a[i+4]))
    d.append(int(a[i+5]))
    e.append(int(a[i+6]))
    e.append(int(a[i+7]))
    e.append(int(a[i+8]))
    grid.append(l)
    grid.append(d)
    grid.append(e)
    return grid
    choicefile.close()

#winning list
winning_list = [[1,2,3],[4,5,6],[7,8,0]]

#win checker
def win_checker(grid):
    if grid == winning_list:
        return True
    else:
        return False
    
#draws numbers
def draw1(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x,y-50),(x,y+50)],3)
def draw2(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x-50,y-50),(x+50,y-50),(x+50,y),(x+50,y),(x-50,y),(x-50,y+50),(x+50,y+50)],3)
def draw3(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x-50,y+50),(x+50,y+50),(x+50,y),(x-50,y),(x+50,y),(x+50,y-50),(x-50,y-50)],3)
def draw4(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x,y+50),(x,y-50),(x-50,y),(x+50,y)],3)
def draw5(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x+50,y-50),(x-50,y-50),(x-50,y),(x+50,y),(x+50,y+50),(x-50,y+50)],3)
def draw6(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x+50,y-50),(x-50,y-50),(x-50,y),(x-50,y+50),(x+50,y+50),(x+50,y),(x-50,y)],3)
def draw7(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x-50,y-50),(x+50,y-50),(x+50,y+50)],3)
def draw8(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x-50,y+50),(x+50,y+50),(x+50,y),(x-50,y),(x-50,y+50),(x-50,y-50),(x+50,y-50),(x+50,y)],3)
def draw_(c):
    x = c[0]
    y = c[1]
    pygame.draw.lines(game,(255,255,255),False,[(x-50,y+50),(x+50,y+50)],3)

#returns the coordinate(in terms of grid) for the mouse click
def mouse_to_grid(mx,my):
    return my//200,mx//200

#main
pygame.init()
pygame.display.set_caption('sliding game')
game = pygame.display.set_mode((600,600))

#initialising grid to a random 3x3 configuration
grid = get_grid()

#tuple of centers
centers = (((100,100),(300,100),(500,100)),((100,300),(300,300),(500,300)),((100,500),(300,500),(500,500)))

d = {0:draw_,1:draw1,2:draw2,3:draw3,4:draw4,5:draw5,6:draw6,7:draw7,8:draw8}

terminate = False

#3x3
while not terminate:

    #x0 and y0 are the coordinates of _    
    x0,y0 = board_init(game,grid,centers)

    #running through all the events
    for event in pygame.event.get():

        #checking for quit
        if event.type == pygame.QUIT:
            terminate = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:

            #checking for left click pressed
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                x,y = mouse_to_grid(mx,my)

                #checks if pressed element can be exchanged with _; if yes, then interchanges 
                if (x0 == x and y0 == y + 1) or (x0 == x and y0 == y - 1) or (x0 == x + 1 and y0 == y) or (x0 == x - 1 and y0 == y) :
                    grid[x0][y0],grid[x][y] = grid[x][y],grid[x0][y0]
                
                elif (x0 == x and y0 == y-2):
                    grid[x0][y0],grid[x][y-1] = grid[x][y-1],grid[x0][y0]
                    grid[x][y-1],grid[x][y] = grid[x][y],grid[x][y-1]
                
                elif (x0 == x and y0 == y+ 2):
                    grid[x0][y0],grid[x][y+1] = grid[x][y+1],grid[x0][y0]
                    grid[x][y+1],grid[x][y] = grid[x][y],grid[x][y+1]
                
                elif (x0 == x+2 and y0 == y):
                    grid[x0][y0],grid[x+1][y] = grid[x+1][y],grid[x0][y0]
                    grid[x+1][y],grid[x][y] = grid[x][y],grid[x+1][y]
                
                elif (x0 == x-2 and y0 == y):
                    grid[x0][y0],grid[x-1][y] = grid[x-1][y],grid[x0][y0]
                    grid[x-1][y],grid[x][y] = grid[x][y],grid[x-1][y]

                else:
                    continue

            else:
                continue

        else:
            continue

    #checks for the win
    if win_checker(grid):
        board_init(game,grid,centers)
        pygame.display.update()
        pygame.time.delay(3000)
        game.fill((17,30,108))
        myfont = pygame.font.SysFont("monospace",30)
        text = myfont.render("You Win!",1,(255,255,255))
        game.blit(text,(240,270))
        pygame.display.update()
        pygame.time.delay(3000)
        terminate = True
                
    pygame.display.update()

pygame.quit()
