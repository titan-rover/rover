
# rover
#Science Controls Team Lead - Andy Nguyen
#Code for this team was not completed. Pyboard code (science_pyboard_code.py) is good example for all code
#Needs to be refactored so that
#1. Get input from external computer (Nvidia Jetson Xavier AGX) through some communication bus
#2. Doesn't rely on buttons for inputs
#3. Can run over our network (Titan-Share)



# ROS Mobility Topics

This folder is a ROS package, containing all topics related to mobility.

## Create Joystick topic

The Joystick topic contains fields used to control the movement of the Rover wheels and arms.

To use this topic, first create a package for mobility.

```
$ cd ~/catkin_ws
$ catkin_create_pkg mobility_topic std_msgs rospy
```

Then, use the following commands to compile the newly created package.

```
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

Return to the src folder, and copy the following files and folders from Github repo to your newly created package.

```
$ cd ~/catkin_ws/src

Copy files package.xml, CMakeLists.txt
Copy folder msg
```
 
Again, compile the package.

```
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

## Publish and Subscribe the Joystick topic

Copy the scripts folder from the Github repo, and Execute the mobility and ESC python scripts, to publish (<b>baseMobilityTalker.py</b>) and subscribe (<b>baseESC.py</b>) the Joystick topic.
