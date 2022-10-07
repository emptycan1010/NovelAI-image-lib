from setuptools import setup, find_packages
from novelaiimglib import __version__

setup(
    name="novelai-img-lib",
    version=__version__,
    description="NovelAI-Image Library for python ",
    author="emptycan1010",
    author_email="siro157@duck.com",
    url="https://github.com/emptycan1010",
    keywords=["novelai", "novelai.net", "novelai image", "novelai image library"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["IPython"],
    python_requires=">=3.9",
    packages=find_packages(),
    zip_safe=False,
)
