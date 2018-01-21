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



### Student Sense Hat Assembly

1. Please get started by ensuring that you have reviewed the [six 15 second soldering videos](https://radiojove.gsfc.nasa.gov/telescope/soldering.htm) and can comment on them. (If you are into materials, look up tin pest and tin whiskers.)
2. Work through as much of this set of instructions as possible. (Feel free to drop through the Humber College Institute of Technology & Advanced Learning North Campus Prototype Lab in J233 for additional guidance both before and after class.)
![Prototype Lab](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/IMG_20170616_184112490_HDR.jpg)
3. For additional soldering guidance such as surface mount and desoldering:
	1. Watch some [YouTube Videos](https://www.youtube.com/watch?v=BLfXXRfRIzY&list=PLQ32vZrF5U2lFOJTtZDytBWBYVLNp4RYz).
	2. Be sure to wear safety glasses and consult an expert regarding safety, you can even start at your [local hackerspace](https://wiki.hackerspaces.org/List_of_Hackerspaces) (Ideally working towards IPC J-STD-001 Requirements for Soldered Electrical and Electronic Assemblies).
4. Please remember your eyewear (safety glasses if you don't regularly wear glasses) and select a seat in J232.
![Image of lab station](https://raw.githubusercontent.com/six0four/MicroRover/master/images/1.1j232station.jpg) 
5. Turn on the computer under the desk on the left side.
6. Note the red power switch to the back right side of the workstation that controls the power to the monitor, overhead light, and test equipment.
7. Also note the under desk grounding strap jack for wrist straps - Electronics (ELIC) students must buy the $4.99 wrist straps while both CENG and ELIC students are to have the $4.99 safety glasses.
8. When soldering move the extraction arm flow control towards the straight through symbol as it is in the photo below.
9. The sponge in the soldering station can be moistened at the sink in J233. 
1. Start with components kit:  
![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/componentskit.jpg)
1. Optional: try out your kit on your breadboard.
![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/bbphoto.jpg)
2. Create schematic.
3. Create board add photos of equipment and guide from 555 timer/prototype lab bb/plab I drive.
4. At this stage you should have:
![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/componentsandpcb.jpg)
5. Decide whether you will be attempting the optional surface mount resistor.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/05.jpg)
6. Or whether you will be going with the through hole resistor.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/02.jpg)
6. Place resistors in corresponding locations:
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/06.jpg)
7. Bend the leads to hold them in place.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/07.jpg)
8. Solder the resistors from the bottom.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/08.jpg)  
9. Add flux if having trouble but, do not depress the end of the flux pen, just touching it is enough.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/09.jpg)
10. Solder the resistors from the top.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/10.jpg)
11. Trim and keep excess leads (hold onto them while cutting to not allow them to become projectiles).
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/11.jpg)
7. Place via wires (can be stripped solid core wire or just leftover cut off resistor/LED leads) in corresponding locations:
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/12.jpg)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/13.jpg)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/14.jpg)
15. Solder vias.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/15.jpg)
16. Trim the excess via leads.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/16.jpg)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/17.jpg)
18. Place MOSFETS and LED (N.B. the LED's longer leg is the same as on a red LED. Thus, when oriented the same way as the fritzing diagrams the red/green will be the opposite of those in the parts crib. Which way you put it is in your hands.)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/18.jpg)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/19.jpg)
20. Solder one pin of each MOSFET only from bottom side, semiconductor devices are heat sensitive.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/20.jpg)
21. Solder another pin of each MOSFET only from bottom side.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/21.jpg)
22. Solder the third  pin of each MOSFET only from bottom side.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/22.jpg)
23. Trim the MOSFET leads and make sure that none of them have solder bridges. (Note that the LED has shifted agianst the PCB here.)  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/23.jpg)
24. Make sure the LED is away from the PCB.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/24.jpg)
25. Solder the LED only from the top side, semiconductor devices are heat sensitive.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/25.jpg)
26. Trim the excess LED leads and use for any remaining vias.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/26.jpg)
27. Place sockets.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/27.jpg)
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/28.jpg)
28. Solder sockets, no lead trimming is necessary.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/29.jpg)
30. If you soldered the through hole 1kΩ resistor into place then skip past the surface mount resistor steps. Else, if you did not solder the through hole 1kΩ resistor then remove surface mount resistor from its packaging.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/04.jpg)
31. Note that the packaging may look empty from the back.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/03.jpg)
32. Place a little bit of solder onto each of the pads, in this photo there is probably a little bit too much.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/31.jpg)
33. Hold the suface mount resistor with tweezers and heat one end of the resistor with the soldering iron.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/33.jpg)
34. It should now look something like this.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/34.jpg)
35. Heat the other end of the resistor with the soldering iron so that it looks like the next photo.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/35.jpg)
36. Continue to alternate reheating the ends to make it flush with the board.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/36.jpg)
37. While considering surface mount resitors, be aware that the RTC module can charge the CR2032 battery causing damage.
    To permanently disable the charging circuit, please remove the 200 ohm surface mount resistor (board on left) near the unused I2C header by pushing it off the PCB (board on right) with a hot soldering iron.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/32.jpg)
37. Place the stackable header into place.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/37.jpg)
38. Solder only where necessary.  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/38.jpg)
39. Place the breakout board modules into their appropriate sockets adding headers as necessary.
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/39.jpg)
47. Be sure to clean up your workstation with the brush and dustpan.
48. Test assembled hat on Vlad's test fixture (and ideally following IPC-A-610 Acceptability of Electronics Assemblies).
[SenseHatTester](https://github.com/vladporcila/SenseHatTester)  
![Prototype Assembly](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/sensehattester.jpg)
49. Use [CorelDRAW X6](https://github.com/vladporcila/CorelDrawProjects/blob/master/Rpi%20Base%20plate.cdr) and laser cutter to create a case guide from plab bb.
50. Tap holes.
51. Mount device.  
![Image of Prototype](https://raw.githubusercontent.com/six0four/StudentSenseHat/master/images/corelcase.jpg)

### Student Raspberry Pi Image Creation and Test Code

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

