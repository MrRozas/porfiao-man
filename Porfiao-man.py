import pygame
import time
import random

#Iniciamos el modulo
pygame.init()

#Detalles pantalla (Titulo e Icono de este)
pygame.display.set_caption("Porfiao-man 19")
icon= pygame.image.load('virus.png')
pygame.display.set_icon(icon)

#Funciones de choque con las paredes, y cambio de dirección del enemigo
def choque(x):
    if sprite1.rect.colliderect(x):
      sprite1.rect.left=oldx
      sprite1.rect.top= oldy
taim= 0
def choque2(x):
    global taim
    global speedy
    global speedx
    if esprite.rect.colliderect(x) and taim==0:
      taim=time.time()
      a= random.randint(0,1)
      if a==0:
          b=random.randint(0,1)
          if b==0:
            speedx=-6
            speedy=0
          if b==1:
            speedx=6
            speedy=0
      elif a==1:
          b=random.randint(0,1)
          if b==0:
              speedy=-6
              speedx=0
          if b==1:
              speedy=6
              speedx=0
      esprite.rect.left = oldenemyx
      esprite.rect.top = oldenemyy
    else:
        taim=0

    return taim
taim2=0
def choque3(x):
    global taim2
    global speedy1
    global speedx1
    if esprite1.rect.colliderect(x) and taim2==0:
      taim2=time.time()
      a= random.randint(0,1)
      if a==0:
          b=random.randint(0,1)
          if b==0:
            speedx1=-6
            speedy1=0
          if b==1:
            speedx1=6
            speedy1=0
      elif a==1:
          b=random.randint(0,1)
          if b==0:
              speedy1=-6
              speedx1=0
          if b==1:
              speedy1=6
              speedx1=0
      esprite1.rect.left = oldenemyx1
      esprite1.rect.top = oldenemyy1
    else:
        taim2=0

    return taim2
taim3=0
def choque4(x):
    global taim3
    global speedy2
    global speedx2
    if esprite2.rect.colliderect(x) and taim3==0:
      taim3=time.time()
      a= random.randint(0,1)
      if a==0:
          b=random.randint(0,1)
          if b==0:
            speedx2=-6
            speedy2=0
          if b==1:
            speedx2=6
            speedy2=0
      elif a==1:
          b=random.randint(0,1)
          if b==0:
              speedy2=-6
              speedx2=0
          if b==1:
              speedy2=6
              speedx2=0
      esprite2.rect.left = oldenemyx2
      esprite2.rect.top = oldenemyy2
    else:
        taim3=0

    return taim3
taim4=0
def choque5(x):
    global taim4
    global speedy3
    global speedx3
    if esprite3.rect.colliderect(x) and taim4==0:
      taim4=time.time()
      a= random.randint(0,1)
      if a==0:
          b=random.randint(0,1)
          if b==0:
            speedx3=-6
            speedy3=0
          if b==1:
            speedx3=6
            speedy3=0
      elif a==1:
          b=random.randint(0,1)
          if b==0:
              speedy3=-6
              speedx3=0
          if b==1:
              speedy3=6
              speedx3=0
      esprite3.rect.left = oldenemyx3
      esprite3.rect.top = oldenemyy3
    else:
        taim4=0

    return taim4

puntos=0
#Definimos la funcion vitamina, para que se vea el sprite y desaparezca al choque
def  vitamina(nombre,x,y,q):
      global puntos
      nombre = pygame.sprite.Sprite()
      nombre.imagen= pellet
      nombre.rect = pellet.get_rect()
      nombre.rect.top = y
      nombre.rect.left = x
      if nombre.rect.colliderect(sprite1):
          pantalla.blit(nada,(x,y))
          q=False
          puntos+=1
          return q
      else:
          pantalla.blit(nombre.imagen, nombre.rect)
          q=True
          return q

#Mostrar las figuras dibujadas en pantalla
def rectdib(q):
    pygame.draw.rect(pantalla, (0, 0, 0), q)

#Definimos la pantalla y las imagenes
pantalla=pygame.display.set_mode((1200,600))
background= pygame.image.load('backgroundrial.png')
medico= pygame.image.load('medico2.png')
mañalich= pygame.image.load('mañalich.png')
virus= pygame.image.load('virus.png')
pellet = pygame.image.load('vitamina.png')
nada = pygame.image.load('nada.png')
marco= pygame.image.load('marco.png')
marco2= pygame.image.load('marco2.png')
fotoinicio= pygame.image.load('Pantallainicio.png')
titulo= pygame.image.load('titulo.png')
linea= pygame.image.load('linearoja.png')
oms= pygame.image.load('oms.png')
covid= pygame.image.load('covid.png')
datos= pygame.image.load('datos.PNG')
cuadro= pygame.image.load('cuadrorojo.png')
youdied= pygame.image.load('youdied.png')
gameover= pygame.image.load('gameover.png')
#Imagenes jugador y valores de movimiento
imagen1 = pygame.image.load("humano2.png")
imagen2 = pygame.image.load("humano.png")
imagen3 = pygame.image.load("humano3.png")
vx=0
vy=0

#Musica
pygame.mixer.music.load('pactrap.wav')
muerte= pygame.mixer.Sound("death.wav")

#Funcion para los fps
reloj1=pygame.time.Clock()

