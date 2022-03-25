import numpy as np
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.io.vasp.sets import MPHSERelaxSet, MPRelaxSet, MPStaticSet
from pymatgen.ext.matproj import MPRester

with open("api_key.txt",'r') as filename:
    API_KEY = filename.readlines()[0]
with MPRester(API_KEY) as mpr:
            structure = mpr.get_structure_by_material_id("mp-2574")
vis=MPRelaxSet(structure, force_gamma=True)
# Adding iput files from Pymatgen
f=open("INCAR",'w')
f.write(str(vis.incar))
f.close()
f=open("KPOINTS",'w')
f.write(str(vis.kpoints))
f.close()
f=open("POSCAR",'w')
f.write(str(vis.poscar))
f.close()

# Compiling POTCAR file from the VASP library

VASP_POTCAR_PATH=""
Des="POTCAR"
lis=[]
for i in range(len(vis.potcar_symbols)):
    #F=vis.potcar_symbols[i]
    lis=lis+[VASP_POTCAR_PATH+vis.potcar_symbols[i]+"/"+"POTCAR"]
    with open(Des,"wb")as wfd:
        for files in lis:
            with open(files,"rb")as fd:
                shutil.copyfileobj(fd,wfd)