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
    *NOTE*: Do not fill in the motion notification section yet. 
![ss1](images/screenshot1.png/?raw=true "title")
![ss2](images/screenshot2.png/?raw=true "asdf")


### The motion notification section:
1. Scroll down under the camera's settings and expand the motion notifications menu
2. enable "Run A Command" and "Run an End Command"

References:
https://www.emqx.com/en/blog/how-to-use-mqtt-in-python


