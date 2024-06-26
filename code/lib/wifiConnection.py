import keys
import network
from time import sleep





def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')

        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)

    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]                # Get the IP address
    print('\nConnected on {}'.format(ip))  # Print the IP address
    return ip                              # Return the IP address

def disconnect():                        # Disconnect WiFi
    wlan = network.WLAN(network.STA_IF)  # Put modem on Station mode
    wlan.disconnect()                    # Disconnect WiFi
    wlan = None                          # Clean up memory