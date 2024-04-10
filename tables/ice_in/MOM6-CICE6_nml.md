| Group                 | Variable                  | [MOM6-CICE6_1deg_jra55do_ryf/<br>ice_in](https://github.com/COSIMA/MOM6-CICE6/blob/1bad3aee5400b908535fea7aff5f8073f0c7876d/ice_in) | [MOM6-CICE6_1deg_jra55do_iaf/<br>ice_in](https://github.com/COSIMA/MOM6-CICE6/blob/de4a6c5cff17b2e7d312a8a05944711b32a9019a/ice_in) | [MOM6-CICE6_025deg_jra55do_ryf_iss101/<br>ice_in](https://github.com/COSIMA/MOM6-CICE6/blob/b44852b554c66271eafb6df9b594ad21663fe29d/ice_in) |
| :-------------------- | :------------------------ | --------------: | --------------: | --------------: |
| [domain_nml           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=domain_nml) | [**block_size_x**         ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=block_size_x) |              16 |              16 |              20 |
|                       | [**block_size_y**         ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=block_size_y) |              15 |              15 |              16 |
|                       | [**distribution_type**    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=distribution_type) |     'cartesian' |     'cartesian' |    'roundrobin' |
|                       | [distribution_wght        ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=distribution_wght) |      'latitude' |      'latitude' |      'latitude' |
|                       | [maskhalo_bound           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=maskhalo_bound) |            True |            True |            True |
|                       | [maskhalo_dyn             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=maskhalo_dyn) |            True |            True |            True |
|                       | [maskhalo_remap           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=maskhalo_remap) |            True |            True |            True |
|                       | [**max_blocks**           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=max_blocks) |              10 |              10 |              15 |
|                       | [ns_boundary_type         ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ns_boundary_type) |       'tripole' |       'tripole' |       'tripole' |
|                       | [**nx_global**            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=nx_global) |             360 |             360 |            1440 |
|                       | [**ny_global**            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ny_global) |             300 |             300 |            1080 |
|                       | [**processor_shape**      ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=processor_shape) |     'slenderX2' |     'slenderX2' |    'square-ice' |
| [dynamics_nml         ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=dynamics_nml) | [advection                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=advection) |         'remap' |         'remap' |         'remap' |
|                       | [ssh_stress               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ssh_stress) |       'coupled' |       'coupled' |       'coupled' |
| [forcing_nml          ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=forcing_nml) | [emissivity               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=emissivity) |            0.95 |            0.95 |            0.95 |
|                       | [highfreq                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=highfreq) |            True |            True |            True |
|                       | [ice_ref_salinity         ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ice_ref_salinity) |             5.0 |             5.0 |             5.0 |
|                       | [tfrz_option              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=tfrz_option) |   'linear_salt' |   'linear_salt' |   'linear_salt' |
|                       | [update_ocn_f             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=update_ocn_f) |            True |            True |            True |
|                       | [ustar_min                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ustar_min) |          0.0005 |          0.0005 |          0.0005 |
| [grid_nml             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_nml) | [bathymetry_file          ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=bathymetry_file) | './input/topog.<br>nc' | './input/topog.<br>nc' | './input/topog.<br>nc' |
|                       | [grid_atm                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_atm) |             'A' |             'A' |             'A' |
|                       | [grid_file                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_file) | './input/grid.n<br>c' | './input/grid.n<br>c' | './input/grid.n<br>c' |
|                       | [grid_format              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_format) |            'nc' |            'nc' |            'nc' |
|                       | [grid_ice                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_ice) |             'B' |             'B' |             'B' |
|                       | [grid_ocn                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_ocn) |             'A' |             'A' |             'A' |
|                       | [grid_type                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=grid_type) |       'tripole' |       'tripole' |       'tripole' |
|                       | [kcatbound                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=kcatbound) |               0 |               0 |               0 |
|                       | [kmt_file                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=kmt_file) | './input/kmt.nc<br>' | './input/kmt.nc<br>' | './input/kmt.nc<br>' |
|                       | [nblyr                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=nblyr) |               1 |               1 |               1 |
|                       | [ncat                     ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ncat) |               5 |               5 |               5 |
|                       | [nfsd                     ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=nfsd) |               1 |               1 |               1 |
|                       | [nilyr                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=nilyr) |               4 |               4 |               4 |
|                       | [nslyr                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=nslyr) |               1 |               1 |               1 |
| [icefields_mechred_nml](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=icefields_mechred_nml) | [f_dardg1dt               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dardg1dt) |             'x' |             'x' |             'x' |
|                       | [f_dardg2dt               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dardg2dt) |             'x' |             'x' |             'x' |
|                       | [f_dvirdgdt               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dvirdgdt) |             'x' |             'x' |             'x' |
| [icefields_nml        ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=icefields_nml) | [f_aice                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_aice) |            'md' |            'md' |            'md' |
|                       | [f_aicen                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_aicen) |             'm' |             'm' |             'm' |
|                       | [f_aisnap                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_aisnap) |             'x' |             'x' |             'x' |
|                       | [f_albpnd                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_albpnd) |             'x' |             'x' |             'x' |
|                       | [f_atmdir                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_atmdir) |             'x' |             'x' |             'x' |
|                       | [f_atmspd                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_atmspd) |             'x' |             'x' |             'x' |
|                       | [f_bounds                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_bounds) |           False |           False |           False |
|                       | [f_congel                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_congel) |            'md' |            'md' |            'md' |
|                       | [f_coszen                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_coszen) |             'x' |             'x' |             'x' |
|                       | [f_dsnow                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dsnow) |             'x' |             'x' |             'x' |
|                       | [f_dvidtd                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dvidtd) |            'md' |            'md' |            'md' |
|                       | [f_dvidtt                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_dvidtt) |            'md' |            'md' |            'md' |
|                       | [f_evap                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_evap) |             'x' |             'x' |             'x' |
|                       | [f_fbot                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fbot) |             'x' |             'x' |             'x' |
|                       | [f_fcondtopn_ai           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fcondtopn_ai) |             'm' |             'm' |             'm' |
|                       | [f_fhocn                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fhocn) |             'x' |             'x' |             'x' |
|                       | [f_flat                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_flat) |             'x' |             'x' |             'x' |
|                       | [f_flatn_ai               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_flatn_ai) |             'm' |             'm' |             'm' |
|                       | [f_flwup                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_flwup) |             'x' |             'x' |             'x' |
|                       | [f_fmelttn_ai             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fmelttn_ai) |             'm' |             'm' |             'm' |
|                       | [f_frazil                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_frazil) |            'md' |            'md' |            'md' |
|                       | [f_fresh                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fresh) |             'x' |             'x' |             'x' |
|                       | [f_frz_onset              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_frz_onset) |             'x' |             'x' |             'x' |
|                       | [f_frzmlt                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_frzmlt) |            'md' |            'md' |            'md' |
|                       | [f_fsens                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsens) |             'x' |             'x' |             'x' |
|                       | [f_fsens_ai               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsens_ai) |             'm' |             'm' |             'm' |
|                       | [f_fsensn_ai              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsensn_ai) |             'm' |             'm' |             'm' |
|                       | [f_fsurf_ai               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsurf_ai) |             'x' |             'x' |             'x' |
|                       | [f_fsurfn_ai              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsurfn_ai) |             'm' |             'm' |             'm' |
|                       | [f_fswabs                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fswabs) |             'x' |             'x' |             'x' |
|                       | [f_fswthru                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fswthru) |             'x' |             'x' |             'x' |
|                       | [f_hi                     ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_hi) |            'md' |            'md' |            'md' |
|                       | [f_hisnap                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_hisnap) |             'x' |             'x' |             'x' |
|                       | [f_hs                     ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_hs) |            'md' |            'md' |            'md' |
|                       | [f_icedir                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_icedir) |             'x' |             'x' |             'x' |
|                       | [f_icespd                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_icespd) |             'x' |             'x' |             'x' |
|                       | [f_mlt_onset              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_mlt_onset) |             'x' |             'x' |             'x' |
|                       | [f_ocndir                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_ocndir) |             'x' |             'x' |             'x' |
|                       | [f_ocnspd                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_ocnspd) |             'x' |             'x' |             'x' |
|                       | [f_qref                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_qref) |             'x' |             'x' |             'x' |
|                       | [f_rain                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_rain) |             'x' |             'x' |             'x' |
|                       | [f_sig1                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_sig1) |             'x' |             'x' |             'x' |
|                       | [f_sig2                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_sig2) |             'x' |             'x' |             'x' |
|                       | [f_sigp                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_sigp) |             'x' |             'x' |             'x' |
|                       | [f_snoice                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_snoice) |            'md' |            'md' |            'md' |
|                       | [f_snow                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_snow) |             'x' |             'x' |             'x' |
|                       | [f_sss                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_sss) |             'x' |             'x' |             'x' |
|                       | [f_sst                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_sst) |             'x' |             'x' |             'x' |
|                       | [f_taubx                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_taubx) |             'x' |             'x' |             'x' |
|                       | [f_tauby                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_tauby) |             'x' |             'x' |             'x' |
|                       | [f_tref                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_tref) |             'x' |             'x' |             'x' |
|                       | [f_uocn                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_uocn) |             'x' |             'x' |             'x' |
|                       | [f_uvel                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_uvel) |            'md' |            'md' |            'md' |
|                       | [f_vicen                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_vicen) |             'm' |             'm' |             'm' |
|                       | [f_vocn                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_vocn) |             'x' |             'x' |             'x' |
|                       | [f_vvel                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_vvel) |            'md' |            'md' |            'md' |
| [icefields_snow_nml   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=icefields_snow_nml) | [f_fsloss                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_fsloss) |             'm' |             'm' |             'm' |
|                       | [f_meltsliq               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_meltsliq) |             'm' |             'm' |             'm' |
|                       | [f_rhos_cmp               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_rhos_cmp) |             'm' |             'm' |             'm' |
|                       | [f_rhos_cnt               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_rhos_cnt) |             'm' |             'm' |             'm' |
|                       | [f_rsnw                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_rsnw) |             'm' |             'm' |             'm' |
|                       | [f_smassice               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_smassice) |             'm' |             'm' |             'm' |
|                       | [f_smassliq               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=f_smassliq) |             'm' |             'm' |             'm' |
| [ponds_nml            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ponds_nml) | [dpscale                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=dpscale) |           0.001 |           0.001 |           0.001 |
|                       | [frzpnd                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=frzpnd) |          'hlid' |          'hlid' |          'hlid' |
|                       | [rfracmax                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=rfracmax) |             1.0 |             1.0 |             1.0 |
| [setup_nml            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=setup_nml) | [bfbflag                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=bfbflag) |           'off' |           'off' |           'off' |
|                       | [conserv_check            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=conserv_check) |           False |           False |           False |
|                       | [debug_forcing            ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=debug_forcing) |            True |            True |            True |
|                       | [debug_model              ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=debug_model) |            True |            True |            True |
|                       | [diagfreq                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=diagfreq) |             960 |             960 |             960 |
|                       | [dump_last                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=dump_last) |            True |            True |            True |
|                       | [dumpfreq                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=dumpfreq) |             'y' |             'y' |             'y' |
|                       | [histfreq                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=histfreq) | ['d', 'm', 'x',<br> 'x', 'x'] | ['d', 'm', 'x',<br> 'x', 'x'] | ['d', 'm', 'x',<br> 'x', 'x'] |
|                       | [history_precision        ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=history_precision) |               8 |               8 |               8 |
|                       | [**ice_ic**               ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ice_ic) | './input/iced.1<br>900-01-01-10800<br>.nc' | './input/iced.1<br>900-01-01-10800<br>.nc' | 'default' |
|                       | [lcdf64                   ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=lcdf64) |           False |           False |           False |
|                       | [npt                      ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=npt) |           35040 |           35040 |           35040 |
|                       | [pointer_file             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=pointer_file) | './rpointer.ice<br>' | './rpointer.ice<br>' | './rpointer.ice<br>' |
|                       | [print_global             ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=print_global) |           False |           False |           False |
|                       | [**use_leap_years**       ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=use_leap_years) |                 |            True |                 |
| [shortwave_nml        ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=shortwave_nml) | [ahmax                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=ahmax) |             0.1 |             0.1 |             0.1 |
|                       | [albicei                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=albicei) |            0.44 |            0.44 |            0.44 |
|                       | [albicev                  ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=albicev) |            0.86 |            0.86 |            0.86 |
|                       | [albsnowi                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=albsnowi) |             0.7 |             0.7 |             0.7 |
|                       | [albsnowv                 ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=albsnowv) |            0.98 |            0.98 |            0.98 |
|                       | [kalg                     ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=kalg) |             0.0 |             0.0 |             0.0 |
|                       | [r_snw                    ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=r_snw) |             0.0 |             0.0 |             0.0 |
|                       | [sw_redist                ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=sw_redist) |            True |            True |            True |
| [thermo_nml           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=thermo_nml) | [dsdt_slow_mode           ](https://cice-consortium-cice.readthedocs.io/en/main/search.html?q=dsdt_slow_mode) |          -5e-08 |          -5e-08 |          -5e-08 |
