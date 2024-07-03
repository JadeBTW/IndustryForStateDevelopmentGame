scrW = 0
scrH = 0
scrPrcW = 0
scrPrcH = 0

def updateVals(width=1280,height=920):
    global scrH,scrW,scrPrcW,scrPrcH
    scrH = height
    scrW = width
    scrPrcH = height/100
    scrPrcW = width/100

def percH(hprc):
    global scrPrcH
    return hprc*scrPrcH

def percW(wprc):
    global scrPrcW
    return wprc*scrPrcW