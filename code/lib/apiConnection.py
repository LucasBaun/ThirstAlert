import keys
import network
import urequests  # Ensure this import is at the top of the file
from time import sleep


def test_api_connection():
    url = f'https://api.thingspeak.com/update?api_key={keys.api_key}&field1=0'
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print('API connection successful')
            return True
        else:
            print('API connection failed with status code', response.status_code)
            return False
    except Exception as e:
        print('API connection failed with error: ', e)
        return False