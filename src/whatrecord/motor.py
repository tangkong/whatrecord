# Auto-generated from R7-2-1-20-gda3bfab4
# May not be backward/forward-compatible or 100% accurate

shell_commands = {
    "A3200AsynConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
        task_number=int,
        linear_move_commands=int,
    ),
    "A3200AsynSetup": dict(
        max_controller_count=int,
    ),
    "ACRCreateController": dict(
        port_name=str,
        acr_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "AG_CONEXCreateController": dict(
        port_name=str,
        serial_port_name=str,
        controller_id=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "AG_UCCreateAxis": dict(
        controller_port_name=str,
        axis_number=int,
        has_limits=int,
        forward_amplitude=int,
        reverse_amplitude=int,
    ),
    "AG_UCCreateController": dict(
        port_name=str,
        serial_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "ANC150AsynConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
    ),
    "ANC150AsynSetup": dict(
        maximum_of_controllers=int,
    ),
    "ANF2CreateAxis": dict(
        port_name=str,
        axis_number=int,
        hex_config=str,
        base_speed=int,
        homing_timeout=int,
    ),
    "ANF2CreateController": dict(
        port_name=str,
        anf2_in_port_name=str,
        anf2_out_port_name=str,
        number_of_axes=int,
    ),
    "ANF2StartPoller": dict(
        port_name=str,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "ANG1CreateController": dict(
        port_name=str,
        ang1_in_port_name=str,
        ang1_out_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "AcsMotionConfig": dict(
        acs_port_name=str,
        asyn_port_name=str,
        num_axes=int,
        moving_polling_rate=float,
        idle_polling_rate=float,
    ),
    "C300CreateController": dict(
        port_name=str,
        c300_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "EMC18011Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "EMC18011Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "ESP300Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "ESP300Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "EnsembleAsynConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
    ),
    "EnsembleAsynSetup": dict(
        max_controller_count=int,
    ),
    "HXPCreateController": dict(
        port_name=str,
        ip_address=str,
        port=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "Hytec8601Configure": dict(
        port_name=str,
        num_axes=int,
        moving_poll_period=int,
        idle_poll_period=int,
        cardnum=int,
        carrier=int,
        ipslot=int,
        vector=int,
        useencoder=int,
        encoder_ratio0=float,
        encoder_ratio1=float,
        encoder_ratio2=float,
        encoder_ratio3=float,
    ),
    "IM483PLConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "IM483PLSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "IM483SMConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "IM483SMSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "ImsMDrivePlusCreateController": dict(
        motor_port_name=str,
        io_port_name=str,
        device_name=str,
        moving_poll_period_ms=float,
        idle_poll_period_ms=float,
    ),
    "LinmotCreateController": dict(
        port_name=str,
        linmot_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "MAXvConfig": dict(
        card_being_configured=int,
        configuration_string=str,
        absolute_encoder_flags=int,
        grey_code_flags=int,
    ),
    "MAXvSetup": dict(
        max_controller_count=int,
        vme_address_type=int,
        base_address_on_4_k_0x1000_boundary=int,
        valid_vectors=int,
        interrupt_level_1_6=int,
        polling_rate_hz=int,
    ),
    "MCB4BConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "MCB4BCreateController": dict(
        port_name=str,
        mcb_4_b_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "MCB4BSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MCDC2805Config": dict(
        card_being_configured=int,
        modules_on_this_serial_port=int,
        asyn_port_name=str,
    ),
    "MCDC2805Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MCS2CreateController": dict(
        port_name=str,
        mcs2_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "MDT695Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "MDT695Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MDriveConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "MDriveSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MM3000Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "MM300Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MM4000AsynConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
    ),
    "MM4000AsynSetup": dict(
        max_controller_count=int,
    ),
    "MM4000Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "MM4000Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "MMC200CreateController": dict(
        port_name=str,
        mmc_200_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
        ignore_limit_flag=int,
    ),
    "MVP2001CreateAxis": dict(
        controller_port_name=str,
        axis_number=int,
        encoder_lines_per_rev=int,
        max_current_ma=int,
        limit_polarity=int,
    ),
    "MVP2001CreateController": dict(
        port_name=str,
        mvp_2001_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "MXmotorSetup": dict(
        max_motor=int,
        mx_data_file=str,
        polling_rate=int,
    ),
    "MicosConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "MicosSetup": dict(
        max_controller_count=int,
        max_motor_count=int,
        polling_rate=int,
    ),
    "MicroMoConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "MicroMoSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "OmsPC68Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "OmsPC68Setup": dict(
        maximum_of_cards=int,
        polling_rate_hz=int,
    ),
    "PC6KConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "PC6KSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PC6KUpLoad": dict(
        controller_card=int,
        upload_file_path=str,
        program_name_null_immediate=str,
    ),
    "PIC630Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        ch_1_current_setting=int,
        ch_2_current_setting=int,
        ch_3_current_setting=int,
        ch_4_current_setting=int,
        ch_5_current_setting=int,
        ch_6_current_setting=int,
        ch_7_current_setting=int,
        ch_8_current_setting=int,
        ch_9_current_setting=int,
    ),
    "PIC630Setup": dict(
        max_controller_groups=int,
        max_axes_per_group=int,
        polling_rate=int,
    ),
    "PIC662Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "PIC662Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIC663Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIC663Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIC844Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIC844Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIC848Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIC848Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIC862Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIC862Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIE516Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIE516Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIE517Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIE517Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIE710Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIE710Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIE816Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIE816Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PIJEDSConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PIJEDSSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PI_GCS2_CreateController": dict(
        port_name=str,
        asyn_port_name=str,
        number_of_axes=int,
        priority=int,
        stack_size=int,
        moving_polling_time_msec=int,
        idle_polling_time_msec=int,
    ),
    "PM304Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        number_of_axes=int,
    ),
    "PM304Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PM500Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PM500Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "PMNC87xxConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "PMNC87xxSetup": dict(
        max_controller_count=int,
        max_drivers_per_controller_count=int,
        polling_rate=int,
    ),
    "SC800Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address_gpib=int,
    ),
    "SC800Setup": dict(
        maximum_of_cards=int,
        polling_rate_hz=int,
    ),
    "SMC100Config": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "SMC100CreateController": dict(
        port_name=str,
        smc100_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
        eg_us_per_step=str,
    ),
    "SMC100Setup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "SMCcorvusChangeResolution": dict(
        smc_corvus_port_name=str,
        axis_number=int,
        axis_resolution=float,
    ),
    "SMCcorvusCreateController": dict(
        port_name=str,
        smc_corvus_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "SMChydraChangeResolution": dict(
        smc_hydra_port_name=str,
        axis_number=int,
        axis_resolution=float,
    ),
    "SMChydraCreateController": dict(
        port_name=str,
        smc_hydra_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "SPiiPlusConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        command_mode_bu_ffer_co_nnect_di_rect=str,
    ),
    "SPiiPlusSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "ScriptAxisConfig": dict(
        controller_port_name=str,
        axis_number=int,
        parameters=str,
    ),
    "ScriptControllerConfig": dict(
        motor_port_name=str,
        number_of_axes=int,
        control_script=str,
        parameters=str,
    ),
    "ScriptMotorReload": dict(
        motor_port_name=str,
    ),
    "SmartMotorConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
    ),
    "SmartMotorSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "SoloistConfig": dict(
        card_being_configured=int,
        asyn_port_name=str,
        asyn_address=int,
    ),
    "SoloistSetup": dict(
        max_controller_count=int,
        polling_rate=int,
    ),
    "XPSAuxConfig": dict(
        port_name=str,
        ip_address=str,
        ip_port=int,
        polling_period=int,
    ),
    "XPSConfig": dict(
        card_being_configured=int,
        ip=str,
        port=int,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
    ),
    "XPSConfigAxis": dict(
        card_number=int,
        axis_number=int,
        axis_name=str,
        steps_per_unit=str,
        no_disabled_error=int,
    ),
    "XPSCreateAxis": dict(
        controller_port_name=str,
        axis_number=int,
        axis_name=str,
        steps_per_unit=str,
    ),
    "XPSCreateController": dict(
        controller_port_name=str,
        ip_address=str,
        ip_port=int,
        number_of_axes=int,
        moving_poll_rate_ms=int,
        idle_poll_rate_ms=int,
        enable_set_position=int,
        set_position_settling_time_ms=int,
    ),
    "XPSCreateProfile": dict(
        controller_port_name=str,
        max_points=int,
        ftp_username=str,
        ftp_password=str,
    ),
    "XPSDisableAutoEnable": dict(
        controller_port_name=str,
    ),
    "XPSDisablePoll": dict(
        set_disable_poll_value=int,
    ),
    "XPSEnableMoveToHome": dict(
        card_number=int,
        axis_name=str,
        distance=int,
    ),
    "XPSEnableMovingMode": dict(
        controller_port_name=str,
    ),
    "XPSEnableSetPosition": dict(
        set_position_flag=int,
    ),
    "XPSGathering": dict(
        interelement_period=int,
    ),
    "XPSInterpose": dict(
        port_name=str,
    ),
    "XPSNoDisableError": dict(
        controller_port_name=str,
    ),
    "XPSSetPosSleepTime": dict(
        set_position_sleep_time=int,
    ),
    "XPSSetup": dict(
        number_of_xps_controllers=int,
    ),
    "asynMotorEnableMoveToHome": dict(
        controller_port_name=str,
        axis_number=int,
        distance=int,
    ),
    # "drvAsynMotorConfigure": dict(
    #     port_name=str,
    #     driver_name=str,
    #     card_num=int,
    #     num_axes=int,
    # ),
    "listMovingMotors": dict(
        list_moving_motors=str,
    ),
    "motorSimConfigAxis": dict(
        post_name=str,
        axis=int,
        high_limit=int,
        low_limit=int,
        home_position=int,
        start_posn=int,
    ),
    "motorSimCreate": dict(
        card=int,
        signal=int,
        high_limit=int,
        low_limit=int,
        home_position=int,
        num_cards=int,
        num_signals=int,
        start_posn=int,
    ),
    "motorSimCreateController": dict(
        port_name=str,
        number_of_axes=int,
        priority=int,
        stack_size=int,
    ),
    "motorUtilInit": dict(
        ioc_name=str,
    ),
    "nf874xCreateController": dict(
        port_name=str,
        nf874x_port_name=str,
        number_of_axes=int,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
    ),
    "oms58Setup": dict(
        num_card=int,
        addrs=int,
        vector=int,
        int_level=int,
        scan_rate=int,
    ),
    "omsMAXnetConfig": dict(
        asyn_motor_port_name=str,
        number_of_axes=int,
        asyn_serial_tcp_port_name=str,
        moving_poll_rate=int,
        idle_poll_rate=int,
        initstring=str,
    ),
    "omsMAXvConfig": dict(
        number_of_card=int,
        asyn_motor_port_name=str,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
        initstring=str,
    ),
    "omsMAXvConfig2": dict(
        slot_number=int,
        address_type_a16_a24_a32=str,
        board_address_on_4_k_0x1000_boundary=int,
        interrupt_vector_noninterrupting_0_64_255=int,
        interrupt_level_1_6=int,
        asyn_motor_port_name=str,
        number_of_axes=int,
        task_priority_0_medium=int,
        stack_size_0_medium=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
        initstring=str,
    ),
    "omsMAXvEncFuncConfig": dict(
        number_of_card=int,
        asyn_motor_port_name=str,
        number_of_axes=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
        initstring=str,
    ),
    "omsMAXvEncFuncConfig2": dict(
        slot_number=int,
        address_type_a16_a24_a32=str,
        board_address_on_4_k_0x1000_boundary=int,
        interrupt_vector_noninterrupting_0_64_255=int,
        interrupt_level_1_6=int,
        asyn_motor_port_name=str,
        number_of_axes=int,
        task_priority_0_medium=int,
        stack_size_0_medium=int,
        moving_poll_rate=int,
        idle_poll_rate=int,
        initstring=str,
    ),
    "omsMAXvSetup": dict(
        max_controller_count=int,
        vme_address_type=int,
        base_address_on_4_k_0x1000_boundary=int,
        noninterrupting_0_valid_vectors_64_255=int,
        interrupt_level_1_6=int,
    ),
    "phytronCreateAxis": dict(
        controller_name=str,
        module_index=int,
        axis_index=int,
    ),
    "phytronCreateController": dict(
        port_name=str,
        phytron_axis_port_name=str,
        moving_poll_period_ms=int,
        idle_poll_period_ms=int,
        timeout_ms=float,
    ),
    "printChIDlist": dict(
        print_motor_util_chid_list=str,
    ),
    "setIdlePollPeriod": dict(
        controller_port_name=str,
        axis_number=float,
    ),
    "setMovingPollPeriod": dict(
        controller_port_name=str,
        axis_number=float,
    ),
    "smarActMCSCreateAxis": dict(
        controller_port_name_string=str,
        axis_number_int=int,
        channel_int=int,
    ),
    "smarActMCSCreateController": dict(
        port_name_string=str,
        i_o_port_name_string=str,
        number_of_axes_int=int,
        moving_poll_period_s_double=float,
        idle_poll_period_s_double=float,
    ),
    "smarActSCUCreateAxis": dict(
        controller_port_name_string=str,
        axis_number_int=int,
        channel_int=int,
    ),
    "smarActSCUCreateController": dict(
        port_name_string=str,
        i_o_port_name_string=str,
        number_of_axes_int=int,
        moving_poll_period_s_double=float,
        idle_poll_period_s_double=float,
    ),
    "tclcall": dict(
        tcl_name=str,
        task_name=str,
        function_args=str,
    ),
    "xps_gathering": dict(
        element_period_10_4=int,
    ),
}


shell_commands.update({
    "EthercatMCCreateAxis": dict(
        motor_port=str,
        axis_num=int,
        amplifier_flags=str,
        axis_config=str,
    ),
    "EthercatMCCreateController": dict(
        motor_port=str,
        asyn_port=str,
        num_axes=int,
        move_poll_rate=float,
        idle_poll_rate=float,
    ),
    "adsAsynPortDriverConfigure": dict(
        portName=str,
        ipaddr=str,
        amsaddr=str,
        amsport=int,
        asynParamTableSize=int,
        priority=int,
        noAutoConnect=int,
        defaultSampleTimeMS=int,
        maxDelayTimeMS=int,
        adsTimeoutMS=int,
        defaultTimeSource=str,
    )
})
