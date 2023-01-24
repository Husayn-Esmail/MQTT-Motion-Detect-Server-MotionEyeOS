# Motion Sense Server For MotionEyeOS

A webserver that receives get requests from MotionEyeOS on motion detection
and publishes an mqtt message for homebridge and by extension homekit motion
detection notifications.

## Requirements
1. MotionEyeOS installed on your raspberry pi.
https://github.com/motioneye-project/motioneyeos
2. python3
3. Some sort of camera compatible with MotionEyeOS
4. a Homebridge Server connected to your Apple Home
5. ffmpeg plugin for homebridge
https://github.com/Sunoo/homebridge-camera-ffmpeg#readme

**NOTE**: *Since this setup best works with tmux, we will be installing and using it here*
### Quick tmux cheatsheet
To exit tmux without killing the session use ctrl+b then d
To exit tmux and kill it use ctrl+b x y enter
To open a pane vertically: ctrl+b %
To open a pane horizontally: ctrl+b "
To navigate between panes: ctrl+b [arrow keys]

## Steps:
### Hardware:
If you do not have a homebridge setup already follow the instructions here:
https://homebridge.io

1. Connect camera to Raspberry Pi
2. Flash MotionEyeOS to your pi's sd card noting that this will wipe all data on the card. (see requirements)
3. Ensure Raspberry Pi is connected to ethernet for best performance, I have not tested on wifi.
4. Power on the MotionEye Pi


### Software:
1. Install tmux and mosquitto:
   ```
   sudo apt-get update && sudo apt-get update -y && sudo apt-get install mosquitto-clients mosquitto tmux -y
   ```
2. Enter tmux
   ```
   tmux new-session -s motion-mqtt-server
   ```
3. Clone this repository on the same machine as your homebridge server
    ```
    git clone git@github.com:Husayn-Esmail/MQTT-Motion-Detect-Server-MotionEyeOS.git && cd MQTT-Motion-Detect-Server-MotionEyeOS
    ```
4. create a virtual environment, enter it and install requirements
   ```
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install -r requirements.txt
   ```
5.  Start the webserver with
    ```
    ./start.sh
    ```
6.  [OPTIONAL TESTING] open a tmux pane horizontally and vertically
7.  run each command in a different tmux pane
   ```
   mosquitto & # run this in one pane
   mosquitto_sub -v -t "homebridge/motion" # run this in the same pane
   mosquitto_pub -v -t "homebridge/motion" "motionStart" # run this in another pane
   ```
8.  After running these commands you should have seen "motionStart" appear in the pane where you ran mosquitto_sub
9.  install the ffmpeg camera plugin on your homebridge server (see requirements)
10. locate the ip address of your motion eye camera, the hostname will be something like "[somechars]meye[somechars]" You can do this via your router or with
```
arp -a
```
however, I never have luck with arp -a so your router software is a safer bet.
### MotionEye Configuration
1.  visit http://[ip address] in a browser and login with the credentials user: admin and no password
2.  click the wrench icon (hover over your camera preview in the motion eye dashboard) and configure according to the screenshots.
3.  it is highly recommended you set the camera to be a static ip address as well as your homebridge server if it is not already.
4.  Take note copy and store two links from the video streaming section
    1.   snapshot url
    2.   streaming url

    *NOTE*: Do not fill in the motion notification section yet. 
![ss1](images/screenshot1.png/?raw=true "title")
![ss2](images/screenshot2.png/?raw=true "asdf")

### The motion notification section:
1. Scroll down under the camera's settings and expand the motion notifications menu
2. enable "Run A Command" and "Run an End Command"
3. in the first command input box put the following
   ```
   curl http://[ip of homebridge server]:8085/motionStart
   ```
4. in the second command input box put the following
    ```curl http://[ip of homebridge server]:8085/motionEnd```
### Homebridge Configuration
Before filling out this section you need two things from the motionEye 
1. In the settings for homebridge-camera-ffmpeg plugin fill in fields with the following
   1. name: literally put whatever you want here
   2. video source: -re -f mjpeg -i [the streaming url you copied from earlier]
   3. still image source: -f mpjpeg -i [the snapshot url you copied from earlier] -vframes 1 -r 1
   4. At the moment audio I have not tested audio so disable audio for now
   5. unbridge the camera (if you would like, I did it)
   6. in the video output sections increase max concurrent streams to 2 or higher if you want
   7. max width and height respectively are 1280 800
   8. max framerate 20fps
   9. in the automation tab enable motion sensor
   10. set automatic motion reset to 0
   11. under mqtt settings set motion topic to homebridge/motion
   12. motion message should be set to start
   13. motion reset topic should be homebridge/motion/reset
   14. motion reset message should be set to end
   15. under global automation -> mqtt client set mqtt server to 127.0.0.1
   16. set mqtt port to 1883
   17. and then hit save and restart homebridge

At this point if you've been able to follow the steps correctly then you should have motion detection and camera output in your homekit app



References:
https://www.emqx.com/en/blog/how-to-use-mqtt-in-python


