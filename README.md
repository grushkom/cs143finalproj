# ![](http://micro.seas.harvard.edu/images/SEASLogo_RGB.jpg) 
# CS 143 Final Project
# VR Camera with Gyroscopic Control
# Mikhail Grushko and Matthew Li
# README

## Instructions for Using this Repository

1. This is an open source project, so anyone can see the source code of the project. Feel free to browse or download the files in this repo. In order to get contributor priviliges, please talk to one of the team members.
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
         
## Contents of the repository

### picam

Picam is a HTML/CSS/JS interface for the Raspberry Pi camera, which is accessible over the local access point. The Local IP address for accessing picam is [171.20.11.10/html/picam](171.20.11.10/html/picam). 

### PiViewer 

PiViewer is an localhost HTML/CSS/JS interface for streaming Google Cardboard - compatible livestream from the RPi camera. The Local IP address for accessing picam is [171.20.11.10/html/picam](171.20.11.10/html/PiViewer).

## Problem Statement 

Currently, there are few consumer solutions on the market that integrate Virtual Reality and Drones.
Being able to use VR for controlling the drone allows for more intuitive control, which has applications in a variety of fields, where full immersion control is an unmet need, such as surveillance, emergency rescue services, reconnaissance in hard-to-reach areas, and entertainment.

## Hardware Used

### 1 . [Raspberry Pi 3 Model B](https://www.raspberrypi.org)

Raspberry Pi was used as a main platform for software-hardware integration. It was the best option for integrating a camera, broadcasting the image over the local network, creating a VR compatibe imagery, and controlling a servo holding the camera on a drone. It can be purchased on Amazon [here](https://www.amazon.com/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92/ref=sr_1_3?s=pc&ie=UTF8&qid=1511748097&sr=1-3&keywords=raspberry+pi).

### 2. [Futaba S3003 Servo](https://www.towerhobbies.com/cgi-bin/wti0001p?&I=LXH288)

Futaba S3003 Servo is a nice motor that can be programmed using a breadboard and a Raspberry Pi or Arduino or any other electronics modeling hardware. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/Futaba-FUTM0031-S3003-Standard-Servo/dp/B0015H2V72/ref=sr_1_1?s=toys-and-games&ie=UTF8&qid=1511748433&sr=1-1&keywords=futaba+s3003).

### 3. [Raspberry PI 5MP Camera Board Module](https://www.sparkfun.com/products/14028)

A nice camera that is meant for use with Raspberry Pi. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/Raspberry-5MP-Camera-Board-Module/dp/B00E1GGE40).

### 4. [Samsung 32GB 95MB/s (U1) MicroSD EVO Select Memory Card](https://www.samsung.com/us/computing/memory-storage/memory-cards/microsdhc-evo-select-memory-card-w--adapter-32gb--2017-model--mb-me32ga-am/)

32GB memory card compatible for use as Raspberry Pi storage. Full specs in the link above. It can be purchased on Amazon [here](https://www.amazon.com/dp/B01DOB6Y5Q/ref=sspa_dk_detail_6?psc=1).

## Software Used

### 1. [Apache2 Server](http://httpd.apache.org)

Apache2 was installed on the Raspberry Pi to run a local HTTP server to broadcast what the camera is currently seeing over the local network.

### 2. [Arduino](https://www.arduino.cc)

Arduino software was used for calibrating the the servo, as well as programming it to respond to the gyroscopic inputs. Downloadable for desktop [here](https://www.arduino.cc/en/Main/Software), as an online editor (Arduino create) [here](https://create.arduino.cc).
