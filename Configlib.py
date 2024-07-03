#imports (os for directory access) (JSON for configuration formatting) (textlib for warning message when file broken)
import os
import json
import Textlib as tlb

opDir = os.path.dirname(os.path.realpath(__file__))
filepath = f'{opDir}\\Config\\mainConfig.json'

def openCfg():
    global filepath

    #try and open configuration file
    try:
        file = open(filepath,"r").read()
        cfg = json.loads(file)
        print(cfg)

    #if it cannot be opened generate new file, if file empty generate template config array
    except:
        tlb.termcritical('failed to locate and load configuration file, may be missing or file structure may be malformed, attempting to generate replacement\nif this fails then filestructure is damaged please reinstall')
        open(filepath,"w")
        cfgdump = open(filepath,"r").read()
        print(cfgdump)
        if cfgdump == "":
            cfg = {"terminal":{"generate-log":False,"write-in-terminal":True},"window-settings":{"window-mode":"windowed","win-width":1280,"win-height":920}}
            cfgdump = json.dumps(cfg, sort_keys=True, indent=2)
            open(filepath,"w").write(cfgdump)
        else:
            cfg = json.loads(cfgdump)

    #return config as dictionary array
    return(cfg)

def updateCfg(cfg):
    cfgdump = json.dumps(cfg, sort_keys=True, indent=2)
    open(filepath,"w").write(cfgdump)
