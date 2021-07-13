# Face Detection Module
A Python module which will work as a boilerplate for any OpenCV projects which involve Face Detection. This module makes use of the OpenCV library to read the videos and do some image processing, and the Mediapipe library which has a large number of pre-trained pose landmarks and  features which help with the main objective of this module. 

## How to Use

To use this module for your own projects, just fork/clone this repo and get started.

To test this on your videos or use the wecam, run the terminal from the cloned repo folder and type the following command:

    python3 main.py -V "your_video_here" -c min_detection_confidence

### Arguments
--video / -V :                        Input video to draw detected faces on, if skipped uses the webcam

-- conf / -C : Minimum confidence required to draw faces on (default = 0.5)
## Examples

Here, I will show you some of the examples from a video I tested the file on from a variety of angles and poses.

![](friends.png)

![](friends2.png)

![](friends3.png)

![](friends4.png)