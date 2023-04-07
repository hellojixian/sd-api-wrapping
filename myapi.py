from webui import initialize
initialize()

from modules.script_callbacks import before_ui_callback
before_ui_callback()

from modules.txt2img import txt2img

id_task = "my-task"
prompt = "suchkalisa<lora:suchkalisa_v16:0.95>,1girl,a cat"
negative_prompt = ""
prompt_styles = ""
steps = 20
sampler_index = 0
restore_faces = False
tiling = False
n_iter = 1
batch_size = 4
cfg_scale = 7
seed = -1
subseed = -1
subseed_strength = 0
seed_resize_from_h = 0
seed_resize_from_w = 0
seed_enable_extras = False
height = 512
width = 512
enable_hr = False
denoising_strength = 0.5
hr_scale = 2.0
hr_upscaler = "Latent"
hr_second_pass_steps = 5
hr_resize_x = 1024
hr_resize_y = 1024
override_settings_texts = []

images, info_str, _ , _ = txt2img(id_task, prompt, negative_prompt, prompt_styles, steps, sampler_index,
                    restore_faces, tiling, n_iter, batch_size, cfg_scale, seed, subseed,
                    subseed_strength, seed_resize_from_h, seed_resize_from_w, seed_enable_extras,
                    height, width, enable_hr, denoising_strength, hr_scale, hr_upscaler,
                    hr_second_pass_steps, hr_resize_x, hr_resize_y, override_settings_texts, 0)
# print output parameters
import json
info = json.loads(info_str)
print(json.dumps(info, indent=4))

# save images
for i, image in enumerate(images):
    filename = f"{id_task}-{i}.png"
    image.save(filename)
    print(f"Saved {filename} ({image.size[0]}x{image.size[1]} pixels")