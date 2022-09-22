cmake_minimum_required(VERSION 2.8.3)
project(cctv_layer_ros)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Locations.msg
  Coordinate.msg
  MultiPoint.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

include_directories(
  include
  src/core
  src/deep_sort
  src/tools
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/tracker0515.py
  src/cctv_layer.py
  src/object_tracker.py
  src/receive_point.py
  src/convert_tflite.py
  src/convert_trt.py
  src/save_model.py
  src/core/backbone.py
  src/core/common.py
  src/core/config.py
  src/core/dataset.py
  src/core/utils.py
  src/core/yolov4.py
  src/deep_sort/__init__.py
  src/deep_sort/detection.py
  src/deep_sort/iou_matching.py
  src/deep_sort/kalman_filter.py
  src/deep_sort/linear_assignment.py
  src/deep_sort/nn_matching.py
  src/deep_sort/preprocessing.py
  src/deep_sort/track.py
  src/deep_sort/tracker.py
  src/tools/freeze_model.py
  src/tools/generate_detections.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
