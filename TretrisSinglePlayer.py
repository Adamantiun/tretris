import pygame, random

pygame.font.init()

blok_siz = 30
lin=1
l_play= (blok_siz+lin)*10
h_play=(blok_siz+lin)*20
l_tel= l_play+200
h_tel=h_play+100

x_top_e = (l_tel-l_play) // 2
y_top_e = (h_tel-h_play)-30

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

formsl = [S, Z, I, O, J, L, T]
rformsl=formsl[:]
coresl = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class piece:
    def __init__(self, s, x=5, y=-1, r=0):
        self.s=s
        self.x=x
        self.y=y
        self.rot=r
        self.clr=coresl[formsl.index(s)]
        if s==I:
            self.h=4
        elif s==O:
            self.h=2
        else:
            self.h=3
    
    def rotate(self, r=1):
        self.rot+=r
        self.rot=self.rot % len(self.s)

def grid_make():
    return([[(0,0,0) for i in range(10)] for j in range(20)])

def draw_score(tela,score):
    s_font=pygame.font.SysFont("Calibri", blok_siz)
    pygame.draw.rect(tela, (100,100,100), ((x_top_e-10-(blok_siz//2)*5,y_top_e+(blok_siz//2+lin)*5+10),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5-10)))
    tela.blit(s_font.render('Score:', True, (225,225,255)), (x_top_e-10-(blok_siz//2)*5+2,y_top_e+(blok_siz//2+lin)*6))
    tela.blit(s_font.render(str(int(score)), True, (225,225,255)), (x_top_e-10-(blok_siz//2)*5+2,y_top_e+(blok_siz//2+lin)*8))
    pass

def draw_waiting(tela,wl):
    for i,s in enumerate(wl):
        pygame.draw.rect(tela, (100,100,100), ((x_top_e+l_play+10,y_top_e+(blok_siz//2+lin)*5*i+10*i),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
        for j in range(5):
            for k in range(5):
                if s[0][j][k]=='.':
                    pygame.draw.rect(tela, (0,0,0), ((x_top_e+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                else:
                    pygame.draw.rect(tela, coresl[formsl.index(s)], ((x_top_e+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                    
def draw_swap(tela,s=[['.....','.....','.....','.....','.....']]):
    pygame.draw.rect(tela, (100,100,100), ((x_top_e-10-(blok_siz//2)*5,y_top_e),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
    for j in range(5):
        for k in range(5):
            if s[0][j][k]=='.':
                pygame.draw.rect(tela, (0,0,0), ((x_top_e-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
            else:
                pygame.draw.rect(tela, coresl[formsl.index(s)], ((x_top_e-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
                    
def is_valid(gd,pç):
    for j in range(5):
        for i in range(5):
            if pç.s[pç.rot][i][j]=='0' and not(pç.y+i-2<0):
                if (pç.x+j-2)*(blok_siz+1)<0 or (pç.x+j-2)*(blok_siz+1)>=l_play:
                    return False
                if (pç.y+i-2)*(blok_siz+1)>=h_play:
                    return False
                if gd[pç.y+i-2][pç.x+j-2]!=(0,0,0):
                    return False
            if pç.s[pç.rot][i][j]=='0' and pç.y+i-2<0:
                if (pç.x+j-2)*(blok_siz+1)<0 or (pç.x+j-2)*(blok_siz+1)>=l_play:
                    return False
    return True

def rpç_choose(rformsl, flst=[]):
    random.shuffle(rformsl)
    r=random.choice(rformsl)
    if r in flst:
        if random.choice([1,2,3,4,5])<=2:
            return(rpç_choose(rformsl, flst))
    return(r)
        
            
def game():
    pygame.init()
    pygame.display.set_caption("Tretris")
    tela = pygame.display.set_mode((l_tel,h_tel))
    tela.fill((58,58,58))
    grid=grid_make()
    waitl=[rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl)]
    draw_waiting(tela, waitl)
    draw_swap(tela)
    peça=piece(rpç_choose(rformsl, waitl))
    rlog=pygame.time.Clock()
    t_queda=0.50
    t_caindo=0
    t_insis=0
    insis=False
    play=True
    Swap_shape=[]
    chgs=0
    holup=False
    lines_cleard=0
    score=0
    combin=False
    combo=0
    lvl=0
    draw_score(tela, score)
    while play:
        c_l_cleard=0
        if lines_cleard>=5:
            lines_cleard-=5
            lvl+=1
            t_queda=t_queda*0.9
        for i in range(len(grid)):
            counter=0
            for j in range(len(grid[i])):
                if grid[i][j]!=(0,0,0):
                    counter+=1
            if counter==len(grid[i]):
                grid.pop(i)
                grid.insert(0,[(0,0,0) for x in range(10)])
                lines_cleard+=1
                c_l_cleard+=1
                combin=True
        if c_l_cleard>0:
            if c_l_cleard==1:
                score+=40*(lvl+1)*(1+0.5*combo)
            elif c_l_cleard==2:
                score+=100*(lvl+1)*(1+0.5*combo)
            elif c_l_cleard==3:
                score+=300*(lvl+1)*(1+0.5*combo)
            else:
                score+=300*c_l_cleard*(lvl+1)*(1+0.5*combo)
            draw_score(tela, score)
        if c_l_cleard>0:
            combo+=1
        if not(combin):
            combo=0
        t_caindo+=1
        if insis:
            t_insis+=1
        if t_caindo/1000>t_queda:
            t_caindo=0
            if holup and t_insis<2500:
                holup=False
            else:
                peça.y+=1
                if not(is_valid(grid, peça)):
                    peça.y-=1
                    if peça.y==-1:
                        peça.y+=1
                        break
                    for i in range(5):
                        for j in range(5):
                            if peça.s[peça.rot][i][j]=='0':
                                grid[peça.y+i-2][peça.x+j-2]=peça.clr
                    peça=piece(waitl[0])
                    chgs=0
                    waitl.pop(0)
                    waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                    draw_waiting(tela, waitl)
                    insis=False
                    t_insis=0
                    combin=False
        rlog.tick()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(tela, grid[i][j], ((x_top_e+j*(blok_siz+lin),y_top_e+i*(blok_siz+lin)),(blok_siz,blok_siz)))
        
        for i in range(5):
            for j in range(5):
                if peça.s[peça.rot][i][j]=='0' and (peça.y+i-2)*(blok_siz+1)>=0:
                    pygame.draw.rect(tela, peça.clr, ((x_top_e+(peça.x+j-2)*(blok_siz+1),y_top_e+(peça.y+i-2)*(blok_siz+1)), (blok_siz,blok_siz)))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    peça.x+=1
                    if not(is_valid(grid, peça)):
                        peça.x-=1
                if event.key == pygame.K_LEFT:
                    peça.x-=1
                    if not(is_valid(grid, peça)):
                        peça.x+=1
                if event.key == pygame.K_DOWN:
                    peça.y+=1
                    if not(is_valid(grid, peça)):
                        peça.y-=1
                        if peça.y==-1:
                            peça.y+=1
                            break
                        for i in range(5):
                            for j in range(5):
                                if peça.s[peça.rot][i][j]=='0':
                                    grid[peça.y+i-2][peça.x+j-2]=peça.clr
                        peça=piece(waitl[0])
                        chgs=0
                        waitl.pop(0)
                        waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                        draw_waiting(tela, waitl)
                        combin=False
                if event.key == pygame.K_UP:
                    peça.rotate()
                    if not(is_valid(grid, peça)):
                        tests=0
                        found=False
                        while tests<peça.h and not(found):
                            peça.x+=1
                            if is_valid(grid,peça):
                                found=True
                                break
                            else:
                                peça.x-=2
                            if is_valid(grid,peça):
                                found=True
                                break
                            else:
                                peça.x+=1
                            if peça.s==I:
                                    peça.x+=2
                                    if is_valid(grid,peça):
                                        found=True
                                        break
                                    else:
                                        peça.x-=2
                            if tests==0:
                                peça.y+=1
                                if is_valid(grid, peça):
                                    found=True
                                    break
                                else:
                                    peça.x+=1
                                    if is_valid(grid,peça):
                                        found=True
                                        break
                                    else:
                                        peça.x-=2
                                        if is_valid(grid,peça):
                                            found=True
                                            break
                                        else:
                                            peça.x+=1
                                            if peça.s==I:
                                                peça.x+=2
                                                if is_valid(grid,peça):
                                                    found=True
                                                    break
                                                else:
                                                    peça.x-=2
                                            peça.y-=1
                            peça.y-=1
                            if is_valid(grid,peça):
                                found=True
                                break
                            tests+=1
                        
                        if not(found):
                            peça.y+=tests
                            peça.rotate(-1)
                        else:
                            holup=True
                            insis=True
                if event.key == pygame.K_c and chgs==0:
                    if Swap_shape==[]:
                        Swap_shape=peça.s
                        peça=piece(waitl[0])
                        waitl.pop(0)
                        waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                        draw_waiting(tela, waitl)
                    else:
                        temp=Swap_shape
                        Swap_shape=peça.s
                        peça=piece(temp)
                    draw_swap(tela,Swap_shape)
                    chgs+=1
                if event.key == pygame.K_SPACE:
                    while is_valid(grid,peça):
                        peça.y+=1
                    peça.y-=1
                    if peça.y==-1:
                        peça.y+=1
                        break
                    for i in range(5):
                        for j in range(5):
                            if peça.s[peça.rot][i][j]=='0':
                                grid[peça.y+i-2][peça.x+j-2]=peça.clr
                    peça=piece(waitl[0])
                    chgs=0
                    waitl.pop(0)
                    waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                    draw_waiting(tela, waitl)
                    combin=False
            if event.type == pygame.QUIT:
                play=False
        pygame.display.update()
    pygame.quit()
    
# def add_peça(tela,grid,peça,waitl,play,chgs):
#     peça.y-=1
#     if peça.y==-1:
#         play=False
#     for i in range(5):
#         for j in range(5):
#             if peça.s[peça.rot][i][j]=='0':
#                 grid[peça.y+i-2][peça.x+j-2]=peça.clr
#     peça=piece(waitl[0])
#     chgs=0
#     waitl.pop(0)
#     waitl.append(random.choice(formsl))
#     draw_waiting(tela, waitl)

# game()

def main():
    pygame.init()
    mfont=pygame.font.SysFont("Calibri", int(blok_siz*1.75))
    # tela = pygame.display.set_mode((612,612))
    # tela.fill(WHITE)
    # tela.blit(bg, (0, 0))
    pygame.display.set_caption("Tretris")
    tela = pygame.display.set_mode((l_tel,h_tel))
    tela.fill((58,58,58))
    grid=grid_make()
    mpeça=piece(O,5,10)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(tela, grid[i][j], ((x_top_e+j*(blok_siz+lin),y_top_e+i*(blok_siz+lin)),(blok_siz,blok_siz)))
        
    tela.blit(mfont.render('Welcome to Tretris', True, (255,255,255)), (x_top_e-int(1.5*blok_siz),y_top_e-blok_siz*2))
    while True:
        for i in range(5):
            for j in range(5):
                if mpeça.s[mpeça.rot][i][j]=='0' and (mpeça.y+i-2)*(blok_siz+1)>=0:
                    pygame.draw.rect(tela, mpeça.clr, ((x_top_e+(mpeça.x+j-2)*(blok_siz+1),y_top_e+(mpeça.y+i-2)*(blok_siz+1)), (blok_siz,blok_siz)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
main()