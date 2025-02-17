adm_scaler_positive, adm_scaler_negative, adm_scaler_end, adaptive_cfg, sampler_name,  \
    scheduler_name, overwrite_step, overwrite_switch, overwrite_width, overwrite_height, \
    overwrite_vary_strength, overwrite_upscale_strength, \
    mixing_image_prompt_and_vary_upscale, mixing_image_prompt_and_inpaint, \
    debugging_cn_preprocessor, controlnet_softness = [None] * 16


def set_all_advanced_parameters(*args):
    global adm_scaler_positive, adm_scaler_negative, adm_scaler_end, adaptive_cfg, sampler_name, \
        scheduler_name, overwrite_step, overwrite_switch, overwrite_width, overwrite_height, \
        overwrite_vary_strength, overwrite_upscale_strength, \
        mixing_image_prompt_and_vary_upscale, mixing_image_prompt_and_inpaint, \
        debugging_cn_preprocessor, controlnet_softness

    adm_scaler_positive, adm_scaler_negative, adm_scaler_end, adaptive_cfg, sampler_name, \
        scheduler_name, overwrite_step, overwrite_switch, overwrite_width, overwrite_height, \
        overwrite_vary_strength, overwrite_upscale_strength, \
        mixing_image_prompt_and_vary_upscale, mixing_image_prompt_and_inpaint, \
        debugging_cn_preprocessor, controlnet_softness = args

    return
