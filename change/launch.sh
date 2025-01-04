#!/bin/bash

# Input request
echo "Please, Insert 'robot' or 'camera' to choose which rotate:"
read input

# Check input
if [ "$input" == "robot" ]; then
    echo "Execution of the robot rotating..."
    ros2 launch robot_urdf gazebo_circle.launch.py execName:=robot_rot
elif [ "$input" == "camera" ]; then
    echo "Execution of the camera rotating..."
    ros2 launch robot_urdf gazebo_circle.launch.py execName:=camera_rot
else
    echo "Invalid input. Running with robot rotating..."
    ros2 launch robot_urdf gazebo_circle.launch.py execName:=robot_rot
fi
