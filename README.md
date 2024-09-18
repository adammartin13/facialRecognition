# Facial Recognition Research
This repository contains some of the old, initial tests conducted for experimenting with facial recognition. A lot of the older, unused in this variation, code has been deleted for cleanliness (nothing to note, just some tests that failed or functions that have been better optimized). This was developed over a couple weeks as a side project between some friends and I, I believe the greater fascination being the biomedical reading conducted and attempts to utilize it to creating a connection between facial landmark data and expression so as to, in an elementary sense, understand human emotion via the position of these facial landmarks.
# Code
For recognizing facial landmarks we use Adam Geitgey's [face-recognition](https://pypi.org/project/face-recognition/) library. Our [analysis.py](/analysis.py) script allows us to open our webcamera, record our facial landmark coordinate data into [facial_coordinates.txt](/facial_coordinates.txt) (Note: This file contains our last recorded frame of facial landmark data), and draws it onto the output video frame. Why? So we can track in real time if our program is drawing our features correctly. More on that later.
# Research
Use proper reference formatting when referencing research articles in this section
# Future Plans
