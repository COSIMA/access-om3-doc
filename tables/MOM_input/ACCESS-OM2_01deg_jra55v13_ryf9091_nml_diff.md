| Group                 | Variable                  | [ACCESS-OM2_01deg_jra55v13_ryf9091/<br>ocean/<br>input.nml](https://github.com/COSIMA/01deg_jra55_ryf/blob/8e47ebb08e4360c16367e87b298dd653c098480b/ocean/input.nml) | [ACCESS-OM2_release-01deg_jra55_ryf/<br>ocean/<br>input.nml](https://github.com/ACCESS-NRI/access-om2-configs/blob/83885a45017b3a34ea4fad15d155449c7217ad70/ocean/input.nml) |
| :-------------------- | :------------------------ | --------------: | --------------: |
| [diag_manager_nml     ](https://github.com/mom-ocean/MOM5/search?q=diag_manager_nml) | [**max_axes**             ](https://github.com/mom-ocean/MOM5/search?q=max_axes) |                 |             400 |
|                       | [**max_files**            ](https://github.com/mom-ocean/MOM5/search?q=max_files) |                 |             200 |
|                       | [**max_num_axis_sets**    ](https://github.com/mom-ocean/MOM5/search?q=max_num_axis_sets) |                 |             200 |
| [mom_oasis3_interface_nml](https://github.com/mom-ocean/MOM5/search?q=mom_oasis3_interface_nml) | [**fields_in**            ](https://github.com/mom-ocean/MOM5/search?q=fields_in) | ['u_flux', 'v_f<br>lux', 'lprec', <br>'fprec', 'salt_<br>flx', 'mh_flux'<br>, 'sw_flux', 'q<br>_flux', 't_flux<br>', 'lw_flux', '<br>runof', 'p', 'a<br>ice', 'wfimelt'<br>, 'wfiform'] | ['u_flux', 'v_f<br>lux', 'lprec', <br>'fprec', 'salt_<br>flx', 'mh_flux'<br>, 'sw_flux', 'q<br>_flux', 't_flux<br>', 'lw_flux', '<br>runof', 'p', 'a<br>ice', 'wfimelt'<br>, 'wfiform', 'l<br>icefw', 'liceht<br>'] |
|                       | [**num_fields_in**        ](https://github.com/mom-ocean/MOM5/search?q=num_fields_in) |              15 |              17 |
| [monin_obukhov_nml    ](https://github.com/mom-ocean/MOM5/search?q=monin_obukhov_nml) | [**neutral**              ](https://github.com/mom-ocean/MOM5/search?q=neutral) |            True |                 |
| [ocean_advection_velocity_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_advection_velocity_nml) | [**max_advection_velocit<br>y**](https://github.com/mom-ocean/MOM5/search?q=max_advection_velocity) |        0.2 |             0.3 |
| [ocean_albedo_nml     ](https://github.com/mom-ocean/MOM5/search?q=ocean_albedo_nml) | [**ocean_albedo_option**  ](https://github.com/mom-ocean/MOM5/search?q=ocean_albedo_option) |               2 |                 |
| [ocean_barotropic_nml ](https://github.com/mom-ocean/MOM5/search?q=ocean_barotropic_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_bbc_nml        ](https://github.com/mom-ocean/MOM5/search?q=ocean_bbc_nml) | [**cdbot**                ](https://github.com/mom-ocean/MOM5/search?q=cdbot) |           0.001 |                 |
|                       | [**cdbot_roughness_lengt<br>h**](https://github.com/mom-ocean/MOM5/search?q=cdbot_roughness_length) |      False |                 |
|                       | [**use_geothermal_heatin<br>g**](https://github.com/mom-ocean/MOM5/search?q=use_geothermal_heating) |      False |                 |
| [ocean_bihgen_friction_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_bihgen_friction_nml) | [**ncar_boundary_scaling**](https://github.com/mom-ocean/MOM5/search?q=ncar_boundary_scaling) |            True |           False |
| [ocean_frazil_nml     ](https://github.com/mom-ocean/MOM5/search?q=ocean_frazil_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_grids_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_grids_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_nphysics_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_nphysics_util_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_nphysics_util_nml) | [**agm**                  ](https://github.com/mom-ocean/MOM5/search?q=agm) |           100.0 |                 |
|                       | [**agm_closure**          ](https://github.com/mom-ocean/MOM5/search?q=agm_closure) |            True |                 |
|                       | [**agm_closure_baroclini<br>c**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_baroclinic) |       True |                 |
|                       | [**agm_closure_buoy_freq**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_buoy_freq) |           0.004 |                 |
|                       | [**agm_closure_length**   ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length) |         50000.0 |                 |
|                       | [**agm_closure_length_bc<br>zone**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length_bczone) |   False |                 |
|                       | [**agm_closure_length_fi<br>xed**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length_fixed) |    False |                 |
|                       | [**agm_closure_length_ro<br>ssby**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_length_rossby) |   False |                 |
|                       | [**agm_closure_lower_dep<br>th**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_lower_depth) |    2000.0 |                 |
|                       | [**agm_closure_max**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_max) |           600.0 |                 |
|                       | [**agm_closure_min**      ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_min) |           100.0 |                 |
|                       | [**agm_closure_scaling**  ](https://github.com/mom-ocean/MOM5/search?q=agm_closure_scaling) |            0.07 |                 |
|                       | [**agm_closure_upper_dep<br>th**](https://github.com/mom-ocean/MOM5/search?q=agm_closure_upper_depth) |     100.0 |                 |
|                       | [**aredi**                ](https://github.com/mom-ocean/MOM5/search?q=aredi) |           600.0 |                 |
|                       | [**aredi_equal_agm**      ](https://github.com/mom-ocean/MOM5/search?q=aredi_equal_agm) |           False |                 |
|                       | [**drhodz_mom4p1**        ](https://github.com/mom-ocean/MOM5/search?q=drhodz_mom4p1) |           False |                 |
|                       | [**drhodz_smooth_horz**   ](https://github.com/mom-ocean/MOM5/search?q=drhodz_smooth_horz) |           False |                 |
|                       | [**drhodz_smooth_vert**   ](https://github.com/mom-ocean/MOM5/search?q=drhodz_smooth_vert) |           False |                 |
|                       | [**rossby_radius_max**    ](https://github.com/mom-ocean/MOM5/search?q=rossby_radius_max) |        100000.0 |                 |
|                       | [**rossby_radius_min**    ](https://github.com/mom-ocean/MOM5/search?q=rossby_radius_min) |         15000.0 |                 |
|                       | [**tracer_mix_micom**     ](https://github.com/mom-ocean/MOM5/search?q=tracer_mix_micom) |           False |                 |
|                       | [**vel_micom**            ](https://github.com/mom-ocean/MOM5/search?q=vel_micom) |             0.0 |                 |
| [ocean_operators_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_operators_nml) | [**use_legacy_div_ud**    ](https://github.com/mom-ocean/MOM5/search?q=use_legacy_div_ud) |           False |                 |
| [ocean_overexchange_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_overexchange_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
|                       | [**overexch_npts**        ](https://github.com/mom-ocean/MOM5/search?q=overexch_npts) |               4 |                 |
|                       | [**overexch_weight_far**  ](https://github.com/mom-ocean/MOM5/search?q=overexch_weight_far) |           False |                 |
|                       | [**overflow_umax**        ](https://github.com/mom-ocean/MOM5/search?q=overflow_umax) |             5.0 |                 |
| [ocean_polar_filter_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_polar_filter_nml) | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |                 |
| [ocean_pressure_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_pressure_nml) | [**zero_pressure_force**  ](https://github.com/mom-ocean/MOM5/search?q=zero_pressure_force) |           False |                 |
| [ocean_rivermix_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_rivermix_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_riverspread_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_riverspread_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_shortwave_gfdl_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_shortwave_gfdl_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
|                       | [**zmax_pen**             ](https://github.com/mom-ocean/MOM5/search?q=zmax_pen) |           300.0 |       1000000.0 |
| [ocean_submesoscale_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_submesoscale_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_tempsalt_nml   ](https://github.com/mom-ocean/MOM5/search?q=ocean_tempsalt_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_thickness_nml  ](https://github.com/mom-ocean/MOM5/search?q=ocean_thickness_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_topog_nml      ](https://github.com/mom-ocean/MOM5/search?q=ocean_topog_nml) | [**min_thickness**        ](https://github.com/mom-ocean/MOM5/search?q=min_thickness) |                 |           0.001 |
| [ocean_tracer_advect_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_advect_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_tracer_nml     ](https://github.com/mom-ocean/MOM5/search?q=ocean_tracer_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_velocity_diag_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_velocity_diag_nml) | [**debug_this_module**    ](https://github.com/mom-ocean/MOM5/search?q=debug_this_module) |           False |                 |
| [ocean_vert_kpp_iow_nml](https://github.com/mom-ocean/MOM5/search?q=ocean_vert_kpp_iow_nml) | [**use_this_module**      ](https://github.com/mom-ocean/MOM5/search?q=use_this_module) |           False |                 |
