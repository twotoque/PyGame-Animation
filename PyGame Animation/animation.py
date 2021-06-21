# By TwoToque (Reddit: u/kazoosportacus ; Discord: EndQuote#2696 ; e-mail: creepersrock28@gmail.com)
# Created in Toronto, Ontario, Canada for a Python 101 class culminating assignment
# See 
# Requires the Bahnshrift font, included in Windows 10 version 1709 and up. If you don't have the aforementioned operating system, feel free to change to a font akin to Bahnschrift or DIN 1451 for a closer looking experience.
# The code is not the greatest- expected coming from a class which we learnt this language within a span of two months. Tried my best and I'm quite proud of what I produced in a week. Yes- this can be improved upon, but this is the climax of what I learnt over this class. Thanks to me teacher, my friends, (which I will keep private for the sake of privacy) and the PyGame Discord server (https://discord.gg/5hg9x7Y7x3)
# Can't view this animation? Go to here for a YouTube version: https://www.youtube.com/watch?v=fzD-_cfd6QE
import pygame, time, math
from pygame.locals import *

# Step 1:  Setup game/animation.
pygame.init()
surfaceWidth  = 1000
surfaceHeight = 1000
surface = pygame.display.set_mode([surfaceWidth, surfaceHeight])
pygame.display.set_caption("Steve Goes Mining")
myFont  = pygame.font.SysFont("Bahnschrift", 60)
myFont2  = pygame.font.SysFont("Bahnschrift", 35)
myFont3 = pygame.font.SysFont("Bahnschrift", 20)
myFont4 = pygame.font.SysFont("Bahnschrift", 27)
white  = (255, 255, 255)
blue   = (0, 0, 255)
teil   = (0, 255, 255)
red    = (255, 0, 0)
green  = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0 ,0)
orange = (247, 91, 0)
gray = (101, 101, 101)
brown = (135, 98, 40)
graystone = (165, 165, 165)
scene = 0
talk1 = 0
image1 = pygame.image.load("minecraftgroundtexture.png")
image1transform = pygame.transform.scale (image1,(1000,200))
image1X = 0
image1Y = 615
image1direction = "right"
musicFile1 = "Happy MBB (No Copyright Music).wav"
musicFile2 = "Minecraft Footsteps - Sound Effect (HD).wav"
musicFile3 = "Mining Sound Effect.wav"
musicFile4 = "Intensemusic.wav"
musicFile5 = "lava.wav"
Speech1 = "stevesspeech1.wav"
Speech2 = "stevespeech2.wav"
Speech3 = "narratorspeech1.wav"
Speech4 = "dababyspeech1.wav"
Speech5 = "stevespeech3.wav"
Speech6 = "dababyspeech2.wav"
Speech7 = "stevespeech4.wav"
Speech8 = "narratorspeech2.wav"
Speech9 = "dababyspeech3.wav"
Speech10 = "stevespeech5.wav"
image2 = pygame.image.load("stevewalk.png")
image2transform = pygame.transform.scale (image2,(200,350))
image2X = -300
image2Y = 450
image2direction = "right"
coalmine = 0
lavafall = 0
mineshaft1 = pygame.image.load("minebackground1.png")
mineshaft1transform = pygame.transform.scale (mineshaft1,(1000,1000))
mineshaft2 = pygame.image.load("minebackground2.png")
mineshaft2transform = pygame.transform.scale (mineshaft2,(1000,1000))
mineshaft3 = pygame.image.load("minebackground3.png")
mineshaft3transform = pygame.transform.scale (mineshaft3,(1000,1000))
mineshaft4 = pygame.image.load("minebackgroundbottom1.png")
mineshaft4transform = pygame.transform.scale (mineshaft4,(1000,200))
mineshaft5 = pygame.image.load("minebackgroundbottom2.png")
mineshaft5transform = pygame.transform.scale (mineshaft5,(1000,400))
background = pygame.image.load("background2.png")
backgroundtransform = pygame.transform.scale (background,(1400,800))
backgroundtransformX = 0
backgroundtransformy = 0
image8 = pygame.image.load("dababy.png")
image8transform = pygame.transform.scale (image8,(200,350))
image8X = 200
image8Y = 800
image9 = pygame.image.load("dababywithdiamonds.png")
image9transform = pygame.transform.scale (image9,(200,350))
image3 = pygame.image.load("stevefront.png")
image3transform = pygame.transform.scale (image3,(200,350))
image3X = -300
image3Y = 450
image4 = pygame.image.load("stevehold.png")
image4transform = pygame.transform.scale (image4,(200,350))
image4X = -300
image4Y = 450
image5 = pygame.image.load("coalblock.png")
image5transform = pygame.transform.scale (image5,(200,200))
image6 = pygame.image.load("coalblock1.png")
image6transform = pygame.transform.scale (image6,(200,200))
image7 = pygame.image.load("coalblock2.png")
image7transform = pygame.transform.scale (image7,(200,200))
startbackground = pygame.image.load("startscreen.png")
startbackgroundtransform = pygame.transform.scale (startbackground,(1000,1000))
endbackground = pygame.image.load("theend.png")
endbackgroundtransform = pygame.transform.scale (endbackground,(1000,1000))
backgroundtransformX = 0
cornerRectX = 900
cornerRectXalt = 400
cornerRect2X = 600
cornerRect2Y = 0
cornerRect3Y = 0
cornerRect4X = 600
cornerRect4Y = 0
cornerRect5X = 0
sunRectX = 800
cornerRect2Y = 0
steveprofilepicture = pygame.image.load("steveprofile.png")
steveprofilepicturetransform = pygame.transform.scale (steveprofilepicture,(80,80))
narratorprofilepicture = pygame.image.load("narratorprofilepicture.png")
narratorprofilepicturetransform = pygame.transform.scale (narratorprofilepicture,(80,80))
unknownprofilepicture = pygame.image.load("unknownprofilepicture.png")
unknownprofilepicturetransform = pygame.transform.scale (unknownprofilepicture,(80,80))
dababyprofilepicture = pygame.image.load("dababyprofile.png")
dababyprofilepicturetransform = pygame.transform.scale (dababyprofilepicture,(80,80))
speechwords1= myFont4.render("What a nice day to go mining!", 1, white)
speechwords2 = myFont4.render("Oh nice! I found some coal blocks! It...", 1, white)
speechwords3 = myFont4.render("ain’t much, but at least it’s honest work!", 1, white)
speechwords4 = myFont4.render("Steve mines the coal blocks. Not soon...", 1, white)
speechwords5 = myFont4.render("after, he hears something.", 1, white)
speechwords6 = myFont4.render("Oh no I have trapped myself", 1, white)
speechwords7 = myFont4.render("Who is that?", 1, white)
speechwords8 = myFont4.render("Yo steve, I need some help!", 1, white)
speechwords9 = myFont4.render("Is that Rapper DaBaby? I will help you!", 1, white)
speechwords10 = myFont4.render("Steve places a stone block, thus...", 1, white)
speechwords11 = myFont4.render("saving DaBaby from the lavafall.", 1, white)
speechwords12 = myFont4.render("Yo thanks man, you’re the GOAT.", 1, white)
speechwords13 = myFont4.render("I’m going to give you a couple diamonds!", 1, white)
speechwords14 = myFont4.render("Let's goooo", 1, white)
creditwords1= myFont3.render("Steve:", 1, white)
creditwords2= myFont3.render("Narrator:", 1, white)
creditwords3= myFont3.render("???:", 1, white)
creditwords4= myFont3.render("DaBaby", 1, white)
theend = myFont.render("The end.", 1, white)
# Step 2:  Set up game loop and poll for events.
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_q):
        break
    elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
        break

