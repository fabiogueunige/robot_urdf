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
```

# Installation 

Inside the ros 2 workspace clone this two package

```bash
git clone https://github.com/fabiogueunige/robot_urdf.git
```
Now give this instructions
```bash
# Passaggio 2: Sostituire il file aruco_node.py
mv robot_urdf/change/aruco_node.py ros2_aruco/ros2_aruco/ros2_aruco/

# Passaggio 3: Spostare launch.sh fuori da robot_urdf
mv robot_urdf/change/launch.sh robot_urdf/

# Passaggio 4: Eliminare la cartella "change"
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




