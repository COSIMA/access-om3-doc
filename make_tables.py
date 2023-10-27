#!/usr/bin/env python

# Update tables of namelists

import nmltab  # from https://github.com/aekiss/nmltab
import os

configs = 'configs'
tables = 'tables'
os.makedirs(tables, exist_ok=True)

os.chdir(configs)

def savetables(nmls, fname, url):
    print('   {}'.format(fname))
    fname += '_nml'
    nmld = nmltab.nmldict(nmls)
    for i in range(2):
        st = nmltab.strnmldict(nmld, fmt='latex', url=url)
        with open(os.path.join('..', tables, fname+'.tex'), 'w') as f:
            f.write(st)
        st = nmltab.strnmldict(nmld, fmt='markdown2', url=url)
        with open(os.path.join('..', tables, fname+'.md'), 'w') as f:
            f.write(st)
        st = nmltab.strnmldict(nmld, fmt='csv', url=url)
        with open(os.path.join('..', tables, fname+'.csv'), 'w') as f:
            f.write(st)
        nmltab.nmldiff(nmld)
        fname += "_diff"

savetables([
        'ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        'MOM6-CICE6_1deg_jra55do_ryf/ice_in'
        ],
        'cice',
        'https://cice-consortium-cice.readthedocs.io/en/main/search.html?q='
        )

savetables( [
        #'ACCESS-OM2_1deg_jra55_ryf/ocean/input.nml',
        'MOM6-examples/ocean_only/global/MOM_input',
        'mom6-om4-025/MOM_input',
        'mom6-panan/MOM_input',
        'mom6-eac/MOM_input',
        'MOM6-CICE6_1deg_jra55do_ryf/MOM_input'
        ],
        'mom6',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'MOM6-examples/ocean_only/global/MOM_input',
        'mom6-om4-025/MOM_input',
        'MOM6-CICE6_1deg_jra55do_ryf/MOM_input'
        ],
        'mom6_global',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'mom6-panan/MOM_input',
        'mom6-eac/MOM_input'
        ],
        'mom6_regional',
        'https://github.com/mom-ocean/MOM6/search?q=')
