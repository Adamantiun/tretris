import pygame
# from pygame.locals import *
Black = (0, 0, 0)


def grid_make():
    return([[(0,0,0) for i in range(10)] for j in range(20)])

blok_siz = 30
lin=1
l_play= (blok_siz+lin)*10
h_play=(blok_siz+lin)*20
l_tel= l_play+200
h_tel=h_play+100

x_top_e = (l_tel-l_play) // 2
y_top_e = (h_tel-h_play)-30

# bg=pygame.image.load(r'C:\Users\Acer\PyGDep\MenuBG.jpg')
def main_menu():
    pygame.init()
    pixf=pygame.font.SysFont("Calibri", 30)
    # tela = pygame.display.set_mode((612,612))
    # tela.fill(WHITE)
    # tela.blit(bg, (0, 0))
    pygame.display.set_caption("Tretris")
    tela = pygame.display.set_mode((l_tel,h_tel))
    tela.fill((58,58,58))
    grid=grid_make()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(tela, grid[i][j], ((x_top_e+j*(blok_siz+lin),y_top_e+i*(blok_siz+lin)),(blok_siz,blok_siz)))
        
    tela.blit(pixf.render('Clique Para Sair', True, Black), (100,100))
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                # sys.exit()
main_menu()