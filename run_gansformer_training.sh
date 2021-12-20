#!/bin/bash
set -e

# Define the location of the training data that was downloaded
export CURDIR=$(pwd)
export COVIDX=$(pwd)/data/2A_images
export HEADCT=$(pwd)/data/ct_png

# Download old version of 1.15.5 with GPU support
# Required for ganformer
docker pull tensorflow/tensorflow:1.15.5-gpu-py3-jupyter

docker run \
--runtime=nvidia -it -p 8888:8888 \
-v $CURDIR:/tf/notebooks \
-v $COVIDX:"/tf/notebooks/Final Project/gansformer/data" \
-v $HEADCT:"/tf/notebooks/Final Project/gansformer/head_data" \
--device /dev/nvidia0 --device /dev/nvidia-modeset  --device /dev/nvidia-uvm \
--device /dev/nvidia-uvm-tools --device /dev/nvidiactl \
tensorflow/tensorflow:1.15.5-gpu-py3-jupyter


