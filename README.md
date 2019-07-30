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

Python is required for this tool, and Real Python's blog post is a great tool to setup your environment on MacOS or Windows:

[Python Setup](https://realpython.com/installing-python/)

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

This tool can be accessed by cloning or downloading as a ZIP file to your workstation from, GitHub directly. In order to start using the tool with your own CSV file, simply remove the "input_test_data.csv" under the ```read_data()``` function with your own CSV file. For your convienience, the code snippet is shown below:

```python
#read from CSV file
def read_data():
    print("starting to read data")
    with open('input_test_data.csv') as input_data:
        print("opened data file")
        global line_count
        csv_reader = csv.reader(input_data, delimiter=',')
        set_of_images=[row for idx, row in enumerate(csv_reader) if idx == line_count]
        print(set_of_images)
        original_image = set_of_images[0][0]
        image_to_compare = set_of_images[0][1]
        line_count += 1
        return [original_image, image_to_compare]
```
and replace it with your data file here:

```python
#read from CSV file
def read_data():
    print("starting to read data")
    with open('DATA FILE HERE.csv') as input_data:
        print("opened data file")
        global line_count
        csv_reader = csv.reader(input_data, delimiter=',')
        set_of_images=[row for idx, row in enumerate(csv_reader) if idx == line_count]
        print(set_of_images)
        original_image = set_of_images[0][0]
        image_to_compare = set_of_images[0][1]
        line_count += 1
        return [original_image, image_to_compare]
```

Ensure that the CSV file has the absolute path for each image you wish to compare

The result CSV file will appear in the same drive as the img.py file

![alt text](https://imgur.com/wSkM8yr "All files appear in same folder as Python file")

## Tests

## Author

Paarth Arora

Bachelors of Computer Engineering, Ryerson University


