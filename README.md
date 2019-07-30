# Loblaws Digital - Developer Take Home Assignment - Comparing 2 Images

## Table of Contents

* [Introduction](https://github.com/p6arora/LoblawsDigital_ImageComparison#Introduction)
* [Design](https://github.com/p6arora/LoblawsDigital_ImageComparison#Design)
* [Implementation](https://github.com/p6arora/LoblawsDigital_ImageComparison#Implementation)
* [Setup](https://github.com/p6arora/LoblawsDigital_ImageComparison#Setup)
* [Usage](https://github.com/p6arora/LoblawsDigital_ImageComparison#Usage)
* [Tests](https://github.com/p6arora/LoblawsDigital_ImageComparison#Tests)
* [Author](https://github.com/p6arora/LoblawsDigital_ImageComparison#Author)

## Introduction

For this assignment, my objective was to make a tool which compared 2 images for similarity and rank them accordingly. It was an open-ended assignment and I had the option to choose whichever stack I would deem the best option. My prefered stack was:

* Python
* OpenCV

The justifications for my design and alternative design are explored in the Design subsection

## Design

## Implementation

## Setup

At the time of the assignment, I was using Python 3.7 and the newest OpenCV version was 4.1.0.25. **However**, in order to use the SIFT Algorithm, 2 older versions of the OpenCV libraries were needed. These can be installed using pip:

```bash
pip3 install opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17
```
In order to measure execution time, time and csv libraries were used but these are available built in to Python. Your final imports should appear as:

```python
import cv2
import numpy as np
import csv
import time

```



## Usage

## Tests

## Author

Paarth Arora

Bachelors of Computer Engineering, Ryerson University


