from django.db import connection


def get_library_books(library_uid):
    query = f"""
select b.id, b.book_uid, b.name, b.author, b.genre, b.condition, lb.available_count
from books as b 
join library_books as lb on b.id = lb.book_id
where lb.library_id = 
(select id from library where library_uid = '{library_uid}')
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        fetched = cursor.fetchall()

    result = [
        {
            "id": row[0],
            "book_uid": str(row[1]),
            "name": row[2],
            "author": row[3],
            "genre": row[4],
            "condition": row[5],
            "available_count": row[6]
        }
        for row in fetched
    ]

    return result
    
