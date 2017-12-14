# ![](http://micro.seas.harvard.edu/images/SEASLogo_RGB.jpg)
# VRView - The Gyroscopic Drone Camera
# CS 143 Final Project
# Virtual Reality Camera with Gyroscopic Control
# Mikhail Grushko and Matthew Li
# README
# Video Demo on Youtube [HERE](https://youtu.be/4krU8vz3BOs)
## Instructions for Using this Repository

1. This is an open source project, so anyone can see the source code of the project. Feel free to browse or download the files in this repo. In order to get contributor privileges, please talk to one of the team members.
    If you want to copy this repository to your Raspberry Pi or any other machine, execute execute the following command inside the folder (where you want to store your repository) in your terminal:

        git clone https://github.com/grushkom/cs143finalproj.git

    You should be all set to start contributing!

2. Before starting work, execute the following command inside the es96wearable folder in your terminal:

         git pull

    This will make the repository on your computer up-to-date.

3. To work on any of the files, use any sort of text editor or IDE you might
prefer. I suggest using Sublime Text 3, available to download for free [here](https://www.sublimetext.com/3).

    Some of the code here is developed through specialized development environments: please see next sections for more details.

4. In order to save progress into your **local** (on your machine) git repo, execute the following command inside the cs143finalproj folder in your terminal:

         git commit -am "THE COMMIT'S NAME GOES HERE"

    please make sure commit messages are informative, so that is easier to track the versions.
    In order to update the repository stored online with your new updates, execute:

         git push

## Contents of the repository and Instructions

### picam

picam is a HTML/CSS/JS interface for the Raspberry Pi camera, which is accessible over the local access point.

In order to launch picam, make sure your RPi, as well as all other devices are connected to the same mobile hotspot, while RPi has [Apache2](https://httpd.apache.org). Check the status of the server by running the following in the terminal:

    sudo service apache2 status

If the apache server is not runnning for whatever reason, run the following:

    sudo service apache2 start

The server should be good to go. The picam itself will be accessible at the following link: [http://171.20.11.10/html/picam/](http://171.20.11.10/html/picam/)

The code prototype was taken from [here](https://elinux.org/RPi-Cam-Web-Interface)

### PiViewer

PiViewer is an localhost HTML/CSS/JS interface for streaming Google Cardboard - compatible livestream from the RPi camera. The Local IP address for accessing picam is [http://171.20.11.10/html/PiViewer/](http://171.20.11.10/html/PiViewer/).

PiViewer is also run by the [Apache2](https://httpd.apache.org) server. Check the status of the server by running the following in the terminal:

    sudo service apache2 status

If the apache server is not runnning for whatever reason, run the following:

    sudo service apache2 start

The server should be good to go. The picam itself will be accessible at the following link: [http://171.20.11.10/html/picam/](http://171.20.11.10/html/picam/)

The code prototype was taken from [here](https://www.sitepoint.com/streaming-a-raspberry-pi-camera-into-vr-with-javascript/)

### servoPWM

servoPWM is a folder with files that control the servo. It does so using Python, and specifically its library RPi.GPIO. The directory contains two important files: calibration.py and servoPWM.py.

calibration.py is the file we used to calibrate the servo. In order to run it, first connect the servo to the VCC, GND, and pin 32 pins according to the color scheme. Then, run the following command in the servoPWM folder:

    sudo python calibration.py

 control.py is the code that actually runs the servo for the purposes of integration with VR. In order to execute it as a part of the VRView system, execute in the same folder:

    sudo python control.py

if you execute the command more than once, you might find the error that the IP Address is already taken. To fix it, type in the command line:

    s -fA | grep python

Find the process number of the second process you see. Execute:

    sudo kill -9 NUMBEROFSECONDPROCESS


## Hardware Used

### 1 . [Raspberry Pi 3 Model B](https://www.raspberrypi.org)

Raspberry Pi was used as a main platform for software-hardware integration. It was the best option for integrating a camera, broadcasting the image over the local network, creating a VR compatibe imagery, and controlling a servo holding the camera on a drone. It can be purchased on Amazon [here](https://www.amazon.com/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92/ref=sr_1_3?s=pc&ie=UTF8&qid=1511748097&sr=1-3&keywords=raspberry+pi).

### 2. [Futaba S3003 Servo](https://www.towerhobbies.com/cgi-bin/wti0001p?&I=LXH288)

Futaba S3003 Servo is a nice motor that can be programmed using a breadboard and a Raspberry Pi or Arduino or any other electronics modeling hardware. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/Futaba-FUTM0031-S3003-Standard-Servo/dp/B0015H2V72/ref=sr_1_1?s=toys-and-games&ie=UTF8&qid=1511748433&sr=1-1&keywords=futaba+s3003).

### 3. [Raspberry PI 5MP Camera Board Module](https://www.sparkfun.com/products/14028)

A nice camera that is meant for use with Raspberry Pi. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/Raspberry-5MP-Camera-Board-Module/dp/B00E1GGE40).

### 4. [Samsung 32GB 95MB/s (U1) MicroSD EVO Select Memory Card](https://www.samsung.com/us/computing/memory-storage/memory-cards/microsdhc-evo-select-memory-card-w--adapter-32gb--2017-model--mb-me32ga-am/)

32GB memory card compatible for use as Raspberry Pi storage. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/dp/B01DOB6Y5Q/ref=sspa_dk_detail_6?psc=1).

### 5. [Google Cardboard](https://vr.google.com/cardboard/)

Google cardboard is a platform that allows for an affordable and accessible VR experience. The App can be downloaded from App Store and Google Play, while the cardboard can be purchased [here](https://vr.google.com/cardboard/get-cardboard/)



## Software Used

### 1. [Apache2 Server](http://httpd.apache.org)

Apache2 was installed on the Raspberry Pi to run a local HTTP server to broadcast what the camera is currently seeing over the local network.

### 2. [Arduino](https://www.arduino.cc)

Arduino software was used for calibrating the the servo, as well as programming it to respond to the gyroscopic inputs. Downloadable for desktop [here](https://www.arduino.cc/en/Main/Software), as an online editor (Arduino create) [here](https://create.arduino.cc).

### 3. [sensorUDP](https://play.google.com/store/apps/details?id=com.ubccapstone.sensorUDP&hl=en&rdid=com.ubccapstone.sensorUDP)

sensorUDP was used for collecting and distributing the gyroscopic data over the local network using UDP stream. It can be downloaded from Google Play [here](https://play.google.com/store/apps/details?id=com.ubccapstone.sensorUDP&hl=en&rdid=com.ubccapstone.sensorUDP)
