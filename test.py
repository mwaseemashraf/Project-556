import numpy as np
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.io.vasp.sets import MPHSERelaxSet, MPRelaxSet, MPStaticSet

vis=MPRelaxSet(structure, force_gamma=True)