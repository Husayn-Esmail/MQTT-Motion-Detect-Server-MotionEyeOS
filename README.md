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

## Steps:
1. Connect camera to Raspberry Pi
2. Flash MotionEyeOS on your pi
3. Ensure Raspberry Pi is connected to ethernet for best performance, I have not tested on wifi.
4. install the ffmpeg camera plugin on your homebridge server
5. install mosquitto-clients and mosquitto on homebridge server 
   (sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install mosquitto mosquitto-clients -y)
   This step isn't entirely necessary but it's helpful for testing.
6. locate the ip address of your motion eye camera, the hostname will be something like "**meye**" where the ** are other characters or numbers
7. visit http://[ip address] in a browser and login with the credentials user: admin and no password
8. click the wrench icon (hover over your camera preview in the motion eye dashboard) and configure according to the screenshots.
    *NOTE*: Do not fill in the motion notification section yet. 
![ss1](images/screenshot1.png/?raw=true "title")
![ss2](images/screenshot2.png/?raw=true "asdf")




References:
https://www.emqx.com/en/blog/how-to-use-mqtt-in-python


