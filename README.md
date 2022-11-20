# "mr_urdf_loader" Python Package Instructions #

## Dependency Requirement

`numpy` , `modern_robotics` , `urdfpy` should be preinstalled.

## Installing the Package ##

### Recommended Method ###

Use [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) to install by
running

```
pip install numpy
pip install modern_robotics
pip install urdfpy

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
## Examples ##
### 1. Simple MR test
```bash
cd example
python3 urdf_loader.py
```
![image](https://user-images.githubusercontent.com/53217819/202921164-f450da46-58bd-4335-a0b7-018957b851b0.png)


### 2. Pybullet Simulation
```bash
cd example
pip install pybullet
python3 sim.py
```
![image](https://user-images.githubusercontent.com/53217819/202921126-a5c297fb-fd0f-4ef4-91fe-4e0b7821c516.png)


## Using the Package Locally ##

It is possible to use the package locally without installation. Download and
place the package in the working directory. Note that since the package is 
not installed, you need to move the package if the working directory is
changed. Importing is still required before using.
