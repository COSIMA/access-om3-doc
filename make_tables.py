#!/usr/bin/env python

# Update latex tables of namelists

import nmltab  # from https://github.com/aekiss/nmltab

nmls = ['ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        'MOM6-CICE6_1deg_jra55do_ryf/ice_in']

texfname = 'cice_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(texfname, 'w') as f:
    f.write(st)
print('   {}'.format(texfname))
