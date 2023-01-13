# CS595-Cotinuous-Control-of-Mobile-Robot-Navigation


Comapred two Policy gradient based deep reinforcement learning algorithms (SAC and DDPG)

Requirements:

- https://github.com/ROBOTIS-GIT/turtlebot3
- https://github.com/ROBOTIS-GIT/turtlebot3_msgs
- https://github.com/ROBOTIS-GIT/turtlebot3_simulations

```
cd ~/catkin_ws/src/
git clone {link_git}
cd ~/catkin_ws && catkin_make
```

## Set State

In: turtlebot3/turtlebot3_description/urdf/turtlebot3_burger.gazebo.xacro.

```
<xacro:arg name="laser_visual" default="false"/>   # Visualization of LDS. If you want to see LDS, set to `true`
```
And
```
<scan>
  <horizontal>
    <samples>360</samples>            # The number of sample. Modify it to 10
    <resolution>1</resolution>
    <min_angle>0.0</min_angle>
    <max_angle>6.28319</max_angle>
  </horizontal>
</scan>
```

## Run Code
There are 2 stages. 

First to run:
```
roslaunch turtlebot3_gazebo turtlebot3_stage_{number_of_stage}.launch
```
For ddpg
In another terminal run:
```
roslaunch project ddpg_stage_{number_of_stage}.launch
```

For sac
In another terminal run:
```
roslaunch project sac_stage_{number_of_stage}.launch
```