#Definimos las paredes
r1=pygame.Rect(0,21,800,1)
r2=pygame.Rect(0,581,800,1)
r3=pygame.Rect(0,0,1,265)
r3_1=pygame.Rect(0,301,1,300)
r4=pygame.Rect(800,0,1,265)
r4_1=pygame.Rect(800,301,1,300)
re= pygame.Rect(800,265,50,1)
re2= pygame.Rect(800,301,50,1)
re3= pygame.Rect(850,265,1,36)
r5=pygame.Rect(48,57,90,36)
r6=pygame.Rect(200,57,126,36)
r7=pygame.Rect(477,57,126,36)
r8=pygame.Rect(660,57,95,36)
r9=pygame.Rect(382,22,37,71)
r10=pygame.Rect(48,129,90,22)
r11=pygame.Rect(660,129,95,22)
r12=pygame.Rect(290,129,221,22)
r13=pygame.Rect(382,152,37,51)
r14=pygame.Rect(197,129,36,135)
r15=pygame.Rect(230,188,90,15)
r16=pygame.Rect(570,129,36,135)
r17=pygame.Rect(480,188,90,15)
r18=pygame.Rect(0,190,138,19)
r19=pygame.Rect(110,204,28,51)
r20=pygame.Rect(0,250,138,15)
r21=pygame.Rect(660,190,140,23)
r22=pygame.Rect(660,200,39,65)
r23=pygame.Rect(689,230,111,35)
r24=pygame.Rect(290,240,65,10)
r25=pygame.Rect(290,240,17,80)
r26=pygame.Rect(290,310,218,10)
r27=pygame.Rect(445,240,65,10)
r28=pygame.Rect(493,240,17,80)
r29=pygame.Rect(0,300,139,23)
r30=pygame.Rect(100,310,39,65)
r31=pygame.Rect(0,340,111,35)
r32=pygame.Rect(197,300,36,75)
r33=pygame.Rect(570,300,36,75)
r34=pygame.Rect(660,300,140,23)
r35=pygame.Rect(660,310,39,65)
r36=pygame.Rect(689,340,111,35)
r37=pygame.Rect(290,355,218,20)
r38=pygame.Rect(382,365,37,62)
r39=pygame.Rect(200,410,126,23)
r40=pygame.Rect(477,410,126,23)
r41=pygame.Rect(48,410,90,23)
r42=pygame.Rect(105,420,39,65)
r43=pygame.Rect(660,410,95,23)
r44=pygame.Rect(660,420,37,65)
r45=pygame.Rect(290,476,221,10)
r46=pygame.Rect(382,495,37,45)
r47=pygame.Rect(0,470,48,19)
r48=pygame.Rect(755,470,45,20)
r49=pygame.Rect(197,476,36,64)
r50=pygame.Rect(570,476,36,64)
r51=pygame.Rect(48,526,278,13)
r52=pygame.Rect(477,526,278,13)
r53=pygame.Rect(400,270,1,10)



#Definimos el sprite del jugador
sprite1=pygame.sprite.Sprite()
sprite1.imagen= imagen1
sprite1.rect=imagen1.get_rect()
sprite1.rect.top=200
sprite1.rect.left=150

#Definimos el sprite del enemigo1
esprite =pygame.sprite.Sprite()
esprite.imagen= virus
esprite.rect=imagen1.get_rect()
esprite.rect.top=270
esprite.rect.left=370
speedx=0
speedy=-3

#Definimos el sprite del enemigo2
esprite1 =pygame.sprite.Sprite()
esprite1.imagen= virus
esprite1.rect=imagen1.get_rect()
esprite1.rect.top=270
esprite1.rect.left=400
speedx1=-3
speedy1=0

#Definimos el sprite del enemigo3
esprite2 =pygame.sprite.Sprite()
esprite2.imagen= virus
esprite2.rect=imagen1.get_rect()
esprite2.rect.top=265
esprite2.rect.left=400
speedx2=0
speedy2=3

#Definimos el sprite del enemigo4
esprite3 =pygame.sprite.Sprite()
esprite3.imagen= virus
esprite3.rect=imagen1.get_rect()
esprite3.rect.top=280
esprite3.rect.left=315
speedx3=0
speedy3=-3

#Variables con valor True para hacer cumplir una condición, luego sera utiliza para las vitaminas
q=True
e=True
r=True
w=True
t=True
y=True
u=True
i=True
o=True
p=True
a=True
s=True
d=True
f=True
g=True
h=True
j=True
k=True
l=True
ñ=True
z=True
x=True
c=True
v=True
b=True
n=True
m=True
qw=True
er=True
ty=True
ui=True
op=True
nm=True
df=True
gh=True
jk=True
lñ=True
zx=True
cv=True
q2=True
e2=True
rr=True
w2=True
t2=True
y2=True
u2=True
i2=True
o2=True
p2=True
a2=True
s2=True
d2=True
f2=True
g2=True
h2=True
j2=True
k2=True
l2=True
ñ2=True
z2=True
x2=True
c2=True
v2=True
b2=True
n2=True
m2=True
qw2=True
er2=True
ty2=True
ui2=True
op2=True
nm2=True
df2=True
gh2=True
jk2=True
lñ2=True
zx2=True
cv2=True
ui3=True
op3=True
nm3=True
df3=True
gh3=True
jk3=True
lñ3=True
zx3=True
cv3=True
cv4=True
zx4=True

