import pygame, random

pygame.font.init()
music='Tetris.mp3'
music_list=['Tetris.mp3', 'MUmusic.mp3', 'PCmusic.mp3', 'SHmusic.mp3', 'ABmusic.mp3']

blok_siz = 30
lin=1
l_play= (blok_siz+lin)*10
h_play=(blok_siz+lin)*20
l_tel= l_play+200
h_tel=h_play+100

x_top_e = (l_tel-l_play) // 2
y_top_e = (h_tel-h_play)-30

S = [['.....',
      '..00.',
      '.00..',
      '......',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.00..',
      '..00.',
      '.....',
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
      '.00..',
      '.00..',
      '.....',
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
        if s==I:
            self.y=-2
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

def draw_score(tela,score, topx=x_top_e):
    s_font=pygame.font.SysFont("Calibri", blok_siz)
    pygame.draw.rect(tela, (100,100,100), ((topx-25-(blok_siz//2)*5,y_top_e+(blok_siz//2+lin)*5+10),((blok_siz//2+lin)*5+20,(blok_siz//2+lin)*5-10)))
    tela.blit(s_font.render('Score:', True, (225,225,255)), (topx-25-(blok_siz//2)*5+2,y_top_e+(blok_siz//2+lin)*6))
    tela.blit(s_font.render(str(int(score)), True, (225,225,255)), (topx-25-(blok_siz//2)*5+2,y_top_e+(blok_siz//2+lin)*8))
    pass

def warning(tela, cond, topx=x_top_e):
    if cond:
        w_font=pygame.font.SysFont("Arial", int(blok_siz*0.8))
        pygame.draw.rect(tela, (255,0,0), ((topx-25-(blok_siz//2)*5,y_top_e+(blok_siz//2+lin)*10+10),((blok_siz//2+lin)*5+20,(blok_siz//2+lin)*3-10)))
        tela.blit(w_font.render('INCOMING', True, (255,225,0)), (topx-25-(blok_siz//2)*5+1,y_top_e+(blok_siz//2+lin)*11))
    else:
        pygame.draw.rect(tela, (58,58,58), ((topx-25-(blok_siz//2)*5,y_top_e+(blok_siz//2+lin)*10+10),((blok_siz//2+lin)*5+20,(blok_siz//2+lin)*3-10)))

def can_send(grid, n):
    for i in range(n):
        ic=0
        for j in grid[i]:
            if j==(0,0,0):
                ic+=1
        if ic==len(grid[i]):
            n-=1
        if n<=0:
            return True
    return False

def send_lines(grid, n):
    hole=random.choice([x for x in range(10)])
    for i in range(n):
        grid.pop(0)
        grid.append([(130,130,130) if x!=hole else (0,0,0) for x in range(10)])        

def draw_waiting(tela,wl, topx=x_top_e):
    for i,s in enumerate(wl):
        pygame.draw.rect(tela, (100,100,100), ((topx+l_play+10,y_top_e+(blok_siz//2+lin)*5*i+10*i),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
        for j in range(5):
            for k in range(5):
                if s[0][j][k]=='.':
                    pygame.draw.rect(tela, (0,0,0), ((topx+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                else:
                    pygame.draw.rect(tela, coresl[formsl.index(s)], ((topx+l_play+10+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*5*i+10*i+j*(blok_siz//2+lin)),(blok_siz//2,blok_siz//2)))
                    
def draw_swap(tela,s=[['.....','.....','.....','.....','.....']], topx=x_top_e):
    pygame.draw.rect(tela, (100,100,100), ((topx-10-(blok_siz//2)*5,y_top_e),((blok_siz//2+lin)*5,(blok_siz//2+lin)*5)))
    for j in range(5):
        for k in range(5):
            if s[0][j][k]=='.':
                pygame.draw.rect(tela, (0,0,0), ((topx-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
            else:
                pygame.draw.rect(tela, coresl[formsl.index(s)], ((topx-10-(blok_siz//2)*5+k*(blok_siz//2+lin) , y_top_e+(blok_siz//2+lin)*j),(blok_siz//2,blok_siz//2)))
                    
def is_valid(gd,pç):
    for j in range(5):
        for i in range(5):
            if pç.s[pç.rot][i][j]=='0' and not(pç.y+i-2<0):
                if (pç.x+j-2)<0 or (pç.x+j-2)>=10:
                    return False
                if (pç.y+i-2)*(blok_siz+1)>=h_play:
                    return False
                if gd[pç.y+i-2][pç.x+j-2]!=(0,0,0):
                    return False
            if pç.s[pç.rot][i][j]=='0' and pç.y+i-2<0:
                if (pç.x+j-2)*(blok_siz+1)<0 or (pç.x+j-2)*(blok_siz+1)>=l_play:
                    return False
    return True

def is_dead(peça):
    for j in range(5):
        for i in range(5):
            if peça.s[peça.rot][i][j]=='0' and peça.y+i-2<0:
                return True
    return False

def rpç_choose(rformsl, flst=[]):
    random.shuffle(rformsl)
    r=random.choice(rformsl)
    ic=0
    for p in flst:
        if r==p:
            ic+=1
    if ic>=2:
        return(rpç_choose(rformsl, flst))
    if ic==1 and random.choice([1,2])==1:
        return(rpç_choose(rformsl, flst))
    return(r)

def add_peça(grid, peça):
    effect = pygame.mixer.Sound('PieceDown.mp3')
    effect.play()
    for i in range(5):
        for j in range(5):
            if peça.s[peça.rot][i][j]=='0':
                grid[peça.y+i-2][peça.x+j-2]=peça.clr
                
def draw_grid(tela,grid, topx=x_top_e):
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(tela, grid[i][j], ((topx+j*(blok_siz+lin),y_top_e+i*(blok_siz+lin)),(blok_siz,blok_siz)))
                
def draw_peça(tela,peça, topx=x_top_e):
    for i in range(5):
            for j in range(5):
                if peça.s[peça.rot][i][j]=='0' and (peça.y+i-2)*(blok_siz+1)>=0:
                    pygame.draw.rect(tela, peça.clr, ((topx+(peça.x+j-2)*(blok_siz+1),y_top_e+(peça.y+i-2)*(blok_siz+1)), (blok_siz,blok_siz)))
                    
def write(tela, font, words, nx, ny, color=(255, 255, 255), topx=x_top_e):
    tela.blit(font.render(words, True, color), (topx+int((blok_siz+lin)*nx),y_top_e+int((blok_siz+lin)*ny)))
    
def add_score(c_l_cleard, lvl, combo):
    if c_l_cleard==1:
        return 40*(lvl+1)*(1+0.5*combo)
    elif c_l_cleard==2:
        return 100*(lvl+1)*(1+0.5*combo)
    elif c_l_cleard==3:
        return 300*(lvl+1)*(1+0.5*combo)
    else:
        return 300*c_l_cleard*(lvl+1)*(1+0.5*combo)    
    
def game():
    pygame.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
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
    GameOver= True
    next=-1
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
            score+=add_score(c_l_cleard, lvl, combo)
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
                    if is_dead(peça):
                        play=False
                        break
                    add_peça(grid,peça)
                    peça=piece(waitl[0])
                    chgs=0
                    waitl.pop(0)
                    waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                    draw_waiting(tela, waitl)
                    insis=False
                    t_insis=0
                    combin=False
        
        rlog.tick()

        draw_grid(tela, grid)
        
        draw_peça(tela, peça)
        
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
                        if is_dead(peça):
                            play=False
                            break
                        add_peça(grid,peça)
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
                    if is_dead(peça):
                        play=False
                        break
                    add_peça(grid,peça)
                    peça=piece(waitl[0])
                    chgs=0
                    waitl.pop(0)
                    waitl.append(rpç_choose(rformsl, waitl+[peça.s]))
                    draw_waiting(tela, waitl)
                    combin=False
            if event.type == pygame.QUIT:
                play=False
                GameOver=False
                break
        pygame.display.update()
    
    mfont=pygame.font.SysFont("Calibri", int(blok_siz*1.75))
    sfont=pygame.font.SysFont("Calibri", int(blok_siz*0.75))
    
    write(tela, mfont, 'Game Over', 1.2, -1.8, (255,0,0))
    write(tela, sfont, 'R: Restart', -3.1, 5.4, (255, 255, 0))
    write(tela, sfont, 'M: Main', -3.1, 6.2, (255, 255, 0))
    write(tela, sfont, '      Menu', -3.1, 7, (255, 255, 0))
    write(tela, sfont, 'Q: Quit', -3.1, 7.8, (255, 255, 0))
    pygame.display.update()
    bliptime=0
    
    while GameOver:
        rlog.tick()
        bliptime+=1
        if bliptime/1000>=0.35:
            bliptime=0
            if peça.clr==(0,0,0):
                peça.clr=coresl[formsl.index(peça.s)]
            else:
                peça.clr=(0,0,0)
        draw_peça(tela,peça)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    GameOver=False
                    break
                if event.key == pygame.K_r:
                    GameOver= False
                    next=0
                    break
                if event.key == pygame.K_m:
                    GameOver= False
                    next=1
                    break
            if event.type == pygame.QUIT:
                GameOver=False
                break
    pygame.quit()
    
    if next==0:
        game()
    if next==1:
        main()

def game_pvp():
    usedkeys=[pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_c, pygame.K_v, pygame.K_RETURN, pygame.K_COMMA]
    pygame.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Tretris")
    tela = pygame.display.set_mode((l_tel*2+blok_siz*5,h_tel))
    x_top_2=x_top_e+int(blok_siz*11.5)+l_play
    tela.fill((58,58,58))
    grid1=grid_make()
    grid2=grid_make()
    waitl1=[rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl)]
    waitl2=[rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl),rpç_choose(rformsl)]
    draw_waiting(tela, waitl1)
    draw_waiting(tela, waitl2, x_top_2)
    draw_swap(tela)
    draw_swap(tela, [['.....','.....','.....','.....','.....']], x_top_2)
    peça1=piece(rpç_choose(rformsl, waitl1))
    peça2=piece(rpç_choose(rformsl, waitl2))
    rlog=pygame.time.Clock()
    t_queda=0.50
    t_caindo1=0
    t_caindo2=0
    t_insis1=0
    t_insis2=0
    insis1=False
    insis2=False
    play1=True
    play2=True
    Swap_shape1=[]
    Swap_shape2=[]
    chgs1=0
    chgs2=0
    holup1=False
    score1=0
    combin1=False
    combo1=0
    holup2=False
    score2=0
    combin2=False
    combo2=0
    lvl=0
    draw_score(tela, score1)
    draw_score(tela, score2, x_top_2)
    GameOver= True
    next=-1
    t_game=0
    sendl1=[]
    sendl2=[]
    while play1 and play2:
        down1=False
        down2=False
        t_game+=1
        if t_game/1000==60:
            lvl+=1
            t_queda=t_queda*0.9
        
        t_caindo1+=1
        t_caindo2+=1
        if insis1:
            t_insis1+=1
        if t_caindo1/1000>t_queda:
            t_caindo1=0
            if holup1 and t_insis1<2500:
                holup1=False
            else:
                peça1.y+=1
                if not(is_valid(grid1, peça1)):
                    peça1.y-=1
                    if is_dead(peça1):
                        play1=False
                    else:
                        add_peça(grid1,peça1)
                        peça1=piece(waitl1[0])
                        chgs1=0
                        waitl1.pop(0)
                        waitl1.append(rpç_choose(rformsl, waitl1+[peça1.s]))
                        draw_waiting(tela, waitl1)
                        insis1=False
                        t_insis1=0
                        combin1=False
                        down1=True
                    
        if insis2:
            t_insis2+=1
        if t_caindo2/1000>t_queda:
            t_caindo2=0
            if holup2 and t_insis2<2500:
                holup2=False
            else:
                peça2.y+=1
                if not(is_valid(grid2, peça2)):
                    peça2.y-=1
                    if is_dead(peça2):
                        play2=False
                    else:
                        add_peça(grid2,peça2)
                        peça2=piece(waitl2[0])
                        chgs2=0
                        waitl2.pop(0)
                        waitl2.append(rpç_choose(rformsl, waitl2+[peça2.s]))
                        draw_waiting(tela, waitl2, x_top_2)
                        insis2=False
                        t_insis2=0
                        combin2=False
                        down2=True
        
        rlog.tick()

        draw_grid(tela, grid1)
        draw_peça(tela, peça1)
        
        draw_grid(tela, grid2, x_top_2)
        draw_peça(tela, peça2, x_top_2)
        
        if not(play1 and play2):
            break
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keysd=pygame.key.get_pressed()
                keys=[]
                for k in usedkeys:
                    if keysd[k]==1:
                        keys.append(k)
                if pygame.K_RIGHT in keys:
                    peça2.x+=1
                    if not(is_valid(grid2, peça2)):
                        peça2.x-=1
                if pygame.K_LEFT in keys:
                    peça2.x-=1
                    if not(is_valid(grid2, peça2)):
                        peça2.x+=1
                if pygame.K_DOWN in keys:
                    peça2.y+=1
                    if not(is_valid(grid2, peça2)):
                        peça2.y-=1
                        if is_dead(peça2):
                            play2=False
                            break
                        add_peça(grid2,peça2)
                        peça2=piece(waitl2[0])
                        chgs2=0
                        waitl2.pop(0)
                        waitl2.append(rpç_choose(rformsl, waitl2+[peça2.s]))
                        draw_waiting(tela, waitl2, x_top_2)
                        combin2=False
                        down2=True
                if pygame.K_UP in keys:
                    peça2.rotate()
                    if not(is_valid(grid2, peça2)):
                        tests2=0
                        found2=False
                        while tests2<peça2.h and not(found2):
                            peça2.x+=1
                            if is_valid(grid2,peça2):
                                found2=True
                                break
                            else:
                                peça2.x-=2
                            if is_valid(grid2,peça2):
                                found2=True
                                break
                            else:
                                peça2.x+=1
                            if peça2.s==I:
                                    peça2.x+=2
                                    if is_valid(grid2,peça2):
                                        found2=True
                                        break
                                    else:
                                        peça2.x-=2
                            if tests2==0:
                                peça2.y+=1
                                if is_valid(grid2, peça2):
                                    found2=True
                                    break
                                else:
                                    peça2.x+=1
                                    if is_valid(grid2,peça2):
                                        found2=True
                                        break
                                    else:
                                        peça2.x-=2
                                        if is_valid(grid2,peça2):
                                            found2=True
                                            break
                                        else:
                                            peça2.x+=1
                                            if peça2.s==I:
                                                peça2.x+=2
                                                if is_valid(grid2,peça2):
                                                    found2=True
                                                    break
                                                else:
                                                    peça2.x-=2
                                            peça2.y-=1
                            peça2.y-=1
                            if is_valid(grid2,peça2):
                                found2=True
                                break
                            tests2+=1
                        
                        if not(found2):
                            peça2.y+=tests2
                            peça2.rotate(-1)
                        else:
                            holup2=True
                            insis2=True
                if pygame.K_d in keys:
                    peça1.x+=1
                    if not(is_valid(grid1, peça1)):
                        peça1.x-=1
                if pygame.K_a in keys:
                    peça1.x-=1
                    if not(is_valid(grid1, peça1)):
                        peça1.x+=1
                if pygame.K_s in keys:
                    peça1.y+=1
                    if not(is_valid(grid1, peça1)):
                        peça1.y-=1
                        if is_dead(peça1):
                            play1=False
                            break
                        add_peça(grid1,peça1)
                        peça1=piece(waitl1[0])
                        chgs1=0
                        waitl1.pop(0)
                        waitl1.append(rpç_choose(rformsl, waitl1+[peça1.s]))
                        draw_waiting(tela, waitl1)
                        combin1=False
                        down1=True
                if pygame.K_w in keys:
                    peça1.rotate()
                    if not(is_valid(grid1, peça1)):
                        tests1=0
                        found1=False
                        while tests1<peça1.h and not(found1):
                            peça1.x+=1
                            if is_valid(grid1,peça1):
                                found1=True
                                break
                            else:
                                peça1.x-=2
                            if is_valid(grid1,peça1):
                                found1=True
                                break
                            else:
                                peça1.x+=1
                            if peça1.s==I:
                                    peça1.x+=2
                                    if is_valid(grid1,peça1):
                                        found1=True
                                        break
                                    else:
                                        peça1.x-=2
                            if tests1==0:
                                peça1.y+=1
                                if is_valid(grid1, peça1):
                                    found1=True
                                    break
                                else:
                                    peça1.x+=1
                                    if is_valid(grid1,peça1):
                                        found1=True
                                        break
                                    else:
                                        peça1.x-=2
                                        if is_valid(grid1,peça1):
                                            found1=True
                                            break
                                        else:
                                            peça1.x+=1
                                            if peça1.s==I:
                                                peça1.x+=2
                                                if is_valid(grid1,peça1):
                                                    found1=True
                                                    break
                                                else:
                                                    peça1.x-=2
                                            peça1.y-=1
                            peça1.y-=1
                            if is_valid(grid1,peça1):
                                found1=True
                                break
                            tests1+=1
                        
                        if not(found1):
                            peça1.y+=tests1
                            peça1.rotate(-1)
                        else:
                            holup1=True
                            insis1=True
                if pygame.K_c in keys and chgs1==0:
                    if Swap_shape1==[]:
                        Swap_shape1=peça1.s
                        peça1=piece(waitl1[0])
                        waitl1.pop(0)
                        waitl1.append(rpç_choose(rformsl, waitl1+[peça1.s]))
                        draw_waiting(tela, waitl1)
                    else:
                        temp1=Swap_shape1
                        Swap_shape1=peça1.s
                        peça1=piece(temp1)
                    draw_swap(tela,Swap_shape1)
                    chgs1+=1
                if pygame.K_COMMA in keys and chgs2==0:
                    if Swap_shape2==[]:
                        Swap_shape2=peça2.s
                        peça2=piece(waitl2[0])
                        waitl2.pop(0)
                        waitl2.append(rpç_choose(rformsl, waitl2+[peça2.s]))
                        draw_waiting(tela, waitl2, x_top_2)
                    else:
                        temp2=Swap_shape2
                        Swap_shape2=peça2.s
                        peça2=piece(temp2)
                    draw_swap(tela,Swap_shape2, x_top_2)
                    chgs2+=1
                        
                if pygame.K_v in keys:
                    while is_valid(grid1,peça1):
                        peça1.y+=1
                    peça1.y-=1
                    if is_dead(peça1):
                        play1=False
                        break
                    add_peça(grid1,peça1)
                    peça1=piece(waitl1[0])
                    chgs1=0
                    waitl1.pop(0)
                    waitl1.append(rpç_choose(rformsl, waitl1+[peça1.s]))
                    draw_waiting(tela, waitl1)
                    combin1=False
                    down1=True
                if pygame.K_RETURN in keys:
                    while is_valid(grid2,peça2):
                        peça2.y+=1
                    peça2.y-=1
                    if is_dead(peça2):
                        play2=False
                        break
                    add_peça(grid2,peça2)
                    peça2=piece(waitl2[0])
                    chgs2=0
                    waitl2.pop(0)
                    waitl2.append(rpç_choose(rformsl, waitl2+[peça2.s]))
                    draw_waiting(tela, waitl2, x_top_2)
                    combin2=False
                    down2=True
            if event.type == pygame.QUIT:
                play1=False
                play2=False
                GameOver=False
                break
        
        dsend1=0
        dsend2=0
        c_l_cleard1=0
        c_l_cleard2=0
        for i in range(len(grid1)):
            counter1=0
            counter2=0
            for j in range(len(grid1[i])):
                if grid2[i][j]!=(0,0,0):
                    counter2+=1
                if grid2[i][j]==(130,130,130):
                    dsend2+=1
                if grid1[i][j]!=(0,0,0):
                    counter1+=1
                if grid1[i][j]==(130,130,130):
                    dsend1+=1
            if counter1==len(grid1[i]):
                grid1.pop(i)
                grid1.insert(0,[(0,0,0) for x in range(10)])
                c_l_cleard1+=1
                combin1=True
            if counter2==len(grid2[i]):
                grid2.pop(i)
                grid2.insert(0,[(0,0,0) for x in range(10)])
                c_l_cleard2+=1
                combin2=True
        if c_l_cleard1>0:
            score1+=add_score(c_l_cleard1, lvl, combo1)
            draw_score(tela, score1)
            combo1+=1
            if c_l_cleard1-dsend1>=4:
                sendl1.append(c_l_cleard1-dsend1)
            elif c_l_cleard1-dsend1>0:
                if combo1>1:
                    sendl1.append(c_l_cleard1-dsend1)
                elif c_l_cleard1-dsend1>1:
                    sendl1.append(c_l_cleard1-dsend1-1)
        if down1:
            for n in sendl2:
                if can_send(grid1, n):
                    sendl2.pop(0)
                    send_lines(grid1, n)
                else:
                    send_lines(grid1, n)
                    play1=False
                    break
        if c_l_cleard2>0:
            score2+=add_score(c_l_cleard2, lvl, combo2)
            draw_score(tela, score2, x_top_2)
            combo2+=1
            if c_l_cleard2-dsend2>=4:
                sendl2.append(c_l_cleard2-dsend2)
            elif c_l_cleard2-dsend2>0:
                if combo2>1:
                    sendl2.append(c_l_cleard2-dsend2)
                elif c_l_cleard2-dsend2>1:
                    sendl2.append(c_l_cleard2-dsend2-1)
        if down2:
            for n in sendl1:
                if can_send(grid2, n):
                    sendl1.pop(0)
                    send_lines(grid2, n)
                else:
                    send_lines(grid2, n)
                    play2=False
                    break        
            
        warning(tela, sendl1!=[], x_top_2)
        warning(tela, sendl2!=[])
        if not(combin1):
            combo1=0
        if not(combin2):
            combo2=0
        
        pygame.display.update()
        
    mfont=pygame.font.SysFont("Calibri", int(blok_siz*1.75))
    sfont=pygame.font.SysFont("Calibri", int(blok_siz*0.75))
    
    if play1 and not play2:
        write(tela, mfont, 'You Win!', 2.05, -1.8, (255,0,0))
        write(tela, mfont, 'You Lose...', 1.8, -1.8, (255,0,0), x_top_2)
    elif not play1 and play2:
        write(tela, mfont, 'You Lose...', 1.8, -1.8, (255,0,0))
        write(tela, mfont, 'You Win!', 2.05, -1.8, (255,0,0), x_top_2)
    else:
        write(tela, mfont, 'Tecnical Tie.', 0.6, -1.8, (255,0,0))
        write(tela, mfont, 'Tecnical Tie.', 0.6, -1.8, (255,0,0), x_top_2)
        
    pygame.draw.rect(tela, (100,100,100), ((x_top_2+int((blok_siz+lin)*(-7.6)),y_top_e+int((blok_siz+lin)*5)), (int((blok_siz+lin)*3.6),int((blok_siz+lin)*4))))
    write(tela, sfont, 'R: Restart', -7.2, 5.4, (255, 255, 0), x_top_2)
    write(tela, sfont, 'M: Main', -7.2, 6.2, (255, 255, 0), x_top_2)
    write(tela, sfont, '      Menu', -7.2, 7, (255, 255, 0), x_top_2)
    write(tela, sfont, 'Q: Quit', -7.2, 7.8, (255, 255, 0), x_top_2)
    pygame.display.update()
    bliptime=0
    
    while GameOver:
        rlog.tick()
        bliptime+=1
        if bliptime/1000>=0.35:
            bliptime=0
            if play1 and not play2:
                if peça2.clr==(0,0,0):
                    peça2.clr=coresl[formsl.index(peça2.s)]
                else:
                    peça2.clr=(0,0,0)
                draw_peça(tela,peça2, x_top_2)
            elif not play1 and play2:
                if peça1.clr==(0,0,0):
                    peça1.clr=coresl[formsl.index(peça1.s)]
                else:
                    peça1.clr=(0,0,0)
                draw_peça(tela,peça1)
            else:
                if peça1.clr==(0,0,0):
                    peça1.clr=coresl[formsl.index(peça1.s)]
                else:
                    peça1.clr=(0,0,0)
                draw_peça(tela,peça1)
                if peça2.clr==(0,0,0):
                    peça2.clr=coresl[formsl.index(peça2.s)]
                else:
                    peça2.clr=(0,0,0)
                draw_peça(tela,peça2, x_top_2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    GameOver=False
                    break
                if event.key == pygame.K_r:
                    GameOver= False
                    next=0
                    break
                if event.key == pygame.K_m:
                    GameOver= False
                    next=1
                    break
            if event.type == pygame.QUIT:
                GameOver=False
                break
    
    pygame.quit()
    
    if next==0:
        game_pvp()
    if next==1:
        main()
    
def main():
    global music
    
    pygame.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    mfont=pygame.font.SysFont("Calibri", int(blok_siz*1.75))
    sfont=pygame.font.SysFont("Calibri", int(blok_siz*0.75))
    ifont=pygame.font.SysFont("Calibri", int(blok_siz*1.25))
    menuplay=True
    pygame.display.set_caption("Tretris")
    tela = pygame.display.set_mode((l_tel,h_tel))
    tela.fill((58,58,58))
    grid=grid_make()
    mpeça=piece(O,5,9)
    grid[19][0]=(255,0,0)
    grid[19][3]=(255,0,0)
    grid[19][6]=(255,0,0)
    grid[19][9]=(255,0,0)
    next=-1
    
    while menuplay:
    
        tela.fill((58,58,58))
        write(tela, mfont, 'Welcome to Tetris', -1.1, -1.8)
        
        if mpeça.y==19 and mpeça.x==2:
            grid[19][0]=(0,255,0)
            grid[19][3]=(0,255,0)
        elif mpeça.y==19 and mpeça.x==5:
            grid[19][6]=(0,255,0)
            grid[19][3]=(0,255,0)
        elif mpeça.y==19 and mpeça.x==8:
            grid[19][6]=(0,255,0)
            grid[19][9]=(0,255,0)
        else:
            grid[19][0]=(255,0,0)
            grid[19][3]=(255,0,0)
            grid[19][6]=(255,0,0)
            grid[19][9]=(255,0,0)
        
        draw_grid(tela, grid)
        
        if mpeça.y>=18 and mpeça.x<=3:
            write(tela, mfont, 'Single Player', 0.8, 2.2)
            write(tela, mfont, '(Classic Tetris)', 0.35, 4.2)
        elif mpeça.y>=18 and mpeça.x<=6:
            write(tela, mfont, 'Battle Mode', 0.85, 2.2)
            write(tela, ifont, '(Same keyboard 1v1)', 0.02, 4.2)
        elif mpeça.y>=18 and mpeça.x<=9:
            write(tela, ifont, 'Single Player:', 0.1, 0.1)
            write(tela, sfont, 'Move: ← ↓ →', 1, 1.5)
            write(tela, sfont, 'Rotate: ↑', 1, 2.5)
            write(tela, sfont, 'Change/Save Piece: C', 1, 3.5)
            write(tela, sfont, 'Insta-Drop: SpaceBar', 1, 4.5)
            write(tela, ifont, 'Multi Player:', 0.1, 6)
            write(tela, sfont, 'Player 1', 3, 7.2)
            write(tela, sfont, 'Player 2', 7, 7.2)
            write(tela, sfont, 'Move:', 0.05, 8.5)
            write(tela, sfont, 'A S D', 3.4, 8.5)
            write(tela, sfont, '← ↓ →', 7, 8.5)
            write(tela, sfont, 'Rotate:', 0.05, 9.5)
            write(tela, sfont, 'W', 3.82, 9.5)
            write(tela, sfont, '↑', 7.82, 9.5)
            write(tela, sfont, 'C./S. Piece:', 0.05, 10.5)
            write(tela, sfont, 'C', 3.95, 10.5)
            write(tela, sfont, "(comma)", 6.9, 10.2)
            write(tela, sfont, ",", 8, 10.7)
            write(tela, sfont, 'Insta-Drop:', 0.05, 11.5)
            write(tela, sfont, 'V', 3.95, 11.5)
            write(tela, sfont, "Enter", 7.3, 11.5)
            write(tela, sfont, 'Developed by Adam Nogueira, 1/21', -0.05, 13.5)
            write(tela, sfont, 'with Pygame (www.pygame.org)', 0.05, 14.5)
        else:
            tela.blit(mfont.render('Move:', True, (255,255,255)), (x_top_e+int((blok_siz+lin)*2.85),y_top_e+int((blok_siz+lin)*2.2)))
            tela.blit(mfont.render('↑', True, (255,255,255)), (x_top_e+int((blok_siz+lin)*4.25),y_top_e+int((blok_siz+lin)*4.2)))
            tela.blit(mfont.render('← ↓ →', True, (255,255,255)), (x_top_e+int((blok_siz+lin)*2.35),y_top_e+int((blok_siz+lin)*6.2)))
        
        if mpeça.y==19 and mpeça.x>5:
            tela.blit(sfont.render('Enter to Toggle Music', True, (255,255,255)), (x_top_e+int((blok_siz+lin)*1.9),y_top_e+int((blok_siz+lin)*16.2)))
        else:
            tela.blit(sfont.render('Enter to Select', True, (255,255,255)), (x_top_e+int((blok_siz+lin)*2.9),y_top_e+int((blok_siz+lin)*16.2)))
        tela.blit(sfont.render('Single', True, (255,255,255)), (x_top_e+blok_siz+lin*5,y_top_e+int((blok_siz+lin)*18.2)))
        tela.blit(sfont.render('Player', True, (255,255,255)), (x_top_e+blok_siz+lin*4,y_top_e+(blok_siz+lin)*19))
        
        write(tela, sfont, 'PVP', 4.45, 18.6)
        
        write(tela, sfont, 'Info &', 7.13, 18.2)
        write(tela, sfont, 'Contrls', 6.97, 19)
        
        for i in range(5):
            for j in range(5):
                if mpeça.s[mpeça.rot][i][j]=='0' and (mpeça.y+i-2)*(blok_siz+1)>=0:
                    pygame.draw.rect(tela, (58,58,58), ((x_top_e+(mpeça.x+j-2)*(blok_siz+1),y_top_e+(mpeça.y+i-2)*(blok_siz+1)), (blok_siz+lin,blok_siz+lin)))
                    pygame.draw.rect(tela, mpeça.clr, ((x_top_e+(mpeça.x+j-2)*(blok_siz+1),y_top_e+(mpeça.y+i-2)*(blok_siz+1)), (blok_siz,blok_siz)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mpeça.x+=1
                    if not(is_valid(grid, mpeça)):
                        mpeça.x-=1
                if event.key == pygame.K_LEFT:
                    mpeça.x-=1
                    if not(is_valid(grid, mpeça)):
                        mpeça.x+=1
                if event.key == pygame.K_DOWN:
                    mpeça.y+=1
                    if not(is_valid(grid, mpeça)):
                        mpeça.y-=1
                if event.key == pygame.K_UP:
                    mpeça.y-=1
                    if not(is_valid(grid, mpeça)):
                        mpeça.y+=1
                if event.key == pygame.K_RETURN:
                    if mpeça.y==19 and mpeça.x==2:
                        menuplay=False
                        next=0
                        break
                    if mpeça.y==19 and mpeça.x==5:
                        menuplay=False
                        next=1
                        break
                    if mpeça.y==19 and mpeça.x>5:
                        music=music_list[(music_list.index(music)+1)%len(music_list)]
                        pygame.mixer.music.load(music)
                        pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                menuplay=False
                break
                # sys.exit()
            
    pygame.quit()
    if next==0:
        game()
    if next==1:
        game_pvp()   
        
main()