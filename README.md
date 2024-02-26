# Skinning

## Introduction
How do animators make those beautiful animations


## Project Set Up

### 1. Install miniconda
Our first step is going to be to install miniconda. This is a so-called _package manager_ that we will 
use in this project for python. If you have a lot of projects, each relying on their own unique, but possibly conflicting packages,
a package manager is super important to be able to properly organize your projects.
[Install miniconda by clicking on the appropriate download from the site according to what kind of computer you have](https://docs.anaconda.com/free/miniconda/index.html)

### 2. Open a terminal window
Once you have miniconda downloaded, you can check that it works by opening a _terminal_.
In Mac/Linux operating systems, just open the standard default terminal. 

In Windows, you can open the Anaconda Prompt, which should have been installed when you installed miniconda.

### 3. Create a new environment
Now that we have a terminal open, we can create a new environment. I usually create one new environment for each one of my projects
so that I can install all the packages I want for it, without worrying how it will affect my other projects.

To create a new environment, type the following command into your terminal:
```
    conda create --name skinning python=3.8
```
This will create an environment named `skinning` with python version 3.8. You can change the name of the environment and the version of python to whatever you want, but this writeup
will assume you are using python 3.8 and an environment named `skinning`.

### 4. Activate the environment
Now that we have created the environment, we need to activate it. This is done with the following command:
```
    conda activate skinning
```
This tells your terminal to use the environment we just created. You can tell that it is activated because the name of the environment will appear in the terminal prompt.

### 5. Install the required packages
Now that we have our environment activated, we can install the packages we need for this project. This is done with the following command:
```
    pip install -r requirements.txt
```
I've taken the time to put all the packages we need in the `requirements.txt`, feel free to have a glance at the contents of that file to
see what packages we are installing.

### 6. Run jupyter notebook
Now that we have all the packages installed, we can run the main IDE we will be using for this project, Jupyter Notebook, which 
was installed by the previous command. An IDE is just a fancy word we use to describe the 
tool we use to look at and write our code.

To run Jupyter Notebook, just type the following command into your terminal:
```
    jupyter notebook
```
This should open a page in your favorite browser that sort of looks like a bunch of files on your computer.








## Affine Transformations

$$
    A = \begin{bmatrix}
            a_{11} & a_{12} & a_{13} & a_{14} \\
            a_{21} & a_{22} & a_{23} & a_{24} \\
            a_{31} & a_{32} & a_{33} & a_{34} \\
        \end{bmatrix}
$$

Scales, Shears and Translations


## Linear Blend Skinning

$$
    x_i = \sum_{j=1}^{n} w_{ij} T_j x
$$


### Tasks

### `translate.py`

### `scale.py`

### `rotate.py`

### `lerp.py`

### `slerp.py`

### `linear_blend_skinning.py`

