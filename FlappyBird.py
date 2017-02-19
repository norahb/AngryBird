import pygame, sys, pygame.mixer
from random import randint
from pygame.locals import *
from Tkinter import *
import datetime
import time
import para

pygame.init()

"""_____BUILD WINDOW_____"""
screen = pygame.display.set_mode(para.size)
pygame.display.set_caption("Flappy Bird")
screen.blit(para.introbg,(0,0))


"""____CLOCK AND GAP____"""
clock = pygame.time.Clock()
global global_gap
global_gap = 150


"""_____OBJECTS____"""
class Bird:
    def __init__(self, screen, birdPos, birdVel,bird, pipe) :
        self.screen = screen
        self.birdPos = birdPos
        self.birdVel = birdVel
        self.bird = bird
        self.pipe = pipe



    def show(self) :
        self.screen.blit(self.bird , [self.birdPos[0],self.birdPos[1]])

    def update_day(self,times):
        global pipeVel,score
        ####MAKE THE SUN MOVE###
        self.screen.blit( para.sun,(para.xsun_org+float(times)*0.5,0))
        self.show()
        

        ##DEAD CONDITION####DOWN PIPE####UPPER PIPE####GROUND##:##SKY##
        if self.birdPos[0] + birdSize[0] >= self.pipe.pipePos [0] \
           and self.birdPos[1] + birdSize[1]-10 >= self.pipe.pipeSize[1] + space \
           and self.birdPos[0] < self.pipe.pipePos[0] + self.pipe.pipeSize[0]\
           or (self.birdPos[0] + birdSize[0]  >= self.pipe.pipePos [0] \
               and self.birdPos[1] + 10 <= self.pipe.pipeSize[1] \
               and self.birdPos[0] < self.pipe.pipePos[0] + self.pipe.pipeSize[0]) \
               or(self.birdPos[1] + birdSize[1]-15 >= ground)\
               or(self.birdPos[1]  <  skyh):
            self.birdVel = 0
            pipeVel = 0
            restart(score)

  
         
        self.birdPos[1] += self.birdVel
    
        if pipeVel == 2.5 and self.birdPos[0] > self.pipe.pipePos[0]+self.pipe.pipeSize[0] and self.birdPos[0] < self.pipe.pipePos[0]+self.pipe.pipeSize[0]+3:
            score += 1
        elif pipeVel == 5.5 and self.birdPos[0] > self.pipe.pipePos[0]+self.pipe.pipeSize[0] and self.birdPos[0] < self.pipe.pipePos[0]+self.pipe.pipeSize[0]+6:
            score += 1
        
        

    def update_night(self,times):
        global pipeVel,score

        ####MAKE THE MOON MOVE####
        self.screen.blit( para.moon,(para.xsun_org+float(times)*0.5,0))
   
        if self.birdPos[0] + birdSize[0] >= self.pipe.pipePos [0] \
           and self.birdPos[1] + birdSize[1]-10 >= self.pipe.pipeSize[1] + space \
           and self.birdPos[0] < self.pipe.pipePos[0] + self.pipe.pipeSize[0]\
           or (self.birdPos[0] + birdSize[0]  >= self.pipe.pipePos [0] \
               and self.birdPos[1] + 10 <= self.pipe.pipeSize[1] \
               and self.birdPos[0] < self.pipe.pipePos[0] + self.pipe.pipeSize[0]):
            para.crash.play()
        
        else:
            self.show()

        screen.blit(para.bolt,(self.pipe.pipePos[0],self.pipe.pipeSize[1]),(para.i*102,0,102,global_gap))
        para.i+=1
        if para.i==10:
            para.i=0

        ######DEAD CODITION#######PIPE GAP####GROUND####SKY##
        if (self.birdPos[0] + birdSize[0] >= self.pipe.pipePos [0] \
            and self.birdPos[1]+birdSize[1] > self.pipe.pipeSize[1] \
            and  self.birdPos[1] < self.pipe.pipeSize[1]+space \
            and self.birdPos[0] - 15 < self.pipe.pipePos[0] + self.pipe.pipeSize[0])\
            or (self.birdPos[1] + birdSize[1]-15 >= ground)\
            or(self.birdPos[1]  <  skyh):
            restart(score)
            self.birdVel = 0
            pipeVel = 0
            

        self.birdPos[1] += self.birdVel
            


        if pipeVel == 2.5 and self.birdPos[0] > self.pipe.pipePos[0]+self.pipe.pipeSize[0] and self.birdPos[0] < self.pipe.pipePos[0]+self.pipe.pipeSize[0]+3:
            score += 1
        elif pipeVel == 5.5 and self.birdPos[0] > self.pipe.pipePos[0]+self.pipe.pipeSize[0] and self.birdPos[0] < self.pipe.pipePos[0]+self.pipe.pipeSize[0]+6:
            score += 1
        
        
        

