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
# Getting POTCAR files from the VASP library
#F1="/fslhome/mwa32/fsl_groups/fslg_msg_vasp/potpaw_PBE"+"/"+vis.potcar_symbols[0]+"/"+"POTCAR"
F1=vis.potcar_symbols[1]+"/"+"POTCAR"
F2=vis.potcar_symbols[1]+"/"+"POTCAR"
F3=vis.potcar_symbols[1]+"/"+"POTCAR"
F4=vis.potcar_symbols[1]+"/"+"POTCAR"
Des="POTCAR"
with open(Des,"wb")as wfd:
    for files in (F1,F2,F3,F4):
        with open(files,"rb")as fd:
            shutil.copyfileobj(fd,wfd)