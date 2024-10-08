import pygame
import random
# pygame setup
kutu= 64
kutu_sayi=(20,10)

ekran_boyutlari = (kutu_sayi[0]*kutu,kutu_sayi[1]*kutu)
pygame.init()
screen = pygame.display.set_mode(ekran_boyutlari)
clock = pygame.time.Clock()
running = True
white = (255,255,255)
red = (255,0,0)
mavi=(0,255,0)
yesil=(0,0,255)
yilan_kafa=[1,0]
vucut_list =[[0,0]]
sayac=0
skor = 0
yem_yer=[5,5]
yon = [1,0]
son_hareket=[1,0]
font = pygame.font.Font(None, 36)


def grid():
    for i in range(0,ekran_boyutlari[0],kutu):
        pygame.draw.line(screen,"black",(i,0),(i,ekran_boyutlari[1]),2)
    for i in range(0,ekran_boyutlari[1],kutu):
        pygame.draw.line(screen,"black",(0,i),(ekran_boyutlari[0],i),2)

def yilan():
    for i in vucut_list:
        pygame.draw.rect(screen,white,(i[0]*kutu,i[1]*kutu,kutu,kutu))

    pygame.draw.rect(screen,red,(yilan_kafa[0]*kutu,yilan_kafa[1]*kutu,kutu,kutu))

def yem_yeri():
    yem_yer[0] = random.randint(0,kutu_sayi[0]-1)
    yem_yer[1] = random.randint(0,kutu_sayi[1]-1)
    for i in vucut_list:
        if yem_yer[0] ==i[0] and yem_yer[1] ==i[1]:
            yem_yeri()
            break
    

def sifirla():
    global yilan_kafa
    global vucut_list
    global sayac
    global yem_yer
    global yon
    global son_hareket
    global skor
    yilan_kafa=[1,0]
    vucut_list =[[0,0]]
    sayac=0
    skor = 0
    yem_yeri()
    skor_yaz()
    yon = [1,0]
    son_hareket=[1,0]
def yem():    
    pygame.draw.rect(screen,"green",(yem_yer[0]*kutu,yem_yer[1]*kutu,kutu,kutu))
    
def skor_yaz():
    yazi = font.render("Skor = "+str(skor) , True, "yellow")
    screen.blit(yazi, (50, 10))


sifirla()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        sifirla()

    if keys[pygame.K_w] and son_hareket[1] != 1:
        yon[1]=-1
        yon[0]=0
    elif keys[pygame.K_s] and son_hareket[1] != -1:
        yon[1]=1
        yon[0]=0
    elif keys[pygame.K_a] and son_hareket[0] !=1:
        yon[0]=-1
        yon[1]=0
    elif keys[pygame.K_d] and son_hareket[0] != -1:
        yon[0]=1
        yon[1]=0
    
    if sayac==30:

        for i in range(len(vucut_list)-1,0,-1):
            vucut_list[i][0]=vucut_list[i-1][0]
            vucut_list[i][1]=vucut_list[i-1][1]
        vucut_list[0][0]=yilan_kafa[0]
        vucut_list[0][1]=yilan_kafa[1]

        son_hareket[0]=yon[0]
        son_hareket[1]=yon[1]
        yilan_kafa[0]+=1*yon[0]
        yilan_kafa[1]+=1*yon[1]
       
        for i in vucut_list:
            if yilan_kafa[0] == i[0] and yilan_kafa[1]==i[1]:
                sifirla()
        
        
        if yilan_kafa[0] ==-1:
            yilan_kafa[0] = kutu_sayi[0]-1
        
        if yilan_kafa[0] == kutu_sayi[0]:
            yilan_kafa[0] = 0
        
        if yilan_kafa[1] == -1:
            yilan_kafa[1] = kutu_sayi[1]-1
        
        if yilan_kafa[1] == kutu_sayi[1]:
            yilan_kafa[1] = 0
       
        if yilan_kafa[0] == yem_yer[0] and yilan_kafa[1] == yem_yer[1]:
            vucut_list.append([yem_yer[0],yem_yer[1]])
            skor+=1
            yem_yeri()
        

        
        sayac=0


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    yem()
    yilan()
    grid()
    skor_yaz()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    sayac+=1

pygame.quit()

