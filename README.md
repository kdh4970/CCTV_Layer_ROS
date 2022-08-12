# CCTV_Layer_ROS
2022 Capstone Design (A - AGV)
This package purpose is to use deepsort-yolov4 on ROS. 

## Developemnt Environment

OS : Ubuntu 18.04 LTS  
Meta OS : ROS1-melodic  
GPU : NVIDIA GTX 1080 Ti  
NVIDIA Graphic Driver version : 470  
CUDA version : 11.4  
CUDNN version : 8.2.4  
Python Interpreter version : Python 3.6.9  
OpenCV version : 4.1.1.26  
Tensorflow version : 2.3.0  
USB mono camera : PWC 500 (2EA)  

## How to Use
First. Download yolov4-tiny.weights into 'data' folder.(https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights) 
Second. 

```
# save yolov4-tiny model
python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --model yolov4 --tiny
```

## Base package
TheAIGuysCode - yolov4-deepsort (https://github.com/theAIGuysCode/yolov4-deepsort)
