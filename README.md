# Facial Recognition Research
This repository contains some of the old, initial tests conducted for experimenting with facial recognition. A lot of the older, unused in this variation, code has been deleted for cleanliness (nothing to note, just some tests that failed or functions that have been better optimized). This was developed over a couple weeks as a side project between some friends and I, I believe the greater fascination being the biomedical reading conducted and attempts to utilize it to creating a connection between facial landmark data and expression so as to, in an elementary sense, understand human emotion via the position of these facial landmarks.
# Code
For recognizing facial landmarks we use Adam Geitgey's [face-recognition](https://pypi.org/project/face-recognition/) library. Our [analysis.py](/analysis.py) script allows us to open our webcamera, record our facial landmark coordinate data into [facial_coordinates.txt](/facial_coordinates.txt) (Note: This file contains our last recorded frame of facial landmark data), and draws it onto the output video frame.

![facial_landmarks](https://cdn-images-1.medium.com/v2/resize:fit:1600/1*AbEg31EgkbXSQehuNJBlWg.png)

Coordinate data is split into groups, which are then numbered. The chart above can be used for reference. This allows us to draw connections between specific landmark points in association with facial structures/muscles, which we do so in [text.py](/text.py) for measuring Palpebral Fissure Length and drawing the Zygomaticus Major.
# Research
Our theory going into this stems from an inherent problem with image recognition: you need to identify a static object for reference in order to ascertain a real-world scale. In many medical implementations of this, items such as a quarter would be placed in frame to convert from pixels to metric. Our research aimed to take certain biological factors into consideration to absolve this prior to measuring muscle and facial changes.

This repo is a time capsule of where our project and research was, its neither where it currently is or is the following to be taken as any form of medical advice. Our final/initial release will include a more in-depth analysis with citations. The information below is gathered from a series of written notes from scattered papers we read and likely contains false information.
## Hypothesis
The eye is one of the least growing organs in terms of physical size. If the size of the eye can be quantified with image recognition, then it can be used as the basis for understanding the real world measurments of particular facial structures. Using this data we can then quantify changes in the face, then associate those changes with expression, and by extension emotion.
## Palpebral Fissure Length
![PFL](https://slideplayer.com/slide/13148188/79/images/5/Figure+15.1a+The+eye+and+accessory+structures..jpg)

The Palpebral Fissure Length (PFL) is the distance from one edge of the eye to the other, also referred to as the Lateral Commissure and the Lacrimal Caruncle. These locations are included in our facial landmarks at points 36, 39, 42, and 45. While there are many papers that suggest there to not be too much of a change in PFL between gender and ethnicity, we also found there to be heavy ethnic bias in many of these conducted studies, and as such is a key interest point in our further research.
## Zygomaticus Major
![ZMM](https://images.ctfassets.net/u2qv1tdtdbbu/3rcKvkhFSeYjJ6OR440X5Y/f35731c5d60e738ef213f139dee134fb/ce597-fig11-zygomaticus-major.jpg)

Measuring the Zygomaticus Major (ZMM) was our first attempt at measuring a facial muscle using our coordinate data. One of the primary functions of this muscle type is to create a smile, which by extension we can associate with happiness/joy, where increased in contraction/decrease in ZMM length can be associated with this emotion.
# Future Plans
New tools are being considered for measuring distance between these landmarks, such as Apples AR technology, along with more investment into our bioscience research. We're improving performance with multithreaded image rendering, and aiming for mobile support to release our initial application as a sortave tech demo.

Training our own neural network for facial recognition was in the books, but has since been sidelined due to a lack of training data. This may seem surprising as there are a lot of pictures of faces on the internet, but a simple picture of a face isn't enough, we need the face in a controlled position expression each of the 7 major forms of emotion (plus an additional 8th "neutral" expression). We looked into using artificially generated faces for our training data, but believed that bias in their AI training data would bleed into our model, with ethnic bias in particular being of interest given our research so far into PFL's. Speaking of which, we did a lot of research into across many papers in order to get data on as many ethnic and gender combinations as possible, and believe that our PFL measurements are on average 30% more accurate, with as much as a 60% discrepency across certain groups. More info on that in the future.

The last time we worked on this project was Summer 2022, but we still remain active as close friends, and I intend to work on this in the future. Other, more important projects are currently at the forefront, but that's a story for another day.
