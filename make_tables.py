#!/usr/bin/env python

# Update latex tables of namelists

import nmltab  # from https://github.com/aekiss/nmltab
import os

configs = 'configs'
namelists = 'namelists'
os.makedirs(namelists, exist_ok=True)

nmls = [#'ACCESS-OM2_1deg_jra55_ryf/ocean/input.nml',
        'MOM6-examples/ocean_only/global/MOM_input',
        'mom6-om4-025/MOM_input',
        'mom6-panan/MOM_input',
        'mom6-eac/MOM_input',
        'MOM6-CICE6_1deg_jra55do_ryf/MOM_input']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'mom_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))

nmls = ['MOM6-examples/ocean_only/global/MOM_input',
        'mom6-om4-025/MOM_input',
        'MOM6-CICE6_1deg_jra55do_ryf/MOM_input']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'mom6_global_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))

nmls = ['mom6-om4-025/MOM_input',
        'mom6-panan/MOM_input',
        'mom6-eac/MOM_input']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'mom6_sis2_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))

nmls = ['mom6-panan/MOM_input',
        'mom6-eac/MOM_input']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'mom6_sis2_regional_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))

nmls = ['ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        'MOM6-CICE6_1deg_jra55do_ryf/ice_in']
nmls = [ os.path.join(configs, d) for d in nmls ]
texfname = 'cice_nml.tex'
st = nmltab.strnmldict(nmltab.nmldict(nmls), fmt='latex')
with open(os.path.join(namelists, texfname), 'w') as f:
    f.write(st)
print('   {}'.format(texfname))
