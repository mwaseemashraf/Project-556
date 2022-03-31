import numpy as np
import shutil


def POTCAR_compiler(potcar_symbols):
    VASP_POTCAR_PATH=""
    Des="POTCAR"
    lis=[]
    for i in range(len(potcar_symbols)):
        #F=vis.potcar_symbols[i]
        lis=lis+[VASP_POTCAR_PATH+potcar_symbols[i]+"/"+"POTCAR"]
        with open(Des,"wb")as wfd:
            for files in lis:
                with open(files,"rb")as fd:
                    shutil.copyfileobj(fd,wfd)