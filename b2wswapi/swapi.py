import requests

from b2wswapi.exceptions.swapi_notfound import SWAPINotFound

class SWAPI():
    def __init__(self):
        self.base_url = 'https://swapi.co/api/'

    def get_planet(self, param):
        if type(param) == int:
            response = requests.get(self.base_url + 'planets/' + param)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return SWAPINotFound('Planet not found in swapi.co')
            else:
                raise Exception('An error has occurred when searching for a planet in swapi.co')
        elif type(param) == str:
            response = requests.get(self.base_url + 'planets/', params={'search': param})

            if response.status_code == 200:
                return response.json().get('results')
            elif response.status_code == 404:
                return SWAPINotFound('Planet not found in swapi.co')
            else:
                raise Exception('An error has occurred when searching for a planet in swapi.co')
        else:
            raise TypeError('Invalid search param for planet')
