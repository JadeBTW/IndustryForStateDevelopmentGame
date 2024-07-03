import os

#start config lib and global cfg dict
import Configlib as clib
cfg = clib.openCfg()

loggen = cfg["terminal"]["generate-log"]
verbosity = cfg["terminal"]["write-in-terminal"]

#import and start proportional graphics scaling lib
import Guiscalelib as gsl
gsl.updateVals(cfg["window-settings"]["win-width"],cfg["window-settings"]["win-height"])

# set up inhouse log generation and text beautification library
import Textlib
log = Textlib.log
Textlib.log.__init__(log)
Textlib.terminfo('Started Log File and initialised terminal library',log,verbosity,loggen)
Textlib.terminfo('running terminal formatting test (if colors do not work you may be using a non ANSI compatible system)',log,verbosity,loggen)

Textlib.terminfo('this is an info entry',log,verbosity,loggen)
Textlib.termwarn('this is a warn entry',log,verbosity,loggen)
Textlib.termcritical('this is a critical error entry',log,verbosity,loggen)

#exit program and generate log
if loggen == True:
    Textlib.log.storeLog(log)