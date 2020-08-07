#!/bin/bash

OUT_DIR="./out"

RESOLUTION=100
SAMPLINGS=128
ANIM_FRAMES_OPTION="--render-anim"

# Make this "true" when testing the scripts
TEST=false
if ${TEST}; then
  RESOLUTION=10
  SAMPLINGS=16
  ANIM_FRAMES_OPTION="--render-frame 1..5"
fi

# Create the output directory
mkdir -p ${OUT_DIR}

# Run the scripts

blender  --python ./15_generate_cloth_data.py ${ANIM_FRAMES_OPTION} -- ${OUT_DIR}/15/frame_ ${RESOLUTION} ${SAMPLINGS}

# Perform ffmpeg for animations

# ffmpeg -y -r 24 -i ${OUT_DIR}/15/frame_%04d.png -pix_fmt yuv420p ${OUT_DIR}/15_generate_cloth_data.mp4