# Step 3:  Update game and objects
    if scene == 0 or scene >= 12:
        backColor = blue
        print("By TwoToque | Reddit: u/kazoosportacus - Discord: EndQuote#2696")
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(musicFile1))
        words = myFont.render("Steve goes mining", 1, white)
        pause = 5
        startscreenrectangle  = (250, 300, 500, 100)
        startmenuwords = myFont.render("Start!", 1, white)
    elif scene == 1 and image2X <= 400:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(musicFile2))
        pygame.mixer.Channel(0).set_volume(0.3)
        backColor = teil
        cornerRectX = cornerRectX - 4
        cornerRectXalt = cornerRectXalt - 5
        sunRectX = sunRectX - 1
        cloud1 = (cornerRectX, 300, 200, 100)
        cloud2 = (cornerRectX + 20, 280, 200, 100)
        cloud3 = (cornerRectX + 10, 350, 200, 100)
        cloud4 = (cornerRectXalt + 150, 100, 200, 100)
        cloud5 = (cornerRectXalt + 140, 90, 200, 100)
        sun = (sunRectX + 170, 100, 100, 100)
        image2X = image2X + 20
        pause = 0.015
        backgroundtransformX = backgroundtransformX - 2
        speechbox1 = (300, 300, 600, 100)
        words = speechwords1
        credit = creditwords1
    elif scene == 1 and image2X == 400:
        backColor = teil
    elif scene == 1 and image2X <= 1001 and talk1 == 1:
        backColor = teil
        cloud1 = (cornerRectX, 300, 200, 100)
        cloud2 = (cornerRectX + 20, 280, 200, 100)
        cloud3 = (cornerRectX + 10, 350, 200, 100)
        cloud4 = (cornerRectXalt + 150, 100, 200, 100)
        cloud5 = (cornerRectXalt + 140, 90, 200, 100)
        sun = (sunRectX + 170, 100, 100, 100)
        backgroundtransformX = backgroundtransformX - 2
        image2X = image2X + 20
        pause = 0.015
        cornerRectX = cornerRectX - 4
        cornerRectXalt = cornerRectXalt - 5
        sunRectX = sunRectX - 1
        speechbox1 = (300, 300, 600, 100)
        words = speechwords2
        credit = creditwords1
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(Speech2))
    elif scene == 2 and image2X <= 200:
        image2X = image2X + 5
        arc1 = (350, 500, 50, 50)
        pause = 0.015
    elif scene == 2 and image2X >= 200:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(musicFile3))
        words = speechwords3
    elif scene == 3 and coalmine > 1 and image2X >= 200:
        pygame.mixer.Channel(3).set_volume(0)
        words = speechwords4
        credit = creditwords2
        pause = 2
    elif scene == 3 and coalmine == 4 and image2X >= 700:
        speechbox1 = (300, 300, 600, 100)
        coalmine == 5
    elif scene == 3 and coalmine == 5 and image2X >= 700:
        speechbox1 = (300, 300, 600, 100)
        credit = creditwords1
        words = speechwords7
        image2X = -300
        scene == 4
    elif scene == 4 and image2X < 400:
        image2X = image2X + 100
        cornerRect3Y = cornerRect3Y + 20
        words = speechwords8
        credit = creditwords4
        speechbox2 = (430, 300, 550, 100)
        speechbox1 = (130, 300, 600, 100)
        rectangle3 = (600, 0, 200, cornerRect3Y)
    elif scene == 4 and image2X >= 400:
        cornerRect3Y = cornerRect3Y + 20
        rectangle3 = (600, 0, 200, cornerRect3Y)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech7))
        pause = 3
        scene = 5
    elif scene == 6:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech8))
        rectangle4 = (600, cornerRect3Y, 200, 75)
    elif scene == 8:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech9))
    elif scene == 10:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech10))
    elif scene == 11:
        backColor = blue
        words = myFont.render("The end", 1, white)
        pause = 5

