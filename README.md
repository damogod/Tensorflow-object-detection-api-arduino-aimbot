# Use tensorflow objection api to make a simple bot to always aim at bounding box


## Getting Started

This project is heavily base on youtuber sentdex's [TensorFlow Object Detection API Tutorial](https://www.youtube.com/watch?v=COlbP62-B-U&list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku). If you don't know anything about tensorflow, strongly recommend to finish his tutorial first. You will definetly know how to use tensorflow objection api and the code here will make sense to you.


## Prerequisites

Python 3.6.6 Anaconda

Tensorflow-gpu 1.9.0

any version between sentdex's requirement should work

Arduino ide and related micro controller

2 stepper motor and drivers(any 3dprinter type can do)

## Installing
From [tensorflow github repo](https://github.com/tensorflow/models) download models.
Within reserch folder there is objection-detection.
Follow sentdex's tutorial, know how to load pre-trained modols, and run real-time object detection.
49tgraph folder contains the frozen_inference_graph,model i trained on fortnite images which targetting on the player models. by now you should know how to load the graph, capture the screen and get the bounding box location.

## Running the tests
If every thing works, you can put object-detection-sentdx.py (change the parameter you have) into your objection-detection folder and replace visualization_utils.py in the utils folder, if there is a bounding box you should see printed location in the terminal.

## Result
The model(49tgraph) is beyond worst, it's missing frame, mistaking grass; trees; rocks; weapons as charactors, can't say it improves the play. The mechanical part is just ok, you need to do settings in number of steps motors rotates for each signal; mouse speed for your own handing or reqirement.

## Deployment
This is a simple demostration of the application of CNN. The goal is to aim any object with fairly good accuracy. You can expand the work to target more object such as car, aeroplane, ship, animal and programme micro-controller for more mechanism.


## Improvement
Originally I use [Yolo V3 from darknet](https://pjreddie.com/darknet/yolo/), which is very acurate and fast, not need to retrain you own models, thir own weights works flawlessly, memory management speed in C++ is almost trippled than python. However, I'm to lazy to code in C++, I tried keras yolo model in python, it's slow as 300ms. Only tensorflow's mobile net v1 can reach frame rate <30ms. For this application is ok. The most time consuming part is actually grab the screen, which took 60ms. so, you only get 10 frame per second. If using camera or Video Capture Card might drastically improve frame, but you might need a second machine.

## Contributing

Just made for fun

## Authors

* **wHo** 

## License

MIT


