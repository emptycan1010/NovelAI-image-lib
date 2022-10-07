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

# Get Token
1. **First** Log in to https://novelai.net/image

2. **Second** Turn on Developer tool using F12 or Ctrl + Shift + I

3. **Third** Go to Application tab.

4. **Fourth** See Local Storage. Look at the value of session key. 

5. **Fifth** get value of "auth_token"

6. **Use** 
```py
novelaiimglib.reqform("Bearer eyjASHx~~~blabla")
```
