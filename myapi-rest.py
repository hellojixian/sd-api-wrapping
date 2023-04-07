import requests
import json
import base64
import io
from PIL import Image

prompt = "suchkalisa<lora:suchkalisa_v16:0.95>,1girl,a cat"

api_server = "http://127.0.0.1:7861"
api_endpoint = "/sdapi/v1/txt2img"
api_payload = {
  "enable_hr": False,
  "denoising_strength": 0,
  "firstphase_width": 0,
  "firstphase_height": 0,
  "hr_scale": 2,
  "hr_second_pass_steps": 0,
  "hr_resize_x": 0,
  "hr_resize_y": 0,
  "prompt": prompt,
  "styles": [],
  "seed": -1,
  "subseed": -1,
  "subseed_strength": 0,
  "seed_resize_from_h": -1,
  "seed_resize_from_w": -1,
  "sampler_name": "DPM++ SDE Karras",
  "batch_size": 4,
  "n_iter": 1,
  "steps": 50,
  "cfg_scale": 7,
  "width": 512,
  "height": 512,
  "restore_faces": False,
  "tiling": False,
  "do_not_save_samples": False,
  "do_not_save_grid": False,
  "negative_prompt": "",
  "eta": 0,
  "s_churn": 0,
  "s_tmax": 0,
  "s_tmin": 0,
  "s_noise": 1,
  "override_settings": {},
  "override_settings_restore_afterwards": True,
  "script_args": [],
  "sampler_index": "Euler",
  "script_name": "",
  "send_images": True,
  "save_images": False,
  "alwayson_scripts": {}
}
response = requests.post(api_server + api_endpoint, json=api_payload)
response = response.json()
images = response['images']
for (i, image) in enumerate(images):
  # save image from base64 string to png file
  img = Image.open(io.BytesIO(base64.b64decode(image)))
  filename = f"my-task-{i}.png"
  img.save(filename)
  print(f"Saved {filename} ({img.size[0]}x{img.size[1]} pixels")


parameters = response['parameters']
print(json.dumps(parameters, indent=4))