class Pipe:

    def __init__(self, screen, pipePos, pipeSize , pipe1, pipe2, b_x1=para.background_org1,b_x2=para.background_org2):
        self.screen = screen
        self.pipePos = pipePos
        self.pipeSize = pipeSize
        self.pipe1 = pipe1
        self.pipe2 = pipe2
        self.b_x1 = b_x1
        self.b_x2 = b_x2
        
    def show(self):
        self.pipe1 = pygame.transform.scale(para.pipeup, (pipeSize))
        self.pipe2 = pygame.transform.scale(para.pipedown, (pipeSize[0],size[1] - (pipeSize[1] + space)))
        self.screen.blit(self.pipe1, [self.pipePos[0], self.pipePos[1]])
        self.screen.blit(self.pipe2, [self.pipePos[0], self.pipeSize[1] + space] )

    def update(self):
        global pipeVel
        self.screen.blit( para.background, [self.b_x1,0])
        self.screen.blit( para.background, [self.b_x2,0])
        #####PIPE DISAPER
        if self.pipePos[0] < - self.pipeSize[0]: 
            self.pipePos [0] = size[0]
            self.pipeSize [1] = randint(0,para.sizey-space)
            

        if self.b_x2 <= 0:
            self.b_x1 = para.background_org1
            self.b_x2 = para.backgroung_setorg2
        self.b_x1+=para.background_speed
        self.b_x2+=para.background_speed
        self.pipePos[0] -= pipeVel
        self.show()
        





    
"""______PRINT TEXTS______"""

def txt(message,size,x,y,c):
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, c)
    rect=text.get_rect()
    rect.center=(x,y)
    screen.blit(text, rect)

