# Example file showing a basic pygame "game loop"

import pygame
import sys
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True
total=786
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
marq=1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
TILE_SIZE = 15
GREEN=(0,255,0)
RED=(255,0,0)
di2=0
di3=0
di=0
c=0
imortal=0
end=False
# Labirinto
maze = [
   "################################################################",
   "#!............................###.............................!#",
   "#.###########.###############.###.################.###########.#",
   "#.###########.###############.###.################.###########.#",
   "#..............................!...............................#",
   "#.####################.########.########.#####################.#",
   "#.####################...................#####################.#",
   "#......................########.########.......................#",
   "#.##########.##################.####################.#########.#",
   "#.##########.##################.####################.#########.#",
   "#..............................................................#",
   "#.####.###############.#################.################.####.#",
   "#.####.###############.#################.################.####.#",
   "#......................#################.......................#",
   "#.####.#####.######################################.#####.####.#",
   "#.####.#####.######################################.#####.####.#",
   "#............                                      ............#",
   "#.####.#####.######################################.#####.####.#",
   "#.####.#####.######################################.#####.####.#",
   "#......................#################.......................#",
   "#.####.###############.#################.################.####.#",
   "#.####.###############.#################.################.####.#",
   "#..............................................................#",
   "#.##########.##################.####################.#########.#",
   "#.##########.##################.####################.#########.#",
   "#......................########.########.......................#",
   "#.####################.########.########.#####################.#",
   "#.####################...................#####################.#",
   "#.####################.########.########.#####################.#",
   "#..............................................................#",
   "#.#############################.##############################.#",
   "#..............................................................#",
   "#.###########.###############.###.################.###########.#",
   "#.###########.###############.###.################.###########.#",
   "#!............................###.............................!#",
   "################################################################"
    ]  

# Posições iniciais
pacman_pos = [31 * TILE_SIZE, 31 * TILE_SIZE]
pacman1_pos = [30 * TILE_SIZE, 16 * TILE_SIZE]
pacman2_pos = [31 * TILE_SIZE, 16 * TILE_SIZE]
pacman3_pos = [32 * TILE_SIZE, 16 * TILE_SIZE]
pacman_speed = 15
direction = (0, 0)
def draw_maze():
   for row in range(len(maze)):
       for col in range(len(maze[row])):
           if maze[row][col] == '#':
               pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
           elif maze[row][col] == '.':
               pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 3)
           elif maze[row][col] == '!':
               pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 5)

