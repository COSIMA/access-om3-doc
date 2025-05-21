#!/usr/bin/env python

# Update tables of namelists

import nmltab  # from https://github.com/aekiss/nmltab
import os
import subprocess

configs = 'configs'
tables = 'tables'
os.makedirs(tables, exist_ok=True)

def getsubmodules(gitmodules='.gitmodules'):
    """Return dict of contents of .gitmodules
    """
    submodules = dict()
    submodule = list()  # deliberately invalid dict key
    with open(gitmodules, 'r') as f:
        for line in f:
            if line.startswith('[submodule "'):
                submodule = line.split('[submodule "')[1].split('"')[0]
                submodules[submodule] = dict()
            else:
                line = line.strip()
                key, value = line.split(' = ')
                submodules[submodule][key] = value
    return submodules

os.chdir(configs)

def getnmlfnameurls(nmls):
    """Return  dict of urls for each namelist path
    nmls: list of paths to namelists
    returns dict:
    key = nml
    value = url
    """
    nmlfnameurls = dict()
    submodules = getsubmodules('../.gitmodules')
    submods = dict()
    for val in submodules.values():  # use submodule paths (relative to conifigs) as keys
        path = os.path.sep.join(val['path'].split(configs+os.path.sep)[1:])  # strip off configs
        submods[path] = val
    for fn in nmls:
        try:
            p = subprocess.Popen('cd ' + os.path.dirname(fn)
                                + ' && git rev-parse HEAD',
                                stdout=subprocess.PIPE, shell=True)
            hash = p.communicate()[0].decode('ascii').strip()
            nmlfnameurls[fn] = '/'.join([
                submods[fn.split(os.path.sep)[0]]['url'].split('.git')[0],
                'blob',
                hash,
                os.path.sep.join(fn.split(os.path.sep)[1:])
                ])
        except:
            pass
    return nmlfnameurls

def savetables(nmls, fname, url):
    """Save tabulated namelists.
    nmls: list of paths to namelists
    fname: initial part of output filenames
    url: link to search on variables
    """
    print('   {}'.format(fname))
    fname += '_nml'
    nmld = nmltab.nmldict(nmls)
    nmlfnameurls = getnmlfnameurls(nmls)
    print(os.path.dirname(fname))
    os.makedirs(os.path.join('..', tables, os.path.dirname(fname)), exist_ok=True)
    for i in range(2):
        st = nmltab.strnmldict(nmld, fmt='latex', url=url)
        with open(os.path.join('..', tables, fname+'.tex'), 'w') as f:
            f.write(st)
        st = nmltab.strnmldict(nmld, fmt='markdown2', url=url, nmlfnameurls=nmlfnameurls, breaks=True)
        with open(os.path.join('..', tables, fname+'.md'), 'w') as f:
            f.write(st)
        st = nmltab.strnmldict(nmld, fmt='csv', url=url)
        with open(os.path.join('..', tables, fname+'.csv'), 'w') as f:
            f.write(st)
        nmltab.nmldiff(nmld)
        fname += "_diff"

savetables([
        'dev-MC_100km_jra_ryf/ice_in',
        'ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        ],
        'ice_in/cice',
        'https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=')

savetables( [
        'dev-MC_100km_jra_ryf/ice_in',
        'dev-MC_25km_jra_ryf/ice_in',
        'ACCESS-OM2_025deg_jra55_ryf/ice/cice_in.nml',
        ],
        'ice_in/cice_1_025',
        'https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=')

savetables( [
        'dev-MC_100km_jra_ryf/ice_in',
        'dev-MC_100km_jra_iaf/ice_in',
        'dev-MC_25km_jra_ryf/ice_in',
        ],
        'ice_in/MOM6-CICE6',
        'https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=')

savetables( [
        'dev-MC_100km_jra_ryf/docs/MOM_parameter_doc.all',
        'dev-MC_100km_jra_iaf/docs/MOM_parameter_doc.all',
        'dev-MC_25km_jra_ryf/docs/MOM_parameter_doc.all',
        ],
        'MOM_input/MOM6-CICE6',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MC_100km_jra_ryf/MOM_input',
        'gmom_jra/MOM_input',
        ],
        'MOM_input/MOM6-CICE6-CESM',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MCW_100km_jra_ryf/MOM_input',
        'dev-MCW_100km_jra_iaf/MOM_input',
        ],
        'MOM_input/MOM6-CICE6-WW3',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MCW_100km_jra_ryf/MOM_input',
        'gmom_jra_wd/MOM_input',
        ],
        'MOM_input/MOM6-CICE6-WW3-CESM',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MC_100km_jra_ryf/MOM_input',
        'dev-MCW_100km_jra_ryf/MOM_input',
        ],
        'MOM_input/MOM6-CICE6_MOM6-CICE6-WW3',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MC_100km_jra_ryf/MOM_input',
        'mom6-om4-025/MOM_input',
        'mom6-panan/MOM_input',
        # 'mom6-eac/MOM_input',  # no relevant differences from mom6-panan
        #'ACCESS-OM2_1deg_jra55_ryf/ocean/input.nml',
        'MOM6-examples/ocean_only/global/MOM_input',
        # 'MOM6-examples/ocean_only/global/MOM_parameter_doc.short',
        ],
        'MOM_input/mom6',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MC_100km_jra_ryf/MOM_input',
        'mom6-om4-025/MOM_input',
        'MOM6-examples/ocean_only/global/MOM_input',
        ],
        'MOM_input/mom6_global',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'mom6-panan/MOM_input',
        'mom6-eac/MOM_input'
        ],
        'MOM_input/mom6_regional',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'ACCESS-OM2_1deg_jra55_ryf/ocean/input.nml',
        'ACCESS-OM2_025deg_jra55_ryf/ocean/input.nml',
        'ACCESS-OM2_01deg_jra55_ryf/ocean/input.nml',
        ],
        'MOM_input/ACCESS-OM2-1-025-01',
        'https://github.com/mom-ocean/MOM5/search?q=')