"""______SCORE BORAD PART_______"""
class ScoreBoard:
    def __init__(self,score):
        self.score = score

    def nameinput(self):
        def nameget():
            global name
            name =text_entry.get()
            if len(name) > 10 or len(name) == 0:
                root.destroy()
                nameinput()
            else:
                root.destroy()
        root = Tk()
        root.title('INPUT NAME')
        root.resizable(False,False)
        root.geometry('+200+200')

        e = StringVar()
        labelc = Label(root,text = 'Congratulations! You are in the top five! \(^o^)/')
        label = Label(root,text = 'Please type your name there,no more that 10 character and at less 1 character')
        text_entry = Entry(root,textvariable = e)
        e.set('Anonymity')
        button = Button(root,text = 'OK',command=nameget)
        labelc.pack()
        label.pack()
        text_entry.pack()
        button.pack()
        root.mainloop()


    def ask(self):
        ####ASK AFTER OVER THE GAME###
        screen.blit(para.SBbg,(0,0))
        self.ask_word()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.Scorelist()
                        return
                    if event.key == pygame.K_RETURN:
                        return                   
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def Scorelist(self):
        #####TO READ BEFORE SCORE###
        scorelist=[]
        readlist=open("text/Scorelist.txt")
        for item in readlist.readlines():
            scorelist+=eval(item),
        ####PLAYER INPUT NAME, ONLY WHEN PLAYER'S SCORE CAN GET INTO TOP 5###
        if self.score == -1:
            newScorelist = scorelist[0:para.TOPNUMBER]
        elif len(scorelist) < para.TOPNUMBER  or scorelist[-1]['score'] < self.score:
            global name
            name=''
            self.nameinput()
            #####IN CASE PLAYER CLOSE THE "NAMEINPUT" WINDOWS
            if len(name) == 0:
                name = 'NoName'
            newscore=[{'name':name,'score':self.score,'time':str(datetime.datetime.now())[0:19]}]
            scorelist+=newscore[0],
            ###TO SORT SCORELIST BY HIGH SCORE
            scorelist=sorted(scorelist,key= lambda item:item['score'])
            scorelist.reverse()
            ##CREAT A NEW LIST WHICH ONLY HAVE TOP 5
            newScorelist=scorelist[0:para.TOPNUMBER]

            ###TO SAVE NEW SCORELIST IN TXT. AND IT CAN BE USED BY NEXT TIME
            savedlist=open('text/Scorelist.txt','w')
            for item in newScorelist:
                savedlist.write(str(item)+'\n')
            savedlist.close
        else:
            newScorelist = scorelist[0:para.TOPNUMBER]
        ###PRINT NEW LIST THER
        wloc_y=150
        screen.blit(para.SBbg,(0,0))
        screen.blit(para.SB,(para.sizex/2-350,0))
        self.title()
        for item in newScorelist:
            wloc_y+=40
            self.txt(item['name'],30,para.sizex/4+10,wloc_y,para.black)
            self.txt(item['score'],30,para.sizex/2-40,wloc_y,para.black)
            self.txt(item['time'],30,para.sizex-280,wloc_y,para.black)
            pygame.display.flip()
        return
                    

        ###DEFINE AGAIN FOR EASIER MOVE THIS CLASS                
    def txt(self,message,size,x,y,c):
        font = pygame.font.SysFont(None, size)
        text = font.render(str(message), True, c)
        rect=text.get_rect()
        rect.center=(x,y)
        screen.blit(text, rect)
    def title(self):
        self.txt("NAME",40,para.sizex/4+10+1,140,para.black)
        self.txt("SCORE",40,para.sizex/2-40+1,140,para.black)
        self.txt("DATE",40,para.sizex-280+1,140,para.black)
        self.txt("NAME",40,para.sizex/4+10,140,para.red)
        self.txt("SCORE",40,para.sizex/2-40,140,para.green)
        self.txt("DATE",40,para.sizex-280,140,para.blue)
    def ask_word(self):
        self.txt("DO YOU WANT TO WATCH THE SCOREBOARD",40,para.sizex/2+1,150,para.black)
        self.txt("YOU MIGHT BE IN TOP 5!(SPACE)",40,para.sizex/2+1,225,para.black)
        self.txt("OR CONTINUE THE GAME?(ENTER)",40,para.sizex/2+1,300,para.black)
        self.txt("DO YOU WANT TO WATCH THE SCOREBOARD",40,para.sizex/2,150,para.white)
        self.txt("YOU MIGHT BE IN TOP 5!(SPACE)",40,para.sizex/2,225,para.white)
        self.txt("OR CONTINUE THE GAME?(ENTER)",40,para.sizex/2,300,para.white)
        self.txt("TIP:IF YOU CONTINUE THE GAME YOUR SCORE WOUNDN'T BE SAVED",20,para.sizex/2+1,350,para.black)
        self.txt("TIP:IF YOU CONTINUE THE GAME YOUR SCORE WOUNDN'T BE SAVED",20,para.sizex/2,350,para.white)
        

        pygame.display.flip()


"""----------------------------------------------"""

"""_______TUTOR______"""

