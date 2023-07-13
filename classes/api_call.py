# api_call.py
import requests

class APICall:
    """Establishes a basic API. Can be used as a base."""
    def __init__(self, base_url, **kwargs):
        self._base_url = base_url
        self._params = kwargs

    def add_parameters(self, **kwargs):
        """Will add desired parameters to the API. If a parameter is already in the dictionary,
        it's value will be replaced. Only accepts keyword arguments."""
        if not self._params:
            self._params = kwargs
        else:
            for key, value in kwargs.items():
                self._params[key] = value

    def remove_parameters(self, *args):
        """Will remove the desired parameters from the API. Will only accept the parameter keys."""
        for key in args:
            try:
                del self._params[key]
            except Exception as e:
                print("remove_parameters failed on key ", key, "! The error was: ", str(e))

    def create_api(self, **kwargs):
        """Creates a new API using self as a base."""
        new_api = APICall(self._base_url, **self._params)
        new_api.add_parameters(**kwargs)
        return new_api

    def request_json(self):
        """Requests the json information from the api."""
        try:
            data = requests.get(self._base_url, params = self._params).json()
        except Exception as e:
            print(f"Error when requesting from the API! Reason: {str(e)}.")
        else:
            return data

    def get_param(self, key):
        """Gets a specific parameter from the params."""
        return self._params.get(key, "")

    def get_params(self):
        """Provides a list of the parameters."""
        return self._params

    def get_url(self):
        """Gets the base url."""
        return self._base_url

    def set_url(self, url):
        """Sets the base url."""
        self._base_url = url