savetables( [
        'ACCESS-OM2_1deg_jra55_ryf/ocean/input.nml',
        'ACCESS-OM2_025deg_jra55_ryf/ocean/input.nml',
        ],
        'MOM_input/ACCESS-OM2-1-025',
        'https://github.com/mom-ocean/MOM5/search?q=')

savetables( [
        'ACCESS-OM2_1deg_jra55_ryf/ice/cice_in.nml',
        'ACCESS-OM2_025deg_jra55_ryf/ice/cice_in.nml',
        'ACCESS-OM2_01deg_jra55_ryf/ice/cice_in.nml',
        ],
        'ice_in/ACCESS-OM2-1-025-01',
        'https://github.com/COSIMA/cice5/search?q=')

savetables( [
        'ACCESS-OM2_01deg_jra55v13_ryf9091/ocean/input.nml',
        'ACCESS-OM2_release-01deg_jra55_ryf/ocean/input.nml',
        ],
        'MOM_input/ACCESS-OM2_01deg_jra55v13_ryf9091',
        'https://github.com/mom-ocean/MOM5/search?q=')

savetables( [
        'ACCESS-OM2_01deg_jra55v13_ryf9091/ice/cice_in.nml',
        'ACCESS-OM2_release-01deg_jra55_ryf/ice/cice_in.nml',
        ],
        'ice_in/ACCESS-OM2_01deg_jra55v13_ryf9091',
        'https://github.com/COSIMA/cice5/search?q=')

savetables( [
        'GFDL-OM5/b00_MOM_parameter_doc.all',
        'GFDL-OM5/b03_update_MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        ],
        'MOM_input/GFDL-OM5',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'GFDL-OM5/b03_update_MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        ],
        'MOM_input/GFDL-OM5-update',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        # 'MOM6-examples/ocean_only/global/MOM_parameter_doc.all',
        # 'MOM6-examples/ice_ocean_SIS2/OM_1deg/MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/OM4_05/MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/OM4_025/MOM_parameter_doc.all',
        'GFDL-OM5/b00_MOM_parameter_doc.all',
        'GFDL-OM5/b03_update_MOM_parameter_doc.all'
        ],
        'MOM_input/GFDL-OM4-OM5',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        # 'GFDL-OM5/b03_update_MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        'dev-MC_100km_jra_ryf/docs/MOM_parameter_doc.all',
        'dev-MC_100km_jra_iaf/docs/MOM_parameter_doc.all',
        'dev-MC_25km_jra_ryf/docs/MOM_parameter_doc.all',
        ],
        'MOM_input/GFDL-OM5_ACCESS-OM3',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        # 'GFDL-OM5/b03_update_MOM_parameter_doc.all',
        'MOM6-examples/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        # 'MOM6-examples-breichl/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        # 'dev-MC_100km_jra_ryf/docs/MOM_parameter_doc.all',
        # 'dev-MC_100km_jra_iaf/docs/MOM_parameter_doc.all',
        'dev-MC_25km_jra_ryf/docs/MOM_parameter_doc.all',
        ],
        'MOM_input/GFDL-OM5_ACCESS-OM3_25km',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'dev-MC_25km_jra_ryf/docs/MOM_parameter_doc.all',
        'dev-MC_25km_jra_ryf-555-params-updates/docs/MOM_parameter_doc.all',
        ],
        'MOM_input/dev-MC_25km_jra_ryf-555-params-updates',
        'https://github.com/mom-ocean/MOM6/search?q=')

savetables( [
        'MOM6-examples/ice_ocean_SIS2/Baltic_OM5_025/MOM_parameter_doc.all',
        'dev-MC_25km_jra_ryf-555-params-updates/docs/MOM_parameter_doc.all',
        ],
        'MOM_input/GFDL-OM5_dev-MC_25km_jra_ryf-555-params-updates',
        'https://github.com/mom-ocean/MOM6/search?q=')