class tutor:
    def __init__(self):
        pass
    def resize(self,picname,x,y):
        return pygame.transform.scale(picname, (x, y))

    def tutocont(self,picname,width,hight,sleeptime):
        screen.blit(self.resize(picname,width,hight),[0,0])
        pygame.display.flip()
        time.sleep(sleeptime)
        
    def tutorial(self):
        self.tutocont(para.tu1,para.sizex,para.sizey,5)
        self.tutocont(para.tu2,para.sizex,para.sizey,3)
        self.tutocont(para.tu3,para.sizex,para.sizey,3)
        self.tutocont(para.tu4,para.sizex,para.sizey,3)
        self.tutocont(para.tu5,para.sizex,para.sizey,3)
        self.tutocont(para.introbg_org,para.sizex,para.sizey,0)
        intro()


"""_______START THE GAME_____"""
def intro():
    intro=True
    pygame.mixer.music.load("sound/Beginning.wav")
    pygame.mixer.music.play(-1, 0.0)
    while intro:
        ##  GREETING
        txt("Press Enter to Start",75,para.sizex/2+1,450,para.black)
        txt("Press Enter to Start",75,para.sizex/2,450,para.white)
        txt("Press [1] to watch Tutor",50,para.sizex/2+1,500,para.black)
        txt("Press [1] to watch Tutor",50,para.sizex/2,500,para.white)
        txt("Press [2] to Setting",50,para.sizex/2+1,550,para.black)
        txt("Press [2] to Setting",50,para.sizex/2,550,para.white)
        ##  UPDATE TXT
        pygame.display.flip()      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    setting()
                if event.key == pygame.K_1:
                    showtutor = tutor()
                    showtutor.tutorial()

                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("sound/BeforeStart.ogg")
                    pygame.mixer.music.play(-1, 0.0)
                    gameloop()

        
"""_____RESTART THE GAME ______"""
def restart(score):
    pygame.mixer.music.stop()
    para.end.play()
    txt("Game over",75,para.sizex/2,200,para.red)
    txt("Your Score : "+str(score),75,para.sizex/2,300,para.red)
    pygame.display.flip()
    ##### THIS IS FOR PAUSING THIS SCREEN SO THAT NEXT PAGE COULD SHOW AFTER EFFECT SOUND FINISH
    clock.tick(0.3)
    creatboard = ScoreBoard(score)
    creatboard.ask()
    time.sleep(1)
    intro()


"""_______setting_____"""
def setting():
    global global_gap
    setting=True
    screen.blit(para.introbg,(0,0))
    txt('Press [1] for Easy Mode',40,para.sizex/2+1,para.sizey*2/3+30,para.black)
    txt('Press [2] for Hard Mode',40,para.sizex/2+1,para.sizey*2/3+70,para.black)
    txt('Press [TAB] to watch Score Board',40,para.sizex/2+1,para.sizey*2/3+110,para.black)
    txt('Press [SPACE] go back to Start Screen',40,para.sizex/2+1,para.sizey*2/3+150,para.black)
    txt('Press [1] for Easy Mode',40,para.sizex/2,para.sizey*2/3+30,para.white)
    txt('Press [2] for Hard Mode',40,para.sizex/2,para.sizey*2/3+70,para.white)
    txt('Press [TAB] to watch Score Board',40,para.sizex/2,para.sizey*2/3+110,para.white)
    txt('Press [SPACE] go back to Start Screen',40,para.sizex/2,para.sizey*2/3+150,para.white)
    pygame.display.flip()
    while setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                ####CHANGE THE MODE TO EASY
                if event.key == pygame.K_1:
                    global_gap = 150
                    screen.blit(para.introbg,(0,0))
                    intro()
                ####CHANGE THE MODE TO HARD
                if event.key == pygame.K_2:
                    global_gap = 110
                    screen.blit(para.introbg,(0,0))
                    intro()
                ####WATCH THE SCOREBOARD
                if event.key == pygame.K_TAB:
                    WatchSB = ScoreBoard(-1)
                    WatchSB.Scorelist()
                    intro()
                ####GO BACK TO TITLE
                if event.key == pygame.K_SPACE:
                    screen.blit(para.introbg,(0,0))
                    intro()    
                    

            


