# general_api.py

import requests
import pandas as pd
from classes.api_call import APICall

def check_correct_api(link):
    """Makes sure that an API's link is correct on input, else returns an error."""
    def decorator(func):
        def wrapper(base_api, *args, **kwargs):
            if base_api.get_url() != link:
                return f"Error: Invalid base url. For this function, your url should be {link}."
            return func(base_api, *args, **kwargs)
        return wrapper
    return decorator