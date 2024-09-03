import os, pygame as pyg, Guiscalelib as gsl, Configlib as clib, time as t

#determine fixed filepath to operating directory for assets
opDir = os.path.dirname(os.path.realpath(__file__))
filepath = f'{opDir}\\Assets\\'

#start config lib and global cfg dict
cfg = clib.openCfg()

#set internal variables to file config ver
loggen = cfg["terminal"]["generate-log"]
verbosity = cfg["terminal"]["write-in-terminal"]

#import and start proportional graphics scaling lib
gsl.updateVals(cfg["window-settings"]["win-width"],cfg["window-settings"]["win-height"])

#start log generation and text beautification library
import Textlib
log = Textlib.log #instanciating log object
Textlib.log.__init__(log)
Textlib.terminfo('Started Log File and initialised terminal library',log,verbosity,loggen)
Textlib.terminfo('running terminal formatting test (if colors do not work you may be using a non ANSI compatible system)',log,verbosity,loggen)

#import and init pygame module
pyg.init()

#start window related variables
run = True
if cfg["window-settings"]["fullscreen"]:
    dispinfo = pyg.display.Info()
    win = pyg.display.set_mode((dispinfo.current_w, dispinfo.current_h),pyg.FULLSCREEN)
else:
    win = pyg.display.set_mode((cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]),pyg.RESIZABLE)

pyg.display.set_caption('Industry For State Development BETA')

#delta time frame cap variables
prvTime = t.time()
fps = cfg["graphics-settings"]["framerate-cap"]

pyg.display.set_caption('Industry For State Development BETA')
bg = pyg.image.load(f'{filepath}\\Background Images\\ISD_1920_1200_sunset_factory_TrueRes.png')
bg = pyg.transform.scale(bg,(cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]))
bgEnabled = True


#ui values
frame = 0
buttonColor = (102, 204, 255)
buttonHoverColor = (153, 204, 255)
textColor = (12, 12, 12)
smallfont = pyg.font.SysFont('Corbel',20)
buttonBuffer = []

#button shit
class button():

    instances = []
        
    def defaultInteraction():
        Textlib.terminfo("Button Without Assigned function pressed (function may be missing)",log,verbosity,loggen)

    #start button object with deafault configuration parameters
    def __init__(self,posx,posy,w,h,text="",img=None,selImg=None,col="#f0f0f0",selCol="#999999",textCol="#000000",onClick=defaultInteraction):
        funcH = gsl.percH(h)
        funcW = gsl.percW(w)
        self.rect = pyg.Rect(gsl.percW(posx)-(funcW/2),gsl.percH(posy)-(funcH/2),funcW,funcH)
        self.textSurf = smallfont.render(text,True,textCol)
        self.img = img
        self.selImg = selImg
        self.col = col
        self.selCol = selCol
        self.textCol = textCol
        self.text = text
        self.func = onClick
        self.posx = posx
        self.posy = posy
        self.widthP = w
        self.heightP = h
        button.instances.append(self)
    
    #update the rect object for button on changing of window resolution
    def updateRect(self):
        self.rect = pyg.Rect(gsl.percW(self.posx)-(gsl.percW(self.widthP)/2),gsl.percH(self.posy)-(gsl.percH(self.heightP)/2),gsl.percW(self.widthP),gsl.percH(self.heightP))

    #return rect position object of button instance
    def grabDat(self):
        return self.rect
    
    #push button object to active buffer for this frame
    def pushToBuffer(self,buffer):
        buffer.append(self)
    
    #render button object including mouse hover detection
    def renderButton(self,mousePos,win):

        #draw rectangle as gray if mouse in bounds, else draw standard configured color
        if mousePos[0] > self.rect.x and mousePos[0] < (self.rect.x + self.rect.width) and mousePos[1] > self.rect.y and mousePos[1] < (self.rect.y + self.rect.height):
            pyg.draw.rect(win,self.selCol,self.rect)
        else:
            pyg.draw.rect(win,self.col,self.rect)

        #draw text
        win.blit(self.textSurf,(self.rect.centerx-(self.textSurf.get_width()/2),self.rect.centery-(self.textSurf.get_height()/2)))
    
    #add button to list of all instances
    def addInstance(self):
        button.instances.append(self)
        print(button.instances)
    
    #draw all button instances in frame buffer to screen using renderbutton method
    def drawToScreen(buffer,mousePos,win):
        for unit in buffer:
            unit.renderButton(mousePos,win)
        #clear buffer for next frame
        buffer = []

    #check if mousepos tuple collides with any objects in frame buffer and if so call operating function for button object
    def collisionCheck(buffer,mousePos):
        for i in buffer:
            if mousePos[0] > i.rect.x and mousePos[0] < (i.rect.x + i.rect.width) and mousePos[1] > i.rect.y and mousePos[1] < (i.rect.y + i.rect.height):
                i.func()
    
    def updateRects():
        for i in button.instances:
            i.updateRect()

#draw all objects in list
def pageObjectRender(pageLs,render,buttonBuffer):
    if render:
        for i in pageLs:
            try:
                i.pushToBuffer(buttonBuffer)
            except:
                Textlib.terminfo(f'encountered error while attempting to draw page buttons: {pageLs}',log,verbosity,loggen)

#ui assembley and definition
#main menu buttons VVVVVVV
MainMenu = True
MainMenuButtons = []

#settings button
def SettingsButtonFunc():
    Textlib.terminfo("button pressed lmao",log,verbosity,loggen)
SettingsButton = button(50,50,10,5,text="Settings",onClick=SettingsButtonFunc)
MainMenuButtons.append(SettingsButton)
    
while run:

    #calculate how long a frame took to draw and calculate required delay to pin fps
    crrTime = t.time()
    diff = crrTime - prvTime
    prvTime = crrTime
    delayTime = 1./fps - diff

    #if time taken to draw last frame was less than the maximum to maintain desired fps, wait amount required to hold desired fps
    if delayTime > 0:
        t.sleep(delayTime)
    
    #update frame count
    frame += 1
    if frame > fps:
        frame = 1
    #print()

    #draw background image when enabled
    if bgEnabled:
        #preloaded image
        win.blit(bg,(0,0))
    else:
        #default background
        win.fill('#81becc')

    #draw all ui elements here so mouseclick event can recive full object buffer
    #frame counter
    win.blit(smallfont.render(f'{frame}/{fps} ({-delayTime} ms Behind)',True,"#000000"),(30,30))
    #Draw Main Menu Object Instance
    pageObjectRender(MainMenuButtons,MainMenu,buttonBuffer)

    #handle window event buffer
    for event in pyg.event.get():

        #handle window rezise event
        if event.type == pyg.WINDOWRESIZED:
            size = pyg.display.get_surface().get_size()
            bg = pyg.transform.scale(bg,size)
            Textlib.terminfo(f'Window Resizesd to {str(size)}',log,verbosity,loggen)
            gsl.updateVals(size[0],size[1])
            button.updateRects()

        #when close button pressed
        if event.type == pyg.QUIT:
            run = False
            Textlib.terminfo('program Closed Manually',log,verbosity,loggen)

        #handle mouseclick
        if event.type == pyg.MOUSEBUTTONDOWN:
            mousePos = pyg.mouse.get_pos()
            button.collisionCheck(buttonBuffer,mousePos)

    #render button buffer after click interaction check
    button.drawToScreen(buttonBuffer,pyg.mouse.get_pos(),win)
    
    #update frame
    pyg.display.update()
    buttonBuffer = []


#exit program and generate log
if loggen == True:
    Textlib.log.storeLog(log)