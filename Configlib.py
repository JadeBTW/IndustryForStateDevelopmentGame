import os
import json
import Textlib as tlb

opDir = os.path.dirname(os.path.realpath(__file__))
filepath = f'{opDir}\\Config\\mainConfig.json'

def initCfg():
    global filepath
    try:
        cfg = json.loads(open(filepath,"r"))
        print(cfg)
    except:
        tlb.termcritical('failed to locate and load configuration file, may be missing or file structure may be malformed, attempting to generate replacement\nif this fails then filestructure is damaged please reinstall')
        open(filepath,"w")
        cfgdump = open(filepath,"r").read()
        print(cfgdump)

initCfg()