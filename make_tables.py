#!/usr/bin/env python

# Update latex tables of namelists

import nmltab  # from https://github.com/aekiss/nmltab
import os

configs = 'configs'
namelists = 'namelists'
os.makedirs(namelists, exist_ok=True)

nmls = ['ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        'MOM6-CICE6_1deg_jra55do_ryf/ice_in']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'cice_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))
