# Importing the necessary libraries
import time
import keys
import machine
import dht
from machine import ADC
from machine import Pin
import urequests

# Variables
TimesInMinutes = 30  # Time in minutes to read the sensor data
min_moisture = 0      # Minimum moisture level
max_moisture = 65535  # Maximum moisture level

# Pin setup
soil = ADC(27) # Soil sensor connected to pin 27
tempSensor = dht.DHT11(machine.Pin(26))     # DHT11 Constructor 
onBoardLed = Pin("LED", Pin.OUT) # Onboard LED


while True:
    try: 
        # Reading the moisture level from the soil sensor and converting it to percentage value.
        moisture = round((max_moisture-soil.read_u16())*130/(max_moisture-min_moisture))
                
        # Reading the temperature and humidity from the DHT11 sensor        
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))


        # Checking if the moisture level is within the range of 0 to 100
        if(moisture >= 0 and moisture <= 100):
            print("Moisture is {}%".format(moisture))
            print("Temperature is {} degrees Celsius".format(temperature))
            print("Humidity is {}%".format(humidity))

            # Sending the data to ThingSpeak using the API key and the moisture level
            url = f'https://api.thingspeak.com/update?api_key={keys.api_key}&field1={moisture}&field2={temperature}&field3={humidity}'
            response = urequests.get(url)
            response.close()

            # Blinking the onboard LED to indicate that the data has been sent to ThingSpeak
            onBoardLed.on()
            time.sleep(1)
            onBoardLed.off()     
   
    # Handling the exceptions
    except Exception as error:
        print("Exception occurred", error)
        time.sleep(1)
    
    # Waiting for the next reading
    time.sleep((TimesInMinutes*60)-1)

