# "modern_robotics" Python Package Instructions #

## Dependency Requirement

`numpy` should be preinstalled.
`modern_robotics` should be preinstalled.
`urdfpy` should be preinstalled.

## Installing the Package ##

### Recommended Method ###

Use [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) to install by
running

```
pip install .
``` 

If pip is not preinstalled, check 
[here](https://pip.pypa.io/en/stable/installing/) for help installing pip. 

## Importing the Package ##

To import the package, we recommend using

```
from mr_urdf_loader import loadURDF
MRSetup = loadURDF(urdf_name)
```


## Using the Package Locally ##

It is possible to use the package locally without installation. Download and
place the package in the working directory. Note that since the package is 
not installed, you need to move the package if the working directory is
changed. Importing is still required before using.