#Fuente sistema/externa
fuentesistema= pygame.font.Font("zig.ttf.ttf",23)
fuentesistema2= pygame.font.Font("zig.ttf.ttf",20)

#Funcion para escribir con determinada fuente
def escribir(tamaño,texto,r,g,b,x,y):
    fuentesistema= pygame.font.Font("zig.ttf.ttf",tamaño)
    texto= fuentesistema.render(texto,0,(r,g,b))
    pantalla.blit(texto, (x, y))
def escribir2(tamaño,texto,r,g,b,x,y):
    fuentesistema= pygame.font.SysFont("Arial Black",tamaño)
    texto= fuentesistema.render(texto,0,(r,g,b))
    pantalla.blit(texto, (x, y))

#Variables utiles
salir=False
aux=1
tiemporial=0
vida=1
impacto=False
condiciontiempo = False
debug=False
error=0
sonido=False

#Empieza a sonar la musica
pygame.mixer.music.play(10)

#Ciclo infinito
while salir!=True:

    #Contador de tiempo
    tiempo = int(pygame.time.get_ticks()/1000)
    #if debug==False:
    #    if tiempo!=1:
    #        debug==True
    #        if tiempo==2:
    #            error=1
    #        elif tiempo==3:
    #            error=2
    #        elif tiempo==4:
    #            error=3
    #    elif tiempo==1:
    #        debug=True

    if condiciontiempo==False:
      for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
            condiciontiempo=True
            #tiempo=0
            aux=1
            for i in range(0,101):
                if tiemporial==i:
                    error+= (i-1)
            tiemporial=0
          if event.type==pygame.QUIT:
              salir=True

    tiempo = (int(pygame.time.get_ticks()/1000))-error


    if aux==tiempo:
        tiemporial=tiempo
        aux+=1
    #print(tiemporial)


    #Definimos textos a escribir (en este caso, con variable actualizable)
    texto2 = fuentesistema.render(f"Puntos={puntos}", 0, (255, 255, 255),(0,0,0))
    texto1 = fuentesistema.render(f"Vidas={vida}", 0, (150, 0, 0))
    texto11 = fuentesistema.render(f"Vidas={vida}", 0, (0, 0, 0))


    #Para salir del juego y moverse
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            salir=True
        if impacto==False and condiciontiempo==True:
          if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT:
               vx+=-5
               sprite1.imagen= imagen2
             if event.key==pygame.K_RIGHT:
               vx+=5
               sprite1.imagen = imagen1
             if event.key==pygame.K_UP:
               vy+=-5
             if event.key==pygame.K_DOWN:
               vy+=5
        if event.type== pygame.KEYUP:
           if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
             vx=0
           if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
             vy=0
    #Condición si jugador con virus chocan, no movimiento y muerte con sonido
    if sprite1.rect.colliderect(esprite) or sprite1.rect.colliderect(esprite1) or sprite1.rect.colliderect(esprite2) or sprite1.rect.colliderect(esprite3):
        pygame.mixer.music.stop()
        if sonido==False:
           muerte.play()
           sonido=True
        impacto=True
        vida=0
        sprite1.imagen= imagen3
        vx=0
        vy=0

    #Posiciones en el momento
    oldx= sprite1.rect.left
    oldy= sprite1.rect.top

    oldenemyx= esprite.rect.left
    oldenemyy = esprite.rect.top

    oldenemyx1 = esprite1.rect.left
    oldenemyy1 = esprite1.rect.top

    oldenemyx2 = esprite2.rect.left
    oldenemyy2 = esprite2.rect.top

    oldenemyx3 = esprite3.rect.left
    oldenemyy3 = esprite3.rect.top

    #Movimiento sprite y enemigo
    if condiciontiempo==True:
      sprite1.rect.move_ip(vx,vy)
      esprite.rect.move_ip(speedx,speedy)
      esprite1.rect.move_ip(speedx1, speedy1)
      esprite2.rect.move_ip(speedx2, speedy2)
      esprite3.rect.move_ip(speedx3, speedy3)

    #Para que pueda ir por el tubo del medio(costados)
    if oldx==-30:
        sprite1.rect.left= 810
        sprite1.rect.top = 267
    elif oldx==815:
        sprite1.rect.left=0
        sprite1.rect.top=267

    #Choques con las funciones
    choque(r1)
    choque(r2)
    choque(r3)
    choque(r3_1)
    choque(r4)
    choque(r4_1)
    choque(re)
    choque(re2)
    choque(re3)
    choque(r5)
    choque(r6)
    choque(r7)
    choque(r8)
    choque(r9)
    choque(r10)
    choque(r11)
    choque(r12)
    choque(r13)
    choque(r14)
    choque(r15)
    choque(r16)
    choque(r17)
    choque(r18)
    choque(r19)
    choque(r20)
    choque(r21)
    choque(r22)
    choque(r23)
    choque(r24)
    choque(r25)
    choque(r26)
    choque(r27)
    choque(r28)
    choque(r29)
    choque(r30)
    choque(r31)
    choque(r32)
    choque(r33)
    choque(r34)
    choque(r35)
    choque(r36)
    choque(r37)
    choque(r38)
    choque(r39)
    choque(r40)
    choque(r41)
    choque(r42)
    choque(r43)
    choque(r44)
    choque(r45)
    choque(r46)
    choque(r47)
    choque(r48)
    choque(r49)
    choque(r50)
    choque(r51)
    choque(r52)
    choque(r53)

    # Choques enemigo
    choque2(r1)
    choque2(r2)
    choque2(r3)
    choque2(r3_1)
    choque2(r4)
    choque2(r4_1)
    choque2(re)
    choque2(re2)
    choque2(re3)
    choque2(r5)
    choque2(r6)
    choque2(r7)
    choque2(r8)
    choque2(r9)
    choque2(r10)
    choque2(r11)
    choque2(r12)
    choque2(r13)
    choque2(r14)
    choque2(r15)
    choque2(r16)
    choque2(r17)
    choque2(r18)
    choque2(r19)
    choque2(r20)
    choque2(r21)
    choque2(r22)
    choque2(r23)
    choque2(r24)
    choque2(r25)
    choque2(r26)
    choque2(r27)
    choque2(r28)
    choque2(r29)
    choque2(r30)
    choque2(r31)
    choque2(r32)
    choque2(r33)
    choque2(r34)
    choque2(r35)
    choque2(r36)
    choque2(r37)
    choque2(r38)
    choque2(r39)
    choque2(r40)
    choque2(r41)
    choque2(r42)
    choque2(r43)
    choque2(r44)
    choque2(r45)
    choque2(r46)
    choque2(r47)
    choque2(r48)
    choque2(r49)
    choque2(r50)
    choque2(r51)
    choque2(r52)
    choque2(r53)

    choque3(r1)
    choque3(r2)
    choque3(r3)
    choque3(r3_1)
    choque3(r4)
    choque3(r4_1)
    choque3(re)
    choque3(re2)
    choque3(re3)
    choque3(r5)
    choque3(r6)
    choque3(r7)
    choque3(r8)
    choque3(r9)
    choque3(r10)
    choque3(r11)
    choque3(r12)
    choque3(r13)
    choque3(r14)
    choque3(r15)
    choque3(r16)
    choque3(r17)
    choque3(r18)
    choque3(r19)
    choque3(r20)
    choque3(r21)
    choque3(r22)
    choque3(r23)
    choque3(r24)
    choque3(r25)
    choque3(r26)
    choque3(r27)
    choque3(r28)
    choque3(r29)
    choque3(r30)
    choque3(r31)
    choque3(r32)
    choque3(r33)
    choque3(r34)
    choque3(r35)
    choque3(r36)
    choque3(r37)
    choque3(r38)
    choque3(r39)
    choque3(r40)
    choque3(r41)
    choque3(r42)
    choque3(r43)
    choque3(r44)
    choque3(r45)
    choque3(r46)
    choque3(r47)
    choque3(r48)
    choque3(r49)
    choque3(r50)
    choque3(r51)
    choque3(r52)
    choque3(r53)

    choque4(r1)
    choque4(r2)
    choque4(r3)
    choque4(r3_1)
    choque4(r4)
    choque4(r4_1)
    choque4(re)
    choque4(re2)
    choque4(re3)
    choque4(r5)
    choque4(r6)
    choque4(r7)
    choque4(r8)
    choque4(r9)
    choque4(r10)
    choque4(r11)
    choque4(r12)
    choque4(r13)
    choque4(r14)
    choque4(r15)
    choque4(r16)
    choque4(r17)
    choque4(r18)
    choque4(r19)
    choque4(r20)
    choque4(r21)
    choque4(r22)
    choque4(r23)
    choque4(r24)
    choque4(r25)
    choque4(r26)
    choque4(r27)
    choque4(r28)
    choque4(r29)
    choque4(r30)
    choque4(r31)
    choque4(r32)
    choque4(r33)
    choque4(r34)
    choque4(r35)
    choque4(r36)
    choque4(r37)
    choque4(r38)
    choque4(r39)
    choque4(r40)
    choque4(r41)
    choque4(r42)
    choque4(r43)
    choque4(r44)
    choque4(r45)
    choque4(r46)
    choque4(r47)
    choque4(r48)
    choque4(r49)
    choque4(r50)
    choque4(r51)
    choque4(r52)
    choque4(r53)

    choque5(r1)
    choque5(r2)
    choque5(r3)
    choque5(r3_1)
    choque5(r4)
    choque5(r4_1)
    choque5(re)
    choque5(re2)
    choque5(re3)
    choque5(r5)
    choque5(r6)
    choque5(r7)
    choque5(r8)
    choque5(r9)
    choque5(r10)
    choque5(r11)
    choque5(r12)
    choque5(r13)
    choque5(r14)
    choque5(r15)
    choque5(r16)
    choque5(r17)
    choque5(r18)
    choque5(r19)
    choque5(r20)
    choque5(r21)
    choque5(r22)
    choque5(r23)
    choque5(r24)
    choque5(r25)
    choque5(r26)
    choque5(r27)
    choque5(r28)
    choque5(r29)
    choque5(r30)
    choque5(r31)
    choque5(r32)
    choque5(r33)
    choque5(r34)
    choque5(r35)
    choque5(r36)
    choque5(r37)
    choque5(r38)
    choque5(r39)
    choque5(r40)
    choque5(r41)
    choque5(r42)
    choque5(r43)
    choque5(r44)
    choque5(r45)
    choque5(r46)
    choque5(r47)
    choque5(r48)
    choque5(r49)
    choque5(r50)
    choque5(r51)
    choque5(r52)
    choque5(r53)


    reloj1.tick(25)

    #Relleno fondo pantalla
    pantalla.fill((255,255,255))

    #Dibujos para ir comprobando posicion paredes
    #rectdib(r1)
    #rectdib(r2)
    #rectdib(r3)
    #rectdib(r3_1)
    #rectdib(r4)
    #rectdib(r4_1)
    ##rectdib(re)
    ##rectdib(re2)
    ##rectdib(re3)
    #rectdib(r5)
    #rectdib(r6)
    #rectdib(r7)
    #rectdib(r8)
    #rectdib(r9)
    #rectdib(r10)
    #rectdib(r11)
    #rectdib(r12)
    #rectdib(r13)
    #rectdib(r14)
    #rectdib(r15)
    #rectdib(r16)
    #rectdib(r17)
    #rectdib(r18)
    #rectdib(r19)
    #rectdib(r20)
    #rectdib(r21)
    #rectdib(r22)
    #rectdib(r23)
    #rectdib(r24)
    #rectdib(r25)
    #rectdib(r26)
    #rectdib(r27)
    #rectdib(r28)
    #rectdib(r29)
    #rectdib(r30)
    #rectdib(r31)
    #rectdib(r32)
    #rectdib(r33)
    #rectdib(r34)
    #rectdib(r35)
    #rectdib(r36)
    #rectdib(r37)
    #rectdib(r38)
    #rectdib(r39)
    #rectdib(r40)
    #rectdib(r41)
    #rectdib(r42)
    #rectdib(r43)
    #rectdib(r44)
    #rectdib(r45)
    #rectdib(r46)
    #rectdib(r47)
    #rectdib(r48)
    #rectdib(r49)
    #rectdib(r50)
    #rectdib(r51)
    #rectdib(r52)
    #rectdib(r53)




    #Lo que se ira mostrando en pantalla
    pantalla.blit(background, (0, 0)) #Fondo
    # Funcion vitamina, las condiciones son para que desaparezca una vez hecha la colision
    if q == True:
        q = vitamina("lol", 20, 40, "q")
    if e == True:
        e = vitamina("nombre1", 165, 50, "e")
    if r == True:
        r = vitamina("nombre2", 340, 35, "r")
    if t == True:
        t = vitamina("nombre3", 445, 35, "t")
    if y == True:
        y = vitamina("nombre4", 630, 40, "y")
    if u == True:
        u = vitamina("nombre5", 780, 35, "u")
    if i == True:
        i = vitamina("nombre6", 660, 115, "i")
    if o == True:
        o = vitamina("nombre7", 445, 105, "o")
    if p == True:
        p = vitamina("nombre8", 705, 110, "p")
    if a == True:
        a = vitamina("nombre9", 20, 160, "a")
    if s == True:
        s = vitamina("nombre10", 160, 175, "s")
    if d == True:
        d = vitamina("nombre11", 340, 170, "d")
    if f == True:
        f = vitamina("nombre12", 535, 160, "f")
    if cv == True:
        cv = vitamina("nombre13", 630, 170, "cv")
    if h == True:
        h = vitamina("nombre14", 775, 165, "h")
    if g == True:
        g = vitamina("nombre15", 265, 225, "g")
    if j == True:
        j = vitamina("nombre16", 445, 220, "j")
    if w == True:
        w = vitamina("nombre17", 48, 270, "w")
    if k == True:
        k = vitamina("nombre18", 215, 275, "k")
    if l == True:
        l = vitamina("nombre19", 585, 275, "l")
    if ñ == True:
        ñ = vitamina("nombre20", 745, 280, "ñ")
    if x == True:
        x = vitamina("nombre22", 15, 390, "x")
    if c == True:
        c = vitamina("nombre23", 255, 395, "c")
    if v == True:
        v = vitamina("nombre24", 530, 395, "v")
    if b == True:
        b = vitamina("nombre25", 630, 385, "b")
    if n == True:
        n = vitamina("nombre26", 775, 392, "n")
    if m == True:
        m = vitamina("nombre27", 75, 448, "m")
    if qw == True:
        qw = vitamina("nombre28", 400, 450, "qw")
    if er == True:
        er = vitamina("nombre29", 115, 500, "er")
    if ty == True:
        ty = vitamina("nombre30", 235, 500, "ty")
    if ui == True:
        ui = vitamina("nombre31", 355, 515, "ui")
    if op == True:
        op = vitamina("nombre32", 445, 500, "op")
    if nm == True:
        nm = vitamina("nombre33", 540, 500, "nm")
    if df == True:
        df = vitamina("nombre34", 715, 505, "df")
    if gh == True:
        gh = vitamina("nombre35", 20, 550, "gh")
    if jk == True:
        jk = vitamina("nombre36", 235, 560, "jk")
    if lñ == True:
        lñ = vitamina("nombre37", 560, 565, "lñ")
    if zx == True:
        zx = vitamina("nombre38", 780, 560, "zx")
    if q2 == True:
        q2 = vitamina("nombre39", 100, 40, "q2")
    if e2 == True:
        e2 = vitamina("nombre40", 260, 40, "e2")
    if rr == True:
        rr = vitamina("nombre41", 545, 35, "rr")
    if t2 == True:
        t2 = vitamina("nombre42", 710, 35, "t2")
    if y2 == True:
        y2 = vitamina("nombre43", 30, 115, "y2")
    if u2 == True:
        u2 = vitamina("nombre44", 100, 115, "u2")
    if i2 == True:
        i2 = vitamina("nombre45", 175, 115, "i2")
    if o2 == True:
        o2 = vitamina("nombre46", 265, 105, "o2")
    if p2 == True:
        p2 = vitamina("nombre47", 355, 110, "p2")
    if a2 == True:
        a2 = vitamina("nombre48", 580, 115, "a2")
    if s2 == True:
        s2 = vitamina("nombre49", 780, 115, "s2")
    if d2 == True:
        d2 = vitamina("nombre50", 270, 170, "d2")
    if f2 == True:
        f2 = vitamina("nombre51", 710, 165, "f2")
    if cv2 == True:
        cv2 = vitamina("nombre52", 100, 280, "cv2")
    if h2 == True:
        h2 = vitamina("nombre53", 165, 280, "h2")
    if g2 == True:
        g2 = vitamina("nombre54", 690, 280, "g2")
    if j2 == True:
        j2 = vitamina("nombre55", 365, 225, "j2")
    if w2 == True:
        w2 = vitamina("nombre56", 545, 225, "w2")
    if k2 == True:
        k2 = vitamina("nombre57", 640, 225, "k2")
    if l2 == True:
        l2 = vitamina("nombre58", 165, 350, "l2")
    if ñ2 == True:
        ñ2 = vitamina("nombre59", 265, 350, "ñ2")
    if x2 == True:
        x2 = vitamina("nombre60", 408, 335, "x2")
    if c2 == True:
        c2 = vitamina("nombre61", 545, 350, "c2")
    if v2 == True:
        v2 = vitamina("nombre62", 635, 355, "v2")
    if b2 == True:
        b2 = vitamina("nombre63", 90, 400, "b2")
    if n2 == True:
        n2 = vitamina("nombre64", 165, 400, "n2")
    if m2 == True:
        m2 = vitamina("nombre65", 350, 400, "m2")
    if qw2 == True:
        qw2 = vitamina("nombre66", 450, 400, "qw2")
    if er2 == True:
        er2 = vitamina("nombre67", 715, 390, "er2")
    if ty2 == True:
        ty2 = vitamina("nombre68", 25, 445, "ty2")
    if ui2 == True:
        ui2 = vitamina("nombre69", 470, 445, "ui2")
    if op2 == True:
        op2 = vitamina("nombre70", 535, 445, "op2")
    if nm2 == True:
        nm2 = vitamina("nombre71", 635, 445, "nm2")
    if df2 == True:
        df2 = vitamina("nombre72", 725, 445, "df2")
    if gh2 == True:
        gh2 = vitamina("nombre73", 785, 445, "gh2")
    if jk2 == True:
        jk2 = vitamina("nombre74", 25, 510, "jk2")
    if lñ2 == True:
        lñ2 = vitamina("nombre75", 635, 510, "lñ2")
    if zx2 == True:
        zx2 = vitamina("nombre76", 785, 510, "zx2")
    if ui3 == True:
        ui3 = vitamina("nombre77", 130, 565, "ui3")
    if op3 == True:
        op3 = vitamina("nombre78", 190, 565, "op3")
    if nm3 == True:
        nm3 = vitamina("nombre79", 310, 565, "nm3")
    if df3 == True:
        df3 = vitamina("nombre80", 310, 565, "df3")
    if gh3 == True:
        gh3 = vitamina("nombre81", 360, 565, "gh3")
    if jk3 == True:
        jk3 = vitamina("nombre82", 435, 565, "jk3")
    if lñ3 == True:
        lñ3 = vitamina("nombre83", 500, 565, "lñ3")
    if zx3 == True:
        zx3 = vitamina("nombre84", 650, 565, "zx3")
    if zx4 == True:
        zx4 = vitamina("nombre85", 715, 565, "zx4")

    if puntos==84 or puntos==168 or puntos==252 or puntos==336 or puntos==420 or puntos==504 or puntos==588 or puntos==672 or puntos==756 or puntos==840 or puntos==924:
        if puntos>=999:
            puntos=999
        q = True
        e = True
        r = True
        w = True
        t = True
        y = True
        u = True
        i = True
        o = True
        p = True
        a = True
        s = True
        d = True
        f = True
        g = True
        h = True
        j = True
        k = True
        l = True
        ñ = True
        z = True
        x = True
        c = True
        v = True
        b = True
        n = True
        m = True
        qw = True
        er = True
        ty = True
        ui = True
        op = True
        nm = True
        df = True
        gh = True
        jk = True
        lñ = True
        zx = True
        cv = True
        q2 = True
        e2 = True
        rr = True
        w2 = True
        t2 = True
        y2 = True
        u2 = True
        i2 = True
        o2 = True
        p2 = True
        a2 = True
        s2 = True
        d2 = True
        f2 = True
        g2 = True
        h2 = True
        j2 = True
        k2 = True
        l2 = True
        ñ2 = True
        z2 = True
        x2 = True
        c2 = True
        v2 = True
        b2 = True
        n2 = True
        m2 = True
        qw2 = True
        er2 = True
        ty2 = True
        ui2 = True
        op2 = True
        nm2 = True
        df2 = True
        gh2 = True
        jk2 = True
        lñ2 = True
        zx2 = True
        cv2 = True
        ui3 = True
        op3 = True
        nm3 = True
        df3 = True
        gh3 = True
        jk3 = True
        lñ3 = True
        zx3 = True
        cv3 = True
        cv4 = True
        zx4 = True

    #Jugador y virus
    pantalla.blit(sprite1.imagen,sprite1.rect)
    pantalla.blit(esprite.imagen, esprite.rect)
    pantalla.blit(esprite1.imagen, esprite1.rect)
    pantalla.blit(esprite2.imagen, esprite2.rect)
    pantalla.blit(esprite3.imagen, esprite3.rect)

    pantalla.blit(medico, (800,0))  #Fondo
    pantalla.blit(mañalich, (760,350))  #Fondo
    pantalla.blit(titulo,(800,70)) #Titulo

    #Textos y marcos
    escribir(20, "", 0, 0, 0, 970, 400)
    escribir(20, "", 255, 255, 255, 972, 400)
    pantalla.blit(marco,(800,0))
    pantalla.blit(marco2,(1050,0))
    pantalla.blit(texto2, (820, 22))
    pantalla.blit(texto11,(1062,15))
    pantalla.blit(texto1, (1064, 15))
    
    escribir2(25, "INFORMACIÓN:",0,0,0,806,131)

    pantalla.blit(linea,(805,157))

    #Información que va saliendo con el tiempo

    if tiempo<15:
       escribir2(20, "El Nuevo Coronavirus COVID-19 es", 0, 0, 0, 804, 180)
       escribir2(20, "una cepa de la familia de", 0, 0, 0, 804, 205)
       escribir2(20, "coronavirus que no se había", 0, 0, 0, 804, 230)
       escribir2(20, "identificado antes en humanos.", 0, 0, 0, 804, 255)
       escribir2(20, "Es el nombre definitivo otorgado por", 0, 0, 0, 804, 280)
       escribir2(20, "la OMS.", 0, 0, 0, 804, 305)
       pantalla.blit(oms,(930,310))
       pantalla.blit(covid,(1050,310))


    elif tiempo>16 and tiempo<30:
        escribir2(20, "Los coronavirus son causantes de", 0, 0, 0, 804, 180)
        escribir2(20, "enfermedades por ejemplo desde un", 0, 0, 0, 804, 205)
        escribir2(20, "resfriado común hasta Insuficiencia", 0, 0, 0, 804, 230)
        escribir2(20, "Respiratoria Aguda Grave.", 0, 0, 0, 804, 255)
        escribir2(20, "El virus se transmite entre personas", 0, 0, 0, 804, 280)
        escribir2(20, "cuando tienen contacto cercano", 0, 0, 0, 804, 305)
        escribir2(20, "con algún enfermo.", 0, 0, 0, 804, 330)

    elif tiempo>31 and tiempo<50:
        escribir2(20, "Algunos síntomas:", 0, 0, 0, 804, 180)
        escribir2(20, "Fiebre, tos, dificultad respiratoria", 0, 0, 0, 804, 205)
        escribir2(20, "dolor toráxico, dolor de garganta", 0, 0, 0, 804, 230)
        escribir2(20, "al comer o tragar fluidos, pérdida", 0, 0, 0, 804, 255)
        escribir2(20, "del gusto y olfato, dolores muscula-", 0, 0, 0, 804, 280)
        escribir2(20, "res, etc.", 0, 0, 0, 804, 305)
        escribir2(20, "Estos síntomas se agravan de forma", 0, 0, 0, 804, 330)
        escribir2(20, "gradual y por eso deben ser tratados.", 0, 0, 0, 804, 355)

    elif tiempo>51 and tiempo<60:
        escribir2(20, "La mayoría de las estimaciones res-", 0, 0, 0, 804, 180)
        escribir2(20, "pecto el tiempo en que transcurre la", 0, 0, 0, 804, 205)
        escribir2(20, "infección por el virus y la aparición", 0, 0, 0, 804, 230)
        escribir2(20, "de síntomas oscilan entre 1 y 14", 0, 0, 0, 804, 255)
        escribir2(20, "días, y en general se sitúan en torno", 0, 0, 0, 804, 280)
        escribir2(20, "a cinco días.", 0, 0, 0, 804, 305)

    if tiempo>61 and tiempo<76:
        escribir2(20, "-Si tienes síntomas de", 0, 0, 0, 804, 180)
        escribir2(20, " enfermedad respiratoria, DEBES IR", 0, 0, 0, 804, 205)
        escribir2(20, " AL MEDICO.", 0, 0, 0, 804, 230)
    if tiempo>67 and tiempo<77:
        escribir2(20, "-Si tienes dificultades para respirar,", 0, 0, 0, 804, 255)
        escribir2(20, " DEBES IR A URGENCIAS.", 0, 0, 0, 804, 280)
    if tiempo>73 and tiempo<78:
        escribir2(20, "-Si tienes síntomas leves, como tos", 0, 0, 0, 804, 305)
        escribir2(20, " o dolor de garganta, pero sin fiebre,", 0, 0, 0, 804, 330)
        escribir2(20, " es recomendable que te cuides en", 0, 0, 0, 804, 355)
        escribir2(20, " casa.", 0, 0, 0, 804, 380)

    elif tiempo>79 and tiempo<94:
        escribir2(20,"Las medidas de prevención son: ",0,0,0,804,180)
        escribir2(20, "•Salir lo mínimo posible del hogar y", 0, 0, 0, 804, 205)
        escribir2(20," respetar la cuarentena.",0, 0, 0, 804, 230)
        escribir2(20, "•Cubrirse con pañuelo desechable o ", 0, 0, 0, 804,255)
        escribir2(20, "el antebrazo (no con la mano) la ", 0, 0, 0, 804, 280)
        escribir2(20, "nariz y la boca al estornudar o toser.", 0, 0, 0, 804, 305)

    elif tiempo>95 and tiempo<100:
        escribir2(20, "Las medidas de prevención son: ", 0, 0, 0, 804, 180)
        escribir2(20,"•Lavarse las manos frecuentemente ",0,0,0,804,205)
        escribir2(20, "con jabón o un desinfectante a base ", 0, 0, 0, 804, 230)
        escribir2(20,"de alcohol por más de 20 segundos.",0, 0, 0, 804, 255)
        escribir2(20, "•Mantener una distancia", 0, 0, 0, 804,280)
        escribir2(20, " mínima de 1 metro entre personas.", 0, 0, 0, 804, 305)

    elif tiempo>101 and tiempo<115:
        escribir2(23, "Las medidas de prevención son: ", 0, 0, 0, 804, 180)
        escribir2(23,"•Evitar tocarse los ojos, la",0,0,0,804,205)
        escribir2(23, " nariz y la boca.", 0, 0, 0, 804, 230)
        escribir2(23,"•No compartir utensilios ni ",0, 0, 0, 804, 255)
        escribir2(23, " cubiertos con otras personas.", 0, 0, 0, 804,280)

    elif tiempo>116 and tiempo<130:
        escribir2(23 , "Las medidas de prevención son: ", 0, 0, 0, 804, 180)
        escribir2(24,"•Evitar saludar con la mano ",0,0,0,804,205)
        escribir2(24, " o dar besos.", 0, 0, 0, 804, 230)
        escribir2(23,"•Permanecer en casa si tienes",0, 0, 0, 804, 255)
        escribir2(23, "sospechas de tener el covid-19.", 0, 0, 0, 804,280)

    elif tiempo>131 and tiempo<146:
        escribir2(20, "Todos tienen la posibilidad de adqui-", 0, 0, 0, 804, 180)
        escribir2(20, "rir el virus, siendo las que tienen", 0, 0, 0, 804, 205)
        escribir2(20, "más riesgo aquellas que tratan con", 0, 0, 0, 804, 230)
        escribir2(20, "personas contagiadas.", 0, 0, 0, 804, 255)
        escribir2(20, "El riesgo aumenta en la medida que", 0, 0, 0, 804, 280)
        escribir2(20, "la persona tiene más exposición social.", 0, 0, 0, 804, 305)
        escribir2(20, "social.", 0, 0, 0, 804, 330)

    elif tiempo>147 and tiempo<157:
        escribir2(23, "Se pide aún más cuidado a", 0, 0, 0, 804, 180)
        escribir2(23, "poblaciones de riesgo, ejemplo:", 0, 0, 0, 804, 205)
        escribir2(23, "adultos mayores y personas", 0, 0, 0, 804, 230)
        escribir2(23, "con enfermedades crónicas", 0, 0, 0, 804, 255)

    elif tiempo>158:
        pantalla.blit(datos,(800,190))


    #Pantalla de inicio, lo que aparece
    if condiciontiempo==False:
        pantalla.blit(fotoinicio,(0,-100))
        escribir(30,"Press any key to start",0,0,0,363,170)
        if tiemporial%2==0:
            escribir(30, "Press any key to start", 255, 255, 255, 363, 170)

        if tiemporial>0:
            escribir(20,"Este eres tu",255,255,255, 500,300)
        if tiemporial>1:
            escribir(20,", una persona irresponsable que",255,255,255,690,300)
        if tiemporial>2:
            escribir(20,"decidio salir de igual forma",255,255,255,500,325)
        if tiemporial>3:
            escribir(20," a pesar de",255,255,255,950,325)
        if tiemporial>4:
            escribir(20, "todas las recomendaciones y restricciones", 255, 255, 255, 500, 350)
        if tiemporial>5:
            escribir(20,"y de el esfuerzo de todos por frenar el",255,255,255,500,375)
        if tiemporial>6:
            escribir(20, "virus.......", 255, 255, 255, 500, 400)
        if tiemporial>9:
            escribir(20,"Ahora estas metido en un loop infinito del",255,255,255,500,440)
        if tiemporial>10:
            escribir(20,"cual no puedes salir.",255,255,255,500,460)
        if tiemporial>12:
            escribir(25,"Tu mision: SOBREVIVIR, escapar",255,255,255,500,500)
            escribir(25, "del virus y conseguir vitaminas", 255, 255, 255, 500, 520)

    #Lo que aparece cuando mueres
    if impacto==True:
        pantalla.blit(gameover,(100,0))
        pantalla.blit(youdied,(800,135))
        pantalla.blit(cuadro,(800,200))
        escribir(24,"No seas irresponsable,",255,255,255,804,220)
        escribir(73, "cuidate.", 255, 255, 255, 804, 240)
        escribir(26, "El virus lo paramos", 255,255,255,804,310)
        escribir(26, "entre todos.", 255, 255, 255, 804, 330)
        escribir(35,"#QuedateEnCasa",255,255,255,804,360)

    #Actualización pantalla
    pygame.display.update()


pygame.quit()