while running:
   if c==150:
       imortal=0
   c+=1
   col4 = pacman_pos[0] // TILE_SIZE
   row4 = pacman_pos[1] // TILE_SIZE
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
           pygame.quit()
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT and maze[row4][col4-1]!="#":
               direction = (-pacman_speed, 0)
           elif event.key == pygame.K_RIGHT and maze[row4][col4+1]!="#":
               direction = (pacman_speed, 0)
           elif event.key == pygame.K_UP and maze[row4-1][col4]!="#":
               direction = (0, -pacman_speed)
           elif event.key == pygame.K_DOWN and maze[row4+1][col4]!="#":
               direction = (0, pacman_speed)
   if (pacman_pos[0] == pacman1_pos[0] and pacman_pos[1] == pacman1_pos[1] and imortal==0 or pacman_pos[0] == pacman1_pos[0]-1*TILE_SIZE and pacman_pos[1] == pacman1_pos[1] and imortal==0 or pacman_pos[0] == pacman1_pos[0] and pacman_pos[1] == pacman1_pos[1]-1*TILE_SIZE and imortal==0 or pacman_pos[0] == pacman1_pos[0]+1*TILE_SIZE and pacman_pos[1] == pacman1_pos[1] and imortal==0 or pacman_pos[0] == pacman1_pos[0] and pacman_pos[1] == pacman1_pos[1]+1*TILE_SIZE  and imortal==0   or  pacman_pos[0] == pacman2_pos[0] and pacman_pos[1] == pacman2_pos[1] and imortal==0 or pacman_pos[0] == pacman2_pos[0]-1*TILE_SIZE and pacman_pos[1] == pacman2_pos[1] and imortal==0 or pacman_pos[0] == pacman2_pos[0] and pacman_pos[1] == pacman2_pos[1]-1*TILE_SIZE and imortal==0 or pacman_pos[0] == pacman2_pos[0]+1*TILE_SIZE and pacman_pos[1] == pacman2_pos[1] and imortal==0 or pacman_pos[0] == pacman2_pos[0] and pacman_pos[1] == pacman2_pos[1]+1*TILE_SIZE and imortal==0 or pacman_pos[0] == pacman3_pos[0] and pacman_pos[1] ==pacman3_pos[1] and imortal==0 or pacman_pos[0] == pacman_pos[0]-1*TILE_SIZE and pacman_pos[1] == pacman3_pos[1] and imortal==0 or pacman_pos[0] == pacman3_pos[0] and pacman_pos[1] == pacman3_pos[1]-1*TILE_SIZE and imortal==0 or pacman_pos[0] == pacman3_pos[0]+1*TILE_SIZE and pacman_pos[1] == pacman3_pos[1]and imortal==0 or pacman_pos[0] == pacman3_pos[0] and pacman_pos[1] == pacman3_pos[1]+1*TILE_SIZE and imortal==0)  :
       running = False
       end=True
       maze = [
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
       ]
       marq=0
   new_pos = [pacman_pos[0] + direction[0], pacman_pos[1] + direction[1]]
   col = new_pos[0] // TILE_SIZE
   row = new_pos[1] // TILE_SIZE

   if maze[row][col] != '#':
       pacman_pos = new_pos
       if maze[row][col] == '.':
           maze[row] = maze[row][:col] + ' ' + maze[row][col + 1:]
           total -= 1
       elif maze[row][col] == '!':
           maze[row] = maze[row][:col] + ' ' + maze[row][col + 1:]
           total -= 1
           imortal=1
           c=0
   #RED
   passar=True
   while passar:
       dire=random.randint(1,5)
       col1 = pacman1_pos[0] // TILE_SIZE
       row1 = pacman1_pos[1] // TILE_SIZE
       if dire == 1 and maze[row1][col1-1]!="#" and di!=2:
           direction1 = (-pacman_speed, 0)
           passar=False
           di=1
       elif dire == 2 and maze[row1][col1+1]!="#" and di!=1:
           direction1 = (pacman_speed, 0)
           passar=False
           di=2
       elif dire == 3 and maze[row1-1][col1]!="#" and di!=4:
           direction1 = (0, -pacman_speed)
           passar=False
           di=3
       elif dire== 4 and maze[row1+1][col1]!="#" and di!=3:
           direction1 = (0, pacman_speed)
           passar=False
           di=4
   if passar==False:
       new_pos1 = [pacman1_pos[0] + direction1[0], pacman1_pos[1] + direction1[1]]
       col1 = new_pos1[0] // TILE_SIZE
       row1 = new_pos1[1] // TILE_SIZE
       if maze[row1][col1] != '#':
           pacman1_pos = new_pos1


   #GREEN
   passar2=True
   while passar2:
       dire2=random.randint(1,5)
       col2 = pacman2_pos[0] // TILE_SIZE
       row2 = pacman2_pos[1] // TILE_SIZE
       if dire2 == 1 and maze[row2][col2-1]!="#" and di2!=2:
           direction2 = (-pacman_speed, 0)
           passar2=False
           di2=1
       elif dire2 == 2 and maze[row2][col2+1]!="#" and di2!=1:
           direction2 = (pacman_speed, 0)
           passar2=False
           di2=2
       elif dire2 == 3 and maze[row2-1][col2]!="#" and di2!=4:
           direction2 = (0, -pacman_speed)
           passar2=False
           di2=3
       elif dire2== 4 and maze[row2+1][col2]!="#" and di2!=3:
           direction2 = (0, pacman_speed)
           passar2=False
           di2=4
   if passar2==False:
       new_pos2 = [pacman2_pos[0] + direction2[0], pacman2_pos[1] + direction2[1]]
       col2 = new_pos2[0] // TILE_SIZE
       row2 = new_pos2[1] // TILE_SIZE
       if maze[row2][col2] != '#':
           pacman2_pos = new_pos2


   #YELLOW
   passar3=True
   while passar3:
       dire3=random.randint(1,5)
       col3 = pacman3_pos[0] // TILE_SIZE
       row3 = pacman3_pos[1] // TILE_SIZE
       if dire3 == 1 and maze[row3][col3-1]!="#" and di3!=2:
           direction3 = (-pacman_speed, 0)
           passar3=False
           di3=1
       elif dire3 == 2 and maze[row3][col3+1]!="#" and di3!=1:
           direction3 = (pacman_speed, 0)
           passar3=False
           di3=2
       elif dire3 == 3 and maze[row3-1][col3]!="#" and di3!=4:
           direction3 = (0, -pacman_speed)
           passar3=False
           di3=3
       elif dire3== 4 and maze[row3+1][col3]!="#" and di3!=3:
           direction3 = (0, pacman_speed)
           passar3=False
           di3=4
   if passar3==False:
       new_pos3 = [pacman3_pos[0] + direction3[0], pacman3_pos[1] + direction3[1]]
       col3 = new_pos3[0] // TILE_SIZE
       row3 = new_pos3[1] // TILE_SIZE
       if maze[row3][col3] != '#':
           pacman3_pos = new_pos3

   
   if total == 0:
       marq=0
       running = False
       end=True
       maze = [
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
           "                                                                ",
       ]
   if imortal==0:
      screen.fill(BLACK)
   else:
       screen.fill("brown")
   draw_maze()
   if marq!=0:
       pygame.draw.circle(screen, WHITE, (pacman_pos[0] + TILE_SIZE // 2, pacman_pos[1] + TILE_SIZE // 2), TILE_SIZE // 2)
       pygame.draw.circle(screen, ("aqua"), (pacman1_pos[0] + TILE_SIZE // 2, pacman1_pos[1] + TILE_SIZE // 2), TILE_SIZE // 2)
       pygame.draw.circle(screen, GREEN, (pacman2_pos[0] + TILE_SIZE // 2, pacman2_pos[1] + TILE_SIZE // 2), TILE_SIZE // 2)
       pygame.draw.circle(screen, YELLOW, (pacman3_pos[0] + TILE_SIZE // 2, pacman3_pos[1] + TILE_SIZE // 2), TILE_SIZE // 2)
   pygame.display.flip()
   clock.tick(10)
while end:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
           pygame.quit()
           
   if total == 0:
       font = pygame.font.Font(None, 140)
       text = font.render("Ganhaste!!!", True, YELLOW)
   else:
       font = pygame.font.Font(None, 140)
       text = font.render("ÉS MESMO MAU!!!", True, RED)
   text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
   screen.blit(text, text_rect)
   pygame.display.flip()
   screen.fill(BLACK)
pygame.quit()