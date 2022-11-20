from setuptools import setup

exec(open('mr_urdf_loader/__version__.py').read())

long_description = """
# Modern Robotics:  Mechanics, Planning, and Control Code Library with urdfpy

This package contains URDF loader python code accompanying [_Modern Robotics:
Mechanics, Planning, and Control_](http://modernrobotics.org) (Kevin Lynch
and Frank Park, Cambridge University Press 2017).



For more information, including a user manual, see the [project's GitHub page](https://github.com/tjdalsckd).
"""

setup(
    name = "mr_urdf_loader",
    version = __version__,
    author = "Minchang Sung",
    author_email = "tjdalsckd@gmail.com",
    description = ("URDF Loader for Modern Robotics Library"),
    license = "MIT",
    long_description = long_description,
    long_description_content_type='text/markdown',
    keywords = "kinematics robotics dynamics",
    url = "http://modernrobotics.org/",
    packages=['mr_urdf_loader'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=[
        'numpy',
        'modern_robotics',
        'urdfpy',
    ],
    platforms='Linux, Mac, Windows',
)
