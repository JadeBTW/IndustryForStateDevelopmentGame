import os, pygame as pyg, Guiscalelib as gsl, Configlib as clib, time as t

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
win = pyg.display.set_mode((cfg["window-settings"]["win-width"], cfg["window-settings"]["win-height"]))
pyg.display.set_caption('Industry For State Development BETA')


#ui values
buttonColor = (102, 204, 255)
buttonHoverColor = (153, 204, 255)
textColor = (12, 12, 12)
smallfont = pyg.font.SysFont('Corbel',20)
buttonBuffer = []

testButton  = button(100,200,100,50)

#button shit

class button():

    def __init__(self,posx,posy,w,h,text="",img=None,selImg=None,col="#f0f0f0",selCol="#999999",textCol="#000000"):
        self.rect = pyg.Rect(posx,posy,w,h)
        self.text = smallfont.render(text,True,textCol)
        self.img = img
        self.selImg = selImg
        self.col = col
        self.selCol = selCol
        self.textCol = textCol
        self.text = text
        
    def grabDat(self):
        return self.rect
    
    def pushToBuffer(self,buffer):
        buffer.append(self)
    
    def renderButton(self,mousePos):
        pass
    
    def drawToScreen(buffer,mousePos):
        for unit in buffer:
            pass
        
    
while run:

    #calculate how long a frame took to draw and calculate required delay to pin fps
    crrTime = t.time()
    diff = crrTime - prvTime
    prvTime = crrTime
    delayTime = 1./fps - diff

    #if time taken to draw last frame was less than the maximum to maintain desired fps, wait amount required to hold desired fps
    if delayTime > 0:
        t.sleep(delayTime)


    #default background
    win.fill('#81becc')

    #handle window event buffer
    for event in pyg.event.get():

        #when close button pressed
        if event.type == pyg.QUIT:
            run = False
            Textlib.terminfo('program Closed Manually',log,verbosity,loggen)

        #handle mouseclick
        if event.type == pyg.MOUSEBUTTONDOWN:
            mousePos = pyg.mouse.get_pos()
    
    #update frame
    pyg.display.update()


#exit program and generate log
if loggen == True:
    Textlib.log.storeLog(log)