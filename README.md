# Tutorial to recreate the Thirst-Alert system
## 1. Overview of the project
**Lucas Baunsgaard | lb224rw**

The ThirstAlert system uses a soil moisture sensor connected to an IoT platform to monitor and report the moisture levels in the soil. When the moisture level drops below a certain threshold, the system sends a notification to alert you that it's time to water your plants. This project is the result of an IoT course at Linnaeus University (LNU) in Sweden. Read more about the LNU course [Introduction to Applied Internet of Things.](https://lnu.se/kurs/tillampad-internet-of-things-introduktion/distans-internationell-engelska-sommar/)

***Time to complete:*** <br>
Approximately X-X hours, depending on your experience with IoT and electronics.

## 2. Objective
### Project idea and purpose
The selection of this project was driven by a desire to explore the functionality of soil moisture sensors and their integration within a home automation system. The intention was to create a solution that bridges the gap between traditional plant care methods and modern IoT technologies. The project was chosen based on its potential to offer practical insights into the implementation of IoT devices in everyday scenarios.
<br>
The primary objective of this project is to develop a system capable of autonomously monitoring the soil moisture levels of plants and providing timely notifications for watering. The purpose is to establish an efficient and reliable method for plant care management that mitigates the risk of over or under-watering, thereby promoting plant health and longevity.
### Insights
Through the execution of this project, it is expected to gain valuable insights into the technical aspects of IoT device integration, sensor calibration, and data interpretation. Furthermore, the project aims to provide a deeper understanding of the role of technology in optimizing plant care routines. The anticipated insights encompass both practical knowledge related to hardware implementation and conceptual understanding of the synergy between IoT and agriculture.

## 3. Material
**Component** | **Description/Function** | **Purchased From** | **Price** (approximately)
--------------| -------------------------| -------------------| ------------------------
Raspberry Pi Pico WH   | Serves as the central controller in the Thirst-Alert system. It processes data from the soil moisture sensor and sends notifications to alert when it's time to water the plants. The onboard WiFi module allows for seamless connectivity to the network, enabling remote monitoring and alerts.     |[Electrokit](https://www.electrokit.com/en/raspberry-pi-pico-wh)| 109 SEK
Solderless Breadboard | The Solderless Breadboard acts as the assembly platform for electronic circuits in the project. It allows easy and temporary connections of components without soldering, facilitating rapid prototyping and testing of the Thirst-Alert system's electronic setup.     |[Electrokit](https://www.electrokit.com/en/kopplingsdack-840-anslutningar)      | 69 SEK
Jumper wires female/male| These wires facilitate connections between components on the breadboard and other hardware, enabling seamless signal and power transmission in the project. |[Electrokit](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hona/hane)| 49 SEK
Soil hygrometer module          | The Soil Hygrometer Module detects soil moisture levels, providing crucial data for the Thirst-Alert system. It consists of two probes that are inserted into the soil, and its analog output varies depending on the moisture content. This module serves as the primary sensor, allowing the system to determine when watering is needed based on the soil's hydration level.     |[Electrokit](https://www.electrokit.com/en/jordfuktighetssensor)      | 29 SEK


## 4. Computer setup
### Chosen IDE
For this project, Visual Studio Code (VS Code) is used as the Integrated Development Environment (IDE). VS Code is a powerful and versatile editor with extensive support for various programming languages and tools.

### Installing Necessary Software
1. **Visual Studio Code**<br>
Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/). Follow the installation instructions specific to your operating system.
3. **Node.js** <br>
Download and install Node.js from the [official website](https://nodejs.org/).<br> After installing it open command promt on your computer and write
```shell
node -v
npm -v
```
in the terminal to verify a successful installation

5. **Raspberry pi pico firmware**<br>
Download the latest firmware release on the [MycroPython site](https://micropython.org/download/RPI_PICO_W/). To install the firmware follow their guide they provide under **Installation instructions** on the same site as you downloaded the firmware.

### Setting Up The IDE
1. **Installing Extensions in Visual Studio Code**
   - To connect to the Raspberry Pi Pico WH board, you will need to add the [***Pymakr***](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) extension by **Pycom**. If you're unsure how to add extensions, you can follow [this guide](https://code.visualstudio.com/docs/editor/extension-marketplace).
   - Additionally, I recommend downloading the [***Python***](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension by **Microsoft**, which enhances the Python programming experience in Visual Studio Code.
 
## 5. Putting everything together
![Electronics](https://t3.ftcdn.net/jpg/06/00/90/50/360_F_600905009_Fk9is0pcoxVFjRiz4IOURB35OSHNIvRH.jpg) <br>
Explains the circuit diagram a bit

## 6. Platform
Some information about what platform did i use and like that

## 7. The code
```Python
import dht
import machine
import time

tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 
# tempSensor = dht.DHT22(machine.Pin(27))   # DHT22 Constructor

while True:
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
    except Exception as error:
        print("Exception occurred", error)
    time.sleep(1)
```

```Python
import wifiConnection


def http_get(url = 'http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close connection

# WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# HTTP request
try:
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("No Internet", err)

# WiFi Disconnect
# wifiConnection.disconnect().
```
