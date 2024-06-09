# Tutorial to recreate the Thirst-Alert system
## Overview of the project
**Lucas Baunsgaard | lb224rw**

The ThirstAlert system uses a soil moisture sensor connected to an IoT platform to monitor and report the moisture levels in the soil. When the moisture level drops below a certain threshold, the system sends a notification to alert you that it's time to water your plants. This project is the result of an IoT course at Linnaeus University (LNU) in Sweden. Read more about the LNU course [Introduction to Applied Internet of Things.](https://lnu.se/kurs/tillampad-internet-of-things-introduktion/distans-internationell-engelska-sommar/)

***Time to complete:*** <br>
Approximately X-X hours, depending on your experience with IoT and electronics.

## Objective
### Project idea and purpose
The selection of this project was driven by a desire to explore the functionality of soil moisture sensors and their integration within a home automation system. The intention was to create a solution that bridges the gap between traditional plant care methods and modern IoT technologies. The project was chosen based on its potential to offer practical insights into the implementation of IoT devices in everyday scenarios.
<br>
The primary objective of this project is to develop a system capable of autonomously monitoring the soil moisture levels of plants and providing timely notifications for watering. The purpose is to establish an efficient and reliable method for plant care management that mitigates the risk of over or under-watering, thereby promoting plant health and longevity.
### Insights
Through the execution of this project, it is expected to gain valuable insights into the technical aspects of IoT device integration, sensor calibration, and data interpretation. Furthermore, the project aims to provide a deeper understanding of the role of technology in optimizing plant care routines. The anticipated insights encompass both practical knowledge related to hardware implementation and conceptual understanding of the synergy between IoT and agriculture.

## Material
**Component** | **Description/Function** | **Purchased From** | **Price** (approximately)
--------------| -------------------------| -------------------| ------------------------
Raspberry Pi Pico WH   | Serves as the central controller in the Thirst-Alert system. It processes data from the soil moisture sensor and sends notifications to alert when it's time to water the plants. The onboard WiFi module allows for seamless connectivity to the network, enabling remote monitoring and alerts.     |[Electrokit](https://www.electrokit.com/en/raspberry-pi-pico-wh)| 109 SEK
Solderless Breadboard | The Solderless Breadboard acts as the assembly platform for electronic circuits in the project. It allows easy and temporary connections of components without soldering, facilitating rapid prototyping and testing of the Thirst-Alert system's electronic setup.     |[Electrokit](https://www.electrokit.com/en/kopplingsdack-840-anslutningar)      | 69 SEK
Jumper wires female/male| These wires facilitate connections between components on the breadboard and other hardware, enabling seamless signal and power transmission in the project. |[Electrokit](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hona/hane)| 49 SEK
Soil hygrometer module          | The Soil Hygrometer Module detects soil moisture levels, providing crucial data for the Thirst-Alert system. It consists of two probes that are inserted into the soil, and its analog output varies depending on the moisture content. This module serves as the primary sensor, allowing the system to determine when watering is needed based on the soil's hydration level.     |[Electrokit](https://www.electrokit.com/en/jordfuktighetssensor)      | 29 SEK


## Computer setup
### Chosen IDE
For this project, Visual Studio Code (VS Code) is used as the Integrated Development Environment (IDE). VS Code is a powerful and versatile editor with extensive support for various programming languages and tools.

### Installing Necessary Software
1. **Visual Studio Code**<br>
Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/). Follow the installation instructions specific to your operating system.
3. **Node.js** <br>
Download and install Node.js from the [official website](https://nodejs.org/).<br> After installing it open command promt and write
```
node -v
npm -v
```
To verify a successful installation

5. **Raspberry pi pico software**

### Setting Up The IDE
1. **Installing Addons/Plugins in Visual Studio Code**
