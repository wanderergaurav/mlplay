from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.0'
DESCRIPTION = 'mlplay'
LONG_DESCRIPTION = 'highlevel ml codes'

# Setting up
setup(
    name="mlplay",
    version=VERSION,
    author="onemriganka",
    
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[ 'ml','onemriganka','codes'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)