# Step 4:  Draw on surface/window
    if scene == 0 or scene >= 12:
        surface.fill(backColor)
        surface.blit(startbackgroundtransform, (0, 0))
        surface.blit(words, ([250, 50]))
        pygame.draw.rect(surface, gray, startscreenrectangle, 0)
        surface.blit(startmenuwords, ([400, 310]))
        scene = 1
    elif scene == 1 and image2X < 400:
        surface.fill(backColor)
        pygame.draw.rect(surface, white, cloud1, 0)
        pygame.draw.rect(surface, white, cloud2, 0)
        pygame.draw.rect(surface, white, cloud3, 0)
        pygame.draw.rect(surface, white, cloud4, 0)
        pygame.draw.rect(surface, white, cloud5, 0)
        pygame.draw.rect(surface, yellow, sun, 0)
        surface.blit(backgroundtransform, (backgroundtransformX, 0))
        surface.blit(image1transform, (0, 800))
        surface.blit(image2transform, (image2X, image2Y))
    elif scene == 1 and image2X == 400:
        surface.fill(backColor)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech1))
        pygame.mixer.Channel(1).set_volume(0)
        pygame.draw.rect(surface, white, cloud1, 0)
        pygame.draw.rect(surface, white, cloud2, 0)
        pygame.draw.rect(surface, white, cloud3, 0)
        pygame.draw.rect(surface, white, cloud4, 0)
        pygame.draw.rect(surface, white, cloud5, 0)
        pygame.draw.rect(surface, yellow, sun, 0)
        surface.blit(backgroundtransform, (backgroundtransformX, 0))
        surface.blit(image1transform, (0, 800))
        surface.blit(image3transform, (500, 450))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (270, 310))
        surface.blit(credit, ([360, 320]))
        surface.blit(words, ([360, 340]))
        pause = 2
        talk1 = 1
    elif scene == 1 and image2X <= 1000 and talk1 == 1:
        surface.fill(backColor)
        pygame.draw.rect(surface, white, cloud1, 0)
        pygame.draw.rect(surface, white, cloud2, 0)
        pygame.draw.rect(surface, white, cloud3, 0)
        pygame.draw.rect(surface, white, cloud4, 0)
        pygame.draw.rect(surface, white, cloud5, 0)
        pygame.draw.rect(surface, yellow, sun, 0)
        surface.blit(backgroundtransform, (backgroundtransformX, 0))
        surface.blit(image1transform, (0, 800))
        surface.blit(image2transform, (image2X, 450))
    elif scene == 1 and image2X >= 1000 and talk1 == 1:
        scene = 2
        image2X = 0
    elif scene == 2 and image2X <= 200:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image2transform, (image2X, 450))
        surface.blit(image5transform, (400, 400))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (270, 310))
        surface.blit(credit, ([360, 320]))
        surface.blit(words, ([360, 340]))
    elif scene == 2 and image2X >= 200 and coalmine == 0:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image4transform, (200, 450))
        pygame.draw.line(surface, brown, (375, 495), (375, 580), 5)
        pygame.draw.arc(surface, gray, arc1, 0, 3.14, 8)
        surface.blit(image5transform, (400, 400))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (270, 310))
        surface.blit(credit, ([360, 320]))
        surface.blit(words, ([360, 340]))
        pause = 2.5
        coalmine = 1
    elif scene == 2 and image2X >= 200 and coalmine == 1:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image4transform, (200, 450))
        pygame.draw.line(surface, brown, (375, 495), (375, 580), 5)
        pygame.draw.arc(surface, gray, arc1, 0, 3.14, 8)
        surface.blit(image6transform, (400, 400))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (270, 310))
        surface.blit(credit, ([360, 320]))
        surface.blit(words, ([360, 340]))
        pause = 2.5
        coalmine = 2
        scene = 3
    elif scene == 3 and image2X >= 200 and coalmine == 2:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(Speech3))
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image4transform, (200, 450))
        pygame.draw.line(surface, brown, (375, 495), (375, 580), 5)
        pygame.draw.arc(surface, gray, arc1, 0, 3.14, 8)
        surface.blit(image7transform, (400, 400))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(narratorprofilepicturetransform, (270, 310))
        surface.blit(creditwords2, ([360, 320]))
        surface.blit(speechwords4, ([360, 340]))
        pause = 3
        coalmine = 3
    elif scene == 3 and image2X >= 200 and coalmine == 3:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image4transform, (200, 450))
        pygame.draw.line(surface, brown, (375, 495), (375, 580), 5)
        pygame.draw.arc(surface, gray, arc1, 0, 3.14, 8)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(narratorprofilepicturetransform, (270, 310))
        surface.blit(creditwords2, ([360, 320]))
        surface.blit(speechwords5, ([360, 340]))
        pause = 2
        coalmine = 4
    elif scene == 3 and coalmine == 4 and image2X < 700:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(musicFile4))
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(musicFile5))
        image2X = image2X + 20
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image2transform, (image2X, 450))
        pause = 0.015
    elif scene == 3 and coalmine == 4 and image2X >= 700:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(Speech4))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(unknownprofilepicturetransform, (270, 310))
        surface.blit(creditwords3, ([360, 320]))
        surface.blit(speechwords6, ([360, 340]))
        coalmine = 5
    elif scene == 3 and coalmine == 5 and image2X >= 700:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech5))
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft1transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft4transform, (0, 0))
        surface.blit(image3transform, (700, 450))
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (270, 310))
        surface.blit(creditwords1, ([360, 320]))
        surface.blit(speechwords7, ([360, 340]))
        image2X = -300
        scene = 4
    elif scene == 4 and image2X <= 400 and lavafall == 0:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Speech6))
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft2transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        surface.blit(image2transform, (image2X, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox2, 0)
        surface.blit(dababyprofilepicturetransform, (400, 310))
        surface.blit(creditwords4, ([500, 320]))
        surface.blit(speechwords8, ([500, 340]))
        lavafall = 1
    elif scene == 4 and image2X < 400:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft2transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (100, 310))
        surface.blit(creditwords1, ([200, 320]))
        surface.blit(speechwords9, ([200, 340]))
        surface.blit(image2transform, (image2X, 450))
    elif scene == 4 and image2X > 400:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft2transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        surface.blit(image2transform, (image2X + 50, 450))
        lavafall = 3
    elif scene == 4 and lavafall == 3:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft2transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (100, 310))
        surface.blit(creditwords1, ([200, 320]))
        surface.blit(speechwords9, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        pause = 3
        scene = 5
    elif scene == 5:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft2transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (100, 310))
        surface.blit(creditwords1, ([200, 320]))
        surface.blit(speechwords9, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        scene = 6
    elif scene == 6:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft3transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(narratorprofilepicturetransform, (100, 310))
        surface.blit(creditwords2, ([200, 320]))
        surface.blit(speechwords10, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        pygame.draw.rect(surface, black, rectangle4, 0)
        pause = 3
        scene = 7
    elif scene == 7:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(musicFile1))
        pygame.mixer.Channel(4).set_volume(0)
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft3transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(narratorprofilepicturetransform, (100, 310))
        surface.blit(creditwords2, ([200, 320]))
        surface.blit(speechwords11, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        pygame.draw.rect(surface, black, rectangle4, 0)
        pause = 3
        scene = 8
    elif scene == 8:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft3transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image8transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(dababyprofilepicturetransform, (100, 310))
        surface.blit(creditwords4, ([200, 320]))
        surface.blit(speechwords12, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        pygame.draw.rect(surface, black, rectangle4, 0)
        pause = 3
        scene = 9
    elif scene == 9:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft3transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image9transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(dababyprofilepicturetransform, (100, 310))
        surface.blit(creditwords4, ([200, 320]))
        surface.blit(speechwords13, ([200, 340]))
        surface.blit(image4transform, (image2X, 450))
        pygame.draw.rect(surface, black, rectangle4, 0)
        pause = 3
        scene = 10
    elif scene == 10:
        surface.fill(backColor)
        surface.blit(words, ([250, 50]))
        surface.blit(mineshaft3transform, (0, 0))
        surface.blit(mineshaft4transform, (0, 800))
        surface.blit(mineshaft5transform, (0, 0))
        surface.blit(image9transform, (600, 450))
        pygame.draw.rect(surface, orange, rectangle3, 0)
        pygame.draw.rect(surface, gray, speechbox1, 0)
        surface.blit(steveprofilepicturetransform, (100, 310))
        surface.blit(creditwords4, ([200, 320]))
        surface.blit(speechwords14, ([200, 340]))
        surface.blit(image3transform, (image2X, 450))
        pygame.draw.rect(surface, black, rectangle4, 0)
        pause = 3
        scene = 11
    elif scene == 11:
        surface.fill(backColor)
        surface.blit(endbackgroundtransform, (0, 0))
        surface.blit(theend, ([250, 50]))
        pause = 3
        scene = 12
# Step 5:  Show/display surface
    pygame.display.flip()
    time.sleep(pause)
pygame.display.update()
pygame.display.quit()
quit()
