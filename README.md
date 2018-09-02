# Use tensorflow objection api to make a simple bot to always aim at bounding box


## Getting Started

This project is heavily base on youtuber sentdex's [TensorFlow Object Detection API Tutorial](https://www.youtube.com/watch?v=COlbP62-B-U&list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku). If you don't know anything about tensorflow, strongly recommend to finish his tutorial first. You will definetly know how to use tensorflow objection api and the code here will make sense to you.


## Prerequisites

Python 3.6.6 Anaconda

Tensorflow-gpu 1.9.0

any version between sentdex's requirement should work

## Installing
From [tensorflow github repo](https://github.com/tensorflow/models) download models.
Within reserch folder there is objection-detection.
Follow sentdex's tutorial, know how to load pre-trained modols, and run real-time object detection.
49tgraph folder contains the frozen_inference_graph,model i trained on fortnite images which targetting on the player models. by now you should know how to load the graph, capture the screen and get the bounding box location.

## Running the tests
If every thing works, you can put object-detection-sentdx.py (change the parameter you have) into your objection-detection folder and replace visualization_utils.py in the utils folder, if there is a bounding box you should see printed location in the terminal.


## Deployment



## Built With



## Contributing

Just made for fun

## Authors

* **wHo** 

## License

Free.4.O


