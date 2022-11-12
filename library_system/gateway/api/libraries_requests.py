import requests
import json

def get_city_libraries(city, page=None, size=None):
    if page is not None and size is not None:
        pass
    
    data = {
        "city": city,
        "page": page,
        "size": size
    }
    response = requests.get(f'http://localhost:8060/api/v1/libraries', data=json.dumps(data)).text
    return json.loads(response)

def get_library_books(library_uid, page=None, size=None, show_all=None):
    if page is not None and size is not None:
        pass
    if show_all is not None:
        pass
    
    data = {
        "library_uid": library_uid,
        "page": page,
        "size": size,
        "show_all": show_all
    }

    response = requests.get(f'http://localhost:8060/api/v1/librarybooks', data=json.dumps(data)).text
    return json.loads(response)
