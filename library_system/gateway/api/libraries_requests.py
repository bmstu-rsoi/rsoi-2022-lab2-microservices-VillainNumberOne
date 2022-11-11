import requests
import json

def get_city_libraries(city, page=None, size=None):
    if page is not None and size is not None:
        pass

    response = requests.get(f'http://localhost:8060/api/v1/libraries/{city}').text
    return json.loads(response)

# print(get_city_libraries("Serzedo"))