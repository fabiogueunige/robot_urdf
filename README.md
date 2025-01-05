Project of Andrea Chiappe, Alberto Di Donna, Fabio Guelfi
This project is all developed using ros2 distro hmble.

## Prequisites needed

``` bash
sudo apt-get update
sudo apt-get upgrade
```
If return some errors run this command, else skip and run the next
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E88979FB9B30ACF2
sudo apt-get update
```

```bash
sudo apt-get install ros-humble-control*
sudo apt-get install ros-humble-ros-control*
sudo apt-get install ros-humble-gazebo*
```

``` bash
sudo apt install ros-humble-gazebo-ros-pkgs
sudo apt install ros-humble-joint-state-publisher ros-humle-joint-state-publisher-gui
sudo apt install ros-humble-xacro
sudo apt install ros-humble-joint-state-publisher
```

For run this cose is also important to have this version of OpenCV library, so in case of different version use this code for unistall and install the one with correct version

``` bash
pip uninstall opencv-contrib-python opencv-python
pip install opencv-contrib-python==4.5.4.60 opencv-python==4.5.4.60
```

Is importanto also to put the models folder inide the .gazebo folder.
So download this git repository in any position you wants
``` bash
 git clone https://github.com/CarmineD8/aruco_ros.git
```
then find inside the folder model and put it inside the .gazebo folder on your pc
# Installation 

Inside the ros 2 workspace clone this two package

```bash
git clone https://github.com/fabiogueunige/robot_urdf.git
https://github.com/CarmineD8/ros2_aruco.git
```

After Cloned this two repositories peerform this code for change the modified package

```bash
mv robot_urdf/change/aruco_node.py ros2_aruco/ros2_aruco/ros2_aruco/
mv robot_urdf/change/launch.sh .
rm -r robot_urdf/change
```
Our launch is organized by the file launch.sh. So after cloning run this command for make the file executable
```bash
chmod +x launch.sh
```

# Running 

then build the ros2 folder,
move inside the ros2 workspace and run
```bash
cd ..
colcon build
```
move in the src folder 
```bash
cd src
```
inside this folder there is the executable launch.sh, 
```bash
./launch.sh
```
and follow the code inside for choose wich node run. there is the option: or move a camera or move a chassis for find the aruco markers

# Algorithm
The goal of our algorithm is to make the robot turning, finding all the markers inside the arena, reorder the finded marker through their ids, put a circle arount the markers and show a photo with all the finded marker reordered.

# Problems
This code is developed using ros2 version humble, so there are some problems running the code with foxy, and there are some problems trying to execute the code inside docker.




