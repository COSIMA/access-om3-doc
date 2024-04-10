| Group                 | Variable                  | [ACCESS-OM2_1deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/COSIMA/1deg_jra55_ryf/blob/6ae053d6f28173c4d844df32e63065e27daaecd4/ocean/input.nml) | [ACCESS-OM2_025deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/COSIMA/025deg_jra55_ryf/blob/82e114a736666caedc52c11e0730f5f18fc855e6/ocean/input.nml) | [ACCESS-OM2_01deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/COSIMA/01deg_jra55_ryf/blob/db8159373531de0f9237557308e179ddd4b69b1b/ocean/input.nml) |
| :-------------------- | :------------------------ | --------------: | --------------: | --------------: |
| [auscom_ice_nml       ](https://github.com/mom-ocean/MOM5/search?q=auscom_ice_nml) | [**redsea_gulfbay_sfix**  ](https://github.com/mom-ocean/MOM5/search?q=redsea_gulfbay_sfix) |           False |                 |                 |
| [fms_io_nml           ](https://github.com/mom-ocean/MOM5/search?q=fms_io_nml) | [**checksum_required**    ](https://github.com/mom-ocean/MOM5/search?q=checksum_required) |                 |                 |           False |
|                       | [**fileset_write**        ](https://github.com/mom-ocean/MOM5/search?q=fileset_write) |        'single' |        'single' |         'multi' |
|                       | [**threading_write**      ](https://github.com/mom-ocean/MOM5/search?q=threading_write) |        'single' |        'single' |         'multi' |
| [fms_nml              ](https://github.com/mom-ocean/MOM5/search?q=fms_nml) | [**clock_grain**          ](https://github.com/mom-ocean/MOM5/search?q=clock_grain) |          'LOOP' |          'LOOP' |       'ROUTINE' |
|                       | [**domains_stack_size**   ](https://github.com/mom-ocean/MOM5/search?q=domains_stack_size) |          115200 |                 |          115200 |
| [mpp_io_nml           ](https://github.com/mom-ocean/MOM5/search?q=mpp_io_nml) | [**deflate_level**        ](https://github.com/mom-ocean/MOM5/search?q=deflate_level) |              -1 |               5 |               5 |
| [ocean_adv_vel_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_adv_vel_diag_nml) | [**diag_step**            ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |             576 |
| [ocean_advection_velocity_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_advection_velocity_nml) | [**max_advection_velocit<br>y**](https://github.com/mom-ocean/MOM5/search?q=max_advection_velocity) |        0.5 |             0.5 |             0.3 |
| [ocean_barotropic_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_barotropic_nml) | [**diag_step**            ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |             576 |
| [ocean_bihgen_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_bihgen_friction_nml) | [**bottom_5point**        ](https://github.com/mom-ocean/MOM5/search?q=bottom_5point) |            True |           False |           False |
|                       | [**ncar_boundary_scaling**](https://github.com/mom-ocean/MOM5/search?q=ncar_boundary_scaling) |            True |           False |           False |
|                       | [**vel_micom_bottom**     ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_bottom) |            0.01 |             0.0 |             0.0 |
|                       | [**vel_micom_iso**        ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_iso) |            0.04 |             0.0 |             0.0 |
|                       | [**visc_crit_scale**      ](https://github.com/mom-ocean/MOM5/search?q=visc_crit_scale) |            0.25 |             1.0 |             1.0 |
| [ocean_lapgen_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_lapgen_friction_nml) | [**bottom_5point**        ](https://github.com/mom-ocean/MOM5/search?q=bottom_5point) |            True |                 |                 |
|                       | [**k_smag_aniso**         ](https://github.com/mom-ocean/MOM5/search?q=k_smag_aniso) |             0.0 |                 |                 |
|                       | [**k_smag_iso**           ](https://github.com/mom-ocean/MOM5/search?q=k_smag_iso) |             0.0 |                 |                 |
|                       | [**restrict_polar_visc**  ](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc) |            True |                 |                 |
|                       | [**restrict_polar_visc_l<br>at**](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc_lat) |      60.0 |                 |                 |
|                       | [**restrict_polar_visc_r<br>atio**](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc_ratio) |    0.35 |                 |                 |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |           False |
|                       | [**vel_micom_iso**        ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_iso) |             0.1 |                 |                 |
|                       | [**viscosity_ncar**       ](https://github.com/mom-ocean/MOM5/search?q=viscosity_ncar) |           False |                 |                 |
|                       | [**viscosity_ncar_2007**  ](https://github.com/mom-ocean/MOM5/search?q=viscosity_ncar_2007) |           False |                 |                 |
|                       | [**viscosity_scale_by_ro<br>ssby**](https://github.com/mom-ocean/MOM5/search?q=viscosity_scale_by_rossby) |    True |                 |                 |
|                       | [**viscosity_scale_by_ro<br>ssby_power**](https://github.com/mom-ocean/MOM5/search?q=viscosity_scale_by_rossby_power) | 4.0 |               |                 |
| [ocean_mixdownslope_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_mixdownslope_nml) | [**mixdownslope_mask_gfd<br>l**](https://github.com/mom-ocean/MOM5/search?q=mixdownslope_mask_gfdl) |      False |                 |                 |
|                       | [**mixdownslope_npts**    ](https://github.com/mom-ocean/MOM5/search?q=mixdownslope_npts) |               4 |                 |                 |
|                       | [**read_mixdownslope_mas<br>k**](https://github.com/mom-ocean/MOM5/search?q=read_mixdownslope_mask) |      False |                 |                 |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |           False |
| [ocean_model_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_model_nml) | [**io_layout**            ](https://github.com/mom-ocean/MOM5/search?q=io_layout) |          [4, 3] |          [6, 5] |          [5, 5] |
|                       | [**layout**               ](https://github.com/mom-ocean/MOM5/search?q=layout) |        [16, 15] |        [48, 40] |        [80, 75] |
| [ocean_nphysics_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_nml) | [**use_nphysicsc**        ](https://github.com/mom-ocean/MOM5/search?q=use_nphysicsc) |            True |            True |           False |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |           False |
| [ocean_nphysics_util_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_util_nml) | [**agm_closure**          ](https://github.com/mom-ocean/MOM5/search?q=agm_closure) |            True |            True |                 |
|                       | [**agm_closure_baroclini<br>c**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_baroclinic) |       True |            True |                 |
|                       | [**agm_closure_buoy_freq**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_buoy_freq) |           0.004 |           0.004 |                 |
|                       | [**agm_closure_eady_ave_<br>mixed**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_ave_mixed) |   True |            True |                 |
|                       | [**agm_closure_eady_cap** ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_cap) |            True |            True |                 |
|                       | [**agm_closure_eady_smoo<br>th_horz**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_smooth_horz) | True |            True |                 |
|                       | [**agm_closure_eady_smoo<br>th_vert**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_smooth_vert) | True |            True |                 |
|                       | [**agm_closure_grid_scal<br>ing**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_grid_scaling) |     True |            True |                 |
|                       | [**agm_closure_length**   ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length) |         50000.0 |         20000.0 |                 |
|                       | [**agm_closure_lower_dep<br>th**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_lower_depth) |    2000.0 |          2000.0 |                 |
|                       | [**agm_closure_max**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_max) |           600.0 |           200.0 |                 |
|                       | [**agm_closure_min**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_min) |            50.0 |             1.0 |                 |
|                       | [**agm_closure_scaling**  ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_scaling) |            0.07 |            0.07 |                 |
|                       | [**agm_closure_upper_dep<br>th**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_upper_depth) |     100.0 |           100.0 |                 |
|                       | [**aredi**                ](https://github.com/mom-ocean/MOM5/search?q=aredi) |           600.0 |           200.0 |                 |
|                       | [**aredi_diffusivity_gri<br>d_scaling**](https://github.com/mom-ocean/MOM5/search?q=aredi_diffusivity_grid_scaling) |    |            True |                 |
|                       | [**aredi_equal_agm**      ](https://github.com/mom-ocean/MOM5/search?q=aredi_equal_agm) |           False |           False |                 |
|                       | [**drhodz_mom4p1**        ](https://github.com/mom-ocean/MOM5/search?q=drhodz_mom4p1) |            True |            True |                 |
|                       | [**nphysics_util_zero_in<br>it**](https://github.com/mom-ocean/MOM5/search?q=nphysics_util_zero_init) |      True |            True |                 |
| [ocean_nphysicsc_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysicsc_nml) | [**bv_freq_smooth_vert**  ](https://github.com/mom-ocean/MOM5/search?q=bv_freq_smooth_vert) |            True |            True |                 |
|                       | [**bvp_bc_mode**          ](https://github.com/mom-ocean/MOM5/search?q=bvp_bc_mode) |               2 |               2 |                 |
|                       | [**bvp_min_speed**        ](https://github.com/mom-ocean/MOM5/search?q=bvp_min_speed) |             0.1 |             0.1 |                 |
|                       | [**bvp_speed**            ](https://github.com/mom-ocean/MOM5/search?q=bvp_speed) |             0.0 |             0.0 |                 |
|                       | [**do_gm_skewsion**       ](https://github.com/mom-ocean/MOM5/search?q=do_gm_skewsion) |            True |            True |                 |
|                       | [**do_neutral_diffusion** ](https://github.com/mom-ocean/MOM5/search?q=do_neutral_diffusion) |            True |            True |                 |
|                       | [**epsln_bv_freq**        ](https://github.com/mom-ocean/MOM5/search?q=epsln_bv_freq) |           1e-12 |           1e-12 |                 |
|                       | [**gm_skewsion_bvproblem**](https://github.com/mom-ocean/MOM5/search?q=gm_skewsion_bvproblem) |            True |            True |                 |
|                       | [**gm_skewsion_modes**    ](https://github.com/mom-ocean/MOM5/search?q=gm_skewsion_modes) |           False |           False |                 |
|                       | [**neutral_eddy_depth**   ](https://github.com/mom-ocean/MOM5/search?q=neutral_eddy_depth) |            True |            True |                 |
|                       | [**neutral_physics_limit**](https://github.com/mom-ocean/MOM5/search?q=neutral_physics_limit) |            True |            True |                 |
|                       | [**number_bc_modes**      ](https://github.com/mom-ocean/MOM5/search?q=number_bc_modes) |               2 |               2 |                 |
|                       | [**regularize_psi**       ](https://github.com/mom-ocean/MOM5/search?q=regularize_psi) |           False |           False |                 |
|                       | [**smax_psi**             ](https://github.com/mom-ocean/MOM5/search?q=smax_psi) |            0.01 |            0.01 |                 |
|                       | [**smooth_psi**           ](https://github.com/mom-ocean/MOM5/search?q=smooth_psi) |            True |            True |                 |
|                       | [**tmask_neutral_on**     ](https://github.com/mom-ocean/MOM5/search?q=tmask_neutral_on) |            True |            True |                 |
|                       | [**turb_blayer_min**      ](https://github.com/mom-ocean/MOM5/search?q=turb_blayer_min) |            50.0 |            50.0 |                 |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |           False |
| [ocean_sbc_nml        ](https://github.com/mom-ocean/MOM5/search?q=ocean_sbc_nml) | [**do_bitwise_exact_sum** ](https://github.com/mom-ocean/MOM5/search?q=do_bitwise_exact_sum) |            True |           False |           False |
|                       | [**max_delta_salinity_re<br>store**](https://github.com/mom-ocean/MOM5/search?q=max_delta_salinity_restore) |   -0.5 |             0.5 |             0.5 |
|                       | [**ocean_ice_salt_limit** ](https://github.com/mom-ocean/MOM5/search?q=ocean_ice_salt_limit) |                 |           0.006 |           0.006 |
|                       | [**runoffspread**         ](https://github.com/mom-ocean/MOM5/search?q=runoffspread) |                 |                 |           False |
|                       | [**salt_restore_tscale**  ](https://github.com/mom-ocean/MOM5/search?q=salt_restore_tscale) |           21.28 |           21.28 |            10.0 |
| [ocean_sigma_transport_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_sigma_transport_nml) | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |           False |
| [ocean_submesoscale_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_submesoscale_nml) | [**smooth_advect_transpo<br>rt_num**](https://github.com/mom-ocean/MOM5/search?q=smooth_advect_transport_num) |     2 |               4 |               4 |
|                       | [**smooth_psi_num**       ](https://github.com/mom-ocean/MOM5/search?q=smooth_psi_num) |               2 |               3 |               3 |
| [ocean_tracer_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_diag_nml) | [**diag_step**            ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |             576 |
| [ocean_velocity_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_velocity_diag_nml) | [**diag_step**            ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |             576 |
|                       | [**energy_diag_step**     ](https://github.com/mom-ocean/MOM5/search?q=energy_diag_step) |            4320 |            4320 |            5760 |
| [ocean_vert_mix_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_vert_mix_nml) | [**j09_bgmax**            ](https://github.com/mom-ocean/MOM5/search?q=j09_bgmax) |           5e-06 |                 |           1e-06 |
|                       | [**j09_bgmin**            ](https://github.com/mom-ocean/MOM5/search?q=j09_bgmin) |           1e-06 |                 |           1e-06 |
|                       | [**j09_diffusivity**      ](https://github.com/mom-ocean/MOM5/search?q=j09_diffusivity) |            True |                 |            True |
|                       | [**j09_lat**              ](https://github.com/mom-ocean/MOM5/search?q=j09_lat) |            20.0 |                 |            20.0 |
| [xgrid_nml            ](https://github.com/mom-ocean/MOM5/search?q=xgrid_nml) | [**do_alltoall**          ](https://github.com/mom-ocean/MOM5/search?q=do_alltoall) |                 |                 |            True |
|                       | [**do_alltoallv**         ](https://github.com/mom-ocean/MOM5/search?q=do_alltoallv) |                 |                 |            True |
