import requests
import json
from datetime import datetime

LIBRARY_SYSTEM = 'http://localhost:8060'
RATING_SYSTEM = 'http://localhost:8050'
RESERVATION_SYSTEM = 'http://localhost:8070'


def get_city_libraries(city, page=None, size=None):
    if page is not None and size is not None:
        pass
    
    data = {
        "city": city,
        "page": page,
        "size": size
    }
    response = requests.get(f'{LIBRARY_SYSTEM}/api/v1/libraries', data=json.dumps(data)).text
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

    response = requests.get(f'{LIBRARY_SYSTEM}/api/v1/librarybooks', data=json.dumps(data)).text
    return json.loads(response)

def get_user_reservations(username):
    reservations = json.loads(requests.get(f'{RESERVATION_SYSTEM}/api/v1/reservations/{username}').text)
    libraries_list = [reservation['library_uid'] for reservation in reservations]
    books_list = [reservation['book_uid'] for reservation in reservations]

    libraryes_info_data = {
        "libraries_list": libraries_list
    }
    books_info_data = {
        "books_list": books_list
    }

    libraries_info = json.loads(requests.get(f'{LIBRARY_SYSTEM}/api/v1/libraries/info', data=json.dumps(libraryes_info_data)).text)
    books_info = json.loads(requests.get(f'{LIBRARY_SYSTEM}/api/v1/books/info', data=json.dumps(books_info_data)).text)

    libraries = {
        library_uid: {
            "libraryUid": library_uid,
            "name": library_info["name"],
            "address": library_info["address"],
            "city": library_info["city"]
        } 
        for library_uid, library_info in libraries_info.items()
    }

    books = {
        book_uid: {
            "bookUid": book_uid,
            "name": book_info["name"],
            "author": book_info["author"],
            "genre": book_info["genre"]
        } 
        for book_uid, book_info in books_info.items()
    }

    result = [
        {
            "reservationUid": reservation["reservation_uid"],
            "status": reservation["status"],
            "startDate": reservation["start_date"],
            "tillDate": reservation["till_date"],
            "book": books[reservation["book_uid"]],
            "library": libraries[reservation["library_uid"]]
        }
        for reservation in reservations
    ]

    return result

def make_reservation(username, book_uid, library_uid, till_date):
    try:
        till_date = datetime.strptime(till_date, "%Y-%m-%d")
    except Exception as ex:
        return None, str(ex)
    start_date = datetime.today() #.strftime('%Y-%m-%d')
    print(start_date, till_date)
    if till_date <= start_date:
        return None, "Wrong tillDate"

    available_count_data = {
        "library_uid": library_uid,
        "book_uid": book_uid
    }
    available_count = json.loads(requests.get(f'{LIBRARY_SYSTEM}/api/v1/books/available', data=json.dumps(available_count_data)).text)
    if available_count == 0:
        return None, "Not available"

    user_rented = json.loads(requests.get(f'{RESERVATION_SYSTEM}/api/v1/reservations/{username}/rented').text)
    user_stars = json.loads(requests.get(f'{RATING_SYSTEM}/api/v1/ratings/{username}').text)

    if user_stars - user_rented <= 0:
        return None, "Insufficient rating"


    # libraryes_info_data = {
    #     "libraries_list": [library_uid]
    # }
    # books_info_data = {
    #     "books_list": [book_uid]
    # }

    # libraries_info = json.loads(requests.get(f'{LIBRARY_SYSTEM}/api/v1/libraries/info', data=json.dumps(libraryes_info_data)).text)
    # books_info = json.loads(requests.get(f'{LIBRARY_SYSTEM}/api/v1/books/info', data=json.dumps(books_info_data)).text)

    # if not (libraries_info[library_uid] is not None and books_info[book_uid] is not None):
    #     return None, "No library/book with given uid"

    # library_info = libraries_info[library_uid]
    # book_info = books_info[book_uid]

    
    # if library_books 


    return ["fine", username, book_uid, library_uid, till_date]