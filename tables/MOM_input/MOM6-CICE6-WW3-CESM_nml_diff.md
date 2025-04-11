| Variable                  | [dev-MCW_100km_jra_ryf/<br>MOM_input](https://github.com/ACCESS-NRI/access-om3-configs/blob/fa244187ee55e0852f0d53baa2ab0fd37284a4e9/MOM_input) | [gmom_jra_wd/<br>MOM_input](https://github.com/ACCESS-NRI/access-om3-configs/blob/6834f9d1b528747a2b90269d32eed36f5d4e24d9/MOM_input) |
| :------------------------ | --------------: | --------------: |
| [**adjust_net_srestore_t<br>o_zero**](https://github.com/mom-ocean/MOM6/search?q=adjust_net_srestore_to_zero) |  True |                 |
| [**ale_coordinate_config**](https://github.com/mom-ocean/MOM6/search?q=ale_coordinate_config) | 'FILE:ocean_vgr<br>id.nc,interface<br>s=zeta' | 'FILE:ocean_vgr<br>id.nc,dz' |
| [**bad_val_column_thickn<br>ess**](https://github.com/mom-ocean/MOM6/search?q=bad_val_column_thickness) |      0.0 |                 |
| [**bad_val_ssh_max**      ](https://github.com/mom-ocean/MOM6/search?q=bad_val_ssh_max) |            50.0 |                 |
| [**bad_val_sss_max**      ](https://github.com/mom-ocean/MOM6/search?q=bad_val_sss_max) |            75.0 |                 |
| [**bad_val_sst_max**      ](https://github.com/mom-ocean/MOM6/search?q=bad_val_sst_max) |            55.0 |                 |
| [**bad_val_sst_min**      ](https://github.com/mom-ocean/MOM6/search?q=bad_val_sst_min) |            -3.0 |                 |
| [**channel_config**       ](https://github.com/mom-ocean/MOM6/search?q=channel_config) |                 |   'global_1deg' |
| [**diag_coord_def_z**     ](https://github.com/mom-ocean/MOM6/search?q=diag_coord_def_z) | 'FILE:ocean_vgr<br>id.nc,interface<br>s=zeta' | 'WOA09' |
| [**eps_omesh**            ](https://github.com/mom-ocean/MOM6/search?q=eps_omesh) |           1e-13 |                 |
| [**eqn_of_state**         ](https://github.com/mom-ocean/MOM6/search?q=eqn_of_state) |        'WRIGHT' |                 |
| [**fluxconst**            ](https://github.com/mom-ocean/MOM6/search?q=fluxconst) |            0.11 |             0.5 |
| [**grid_file**            ](https://github.com/mom-ocean/MOM6/search?q=grid_file) | 'ocean_hgrid.nc<br>' | 'ocean_hgrid_23<br>0424.nc' |
| [**inputdir**             ](https://github.com/mom-ocean/MOM6/search?q=inputdir) |      './INPUT/' |      './input/' |
| [**mask_srestore_under_i<br>ce**](https://github.com/mom-ocean/MOM6/search?q=mask_srestore_under_ice) |     False |                 |
| [**niglobal**             ](https://github.com/mom-ocean/MOM6/search?q=niglobal) |             360 |             320 |
| [**njglobal**             ](https://github.com/mom-ocean/MOM6/search?q=njglobal) |             300 |             384 |
| [**nk**                   ](https://github.com/mom-ocean/MOM6/search?q=nk) |              50 |              60 |
| [**restore_salinity**     ](https://github.com/mom-ocean/MOM6/search?q=restore_salinity) |            True |           False |
| [**salt_restore_file**    ](https://github.com/mom-ocean/MOM6/search?q=salt_restore_file) | 'salt_sfc_resto<br>re.nc' |       |
| [**srestore_as_sflux**    ](https://github.com/mom-ocean/MOM6/search?q=srestore_as_sflux) |            True |                 |
| [**temp_salt_init_vertic<br>al_remap_only**](https://github.com/mom-ocean/MOM6/search?q=temp_salt_init_vertical_remap_only) | True |           |
| [**temp_salt_z_init_file**](https://github.com/mom-ocean/MOM6/search?q=temp_salt_z_init_file) | 'ocean_temp_sal<br>t.res.nc' | 'WOA05_pottemp_<br>salt.nc' |
| [**topo_file**            ](https://github.com/mom-ocean/MOM6/search?q=topo_file) |      'topog.nc' | 'ocean_topog_23<br>0424.nc' |
| [**tripolar_n**           ](https://github.com/mom-ocean/MOM6/search?q=tripolar_n) |            True |           False |
| [**use_contemp_abssal**   ](https://github.com/mom-ocean/MOM6/search?q=use_contemp_abssal) |           False |                 |
| [**z_init_file_ptemp_var**](https://github.com/mom-ocean/MOM6/search?q=z_init_file_ptemp_var) |          'temp' |         'PTEMP' |
| [**z_init_file_salt_var** ](https://github.com/mom-ocean/MOM6/search?q=z_init_file_salt_var) |          'salt' |          'SALT' |
| [**z_init_remap_general** ](https://github.com/mom-ocean/MOM6/search?q=z_init_remap_general) |            True |                 |
