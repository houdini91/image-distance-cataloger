---
title: Image distance cataloger
author: Mikey Strauss
date: June 20, 2021
geometry: margin=2cm
---

📷 # Image distance cataloger 📷
Python CLI tool allows you to organize images by there geotagging.
Tool supports a configurable distance radius to catalog groups by.

# Setup
---

## Virutalenv
Note you need `virtualenv` installed.

Setup env with the following command. (only do once)
```
    virtualenv venv
```
Drop in to env (every time you want to use the application)
```
source venv/bin/activate
```

## Install Requirements
```
    pip install -r requirements.txt
```

# Usage
---
```
usage: main.py [-h] [-r RADIUS] [-I INPUT] [-O OUTPUT] [-f]

add, modify and delete upstream nodes

optional arguments:
  -h, --help            show this help message and exit
  -r RADIUS, --radius RADIUS
                        radius length in meters
  -I INPUT, --input INPUT
                        input directory path
  -O OUTPUT, --output OUTPUT
                        output directory path
  -f, --force           force overwrite output directory
```