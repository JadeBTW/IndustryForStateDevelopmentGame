import os

#start config lib and global cfg dict
import Configlib as clib
cfg = clib.openCfg()

#set internal variables to file config ver
loggen = cfg["terminal"]["generate-log"]
verbosity = cfg["terminal"]["write-in-terminal"]

#import and start proportional graphics scaling lib
import Guiscalelib as gsl
gsl.updateVals(cfg["window-settings"]["win-width"],cfg["window-settings"]["win-height"])

# set up inhouse log generation and text beautification library
import Textlib
log = Textlib.log #instanciating log object
Textlib.log.__init__(log)
Textlib.terminfo('Started Log File and initialised terminal library',log,verbosity,loggen)
Textlib.terminfo('running terminal formatting test (if colors do not work you may be using a non ANSI compatible system)',log,verbosity,loggen)

#1 print of each terminal type to test coloring in term
Textlib.terminfo('this is an info entry',log,verbosity,loggen)
Textlib.termwarn('this is a warn entry',log,verbosity,loggen)
Textlib.termcritical('this is a critical error entry',log,verbosity,loggen)

#import and init pygame module
import pygame
pygame.init()

#exit program and generate log
if loggen == True:
    Textlib.log.storeLog(log)