"""______MAIN FUNCTION_______"""
def gameloop():
##name the game loop to call for restart or other behavior
##ALSO CAN CREATE ANOTHER GAME LOOP FOR OTHER MODE
    global birdSize,pipeVel,pipeSize,space,ground,skyh,score,size
    size = para.size
    """____PIPE PARAMITERS____"""    
    pipeSize = [ para.xsize_org, para.ysize_org ] 
    pipePos = [ para.xloc_org, para.yloc_org]
    pipeVel = para.obspeed
    space = global_gap
    """____BIRD PARAMITERS____"""   
    birdSize = para.birdsize
    birdPos = [para.sizex/2, para.sizey/2] 
    birdVel = para.y_speed_org
    """____NPC BIRD PARAMITERS____""" 
    xa=para.sizex
    ya=randint(100,para.sizey-100)
    xn=para.sizex
    yn=randint(100,para.sizey-100)
    
    """____OTHER PARAMITERS____""" 
    ground = para.ground_org
    skyh = para.ceiling_org
    score = para.score_org

    
    pipe = Pipe(screen = screen , pipePos = pipePos, pipeSize = pipeSize ,pipe1 = para.pipeup, pipe2= para.pipeup)
    bird = Bird (screen  = screen , birdPos = birdPos ,birdVel=birdVel,bird = para.bird, pipe= pipe)
    score = para.score_org
    MOD = para.mod_org

    times = 0



    while True:
        times+=1
        pipe.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    para.fly.play()
                    bird.birdVel = para.y_speed_up
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    bird.birdVel = para.y_speed_down



        if MOD == 'DAY':
            bird.update_day(times)
            ##CHANGE MOD##
            if times >= para.looptimes:
                ###INCASE MOD CHANGED WHEN BIRD IN PIPE GAP##
                if bird.birdPos[0]+birdSize[0] > bird.pipe.pipePos [0] and bird.birdPos[0] < bird.pipe.pipePos [0]+15 + bird.pipe.pipeSize[0]:
                
                    pipe.b_x1-=para.background_speed
                    pipe.b_x2-=para.background_speed
                else:
                    MOD = 'NIGHT'
                    times = 0


        elif MOD == 'NIGHT':
            bird.update_night(times)
            ##CHANGE MOD##
            if times >= para.looptimes:
                ###INCASE MOD CHANGED WHEN BIRD IN PIPE##
                if bird.birdPos[0]+birdSize[0] > bird.pipe.pipePos [0] and bird.birdPos[0] < bird.pipe.pipePos [0]+15 + bird.pipe.pipeSize[0]:
                
                    pipe.b_x1-=para.background_speed
                    pipe.b_x2-=para.background_speed
                else:
                    MOD = 'DAY'
                    times = 0

         ##_____NPC BIRD PART_____"""
        if times > 200:
            screen.blit(para.aBird,(xa,ya))
            xa=xa-5
            ya+=randint(-10,10)
            if (bird.birdPos[0]< xa and xa< bird.birdPos[0]+40 and bird.birdPos[1]<ya and ya<bird.birdPos[1]+40) or (bird.birdPos[0]< xa+40 and xa+40< bird.birdPos[0]+40 and bird.birdPos[1]<ya+40 and ya+40<bird.birdPos[1]+40):
                pipeVel = 5.5 
                    
        if times > 600:
            screen.blit(para.nBird,(xn,yn))
            xn=xn-5
            yn+=randint(-10,10)
            ###          
            if (bird.birdPos[0]< xn and xn< bird.birdPos[0]+40 and bird.birdPos[1]<yn and yn<bird.birdPos[1]+40) or (bird.birdPos[0]< xn+40 and xn+40< bird.birdPos[0]+40 and bird.birdPos[1]<yn+40 and yn+40<bird.birdPos[1]+40):
                pipeVel =2.5

        if times >= 900:
            xa=para.sizex
            xn=para.sizex
        ########################

        
        txt("Score:"+str(score),75,120,50,para.black)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(para.fps)

intro()
