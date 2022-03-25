import numpy as np
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.io.vasp.sets import MPHSERelaxSet, MPRelaxSet, MPStaticSet
from pymatgen.ext.matproj import MPRester

with open("api_key.txt",'r') as filename:
    API_KEY = filename.readlines()[0]
with MPRester(API_KEY) as mpr:
            structure = mpr.get_structure_by_material_id("mp-2574")
vis=MPRelaxSet(structure, force_gamma=True)

f=open("INCAR",'w')
f.write(str(vis.incar))
f.close()
f=open("KPOINTS",'w')
f.write(str(vis.kpoints))
f.close()
f=open("POSCAR",'w')
f.write(str(vis.poscar))
f.close()