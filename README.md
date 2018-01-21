# QR Code Scanner

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials/Budget](#student-sense-hat-specifications)
3. [Time Commitment](#student-sense-hat-electronic-design-files)
4. [Mechanical Assembly](#student-sense-hat-assembly)
5. [Unit Testing](#student-raspberry-pi-image-creation-and-test-code)
6. [Production Testing](#enterprise-wi-fi)

### Introduction

This project is regarding e-money transfer using Qr code sensor. The components that have been used for this project are raspberry pi 3 and Qr code sensor. The raspberry pi comes with a case, power adapter and micro sd card with raspbian OS. A monitor, mouse and a keyboard is required to operate raspberry pi, unless you have laptop to connect it with. To connect a laptop with the pi you have to configure specific settings accordingly which is not covered in the following instructions. The qr code sensor is connected through usb with raspberry pi. Recomended liberary has been used to power up the sensor. I plan to demonstrate transaction of an amount of money using the qr code sensor. It can be used in stores to buy stuff and to transfer money. Building this project will only require a couple of hours if you follow these instructions.

![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/SSHrev05.jpg)

### Bill of Materials/Budget

I ordered raspberry pi from amazon and it arrived within three days as I am using amazon Prime shipping. For the most part i used QR  code scanner and raspberry pi. QR code sensor can be used to scan both barcodes and QR codes, that's one of the reason they are more expensive compare to barcode scanners, they can scan both 1 dimentional and 2 dimentional codes and are equiped with laser. 

![PLA Card](https://github.com/n01033547/Bluetooth/blob/master/screenshot%20budget.PNG?raw=yes)

### Time Commitment

Once I got the equipment it took me 2 weeks to complete the project. This period includes the time that I spent on researching and building my sensors so that it can operate the way i wanted it to. My qr code scanner in connected to the pi through usb so I spend only 2 minutes to connect and test it. But the part that took most of the time was creating the python code.

### Mechanical Assembly



### Unit Testing

1.	Building the Humber image for the Sense Hat: [https://github.com/six0four/StudentSenseHat/blob/master/cribpisdcard.md](https://github.com/six0four/StudentSenseHat/blob/master/cribpisdcard.md)  
	Note that apt-get puts the installed packages into
    /var/cache/apt/archives/ so a zip of the files from there would
    complement the script used by these instructions.

5.  Open a terminal and type:
	```
	git clone https://github.com/six0four/StudentSenseHat.git
	cd StudentSenseHat/firmware
	gcc -Wall -o traffic2B traffic2B.c -lwiringPi
	sudo ./traffic2B
	```
	write to your blog what happens with your LED.
	
6.	From the Start Menu->Preferences->Raspberry Pi Configuration->Interfaces set I2C to Enabled.

7.	Return to your terminal and type:
    ```Shell
	make
	sudo ./ghmain
	```
	write to your blog what happens.

8.	You can read the OS date with:
    ```Shell
	date
	```
	You can set the OS date with:
	```Shell
	sudo date –s “29 AUG 1997 13:00:00”
	```
	You can write the OS date to the RTC with:
	```Shell
	sudo hwclock –w
	```
	You can read the RTC date with:
	```Shell
	sudo hwclock -r
	```
	
9.	Things to consider for your particular application: boot options (Gui to terminal), and permissions when auto mounting usb keys.
	
10.  Use <http://sourceforge.net/projects/win32diskimager/> to read the image
    into a file.

