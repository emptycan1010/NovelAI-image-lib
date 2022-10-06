from base64 import b64decode
import random
import requests
from IPython.display import Image, display


class reqform:
    def __init__(self, auth):
        self.auth = auth

    def makeIMG(self, prompt, seed=random.randint(0, 1000000)):
        self.r = requests.post(
            "https://api.novelai.net/ai/generate-image",
            headers={
                "Authorization": self.auth,
                "Origin": "https://novelai.net",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                "Referer": "https://novelai.net/",
            },
            json={
                "input": prompt,
                "model": "safe-diffusion",
                "parameters": {
                    "width": 512,
                    "height": 512,
                    "scale": 12,
                    "sampler": "k_euler_ancestral",
                    "steps": 28,
                    "seed": seed,
                    "n_samples": 1,
                    "strength": 0.7,
                    "noise": 0.2,
                    "ucPreset": 0,
                    "uc": "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
                },
            },
        )

    def saveIMG(self, filename):
        e = open("filename.png", "wb")
        e.write(b64decode(self.r.text.split("\n")[-3][5:]))
        e.close()

    def imgvalue(self):
        return b64decode(self.r.text.split("\n")[-3][5:])
