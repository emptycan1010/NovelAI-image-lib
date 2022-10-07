# NovelAI-image-lib
Python Library for NovelAI Image generate using requests

# Install
```py
pip install git+https://github.com/emptycan1010/NovelAi-image-lib
```

# Example

```py
import novelaiimglib

novimg = novelaiimglib.reqform("Your Token Here") # its like "Bearer abcdefg..."
novimg.makeIMG("NSFW") # Prompt Here. Seed is your choice. 
"""You can use seed like novimg.makeIMG("NSFW", "10382")"""
novimg.saveIMG("image") # save as "image.png"
novimg.imgvalue() # returns decoded value of image. 
```

You can get Token using fiddler. Log in with Email and Password is not supported yet.
