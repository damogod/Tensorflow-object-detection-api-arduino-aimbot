import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt

import cv2
import time
from PIL import ImageGrab
from win32api import GetSystemMetrics

Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)

# cap = cv2.VideoCapture(0)

# ## Object detection imports
# Here are the imports from the object detection module.
sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as vis_util

# # Model preparation 
# What model to download.
MODEL_NAME = '49tgraph'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('training', '49t_detection.pbtxt')

NUM_CLASSES = 1

# ## Load a (frozen) Tensorflow model into memory.

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# ## Helper code
def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

# # Detection
last_time = time.time()
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    while True:
      # image_np = np.asarray(mss.mss().grab({"top": 0, "left": 0, "width": 1280, "height": 720}))[...,:-1]
      # image_np = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(Width/2.2,Height/5,Width/1.8,Height/1.3))), cv2.COLOR_BGR2RGB)
      image_np = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(Width/2-70,Height/2-200,Width/2+140,Height/2+200))), cv2.COLOR_BGR2RGB)
      
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
      # image_np_expanded = np.expand_dims(image_np, axis=-1)
      # image_np_expanded = np.repeat(image_np_expanded, 3, 2)
      image_np_expanded = np.expand_dims(image_np, axis=0)

      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      # Each box represents a part of the image where a particular object was detected.
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      # Each score represent how level of confidence for each of the objects.
      # Score is shown on the result image, together with the class label.
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')
      # Actual detection.
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})
      # Visualization of the results of a detection.
      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)

      print('loop took {} seconds'.format(time.time()-last_time))
      last_time = time.time()
      cv2.imshow('object detection', image_np)
      if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
