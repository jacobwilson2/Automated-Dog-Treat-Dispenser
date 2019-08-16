# Automated-Dog-Treat-Dispenser

**Contributors: Jacob Wilson & Danielle Seedman**

**Description:**

For our project, we created a cyber-physical computing system that automatically dispenses dog treats when a dog stands within
a certain distance from a sensor. The system is powered by a 5V power supply and driven by a stepper motor driver. The motor 
connects to an arm used as a pushing mechanism that dispenses the treats. After a dog is detected and the treat is dispensed, 
the system takes a picture using a Raspberry Pi camera, and then sends the picture to a specified email address with a 
timestamp so the owner can monitor the dog’s treat eating habitats.

**List of Equipment:**

*	LEDs
*	Raspberry Pi
* Laptop
* Raspberry Pi Camera 
* SR04 Rangefinder 
* Jumper Wires
* MBC25081TB stepper motor driver
* 5V Switch Mode Power Supply
* 3D printer
* Soldering Iron
* Metal Screws

**Code:**

* dog.py (main)
* led.py
* rangefinder.py
* treatDispenser.py
* cameraControl.py
* sendPix.py

**Spreadsheet of GPIO pin outputs:**

![GPIO](https://user-images.githubusercontent.com/44330919/63144065-d3cea880-bfb6-11e9-9402-32bd0312e217.png)

![Picture1](https://user-images.githubusercontent.com/44330919/63144276-c36afd80-bfb7-11e9-8153-1442b6a82b76.png)

![Picture2](https://user-images.githubusercontent.com/44330919/63144323-f6ad8c80-bfb7-11e9-9205-efff16fc06c6.png)

![Picture3](https://user-images.githubusercontent.com/44330919/63144387-4db36180-bfb8-11e9-9869-2d784f4fb84b.png)
