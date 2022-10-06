# NovelAI-image-lib
Python Library for NovelAI Image generate

# Install
```py
pip install git+https://github.com/emptycan1010/NovelAi-image-lib
```

# Example

```py
import novelaiimglib

novimg = novelaiimglib.reqform("Your Token Here")
novimg.makeIMG("NSFW") # Prompt Here
novimg.saveIMG("image") # save as "image.png"
```

You can get Token using fiddler. Log in with Email and Password is not supported yet.
