# import external libs (datetime for log file names) (os for colored text initialization)
import datetime
import os

#find and format operating directory for relative pathing
opDir = os.path.dirname(os.path.realpath(__file__))

#log object class
class log:

    #start log object and log array
    def __init__(self) -> None:
        self.logEnt = []
        return(self)
    
    #write text to log object
    def writeLog(self,item):
        self.logEnt.append(item)
    
    #return all (or one specific index) of log file programatically
    def grabLog(self,index=None):
        if index != None:
            try:
                return(self.logEnt[index])
            except:
                return(None)
        else:
            return(self.logEnt)
    
    #write log to procedurally named log file
    def storeLog(self):
        logname = datetime.datetime.now()
        logname = str(logname).replace(" ","-").replace(":","-").replace(".","-")
        logfile = open(f'{opDir}\\Logs\\{logname}',"w").write("\n".join(self.logEnt))

#automated formatting of ANSI escape sequences for coloured terminal text
def colprint(txtype=0,txtcol=37,bgcol=40,text="",end="\n"):
    os.system("")
    print(f'\033[{str(txtype)};{str(txtcol)};{str(bgcol)}m{text}\033[0;37;40m',end=end)

#automated log file writing and coloured formatted printing for three main types of information printouts
#info for noncritical logging of progress and happenings
def terminfo(text,logfile=None,verbosity=True,writelog=True):
    txtformat = f'[INFO] {text}'
    if verbosity == True:
        colprint(txtype=1,text=txtformat,txtcol=32)
    if logfile != None:
        if writelog == True:
            log.writeLog(logfile,txtformat)

#warn for important but noncritical alerts
def termwarn(text,logfile=None,verbosity=True,writelog=True):
    txtformat = f'[WARN] {text}'
    if verbosity == True:
        colprint(txtype=1,text=txtformat,txtcol=33)
    if logfile != None:
        if writelog == True:
            log.writeLog(logfile,txtformat)

#critical for critical errors that cause major functionality breakdown or crash
def termcritical(text,logfile=None,verbosity=True,writelog=True):
    txtformat = f'[CRITICAL] {text}'
    if verbosity == True:
        colprint(txtype=1,text=txtformat,txtcol=31)
    if logfile != None:
        if writelog == True:
            log.writeLog(logfile,txtformat)
