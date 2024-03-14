| Group                 | Variable                  | [ACCESS-OM2_1deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/COSIMA/1deg_jra55_ryf/blob/7c6be951530901082be8106a4f819e437fbeb19b/ocean/input.nml) | [ACCESS-OM2_025deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/COSIMA/025deg_jra55_ryf/blob/0b84d5a8c983d8121f784654381ef5f4acc74688/ocean/input.nml) |
| :-------------------- | :------------------------ | --------------: | --------------: |
| [auscom_ice_nml       ](https://github.com/mom-ocean/MOM5/search?q=auscom_ice_nml) | [aice_cutoff              ](https://github.com/mom-ocean/MOM5/search?q=aice_cutoff) |            0.15 |            0.15 |
|                       | [chk_i2o_fields           ](https://github.com/mom-ocean/MOM5/search?q=chk_i2o_fields) |           False |           False |
|                       | [chk_o2i_fields           ](https://github.com/mom-ocean/MOM5/search?q=chk_o2i_fields) |           False |           False |
|                       | [do_ice_once              ](https://github.com/mom-ocean/MOM5/search?q=do_ice_once) |           False |           False |
|                       | [fixmeltt                 ](https://github.com/mom-ocean/MOM5/search?q=fixmeltt) |           False |           False |
|                       | [frazil_factor            ](https://github.com/mom-ocean/MOM5/search?q=frazil_factor) |             1.0 |             1.0 |
|                       | [iceform_adj_salt         ](https://github.com/mom-ocean/MOM5/search?q=iceform_adj_salt) |           False |           False |
|                       | [icemlt_factor            ](https://github.com/mom-ocean/MOM5/search?q=icemlt_factor) |             1.0 |             1.0 |
|                       | [kmxice                   ](https://github.com/mom-ocean/MOM5/search?q=kmxice) |               5 |               5 |
|                       | [pop_icediag              ](https://github.com/mom-ocean/MOM5/search?q=pop_icediag) |            True |            True |
|                       | [**redsea_gulfbay_sfix**  ](https://github.com/mom-ocean/MOM5/search?q=redsea_gulfbay_sfix) |           False |                 |
|                       | [sign_stflx               ](https://github.com/mom-ocean/MOM5/search?q=sign_stflx) |             1.0 |             1.0 |
|                       | [tmelt                    ](https://github.com/mom-ocean/MOM5/search?q=tmelt) |          -0.216 |          -0.216 |
|                       | [use_ioaice               ](https://github.com/mom-ocean/MOM5/search?q=use_ioaice) |            True |            True |
| [diag_manager_nml     ](https://github.com/mom-ocean/MOM5/search?q=diag_manager_nml) | [debug_diag_manager       ](https://github.com/mom-ocean/MOM5/search?q=debug_diag_manager) |           False |           False |
|                       | [issue_oor_warnings       ](https://github.com/mom-ocean/MOM5/search?q=issue_oor_warnings) |            True |            True |
|                       | [max_axes                 ](https://github.com/mom-ocean/MOM5/search?q=max_axes) |             400 |             400 |
|                       | [max_files                ](https://github.com/mom-ocean/MOM5/search?q=max_files) |             200 |             200 |
|                       | [max_num_axis_sets        ](https://github.com/mom-ocean/MOM5/search?q=max_num_axis_sets) |             200 |             200 |
| [fms_io_nml           ](https://github.com/mom-ocean/MOM5/search?q=fms_io_nml) | [fileset_write            ](https://github.com/mom-ocean/MOM5/search?q=fileset_write) |        'single' |        'single' |
|                       | [threading_read           ](https://github.com/mom-ocean/MOM5/search?q=threading_read) |         'multi' |         'multi' |
|                       | [threading_write          ](https://github.com/mom-ocean/MOM5/search?q=threading_write) |        'single' |        'single' |
| [fms_nml              ](https://github.com/mom-ocean/MOM5/search?q=fms_nml) | [clock_grain              ](https://github.com/mom-ocean/MOM5/search?q=clock_grain) |          'LOOP' |          'LOOP' |
|                       | [**domains_stack_size**   ](https://github.com/mom-ocean/MOM5/search?q=domains_stack_size) |          115200 |                 |
| [mom_oasis3_interface_nml](https://github.com/mom-ocean/MOM5/search?q=mom_oasis3_interface_nml) | [fields_in                ](https://github.com/mom-ocean/MOM5/search?q=fields_in) | ['u_flux', 'v_f<br>lux', 'lprec', <br>'fprec', 'salt_<br>flx', 'mh_flux'<br>, 'sw_flux', 'q<br>_flux', 't_flux<br>', 'lw_flux', '<br>runof', 'p', 'a<br>ice', 'wfimelt'<br>, 'wfiform', 'l<br>icefw', 'liceht<br>'] | ['u_flux', 'v_f<br>lux', 'lprec', <br>'fprec', 'salt_<br>flx', 'mh_flux'<br>, 'sw_flux', 'q<br>_flux', 't_flux<br>', 'lw_flux', '<br>runof', 'p', 'a<br>ice', 'wfimelt'<br>, 'wfiform', 'l<br>icefw', 'liceht<br>'] |
|                       | [fields_out               ](https://github.com/mom-ocean/MOM5/search?q=fields_out) | ['t_surf', 's_s<br>urf', 'u_surf',<br> 'v_surf', 'dss<br>ldx', 'dssldy',<br> 'frazil'] | ['t_surf', 's_s<br>urf', 'u_surf',<br> 'v_surf', 'dss<br>ldx', 'dssldy',<br> 'frazil'] |
|                       | [num_fields_in            ](https://github.com/mom-ocean/MOM5/search?q=num_fields_in) |              17 |              17 |
|                       | [num_fields_out           ](https://github.com/mom-ocean/MOM5/search?q=num_fields_out) |               7 |               7 |
|                       | [send_after_ocean_upda<br>te](https://github.com/mom-ocean/MOM5/search?q=send_after_ocean_update) |          True |            True |
|                       | [send_before_ocean_upd<br>ate](https://github.com/mom-ocean/MOM5/search?q=send_before_ocean_update) |        False |           False |
| [mpp_io_nml           ](https://github.com/mom-ocean/MOM5/search?q=mpp_io_nml) | [**deflate_level**        ](https://github.com/mom-ocean/MOM5/search?q=deflate_level) |              -1 |               5 |
|                       | [shuffle                  ](https://github.com/mom-ocean/MOM5/search?q=shuffle) |               1 |               1 |
| [ocean_adv_vel_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_adv_vel_diag_nml) | [diag_step                ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |
|                       | [large_cfl_value          ](https://github.com/mom-ocean/MOM5/search?q=large_cfl_value) |            10.0 |            10.0 |
|                       | [max_cfl_value            ](https://github.com/mom-ocean/MOM5/search?q=max_cfl_value) |           100.0 |           100.0 |
|                       | [verbose_cfl              ](https://github.com/mom-ocean/MOM5/search?q=verbose_cfl) |            True |            True |
| [ocean_advection_velocity_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_advection_velocity_nml) | [max_advection_velocit<br>y](https://github.com/mom-ocean/MOM5/search?q=max_advection_velocity) |            0.5 |             0.5 |
| [ocean_barotropic_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_barotropic_nml) | [barotropic_halo          ](https://github.com/mom-ocean/MOM5/search?q=barotropic_halo) |              10 |              10 |
|                       | [barotropic_time_stepp<br>ing_a](https://github.com/mom-ocean/MOM5/search?q=barotropic_time_stepping_a) |       True |            True |
|                       | [barotropic_time_stepp<br>ing_b](https://github.com/mom-ocean/MOM5/search?q=barotropic_time_stepping_b) |      False |           False |
|                       | [diag_step                ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |
|                       | [eta_max                  ](https://github.com/mom-ocean/MOM5/search?q=eta_max) |             8.0 |             8.0 |
|                       | [frac_crit_cell_height    ](https://github.com/mom-ocean/MOM5/search?q=frac_crit_cell_height) |             0.2 |             0.2 |
|                       | [pred_corr_gamma          ](https://github.com/mom-ocean/MOM5/search?q=pred_corr_gamma) |             0.2 |             0.2 |
|                       | [smooth_eta_diag_lapla<br>cian](https://github.com/mom-ocean/MOM5/search?q=smooth_eta_diag_laplacian) |        True |            True |
|                       | [smooth_eta_t_biharmon<br>ic](https://github.com/mom-ocean/MOM5/search?q=smooth_eta_t_biharmonic) |         False |           False |
|                       | [smooth_eta_t_laplacia<br>n](https://github.com/mom-ocean/MOM5/search?q=smooth_eta_t_laplacian) |           True |            True |
|                       | [smooth_pbot_t_biharmo<br>nic](https://github.com/mom-ocean/MOM5/search?q=smooth_pbot_t_biharmonic) |        False |           False |
|                       | [smooth_pbot_t_laplaci<br>an](https://github.com/mom-ocean/MOM5/search?q=smooth_pbot_t_laplacian) |          True |            True |
|                       | [truncate_eta             ](https://github.com/mom-ocean/MOM5/search?q=truncate_eta) |           False |           False |
|                       | [use_legacy_barotropic<br>_halos](https://github.com/mom-ocean/MOM5/search?q=use_legacy_barotropic_halos) |     False |           False |
|                       | [vel_micom_bih            ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_bih) |            0.01 |            0.01 |
|                       | [vel_micom_lap            ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_lap) |            0.05 |            0.05 |
|                       | [vel_micom_lap_diag       ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_lap_diag) |             0.2 |             0.2 |
|                       | [verbose_truncate         ](https://github.com/mom-ocean/MOM5/search?q=verbose_truncate) |            True |            True |
|                       | [zero_tendency            ](https://github.com/mom-ocean/MOM5/search?q=zero_tendency) |           False |           False |
| [ocean_bbc_nml        ](https://github.com/mom-ocean/MOM5/search?q=ocean_bbc_nml) | [bmf_implicit             ](https://github.com/mom-ocean/MOM5/search?q=bmf_implicit) |            True |            True |
|                       | [cdbot_hi                 ](https://github.com/mom-ocean/MOM5/search?q=cdbot_hi) |           0.007 |           0.007 |
|                       | [cdbot_roughness_uamp     ](https://github.com/mom-ocean/MOM5/search?q=cdbot_roughness_uamp) |            True |            True |
|                       | [uresidual                ](https://github.com/mom-ocean/MOM5/search?q=uresidual) |            0.05 |            0.05 |
| [ocean_bih_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_bih_friction_nml) | [bih_friction_scheme      ](https://github.com/mom-ocean/MOM5/search?q=bih_friction_scheme) |       'general' |       'general' |
| [ocean_bih_tracer_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_bih_tracer_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_bihcst_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_bihcst_friction_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_bihgen_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_bihgen_friction_nml) | [**bottom_5point**        ](https://github.com/mom-ocean/MOM5/search?q=bottom_5point) |            True |           False |
|                       | [eq_lat_micom             ](https://github.com/mom-ocean/MOM5/search?q=eq_lat_micom) |             0.0 |             0.0 |
|                       | [eq_vel_micom_aniso       ](https://github.com/mom-ocean/MOM5/search?q=eq_vel_micom_aniso) |             0.0 |             0.0 |
|                       | [eq_vel_micom_iso         ](https://github.com/mom-ocean/MOM5/search?q=eq_vel_micom_iso) |             0.0 |             0.0 |
|                       | [equatorial_zonal         ](https://github.com/mom-ocean/MOM5/search?q=equatorial_zonal) |           False |           False |
|                       | [k_smag_aniso             ](https://github.com/mom-ocean/MOM5/search?q=k_smag_aniso) |             0.0 |             0.0 |
|                       | [k_smag_iso               ](https://github.com/mom-ocean/MOM5/search?q=k_smag_iso) |             2.0 |             2.0 |
|                       | [**ncar_boundary_scaling**](https://github.com/mom-ocean/MOM5/search?q=ncar_boundary_scaling) |            True |           False |
|                       | [ncar_boundary_scaling<br>_read](https://github.com/mom-ocean/MOM5/search?q=ncar_boundary_scaling_read) |      False |           False |
|                       | [ncar_rescale_power       ](https://github.com/mom-ocean/MOM5/search?q=ncar_rescale_power) |               2 |               2 |
|                       | [ncar_vconst_4            ](https://github.com/mom-ocean/MOM5/search?q=ncar_vconst_4) |           2e-08 |           2e-08 |
|                       | [ncar_vconst_5            ](https://github.com/mom-ocean/MOM5/search?q=ncar_vconst_5) |               5 |               5 |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
|                       | [vel_micom_aniso          ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_aniso) |             0.0 |             0.0 |
|                       | [**vel_micom_bottom**     ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_bottom) |            0.01 |             0.0 |
|                       | [**vel_micom_iso**        ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_iso) |            0.04 |             0.0 |
|                       | [**visc_crit_scale**      ](https://github.com/mom-ocean/MOM5/search?q=visc_crit_scale) |            0.25 |             1.0 |
| [ocean_convect_nml    ](https://github.com/mom-ocean/MOM5/search?q=ocean_convect_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_coriolis_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_coriolis_nml) | [acor                     ](https://github.com/mom-ocean/MOM5/search?q=acor) |             0.5 |             0.5 |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_density_nml    ](https://github.com/mom-ocean/MOM5/search?q=ocean_density_nml) | [eos_linear               ](https://github.com/mom-ocean/MOM5/search?q=eos_linear) |           False |           False |
|                       | [eos_preteos10            ](https://github.com/mom-ocean/MOM5/search?q=eos_preteos10) |            True |            True |
|                       | [layer_nk                 ](https://github.com/mom-ocean/MOM5/search?q=layer_nk) |              80 |              80 |
|                       | [neutralrho_max           ](https://github.com/mom-ocean/MOM5/search?q=neutralrho_max) |          1038.0 |          1038.0 |
|                       | [neutralrho_min           ](https://github.com/mom-ocean/MOM5/search?q=neutralrho_min) |          1028.0 |          1028.0 |
|                       | [potrho_max               ](https://github.com/mom-ocean/MOM5/search?q=potrho_max) |          1038.0 |          1038.0 |
|                       | [potrho_min               ](https://github.com/mom-ocean/MOM5/search?q=potrho_min) |          1028.0 |          1028.0 |
| [ocean_domains_nml    ](https://github.com/mom-ocean/MOM5/search?q=ocean_domains_nml) | [max_tracers              ](https://github.com/mom-ocean/MOM5/search?q=max_tracers) |               5 |               5 |
| [ocean_form_drag_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_form_drag_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_frazil_nml     ](https://github.com/mom-ocean/MOM5/search?q=ocean_frazil_nml) | [frazil_only_in_surfac<br>e](https://github.com/mom-ocean/MOM5/search?q=frazil_only_in_surface) |          False |           False |
|                       | [freezing_temp_preteos<br>10](https://github.com/mom-ocean/MOM5/search?q=freezing_temp_preteos10) |          True |            True |
|                       | [freezing_temp_simple     ](https://github.com/mom-ocean/MOM5/search?q=freezing_temp_simple) |           False |           False |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_increment_eta_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_increment_eta_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_increment_tracer_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_increment_tracer_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_increment_velocity_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_increment_velocity_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_lap_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_lap_friction_nml) | [lap_friction_scheme      ](https://github.com/mom-ocean/MOM5/search?q=lap_friction_scheme) |       'general' |       'general' |
| [ocean_lap_tracer_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_lap_tracer_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_lapcst_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_lapcst_friction_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_lapgen_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_lapgen_friction_nml) | [**bottom_5point**        ](https://github.com/mom-ocean/MOM5/search?q=bottom_5point) |            True |                 |
|                       | [**k_smag_aniso**         ](https://github.com/mom-ocean/MOM5/search?q=k_smag_aniso) |             0.0 |                 |
|                       | [**k_smag_iso**           ](https://github.com/mom-ocean/MOM5/search?q=k_smag_iso) |             0.0 |                 |
|                       | [**restrict_polar_visc**  ](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc) |            True |                 |
|                       | [**restrict_polar_visc_l<br>at**](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc_lat) |      60.0 |                 |
|                       | [**restrict_polar_visc_r<br>atio**](https://github.com/mom-ocean/MOM5/search?q=restrict_polar_visc_ratio) |    0.35 |                 |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |
|                       | [**vel_micom_iso**        ](https://github.com/mom-ocean/MOM5/search?q=vel_micom_iso) |             0.1 |                 |
|                       | [**viscosity_ncar**       ](https://github.com/mom-ocean/MOM5/search?q=viscosity_ncar) |           False |                 |
|                       | [**viscosity_ncar_2007**  ](https://github.com/mom-ocean/MOM5/search?q=viscosity_ncar_2007) |           False |                 |
|                       | [**viscosity_scale_by_ro<br>ssby**](https://github.com/mom-ocean/MOM5/search?q=viscosity_scale_by_rossby) |    True |                 |
|                       | [**viscosity_scale_by_ro<br>ssby_power**](https://github.com/mom-ocean/MOM5/search?q=viscosity_scale_by_rossby_power) | 4.0 |               |
| [ocean_mixdownslope_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_mixdownslope_nml) | [**mixdownslope_mask_gfd<br>l**](https://github.com/mom-ocean/MOM5/search?q=mixdownslope_mask_gfdl) |      False |                 |
|                       | [**mixdownslope_npts**    ](https://github.com/mom-ocean/MOM5/search?q=mixdownslope_npts) |               4 |                 |
|                       | [**read_mixdownslope_mas<br>k**](https://github.com/mom-ocean/MOM5/search?q=read_mixdownslope_mask) |      False |                 |
|                       | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |
| [ocean_model_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_model_nml) | [baroclinic_split         ](https://github.com/mom-ocean/MOM5/search?q=baroclinic_split) |               1 |               1 |
|                       | [barotropic_split         ](https://github.com/mom-ocean/MOM5/search?q=barotropic_split) |              80 |              80 |
|                       | [cmip_units               ](https://github.com/mom-ocean/MOM5/search?q=cmip_units) |            True |            True |
|                       | [debug                    ](https://github.com/mom-ocean/MOM5/search?q=debug) |           False |           False |
|                       | [**io_layout**            ](https://github.com/mom-ocean/MOM5/search?q=io_layout) |          [4, 3] |          [6, 5] |
|                       | [**layout**               ](https://github.com/mom-ocean/MOM5/search?q=layout) |        [16, 15] |        [48, 40] |
|                       | [surface_height_split     ](https://github.com/mom-ocean/MOM5/search?q=surface_height_split) |               1 |               1 |
|                       | [time_tendency            ](https://github.com/mom-ocean/MOM5/search?q=time_tendency) |      'twolevel' |      'twolevel' |
|                       | [vertical_coordinate      ](https://github.com/mom-ocean/MOM5/search?q=vertical_coordinate) |         'zstar' |         'zstar' |
| [ocean_momentum_source_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_momentum_source_nml) | [rayleigh_damp_exp_fro<br>m_bottom](https://github.com/mom-ocean/MOM5/search?q=rayleigh_damp_exp_from_bottom) |   False |           False |
|                       | [use_rayleigh_damp_tab<br>le](https://github.com/mom-ocean/MOM5/search?q=use_rayleigh_damp_table) |          True |            True |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_nphysics_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_nml) | [use_nphysicsa            ](https://github.com/mom-ocean/MOM5/search?q=use_nphysicsa) |           False |           False |
|                       | [use_nphysicsb            ](https://github.com/mom-ocean/MOM5/search?q=use_nphysicsb) |           False |           False |
|                       | [use_nphysicsc            ](https://github.com/mom-ocean/MOM5/search?q=use_nphysicsc) |            True |            True |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_nphysics_util_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_util_nml) | [agm_closure              ](https://github.com/mom-ocean/MOM5/search?q=agm_closure) |            True |            True |
|                       | [agm_closure_baroclini<br>c](https://github.com/mom-ocean/MOM5/search?q=agm_closure_baroclinic) |           True |            True |
|                       | [agm_closure_buoy_freq    ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_buoy_freq) |           0.004 |           0.004 |
|                       | [agm_closure_eady_ave_<br>mixed](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_ave_mixed) |       True |            True |
|                       | [agm_closure_eady_cap     ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_cap) |            True |            True |
|                       | [agm_closure_eady_smoo<br>th_horz](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_smooth_horz) |     True |            True |
|                       | [agm_closure_eady_smoo<br>th_vert](https://github.com/mom-ocean/MOM5/search?q=agm_closure_eady_smooth_vert) |     True |            True |
|                       | [agm_closure_grid_scal<br>ing](https://github.com/mom-ocean/MOM5/search?q=agm_closure_grid_scaling) |         True |            True |
|                       | [**agm_closure_length**   ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length) |         50000.0 |         20000.0 |
|                       | [agm_closure_lower_dep<br>th](https://github.com/mom-ocean/MOM5/search?q=agm_closure_lower_depth) |        2000.0 |          2000.0 |
|                       | [**agm_closure_max**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_max) |           600.0 |           200.0 |
|                       | [**agm_closure_min**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_min) |            50.0 |             1.0 |
|                       | [agm_closure_scaling      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_scaling) |            0.07 |            0.07 |
|                       | [agm_closure_upper_dep<br>th](https://github.com/mom-ocean/MOM5/search?q=agm_closure_upper_depth) |         100.0 |           100.0 |
|                       | [**aredi**                ](https://github.com/mom-ocean/MOM5/search?q=aredi) |           600.0 |           200.0 |
|                       | [**aredi_diffusivity_gri<br>d_scaling**](https://github.com/mom-ocean/MOM5/search?q=aredi_diffusivity_grid_scaling) |    |            True |
|                       | [aredi_equal_agm          ](https://github.com/mom-ocean/MOM5/search?q=aredi_equal_agm) |           False |           False |
|                       | [drhodz_mom4p1            ](https://github.com/mom-ocean/MOM5/search?q=drhodz_mom4p1) |            True |            True |
|                       | [nphysics_util_zero_in<br>it](https://github.com/mom-ocean/MOM5/search?q=nphysics_util_zero_init) |          True |            True |
| [ocean_nphysicsa_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysicsa_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_nphysicsb_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysicsb_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_nphysicsc_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysicsc_nml) | [bv_freq_smooth_vert      ](https://github.com/mom-ocean/MOM5/search?q=bv_freq_smooth_vert) |            True |            True |
|                       | [bvp_bc_mode              ](https://github.com/mom-ocean/MOM5/search?q=bvp_bc_mode) |               2 |               2 |
|                       | [bvp_min_speed            ](https://github.com/mom-ocean/MOM5/search?q=bvp_min_speed) |             0.1 |             0.1 |
|                       | [bvp_speed                ](https://github.com/mom-ocean/MOM5/search?q=bvp_speed) |             0.0 |             0.0 |
|                       | [do_gm_skewsion           ](https://github.com/mom-ocean/MOM5/search?q=do_gm_skewsion) |            True |            True |
|                       | [do_neutral_diffusion     ](https://github.com/mom-ocean/MOM5/search?q=do_neutral_diffusion) |            True |            True |
|                       | [epsln_bv_freq            ](https://github.com/mom-ocean/MOM5/search?q=epsln_bv_freq) |           1e-12 |           1e-12 |
|                       | [gm_skewsion_bvproblem    ](https://github.com/mom-ocean/MOM5/search?q=gm_skewsion_bvproblem) |            True |            True |
|                       | [gm_skewsion_modes        ](https://github.com/mom-ocean/MOM5/search?q=gm_skewsion_modes) |           False |           False |
|                       | [neutral_eddy_depth       ](https://github.com/mom-ocean/MOM5/search?q=neutral_eddy_depth) |            True |            True |
|                       | [neutral_physics_limit    ](https://github.com/mom-ocean/MOM5/search?q=neutral_physics_limit) |            True |            True |
|                       | [number_bc_modes          ](https://github.com/mom-ocean/MOM5/search?q=number_bc_modes) |               2 |               2 |
|                       | [regularize_psi           ](https://github.com/mom-ocean/MOM5/search?q=regularize_psi) |           False |           False |
|                       | [smax_psi                 ](https://github.com/mom-ocean/MOM5/search?q=smax_psi) |            0.01 |            0.01 |
|                       | [smooth_psi               ](https://github.com/mom-ocean/MOM5/search?q=smooth_psi) |            True |            True |
|                       | [tmask_neutral_on         ](https://github.com/mom-ocean/MOM5/search?q=tmask_neutral_on) |            True |            True |
|                       | [turb_blayer_min          ](https://github.com/mom-ocean/MOM5/search?q=turb_blayer_min) |            50.0 |            50.0 |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_overexchange_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_overexchange_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_overflow_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_overflow_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_overflow_ofp_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_overflow_ofp_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_rivermix_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_rivermix_nml) | [river_diffuse_salt       ](https://github.com/mom-ocean/MOM5/search?q=river_diffuse_salt) |            True |            True |
|                       | [river_diffuse_temp       ](https://github.com/mom-ocean/MOM5/search?q=river_diffuse_temp) |            True |            True |
|                       | [river_diffusion_thick<br>ness](https://github.com/mom-ocean/MOM5/search?q=river_diffusion_thickness) |         0.0 |             0.0 |
|                       | [river_diffusivity        ](https://github.com/mom-ocean/MOM5/search?q=river_diffusivity) |             0.0 |             0.0 |
|                       | [river_insertion_thick<br>ness](https://github.com/mom-ocean/MOM5/search?q=river_insertion_thickness) |        40.0 |            40.0 |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_riverspread_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_riverspread_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_rough_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_rough_nml) | [rough_scheme             ](https://github.com/mom-ocean/MOM5/search?q=rough_scheme) |      'beljaars' |      'beljaars' |
| [ocean_sbc_nml        ](https://github.com/mom-ocean/MOM5/search?q=ocean_sbc_nml) | [avg_sfc_temp_salt_eta    ](https://github.com/mom-ocean/MOM5/search?q=avg_sfc_temp_salt_eta) |            True |            True |
|                       | [avg_sfc_velocity         ](https://github.com/mom-ocean/MOM5/search?q=avg_sfc_velocity) |            True |            True |
|                       | [calvingspread            ](https://github.com/mom-ocean/MOM5/search?q=calvingspread) |           False |           False |
|                       | [**do_bitwise_exact_sum** ](https://github.com/mom-ocean/MOM5/search?q=do_bitwise_exact_sum) |            True |           False |
|                       | [do_flux_correction       ](https://github.com/mom-ocean/MOM5/search?q=do_flux_correction) |           False |           False |
|                       | [land_model_heat_fluxe<br>s](https://github.com/mom-ocean/MOM5/search?q=land_model_heat_fluxes) |          False |           False |
|                       | [**max_delta_salinity_re<br>store**](https://github.com/mom-ocean/MOM5/search?q=max_delta_salinity_restore) |   -0.5 |             0.5 |
|                       | [max_ice_thickness        ](https://github.com/mom-ocean/MOM5/search?q=max_ice_thickness) |             0.0 |             0.0 |
|                       | [**ocean_ice_salt_limit** ](https://github.com/mom-ocean/MOM5/search?q=ocean_ice_salt_limit) |                 |           0.006 |
|                       | [read_restore_mask        ](https://github.com/mom-ocean/MOM5/search?q=read_restore_mask) |           False |           False |
|                       | [restore_mask_gfdl        ](https://github.com/mom-ocean/MOM5/search?q=restore_mask_gfdl) |           False |           False |
|                       | [runoff_salinity          ](https://github.com/mom-ocean/MOM5/search?q=runoff_salinity) |             0.0 |             0.0 |
|                       | [salt_correction_scale    ](https://github.com/mom-ocean/MOM5/search?q=salt_correction_scale) |             0.0 |             0.0 |
|                       | [salt_restore_as_salt_<br>flux](https://github.com/mom-ocean/MOM5/search?q=salt_restore_as_salt_flux) |        True |            True |
|                       | [salt_restore_tscale      ](https://github.com/mom-ocean/MOM5/search?q=salt_restore_tscale) |           21.28 |           21.28 |
|                       | [salt_restore_under_ic<br>e](https://github.com/mom-ocean/MOM5/search?q=salt_restore_under_ice) |           True |            True |
|                       | [temp_restore_tscale      ](https://github.com/mom-ocean/MOM5/search?q=temp_restore_tscale) |           -10.0 |           -10.0 |
|                       | [use_full_patm_for_sea<br>_level](https://github.com/mom-ocean/MOM5/search?q=use_full_patm_for_sea_level) |     False |           False |
|                       | [use_waterflux            ](https://github.com/mom-ocean/MOM5/search?q=use_waterflux) |            True |            True |
|                       | [zero_heat_fluxes         ](https://github.com/mom-ocean/MOM5/search?q=zero_heat_fluxes) |           False |           False |
|                       | [zero_net_salt_correct<br>ion](https://github.com/mom-ocean/MOM5/search?q=zero_net_salt_correction) |        False |           False |
|                       | [zero_net_salt_restore    ](https://github.com/mom-ocean/MOM5/search?q=zero_net_salt_restore) |            True |            True |
|                       | [zero_net_water_correc<br>tion](https://github.com/mom-ocean/MOM5/search?q=zero_net_water_correction) |       False |           False |
|                       | [zero_net_water_couple<br>_restore](https://github.com/mom-ocean/MOM5/search?q=zero_net_water_couple_restore) |    True |            True |
|                       | [zero_net_water_couple<br>r](https://github.com/mom-ocean/MOM5/search?q=zero_net_water_coupler) |           True |            True |
|                       | [zero_net_water_restor<br>e](https://github.com/mom-ocean/MOM5/search?q=zero_net_water_restore) |           True |            True |
|                       | [zero_surface_stress      ](https://github.com/mom-ocean/MOM5/search?q=zero_surface_stress) |           False |           False |
|                       | [zero_water_fluxes        ](https://github.com/mom-ocean/MOM5/search?q=zero_water_fluxes) |           False |           False |
| [ocean_shortwave_csiro_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_shortwave_csiro_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_shortwave_gfdl_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_shortwave_gfdl_nml) | [enforce_sw_frac          ](https://github.com/mom-ocean/MOM5/search?q=enforce_sw_frac) |            True |            True |
|                       | [optics_manizza           ](https://github.com/mom-ocean/MOM5/search?q=optics_manizza) |            True |            True |
|                       | [optics_morel_antoine     ](https://github.com/mom-ocean/MOM5/search?q=optics_morel_antoine) |           False |           False |
|                       | [read_chl                 ](https://github.com/mom-ocean/MOM5/search?q=read_chl) |            True |            True |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
|                       | [zmax_pen                 ](https://github.com/mom-ocean/MOM5/search?q=zmax_pen) |       1000000.0 |       1000000.0 |
| [ocean_shortwave_jerlov_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_shortwave_jerlov_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_shortwave_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_shortwave_nml) | [use_shortwave_csiro      ](https://github.com/mom-ocean/MOM5/search?q=use_shortwave_csiro) |           False |           False |
|                       | [use_shortwave_gfdl       ](https://github.com/mom-ocean/MOM5/search?q=use_shortwave_gfdl) |            True |            True |
|                       | [use_shortwave_jerlov     ](https://github.com/mom-ocean/MOM5/search?q=use_shortwave_jerlov) |           False |           False |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_sigma_transport_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_sigma_transport_nml) | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |           False |
| [ocean_sponges_eta_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_sponges_eta_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_sponges_tracer_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_sponges_tracer_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_sponges_velocity_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_sponges_velocity_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_submesoscale_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_submesoscale_nml) | [coefficient_ce           ](https://github.com/mom-ocean/MOM5/search?q=coefficient_ce) |            0.05 |            0.05 |
|                       | [front_length_const       ](https://github.com/mom-ocean/MOM5/search?q=front_length_const) |          5000.0 |          5000.0 |
|                       | [front_length_deform_r<br>adius](https://github.com/mom-ocean/MOM5/search?q=front_length_deform_radius) |       True |            True |
|                       | [limit_psi                ](https://github.com/mom-ocean/MOM5/search?q=limit_psi) |            True |            True |
|                       | [limit_psi_velocity_sc<br>ale](https://github.com/mom-ocean/MOM5/search?q=limit_psi_velocity_scale) |          0.5 |             0.5 |
|                       | [min_kblt                 ](https://github.com/mom-ocean/MOM5/search?q=min_kblt) |               4 |               4 |
|                       | [smooth_advect_transpo<br>rt](https://github.com/mom-ocean/MOM5/search?q=smooth_advect_transport) |          True |            True |
|                       | [**smooth_advect_transpo<br>rt_num**](https://github.com/mom-ocean/MOM5/search?q=smooth_advect_transport_num) |     2 |               4 |
|                       | [smooth_hblt              ](https://github.com/mom-ocean/MOM5/search?q=smooth_hblt) |           False |           False |
|                       | [smooth_psi               ](https://github.com/mom-ocean/MOM5/search?q=smooth_psi) |            True |            True |
|                       | [**smooth_psi_num**       ](https://github.com/mom-ocean/MOM5/search?q=smooth_psi_num) |               2 |               3 |
|                       | [submeso_advect_flux      ](https://github.com/mom-ocean/MOM5/search?q=submeso_advect_flux) |           False |           False |
|                       | [submeso_advect_limit     ](https://github.com/mom-ocean/MOM5/search?q=submeso_advect_limit) |            True |            True |
|                       | [submeso_advect_upwind    ](https://github.com/mom-ocean/MOM5/search?q=submeso_advect_upwind) |            True |            True |
|                       | [submeso_advect_zero_b<br>dy](https://github.com/mom-ocean/MOM5/search?q=submeso_advect_zero_bdy) |          True |            True |
|                       | [submeso_diffusion        ](https://github.com/mom-ocean/MOM5/search?q=submeso_diffusion) |           False |           False |
|                       | [submeso_diffusion_bih<br>armonic](https://github.com/mom-ocean/MOM5/search?q=submeso_diffusion_biharmonic) |     True |            True |
|                       | [submeso_diffusion_sca<br>le](https://github.com/mom-ocean/MOM5/search?q=submeso_diffusion_scale) |          10.0 |            10.0 |
|                       | [submeso_skew_flux        ](https://github.com/mom-ocean/MOM5/search?q=submeso_skew_flux) |            True |            True |
|                       | [use_hblt_equal_mld       ](https://github.com/mom-ocean/MOM5/search?q=use_hblt_equal_mld) |            True |            True |
|                       | [use_psi_legacy           ](https://github.com/mom-ocean/MOM5/search?q=use_psi_legacy) |           False |           False |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
| [ocean_tempsalt_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_tempsalt_nml) | [pottemp_2nd_iteration    ](https://github.com/mom-ocean/MOM5/search?q=pottemp_2nd_iteration) |            True |            True |
|                       | [s_max                    ](https://github.com/mom-ocean/MOM5/search?q=s_max) |            70.0 |            70.0 |
|                       | [s_max_limit              ](https://github.com/mom-ocean/MOM5/search?q=s_max_limit) |            42.0 |            42.0 |
|                       | [s_min                    ](https://github.com/mom-ocean/MOM5/search?q=s_min) |             0.0 |             0.0 |
|                       | [s_min_limit              ](https://github.com/mom-ocean/MOM5/search?q=s_min_limit) |             2.0 |             2.0 |
|                       | [t_max                    ](https://github.com/mom-ocean/MOM5/search?q=t_max) |            55.0 |            55.0 |
|                       | [t_max_limit              ](https://github.com/mom-ocean/MOM5/search?q=t_max_limit) |            32.0 |            32.0 |
|                       | [t_min                    ](https://github.com/mom-ocean/MOM5/search?q=t_min) |           -20.0 |           -20.0 |
|                       | [t_min_limit              ](https://github.com/mom-ocean/MOM5/search?q=t_min_limit) |            -5.0 |            -5.0 |
|                       | [temperature_variable     ](https://github.com/mom-ocean/MOM5/search?q=temperature_variable) | 'conservative_t<br>emp' | 'conservative_t<br>emp' |
| [ocean_thickness_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_thickness_nml) | [debug_this_module_det<br>ail](https://github.com/mom-ocean/MOM5/search?q=debug_this_module_detail) |        False |           False |
|                       | [rescale_mass_to_get_h<br>t_mod](https://github.com/mom-ocean/MOM5/search?q=rescale_mass_to_get_ht_mod) |      False |           False |
|                       | [thickness_method         ](https://github.com/mom-ocean/MOM5/search?q=thickness_method) |     'energetic' |     'energetic' |
| [ocean_topog_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_topog_nml) | [min_thickness            ](https://github.com/mom-ocean/MOM5/search?q=min_thickness) |           0.001 |           0.001 |
| [ocean_tracer_advect_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_advect_nml) | [read_basin_mask          ](https://github.com/mom-ocean/MOM5/search?q=read_basin_mask) |           False |           False |
| [ocean_tracer_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_diag_nml) | [diag_step                ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |
|                       | [do_bitwise_exact_sum     ](https://github.com/mom-ocean/MOM5/search?q=do_bitwise_exact_sum) |           False |           False |
|                       | [tracer_conserve_days     ](https://github.com/mom-ocean/MOM5/search?q=tracer_conserve_days) |            30.0 |            30.0 |
| [ocean_tracer_nml     ](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_nml) | [age_tracer_max_init      ](https://github.com/mom-ocean/MOM5/search?q=age_tracer_max_init) |             0.0 |             0.0 |
|                       | [frazil_heating_after_<br>vphysics](https://github.com/mom-ocean/MOM5/search?q=frazil_heating_after_vphysics) |    True |            True |
|                       | [frazil_heating_before<br>_vphysics](https://github.com/mom-ocean/MOM5/search?q=frazil_heating_before_vphysics) |  False |           False |
|                       | [limit_age_tracer         ](https://github.com/mom-ocean/MOM5/search?q=limit_age_tracer) |            True |            True |
|                       | [remap_depth_to_s_init    ](https://github.com/mom-ocean/MOM5/search?q=remap_depth_to_s_init) |           False |           False |
|                       | [use_tempsalt_check_ra<br>nge](https://github.com/mom-ocean/MOM5/search?q=use_tempsalt_check_range) |         True |            True |
|                       | [zero_tendency            ](https://github.com/mom-ocean/MOM5/search?q=zero_tendency) |           False |           False |
|                       | [zero_tracer_source       ](https://github.com/mom-ocean/MOM5/search?q=zero_tracer_source) |           False |           False |
| [ocean_velocity_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_velocity_diag_nml) | [diag_step                ](https://github.com/mom-ocean/MOM5/search?q=diag_step) |            4320 |            4320 |
|                       | [energy_diag_step         ](https://github.com/mom-ocean/MOM5/search?q=energy_diag_step) |            4320 |            4320 |
|                       | [large_cfl_value          ](https://github.com/mom-ocean/MOM5/search?q=large_cfl_value) |            10.0 |            10.0 |
|                       | [max_cfl_value            ](https://github.com/mom-ocean/MOM5/search?q=max_cfl_value) |           100.0 |           100.0 |
| [ocean_velocity_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_velocity_nml) | [adams_bashforth_third    ](https://github.com/mom-ocean/MOM5/search?q=adams_bashforth_third) |            True |            True |
|                       | [max_cgint                ](https://github.com/mom-ocean/MOM5/search?q=max_cgint) |             1.0 |             1.0 |
|                       | [truncate_velocity        ](https://github.com/mom-ocean/MOM5/search?q=truncate_velocity) |           False |           False |
|                       | [truncate_velocity_val<br>ue](https://github.com/mom-ocean/MOM5/search?q=truncate_velocity_value) |           2.0 |             2.0 |
|                       | [truncate_verbose         ](https://github.com/mom-ocean/MOM5/search?q=truncate_verbose) |            True |            True |
|                       | [zero_tendency            ](https://github.com/mom-ocean/MOM5/search?q=zero_tendency) |           False |           False |
|                       | [zero_tendency_explici<br>t_a](https://github.com/mom-ocean/MOM5/search?q=zero_tendency_explicit_a) |        False |           False |
|                       | [zero_tendency_explici<br>t_b](https://github.com/mom-ocean/MOM5/search?q=zero_tendency_explicit_b) |        False |           False |
|                       | [zero_tendency_implici<br>t](https://github.com/mom-ocean/MOM5/search?q=zero_tendency_implicit) |          False |           False |
| [ocean_vert_kpp_mom4p1_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_vert_kpp_mom4p1_nml) | [diff_cbt_iw              ](https://github.com/mom-ocean/MOM5/search?q=diff_cbt_iw) |             0.0 |             0.0 |
|                       | [double_diffusion         ](https://github.com/mom-ocean/MOM5/search?q=double_diffusion) |            True |            True |
|                       | [kbl_standard_method      ](https://github.com/mom-ocean/MOM5/search?q=kbl_standard_method) |           False |           False |
|                       | [ricr                     ](https://github.com/mom-ocean/MOM5/search?q=ricr) |             0.3 |             0.3 |
|                       | [smooth_blmc              ](https://github.com/mom-ocean/MOM5/search?q=smooth_blmc) |           False |           False |
|                       | [smooth_ri_kmax_eq_kmu    ](https://github.com/mom-ocean/MOM5/search?q=smooth_ri_kmax_eq_kmu) |            True |            True |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
|                       | [visc_cbu_iw              ](https://github.com/mom-ocean/MOM5/search?q=visc_cbu_iw) |             0.0 |             0.0 |
| [ocean_vert_mix_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_vert_mix_nml) | [aidif                    ](https://github.com/mom-ocean/MOM5/search?q=aidif) |             1.0 |             1.0 |
|                       | [bryan_lewis_diffusivi<br>ty](https://github.com/mom-ocean/MOM5/search?q=bryan_lewis_diffusivity) |         False |           False |
|                       | [bryan_lewis_lat_depen<br>d](https://github.com/mom-ocean/MOM5/search?q=bryan_lewis_lat_depend) |          False |           False |
|                       | [hwf_diffusivity          ](https://github.com/mom-ocean/MOM5/search?q=hwf_diffusivity) |           False |           False |
|                       | [hwf_min_diffusivity      ](https://github.com/mom-ocean/MOM5/search?q=hwf_min_diffusivity) |           2e-06 |           2e-06 |
|                       | [hwf_n0_2omega            ](https://github.com/mom-ocean/MOM5/search?q=hwf_n0_2omega) |            20.0 |            20.0 |
|                       | [**j09_bgmax**            ](https://github.com/mom-ocean/MOM5/search?q=j09_bgmax) |           5e-06 |                 |
|                       | [**j09_bgmin**            ](https://github.com/mom-ocean/MOM5/search?q=j09_bgmin) |           1e-06 |                 |
|                       | [**j09_diffusivity**      ](https://github.com/mom-ocean/MOM5/search?q=j09_diffusivity) |            True |                 |
|                       | [**j09_lat**              ](https://github.com/mom-ocean/MOM5/search?q=j09_lat) |            20.0 |                 |
|                       | [use_diff_cbt_table       ](https://github.com/mom-ocean/MOM5/search?q=use_diff_cbt_table) |           False |           False |
|                       | [vert_diff_back_via_ma<br>x](https://github.com/mom-ocean/MOM5/search?q=vert_diff_back_via_max) |           True |            True |
|                       | [vert_mix_scheme          ](https://github.com/mom-ocean/MOM5/search?q=vert_mix_scheme) |    'kpp_mom4p1' |    'kpp_mom4p1' |
| [ocean_vert_tidal_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_vert_tidal_nml) | [background_diffusivit<br>y](https://github.com/mom-ocean/MOM5/search?q=background_diffusivity) |            0.0 |             0.0 |
|                       | [background_viscosity     ](https://github.com/mom-ocean/MOM5/search?q=background_viscosity) |          0.0001 |          0.0001 |
|                       | [decay_scale              ](https://github.com/mom-ocean/MOM5/search?q=decay_scale) |           500.0 |           500.0 |
|                       | [drag_dissipation_use_<br>cdbot](https://github.com/mom-ocean/MOM5/search?q=drag_dissipation_use_cdbot) |       True |            True |
|                       | [drhodz_min               ](https://github.com/mom-ocean/MOM5/search?q=drhodz_min) |           1e-10 |           1e-10 |
|                       | [fixed_wave_dissipatio<br>n](https://github.com/mom-ocean/MOM5/search?q=fixed_wave_dissipation) |          False |           False |
|                       | [max_wave_diffusivity     ](https://github.com/mom-ocean/MOM5/search?q=max_wave_diffusivity) |            0.01 |            0.01 |
|                       | [mixing_efficiency_n2d<br>epend](https://github.com/mom-ocean/MOM5/search?q=mixing_efficiency_n2depend) |       True |            True |
|                       | [read_roughness           ](https://github.com/mom-ocean/MOM5/search?q=read_roughness) |            True |            True |
|                       | [read_tide_speed          ](https://github.com/mom-ocean/MOM5/search?q=read_tide_speed) |            True |            True |
|                       | [read_wave_dissipation    ](https://github.com/mom-ocean/MOM5/search?q=read_wave_dissipation) |           False |           False |
|                       | [reading_roughness_amp    ](https://github.com/mom-ocean/MOM5/search?q=reading_roughness_amp) |            True |            True |
|                       | [reading_roughness_len<br>gth](https://github.com/mom-ocean/MOM5/search?q=reading_roughness_length) |        False |           False |
|                       | [roughness_scale          ](https://github.com/mom-ocean/MOM5/search?q=roughness_scale) |         12000.0 |         12000.0 |
|                       | [shelf_depth_cutoff       ](https://github.com/mom-ocean/MOM5/search?q=shelf_depth_cutoff) |         -1000.0 |         -1000.0 |
|                       | [tide_speed_data_on_t_<br>grid](https://github.com/mom-ocean/MOM5/search?q=tide_speed_data_on_t_grid) |        True |            True |
|                       | [use_drag_dissipation     ](https://github.com/mom-ocean/MOM5/search?q=use_drag_dissipation) |            True |            True |
|                       | [use_legacy_methods       ](https://github.com/mom-ocean/MOM5/search?q=use_legacy_methods) |           False |           False |
|                       | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |            True |            True |
|                       | [use_wave_dissipation     ](https://github.com/mom-ocean/MOM5/search?q=use_wave_dissipation) |            True |            True |
|                       | [wave_energy_flux_max     ](https://github.com/mom-ocean/MOM5/search?q=wave_energy_flux_max) |             0.1 |             0.1 |
| [ocean_xlandinsert_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_xlandinsert_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [ocean_xlandmix_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_xlandmix_nml) | [use_this_module          ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |           False |
| [xgrid_nml            ](https://github.com/mom-ocean/MOM5/search?q=xgrid_nml) | [interp_method            ](https://github.com/mom-ocean/MOM5/search?q=interp_method) |  'second_order' |  'second_order' |
|                       | [make_exchange_reprodu<br>ce](https://github.com/mom-ocean/MOM5/search?q=make_exchange_reproduce) |         False |           False |
|                       | [nsubset                  ](https://github.com/mom-ocean/MOM5/search?q=nsubset) |              16 |              16 |
