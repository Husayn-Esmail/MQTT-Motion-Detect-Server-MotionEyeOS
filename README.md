# Motion Sense Server For MotionEyeOS

uses mqtt to push motion updates to the ffmpeg homebridge plugin

## Requirements
1. MotionEyeOS installed on your raspberry pi.
https://github.com/motioneye-project/motioneyeos
2. python3
3. modules required in requirements.txt (use python3 -m pip install -r requirements.txt)
4. Some sort of camera compatible with MotionEyeOS
5. a Homebridge Server connected to your Apple Home
6. ffmpeg plugin for homebridge
https://github.com/Sunoo/homebridge-camera-ffmpeg#readme

*NOTE*: Since this setup best works with tmux, we will be installing and using it here
### Quick tmux cheatsheet
To exit tmux without killing the session use ctrl+b then d
To exit tmux and kill it use ctrl+b x y enter
To open a pane vertically: ctrl+b %
To open a pane horizontally: ctrl+b "

## Steps:
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
5. 
6. Connect camera to Raspberry Pi
7. Flash MotionEyeOS on your pi
8. Ensure Raspberry Pi is connected to ethernet for best performance, I have not tested on wifi.
9.  install the ffmpeg camera plugin on your homebridge server
10. install mosquitto-clients and mosquitto on homebridge server 
   (sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install mosquitto mosquitto-clients -y)
   This step isn't entirely necessary but it's helpful for testing.
11. locate the ip address of your motion eye camera, the hostname will be something like "[somechars]meye[somechars]" 
12. visit http://[ip address] in a browser and login with the credentials user: admin and no password
13. click the wrench icon (hover over your camera preview in the motion eye dashboard) and configure according to the screenshots.
    *NOTE*: Do not fill in the motion notification section yet. 
![ss1](images/screenshot1.png/?raw=true "title")
![ss2](images/screenshot2.png/?raw=true "asdf")




References:
https://www.emqx.com/en/blog/how-to-use-mqtt-in-python


