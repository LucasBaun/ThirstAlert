# This module provides a backwards-compatble import for `urequests`.
# It lazy-loads from `requests` without duplicating its globals dict.
# https://github.com/micropython/micropython-lib/blob/master/micropython/urequests/urequests.py

def __getattr__(attr):
    import requests

    return getattr(requests, attr)