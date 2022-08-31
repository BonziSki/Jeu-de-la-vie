import pygame
from sys import exit



#Variables

height = 720
width = 720

cell_h = height / 10
cell_w = width / 10

tick_rate = 4

pause = 0


#Pygame conf

pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Jeu de la Vie')
clock = pygame.time.Clock()

black_surface = pygame.Surface((cell_h, cell_w))
black_surface.fill('black')


#Tableaux

table_n0 = [
    [0,1,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

table_n1 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]





def cell_alive(table, x, y) :
    count = 0

    if x == 0 :
        if y == 0 :
            for i in [0, 1] :
                for j in [0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1

        elif y == (height / cell_h) - 1 :
            for i in [-1, 0] :
                for j in [0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1
        else :
            for i in [-1, 0, 1] :
                for j in [0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1

    elif x == (width / cell_w) - 1 :
        if y == 0 :
            for i in [0, 1] :
                for j in [-1, 0] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1

        elif y == (height / cell_h) - 1 :
            for i in [-1, 0] :
                for j in [-1, 0] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1
        else :
            for i in [-1, 0, 1] :
                for j in [-1, 0] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1

    else :
        if y == 0 :
            for i in [0, 1] :
                for j in [-1, 0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1
        elif y == (height / cell_h) - 1 :
            for i in [-1, 0] :
                for j in [-1, 0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1
        else :
            for i in [-1, 0, 1] :
                for j in [-1, 0, 1] :
                    if not (i == 0 and j == 0) :
                        if table[y + i][x + j] == 1 :
                            count += 1

    if (count == 3) or (count == 2 and table[y][x] == 1) :
        return 1
    else :
        return 0


while True :
    #Event
    for event in pygame.event.get() :
        #Fermeture du programme
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        


        
        #Touches de clavier
        if event.type == pygame.KEYDOWN :
            #Mise en pause
            if event.unicode == ' ' :
                if pause == 0 :
                    print("pause")
                    pause = 1
                else :
                    print("play")
                    pause = 0
            
            #Clear de toutes les cellules
            if event.unicode == 'c' :
                print("clear")
                for i, row in enumerate(table_n0) :
                    for j, cell in enumerate(row) :
                        table_n0[i][j] = 0
                if pause == 0 :
                    print("pause")
                    pause = 1

    if pause == 0 :
        #Reset de la fenetre
        window.fill('white')

        #Changement du tableau
        for index_y, row in enumerate(table_n0) :
            for index_x, cell in enumerate(row) :
                table_n1[index_y][index_x] = cell_alive(table_n0, index_x, index_y)


        #Mise à jour du tableau
        for i in range(len(table_n0)) :
            for j in range(len(table_n0[i])) :
                table_n0[i][j] = table_n1[i][j]
                

        #Dessin des cellules
        for index_y, row in enumerate(table_n0) :
            for index_x, cell in enumerate(row) :
                if cell == 1 :
                    window.blit(black_surface, (index_x * cell_h, index_y * cell_w))


        #Dessin des lignes horizontales
        for i in range (0, int(width/cell_w)) :
            pygame.draw.line(window,'grey', (0, i * cell_w), (height, i * cell_w), 2)

        #Dessin des lignes verticales
        for i in range (0, int(height/cell_h)) :
            pygame.draw.line(window,'grey', (i * cell_h, 0), (i * cell_h, width), 2)

        #Update de la fenetre
        pygame.display.update()


    clock.tick(tick_rate)
