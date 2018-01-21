# QR Code Scanner

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials/Budget](#student-sense-hat-specifications)
3. [Time Commitment](#student-sense-hat-electronic-design-files)
4. [Mechanical Assembly](#student-sense-hat-assembly)
5. [Unit Testing](#student-raspberry-pi-image-creation-and-test-code)
6. [Production Testing](#enterprise-wi-fi)

### Introduction

This project is about e-money transfer by using Qr code sensor. The components that have been used for this project are raspberry pi 3 and Qr code sensor. The raspberry pi comes with a case, power adapter and micro sd card with raspbian OS. A monitor, mouse and a keyboard is required to operate raspberry pi, unless you have laptop to connect it with. To connect a laptop with the pi, you have to configure specific settings accordingly which is not covered in the following instructions. The qr code sensor is connected through a usb with raspberry pi. Recommended libraries have been used to power up the sensor. I plan to demonstrate transactions of an amount of money using the qr code sensor. It can be used in stores to buy stuff and to transfer money. Building this project should require a couple of hours if you follow these instructions.

![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/SSHrev05.jpg)

### Bill of Materials/Budget

I ordered raspberry pi from amazon and it arrived within three days as I used amazon prime shipping. For the most part, I used QR code scanner and raspberry pi. QR code sensor can be used to scan both barcodes and QR codes which is one of the reasons they are more expensive compared to barcode scanners. They can also scan both 1 dimentional and 2 dimentional codes and are equiped with laser. 

![PLA Card](https://github.com/n01033547/Bluetooth/blob/master/screenshot%20budget.PNG?raw=yes)

### Time Commitment

Once I got the equipment it took me 2 weeks to complete the project. This period includes the time that I spent on researching and building my sensors so that it can operate the way i wanted it to. My qr code scanner in connected to the pi through usb so I spend only 2 minutes to connect and test it. But the part that took most of the time was creating the python code.

### Mechanical Assembly

I did not need any extra electrical equipment such as wires, motors, resistors, capacitors etc. The assembly of this project requires raspberry pi, power adaptor and QR code scanner with usb interface. I used a mouse, keyboard and monitor to connect the pi and to test my sensor.

### Unit Testing

When I first got my sensor I was testing it by connecting it to my powered up pi. I was just scanning randomly generated qr codes and barcodes from the internet. And everytime I scanned, the screen I was on happened to scroll down automatically. I thought that the scanned item was being stored somewhere on my the pi. But after searching I could not find it anywhere. Then I though that maybe it will store it on a text editor like notepad or MS word. So I scanned while openning a text editor and the code was stored in the file. 

### Production Testing

Then I started working on programming my sensor so that it can compare the codes i am sccanning with existing codes ina database. If that Qr code or barcode exists in the databse then my program will store in a new file called cart. And if ti does not exist in the invetory or databse then a message will be displayed saying that we dont have that item.

