| Variable                  | [MOM6-CICE6_iss83_MOM_input_update/<br>MOM_input](https://github.com/COSIMA/MOM6-CICE6/blob/f4071c1e7704671d8a4a412c179631a9586c8b41/MOM_input) | [mom6-om4-025/<br>MOM_input](https://github.com/COSIMA/mom6-om4-025/blob/9976b7963ba94b89c3d660f777d62836c553c412/MOM_input) |
| :------------------------ | --------------: | --------------: |
| [**adjust_net_fresh_wate<br>r_to_zero**](https://github.com/mom-ocean/MOM6/search?q=adjust_net_fresh_water_to_zero) | True |               |
| [**ah**                   ](https://github.com/mom-ocean/MOM6/search?q=ah) | 1000000000000.0 |                 |
| [**ah_vel_scale**         ](https://github.com/mom-ocean/MOM6/search?q=ah_vel_scale) |                 |            0.01 |
| [**ale_coordinate_config**](https://github.com/mom-ocean/MOM6/search?q=ale_coordinate_config) | 'FILE:ocean_vgr<br>id.nc,interface<br>s=zeta' | 'HYBRID:hycom1_<br>75_800m.nc,sigm<br>a2,FNC1:2,4000,<br>4.5,.01' |
| [**bbl_use_eos**          ](https://github.com/mom-ocean/MOM6/search?q=bbl_use_eos) |                 |            True |
| [**boundary_extrapolatio<br>n**](https://github.com/mom-ocean/MOM6/search?q=boundary_extrapolation) |            |            True |
| [**bt_use_old_coriolis_b<br>racket_bug**](https://github.com/mom-ocean/MOM6/search?q=bt_use_old_coriolis_bracket_bug) |   |            True |
| [**cd_tides**             ](https://github.com/mom-ocean/MOM6/search?q=cd_tides) |                 |          0.0018 |
| [**cfl_truncate_ramp_tim<br>e**](https://github.com/mom-ocean/MOM6/search?q=cfl_truncate_ramp_time) |     7200.0 |                 |
| [**channel_config**       ](https://github.com/mom-ocean/MOM6/search?q=channel_config) |   'global_1deg' |          'list' |
| [**channel_list_file**    ](https://github.com/mom-ocean/MOM6/search?q=channel_list_file) |                 | 'MOM_channels_g<br>lobal_025' |
| [**chl_file**             ](https://github.com/mom-ocean/MOM6/search?q=chl_file) |                 | 'seawifs-clim-1<br>997-2010.1440x1<br>080.v20180328.n<br>c' |
| [**chl_varname**          ](https://github.com/mom-ocean/MOM6/search?q=chl_varname) |                 |       'chlor_a' |
| [**coord_config**         ](https://github.com/mom-ocean/MOM6/search?q=coord_config) |                 |           'ALE' |
| [**coriolis_scheme**      ](https://github.com/mom-ocean/MOM6/search?q=coriolis_scheme) |                 | 'SADOURNY75_ENS<br>TRO' |
| [**default_2018_answers** ](https://github.com/mom-ocean/MOM6/search?q=default_2018_answers) |                 |            True |
| [**diabatic_first**       ](https://github.com/mom-ocean/MOM6/search?q=diabatic_first) |            True |                 |
| [**diag_coord_def_rho2**  ](https://github.com/mom-ocean/MOM6/search?q=diag_coord_def_rho2) |                 | 'RFNC1:35,999.5<br>,1028,1028.5,8.<br>,1038.,0.007812<br>5' |
| [**diag_coord_def_z**     ](https://github.com/mom-ocean/MOM6/search?q=diag_coord_def_z) | 'FILE:ocean_vgr<br>id.nc,interface<br>s=zeta' |  |
| [**diag_coords**          ](https://github.com/mom-ocean/MOM6/search?q=diag_coords) |                 | ['z Z ZSTAR', '<br>rho2 RHO2 RHO'] |
| [**do_geothermal**        ](https://github.com/mom-ocean/MOM6/search?q=do_geothermal) |                 |            True |
| [**dt**                   ](https://github.com/mom-ocean/MOM6/search?q=dt) |          1800.0 |           900.0 |
| [**dt_therm**             ](https://github.com/mom-ocean/MOM6/search?q=dt_therm) |          3600.0 |          7200.0 |
| [**dtbt**                 ](https://github.com/mom-ocean/MOM6/search?q=dtbt) |           -0.95 |            -0.9 |
| [**dtbt_reset_period**    ](https://github.com/mom-ocean/MOM6/search?q=dtbt_reset_period) |             0.0 |                 |
| [**dynamic_surface_press<br>ure**](https://github.com/mom-ocean/MOM6/search?q=dynamic_surface_pressure) |          |            True |
| [**energetics_sfc_pbl**   ](https://github.com/mom-ocean/MOM6/search?q=energetics_sfc_pbl) |                 |            True |
| [**energysavedays**       ](https://github.com/mom-ocean/MOM6/search?q=energysavedays) |                 |            0.25 |
| [**enthalpy_from_coupler**](https://github.com/mom-ocean/MOM6/search?q=enthalpy_from_coupler) |            True |                 |
| [**epbl_is_additive**     ](https://github.com/mom-ocean/MOM6/search?q=epbl_is_additive) |                 |           False |
| [**epbl_langmuir_scheme** ](https://github.com/mom-ocean/MOM6/search?q=epbl_langmuir_scheme) |                 |      'ADDITIVE' |
| [**epbl_mstar_scheme**    ](https://github.com/mom-ocean/MOM6/search?q=epbl_mstar_scheme) |                 |           'OM4' |
| [**epbl_transition_scale**](https://github.com/mom-ocean/MOM6/search?q=epbl_transition_scale) |                 |            0.01 |
| [**eta_tolerance_aux**    ](https://github.com/mom-ocean/MOM6/search?q=eta_tolerance_aux) |                 |           0.001 |
| [**fgnv_c_min**           ](https://github.com/mom-ocean/MOM6/search?q=fgnv_c_min) |            0.01 |                 |
| [**fix_ustar_gustless_bu<br>g**](https://github.com/mom-ocean/MOM6/search?q=fix_ustar_gustless_bug) |            |           False |
| [**fluxconst**            ](https://github.com/mom-ocean/MOM6/search?q=fluxconst) |            0.11 |                 |
| [**geothermal_file**      ](https://github.com/mom-ocean/MOM6/search?q=geothermal_file) |                 | 'geothermal_dav<br>ies2013_v1.nc' |
| [**geothermal_scale**     ](https://github.com/mom-ocean/MOM6/search?q=geothermal_scale) |                 |             1.0 |
| [**geothermal_varname**   ](https://github.com/mom-ocean/MOM6/search?q=geothermal_varname) |                 | 'geothermal_hf' |
| [**gill_equatorial_ld**   ](https://github.com/mom-ocean/MOM6/search?q=gill_equatorial_ld) |                 |            True |
| [**gust_const**           ](https://github.com/mom-ocean/MOM6/search?q=gust_const) |            0.02 |             0.0 |
| [**h2_file**              ](https://github.com/mom-ocean/MOM6/search?q=h2_file) |                 | 'ocean_topog.nc<br>' |
| [**hbd_linear_transition**](https://github.com/mom-ocean/MOM6/search?q=hbd_linear_transition) |            True |                 |
| [**henyey_igw_background**](https://github.com/mom-ocean/MOM6/search?q=henyey_igw_background) |                 |            True |
| [**hfreeze**              ](https://github.com/mom-ocean/MOM6/search?q=hfreeze) |            10.0 |                 |
| [**horiz_varying_backgro<br>und**](https://github.com/mom-ocean/MOM6/search?q=horiz_varying_background) |     True |                 |
| [**inputdir**             ](https://github.com/mom-ocean/MOM6/search?q=inputdir) |      './input/' |         'INPUT' |
| [**int_tide_decay_scale** ](https://github.com/mom-ocean/MOM6/search?q=int_tide_decay_scale) |                 | 300.30030030030<br>03 |
| [**int_tide_dissipation** ](https://github.com/mom-ocean/MOM6/search?q=int_tide_dissipation) |                 |            True |
| [**int_tide_profile**     ](https://github.com/mom-ocean/MOM6/search?q=int_tide_profile) |                 |     'POLZIN_09' |
| [**interpolate_res_fn**   ](https://github.com/mom-ocean/MOM6/search?q=interpolate_res_fn) |                 |           False |
| [**kappa_h2_factor**      ](https://github.com/mom-ocean/MOM6/search?q=kappa_h2_factor) |                 |            0.84 |
| [**kappa_itides**         ](https://github.com/mom-ocean/MOM6/search?q=kappa_itides) |                 |     0.000628319 |
| [**kappa_shear_all_layer<br>_tke_bug**](https://github.com/mom-ocean/MOM6/search?q=kappa_shear_all_layer_tke_bug) |     |            True |
| [**kappa_shear_iter_bug** ](https://github.com/mom-ocean/MOM6/search?q=kappa_shear_iter_bug) |                 |            True |
| [**kd**                   ](https://github.com/mom-ocean/MOM6/search?q=kd) |           2e-05 |         1.5e-05 |
| [**kh_res_scale_coef**    ](https://github.com/mom-ocean/MOM6/search?q=kh_res_scale_coef) |             0.4 |                 |
| [**khth_max_cfl**         ](https://github.com/mom-ocean/MOM6/search?q=khth_max_cfl) |                 |             0.1 |
| [**khth_slope_cff**       ](https://github.com/mom-ocean/MOM6/search?q=khth_slope_cff) |            0.01 |                 |
| [**khth_use_ebt_struct**  ](https://github.com/mom-ocean/MOM6/search?q=khth_use_ebt_struct) |            True |                 |
| [**khth_use_fgnv_streamf<br>unction**](https://github.com/mom-ocean/MOM6/search?q=khth_use_fgnv_streamfunction) | True |                 |
| [**khtr_min**             ](https://github.com/mom-ocean/MOM6/search?q=khtr_min) |            50.0 |                 |
| [**khtr_slope_cff**       ](https://github.com/mom-ocean/MOM6/search?q=khtr_slope_cff) |                 |            0.25 |
| [**kpp_is_additive**      ](https://github.com/mom-ocean/MOM6/search?q=kpp_is_additive) |           False |                 |
| [**kv_bbl_min**           ](https://github.com/mom-ocean/MOM6/search?q=kv_bbl_min) |                 |             0.0 |
| [**kv_tbl_min**           ](https://github.com/mom-ocean/MOM6/search?q=kv_tbl_min) |                 |             0.0 |
| [**latent_heat_fusion**   ](https://github.com/mom-ocean/MOM6/search?q=latent_heat_fusion) |        333700.0 |                 |
| [**latent_heat_vaporizat<br>ion**](https://github.com/mom-ocean/MOM6/search?q=latent_heat_vaporization) | 2501000.0 |                |
| [**leith_ah**             ](https://github.com/mom-ocean/MOM6/search?q=leith_ah) |            True |                 |
| [**leith_bi_const**       ](https://github.com/mom-ocean/MOM6/search?q=leith_bi_const) |           128.0 |                 |
| [**lt_enhance_coef**      ](https://github.com/mom-ocean/MOM6/search?q=lt_enhance_coef) |                 |           0.044 |
| [**lt_enhance_exp**       ](https://github.com/mom-ocean/MOM6/search?q=lt_enhance_exp) |                 |            -1.5 |
| [**lt_mod_lac1**          ](https://github.com/mom-ocean/MOM6/search?q=lt_mod_lac1) |                 |             0.0 |
| [**lt_mod_lac4**          ](https://github.com/mom-ocean/MOM6/search?q=lt_mod_lac4) |                 |             0.0 |
| [**lt_mod_lac5**          ](https://github.com/mom-ocean/MOM6/search?q=lt_mod_lac5) |                 |            0.22 |
| [**masking_depth**        ](https://github.com/mom-ocean/MOM6/search?q=masking_depth) |                 |             0.0 |
| [**match_technique**      ](https://github.com/mom-ocean/MOM6/search?q=match_technique) | 'MatchGradient' |                 |
| [**max_delta_srestore**   ](https://github.com/mom-ocean/MOM6/search?q=max_delta_srestore) |             0.5 |                 |
| [**max_layer_thickness_c<br>onfig**](https://github.com/mom-ocean/MOM6/search?q=max_layer_thickness_config) |        | 'FNC1:400,31000<br>.0,0.1,.01' |
| [**max_p_surf**           ](https://github.com/mom-ocean/MOM6/search?q=max_p_surf) |                 |             0.0 |
| [**max_rino_it**          ](https://github.com/mom-ocean/MOM6/search?q=max_rino_it) |                 |              25 |
| [**max_tr_diffusion_cfl** ](https://github.com/mom-ocean/MOM6/search?q=max_tr_diffusion_cfl) |             2.0 |                 |
| [**maximum_depth**        ](https://github.com/mom-ocean/MOM6/search?q=maximum_depth) |          6000.0 |          6500.0 |
| [**maximum_int_depth_con<br>fig**](https://github.com/mom-ocean/MOM6/search?q=maximum_int_depth_config) |          | 'FNC1:5,8000.0,<br>1.0,.01' |
| [**maxtrunc**             ](https://github.com/mom-ocean/MOM6/search?q=maxtrunc) |                 |          100000 |
| [**meke_advection_factor**](https://github.com/mom-ocean/MOM6/search?q=meke_advection_factor) |             1.0 |                 |
| [**meke_alpha_deform**    ](https://github.com/mom-ocean/MOM6/search?q=meke_alpha_deform) |             1.0 |                 |
| [**meke_alpha_eady**      ](https://github.com/mom-ocean/MOM6/search?q=meke_alpha_eady) |             1.0 |            0.15 |
| [**meke_alpha_frict**     ](https://github.com/mom-ocean/MOM6/search?q=meke_alpha_frict) |             1.0 |                 |
| [**meke_alpha_grid**      ](https://github.com/mom-ocean/MOM6/search?q=meke_alpha_grid) |             1.0 |                 |
| [**meke_alpha_rhines**    ](https://github.com/mom-ocean/MOM6/search?q=meke_alpha_rhines) |             1.0 |            0.15 |
| [**meke_bgsrc**           ](https://github.com/mom-ocean/MOM6/search?q=meke_bgsrc) |                 |           1e-13 |
| [**meke_equilibrium_alt** ](https://github.com/mom-ocean/MOM6/search?q=meke_equilibrium_alt) |            True |                 |
| [**meke_equilibrium_rest<br>oring**](https://github.com/mom-ocean/MOM6/search?q=meke_equilibrium_restoring) |   True |                 |
| [**meke_geometric**       ](https://github.com/mom-ocean/MOM6/search?q=meke_geometric) |            True |                 |
| [**meke_gmcoeff**         ](https://github.com/mom-ocean/MOM6/search?q=meke_gmcoeff) |             0.0 |             1.0 |
| [**meke_khmeke_fac**      ](https://github.com/mom-ocean/MOM6/search?q=meke_khmeke_fac) |             0.5 |             1.0 |
| [**meke_khth_fac**        ](https://github.com/mom-ocean/MOM6/search?q=meke_khth_fac) |             1.0 |                 |
| [**meke_khtr_fac**        ](https://github.com/mom-ocean/MOM6/search?q=meke_khtr_fac) |             1.0 |                 |
| [**meke_min_lscale**      ](https://github.com/mom-ocean/MOM6/search?q=meke_min_lscale) |            True |                 |
| [**meke_restoring_timesc<br>ale**](https://github.com/mom-ocean/MOM6/search?q=meke_restoring_timescale) | 10000000.0 |               |
| [**meke_visc_drag**       ](https://github.com/mom-ocean/MOM6/search?q=meke_visc_drag) |           False |                 |
| [**meke_viscosity_coeff_<br>ku**](https://github.com/mom-ocean/MOM6/search?q=meke_viscosity_coeff_ku) |       0.2 |                 |
| [**min_salinity**         ](https://github.com/mom-ocean/MOM6/search?q=min_salinity) |                 |            0.01 |
| [**minimum_depth**        ](https://github.com/mom-ocean/MOM6/search?q=minimum_depth) |             0.5 |             9.5 |
| [**mix_len_exponent**     ](https://github.com/mom-ocean/MOM6/search?q=mix_len_exponent) |                 |             1.0 |
| [**ml_omega_frac**        ](https://github.com/mom-ocean/MOM6/search?q=ml_omega_frac) |                 |           0.001 |
| [**mle_front_length**     ](https://github.com/mom-ocean/MOM6/search?q=mle_front_length) |          1000.0 |           500.0 |
| [**mle_mld_decay_time**   ](https://github.com/mom-ocean/MOM6/search?q=mle_mld_decay_time) |        345600.0 |       2592000.0 |
| [**mle_use_pbl_mld**      ](https://github.com/mom-ocean/MOM6/search?q=mle_use_pbl_mld) |                 |            True |
| [**mstar2_coef1**         ](https://github.com/mom-ocean/MOM6/search?q=mstar2_coef1) |                 |            0.29 |
| [**mstar2_coef2**         ](https://github.com/mom-ocean/MOM6/search?q=mstar2_coef2) |                 |           0.152 |
| [**mstar_cap**            ](https://github.com/mom-ocean/MOM6/search?q=mstar_cap) |                 |            10.0 |
| [**mstar_conv_adj**       ](https://github.com/mom-ocean/MOM6/search?q=mstar_conv_adj) |                 |           0.667 |
| [**n_smooth**             ](https://github.com/mom-ocean/MOM6/search?q=n_smooth) |               3 |                 |
| [**n_smooth_ri**          ](https://github.com/mom-ocean/MOM6/search?q=n_smooth_ri) |               1 |                 |
| [**ndiff_interior_only**  ](https://github.com/mom-ocean/MOM6/search?q=ndiff_interior_only) |            True |                 |
| [**niglobal**             ](https://github.com/mom-ocean/MOM6/search?q=niglobal) |             360 |            1440 |
| [**nihalo**               ](https://github.com/mom-ocean/MOM6/search?q=nihalo) |                 |               4 |
| [**njglobal**             ](https://github.com/mom-ocean/MOM6/search?q=njglobal) |             300 |            1080 |
| [**njhalo**               ](https://github.com/mom-ocean/MOM6/search?q=njhalo) |                 |               4 |
| [**nk**                   ](https://github.com/mom-ocean/MOM6/search?q=nk) |              50 |              75 |
| [**nstar**                ](https://github.com/mom-ocean/MOM6/search?q=nstar) |                 |            0.06 |
| [**num_diag_coords**      ](https://github.com/mom-ocean/MOM6/search?q=num_diag_coords) |                 |               2 |
| [**ocean_surface_stagger**](https://github.com/mom-ocean/MOM6/search?q=ocean_surface_stagger) |             'A' |                 |
| [**parallel_restartfiles**](https://github.com/mom-ocean/MOM6/search?q=parallel_restartfiles) |                 |            True |
| [**pen_sw_frac**          ](https://github.com/mom-ocean/MOM6/search?q=pen_sw_frac) |            0.42 |                 |
| [**pen_sw_nbands**        ](https://github.com/mom-ocean/MOM6/search?q=pen_sw_nbands) |                 |               3 |
| [**pen_sw_scale**         ](https://github.com/mom-ocean/MOM6/search?q=pen_sw_scale) |            15.0 |                 |
| [**prandtl_bkgnd**        ](https://github.com/mom-ocean/MOM6/search?q=prandtl_bkgnd) |             5.0 |                 |
| [**prandtl_turb**         ](https://github.com/mom-ocean/MOM6/search?q=prandtl_turb) |                 |            1.25 |
| [**read_tideamp**         ](https://github.com/mom-ocean/MOM6/search?q=read_tideamp) |                 |            True |
| [**regrid_compressibilit<br>y_fraction**](https://github.com/mom-ocean/MOM6/search?q=regrid_compressibility_fraction) |   |            0.01 |
| [**regridding_coordinate<br>_mode**](https://github.com/mom-ocean/MOM6/search?q=regridding_coordinate_mode) | 'ZSTAR' |       'HYCOM1' |
| [**remap_uv_using_old_al<br>g**](https://github.com/mom-ocean/MOM6/search?q=remap_uv_using_old_alg) |            |            True |
| [**restart_checksums_req<br>uired**](https://github.com/mom-ocean/MOM6/search?q=restart_checksums_required) |        |           False |
| [**restart_control**      ](https://github.com/mom-ocean/MOM6/search?q=restart_control) |               3 |                 |
| [**restore_salinity**     ](https://github.com/mom-ocean/MOM6/search?q=restore_salinity) |            True |                 |
| [**salt_restore_file**    ](https://github.com/mom-ocean/MOM6/search?q=salt_restore_file) | 'salt_sfc_resto<br>re.nc' |       |
| [**salt_z_init_file**     ](https://github.com/mom-ocean/MOM6/search?q=salt_z_init_file) |                 | 'woa13_decav_s_<br>monthly_fulldep<br>th_01.nc' |
| [**save_initial_conds**   ](https://github.com/mom-ocean/MOM6/search?q=save_initial_conds) |            True |                 |
| [**sea_ice_rigid_mass**   ](https://github.com/mom-ocean/MOM6/search?q=sea_ice_rigid_mass) |                 |           100.0 |
| [**simple_tke_to_kd**     ](https://github.com/mom-ocean/MOM6/search?q=simple_tke_to_kd) |                 |            True |
| [**smag_bi_const**        ](https://github.com/mom-ocean/MOM6/search?q=smag_bi_const) |                 |            0.06 |
| [**smagorinsky_ah**       ](https://github.com/mom-ocean/MOM6/search?q=smagorinsky_ah) |                 |            True |
| [**srestore_as_sflux**    ](https://github.com/mom-ocean/MOM6/search?q=srestore_as_sflux) |            True |                 |
| [**temp_salt_init_vertic<br>al_remap_only**](https://github.com/mom-ocean/MOM6/search?q=temp_salt_init_vertical_remap_only) | True |           |
| [**temp_salt_z_init_file**](https://github.com/mom-ocean/MOM6/search?q=temp_salt_z_init_file) | 'ocean_temp_sal<br>t.res.nc' | '' |
| [**temp_z_init_file**     ](https://github.com/mom-ocean/MOM6/search?q=temp_z_init_file) |                 | 'woa13_decav_pt<br>emp_monthly_ful<br>ldepth_01.nc' |
| [**thermo_spans_coupling**](https://github.com/mom-ocean/MOM6/search?q=thermo_spans_coupling) |                 |            True |
| [**tide_m2**              ](https://github.com/mom-ocean/MOM6/search?q=tide_m2) |            True |                 |
| [**tide_sal_scalar_value**](https://github.com/mom-ocean/MOM6/search?q=tide_sal_scalar_value) |           0.094 |                 |
| [**tideamp_file**         ](https://github.com/mom-ocean/MOM6/search?q=tideamp_file) |                 | 'tidal_amplitud<br>e.v20140616.nc' |
| [**tides**                ](https://github.com/mom-ocean/MOM6/search?q=tides) |            True |                 |
| [**tke_decay**            ](https://github.com/mom-ocean/MOM6/search?q=tke_decay) |                 |            0.01 |
| [**tke_itide_max**        ](https://github.com/mom-ocean/MOM6/search?q=tke_itide_max) |                 |             0.1 |
| [**topo_edits_file**      ](https://github.com/mom-ocean/MOM6/search?q=topo_edits_file) |                 |  'All_edits.nc' |
| [**topo_file**            ](https://github.com/mom-ocean/MOM6/search?q=topo_file) |                 | 'ocean_topog.nc<br>' |
| [**use_cvmix_convection** ](https://github.com/mom-ocean/MOM6/search?q=use_cvmix_convection) |            True |                 |
| [**use_cvmix_ddiff**      ](https://github.com/mom-ocean/MOM6/search?q=use_cvmix_ddiff) |            True |                 |
| [**use_horizontal_bounda<br>ry_diffusion**](https://github.com/mom-ocean/MOM6/search?q=use_horizontal_boundary_diffusion) | True |            |
| [**use_jackson_param**    ](https://github.com/mom-ocean/MOM6/search?q=use_jackson_param) |                 |            True |
| [**use_kh_in_meke**       ](https://github.com/mom-ocean/MOM6/search?q=use_kh_in_meke) |            True |                 |
| [**use_kpp**              ](https://github.com/mom-ocean/MOM6/search?q=use_kpp) |            True |                 |
| [**use_la_li2016**        ](https://github.com/mom-ocean/MOM6/search?q=use_la_li2016) |                 |            True |
| [**use_land_mask_for_hvi<br>sc**](https://github.com/mom-ocean/MOM6/search?q=use_land_mask_for_hvisc) |           |           False |
| [**use_legacy_diabatic_d<br>river**](https://github.com/mom-ocean/MOM6/search?q=use_legacy_diabatic_driver) |  False |                 |
| [**use_lmd94**            ](https://github.com/mom-ocean/MOM6/search?q=use_lmd94) |            True |                 |
| [**use_mld_iteration**    ](https://github.com/mom-ocean/MOM6/search?q=use_mld_iteration) |                 |            True |
| [**use_neutral_diffusion**](https://github.com/mom-ocean/MOM6/search?q=use_neutral_diffusion) |            True |                 |
| [**use_psurf_in_eos**     ](https://github.com/mom-ocean/MOM6/search?q=use_psurf_in_eos) |                 |           False |
| [**use_rigid_sea_ice**    ](https://github.com/mom-ocean/MOM6/search?q=use_rigid_sea_ice) |                 |            True |
| [**var_pen_sw**           ](https://github.com/mom-ocean/MOM6/search?q=var_pen_sw) |                 |            True |
| [**velocity_tolerance**   ](https://github.com/mom-ocean/MOM6/search?q=velocity_tolerance) |          0.0001 |                 |
| [**write_geom**           ](https://github.com/mom-ocean/MOM6/search?q=write_geom) |                 |               0 |
| [**z_init_file_ptemp_var**](https://github.com/mom-ocean/MOM6/search?q=z_init_file_ptemp_var) |          'temp' |      'ptemp_an' |
| [**z_init_file_salt_var** ](https://github.com/mom-ocean/MOM6/search?q=z_init_file_salt_var) |                 |          's_an' |
| [**z_init_remap_old_alg** ](https://github.com/mom-ocean/MOM6/search?q=z_init_remap_old_alg) |                 |            True |
