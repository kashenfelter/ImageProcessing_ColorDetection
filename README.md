ImageProcessing_ColorDetection
==============================

Color detection method in Python using the Python Image Library and Myro Library for use in the SE 101 Scribbler Robot Group 19 Assignment. This algorithm enabled the Scribbler robot to use the built in camera on the Fluke chip to follow an object of a specific colour, mainly red, green, and blue.

How It Works
============
Using the Python Image Library (PIL) and the Myro Library, colour detection in images are processed through the use of the HSV color space. Depending on the parameters set on the color range to detect, the image is converted into a mask where only the detected color of the image processed is returned. Furthermore, the average X and Y coordinate of the coloured pixels are returned, thus enabling the approximate location of the colour to be known.
