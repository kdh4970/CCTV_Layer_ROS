# cctv_layer_ros
2022 Capstone Design (A - AGV)
1. Get CCTV video by 2 usb webcam  
2. Camera calibration  
3. Get person's coordinate on video by Deep learning Yolo  
4. Homography transform : video to 2D map  
5. publish calculated coordinate group(/points ROS topic)  

## Development Environment

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
