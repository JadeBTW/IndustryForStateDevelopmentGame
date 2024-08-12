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
win = pyg.display.set_mode((cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]))
pyg.display.set_caption('Industry For State Development BETA')

#delta time frame cap variables
prvTime = t.time()
fps = cfg["graphics-settings"]["framerate-cap"]

#start window related variables
run = True
if cfg["window-settings"]["fullscreen"]:
    win = pyg.display.set_mode((cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]),pyg.FULLSCREEN)
else:
    win = pyg.display.set_mode((cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]),pyg.RESIZABLE)

pyg.display.set_caption('Industry For State Development BETA')
bg = pyg.image.load(f'{filepath}\\Background Images\\ISD_1920_1200_sunset_factory_TrueRes.png')
bg = pyg.transform.scale(bg,(cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]))
bgEnabled = True


#ui values
buttonColor = (102, 204, 255)
buttonHoverColor = (153, 204, 255)
textColor = (12, 12, 12)
smallfont = pyg.font.SysFont('Corbel',20)
buttonBuffer = []

#button shit
class button():

    #start button object with deafault configuration parameters
    def __init__(self,posx,posy,w,h,text="",img=None,selImg=None,col="#f0f0f0",selCol="#999999",textCol="#000000"):
        self.rect = pyg.Rect(posx,posy,w,h)
        self.textSurf = smallfont.render(text,True,textCol)
        self.img = img
        self.selImg = selImg
        self.col = col
        self.selCol = selCol
        self.textCol = textCol
        self.text = text
    
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
        win.blit(self.textSurf,(self.rect.x+5,self.rect.centery-10))
    
    #draw all button instances in frame buffer to screen using renderbutton method
    def drawToScreen(buffer,mousePos,win):
        for unit in buffer:
            unit.renderButton(mousePos,win)
        #clear buffer for next frame
        buffer = []

#ui assembley and definition
testButton  = button(100,200,100,50,text="test_icles")  
    
while run:

    #calculate how long a frame took to draw and calculate required delay to pin fps
    crrTime = t.time()
    diff = crrTime - prvTime
    prvTime = crrTime
    delayTime = 1./fps - diff

    #if time taken to draw last frame was less than the maximum to maintain desired fps, wait amount required to hold desired fps
    if delayTime > 0:
        t.sleep(delayTime)

    #draw background image when enabled
    if bgEnabled:
        #preloaded image
        win.blit(bg,(0,0))
    else:
        #default background
        win.fill('#81becc')

    #draw all ui elements here so mouseclick event can recive full object buffer
    testButton.pushToBuffer(buttonBuffer)

    #handle window event buffer
    for event in pyg.event.get():

        #handle window rezise event
        if event.type == pyg.WINDOWRESIZED:
            bg = pyg.transform.scale(bg,pyg.display.get_surface().get_size())

        #when close button pressed
        if event.type == pyg.QUIT:
            run = False
            Textlib.terminfo('program Closed Manually',log,verbosity,loggen)

        #handle mouseclick
        if event.type == pyg.MOUSEBUTTONDOWN:
            mousePos = pyg.mouse.get_pos()

    #render button buffer after click interaction check
    button.drawToScreen(buttonBuffer,pyg.mouse.get_pos(),win)
    
    #update frame
    pyg.display.update()


#exit program and generate log
if loggen == True:
    Textlib.log.storeLog(log)