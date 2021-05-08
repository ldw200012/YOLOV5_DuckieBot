# <div align=center>duckietown_object_recognition</div>
#### <div align="center">" This repository is created for object recognition functionality of Duckiebot, </div>
#### <div align="center"> which reads the camera view of a duckiebot and detects the obstacle in the front. "</div>

***

# What you need to prepare
1. Linux environment
2. Annotated Image group for your own dataset
3. 

# I. Introduction to YOLOv5 on Custom Dataset
Reference Video : https://www.youtube.com/watch?v=MdF6x6ZmLAY by Roboflow

- YOLOv5 algorithm on Google Colab
       Fully follow the instructions of the reference video.

- YOLOv5 algorithm on ROS
       Follow the instructions on the reference video until 15:40.



# II. Introduction to ROS

### A. How to install ROS Noetic
You can take a look at below ROS Wiki page to follow instructions to ROS Noetic installation

http://wiki.ros.org/noetic/Installation/Ubuntu

### B. How to create ROS Workspace and Package
1. Create a ROS workspace

       $ mkdir -p ~/catkin_ws/src
       $ cd ~/catkin_ws/
       $ catkin_make
       $ source devel/setup.bash

2. Get into your ROS workspace

       $ cd ~/catkin_ws/src
       
3. Copy a ROS Package

       $ git clone https://github.com/ldw200012/duckietown_object_recognition.git

4. Run below commands to configure your ROS Package

       $ cd ~/catkin_ws
       $ catkin_make
       $ source devel/setup.bash (This command must be run on every shell you are using for ROS from now on)
       
# III. How to run the program

### A. Input your own dataset
You can simply replace all the image files in the 'img' folder, but if you want to collect the image data from your own duckiebot's camera, follow below commands
1. Make your duckiebot see
       
       $ dts start_gui_tools JoudiDuck
       $ rqt_image_view
   
   Now you can see the camera view of your duckiebot

2. Convert the compressed images into raw image

       $ rosrun image_transport republish compressed in:=/[duckiebot_name]/camera_node/image raw out:=/[duckiebot_name]/camera_node/image/raw
   
   Now you will see a new rostopic with name '/[duckiebot_name]/camera_node/image/raw'

3. Direct to 'img' folder and save

       $ roscd duckietown_object_recognition/img
       $ rosrun image_view image_saver image:=/JoudiDuck/camera_node/image/raw
       
   Now the images will be saved to the 'img' folder.
   Move your duckiebot and collect the image data!
  
### B. Train dataset

### C. Detect Objects 

***
# About the Project

#### Module Name: 
#### Instructors: 
#### Contributors: 


