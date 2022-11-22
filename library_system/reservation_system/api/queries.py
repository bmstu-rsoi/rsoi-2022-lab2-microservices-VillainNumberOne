from django.db import connection
import uuid

def get_rented_count(username):
    query = f"""
select count(id) from reservation 
where status = 'RENTED'
and username = '{username}'
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        fetched = cursor.fetchall()

    if len(fetched) == 0:
        return 0
    else:
        return fetched[0][0]

def make_reservation(username, book_uid, library_uid, start_date, till_date):
    uid = str(uuid.uuid4())
    query = f"""
insert into reservation (reservation_uid, username, book_uid, library_uid, status, start_date, till_date)
values ('{uid}', '{username}', '{book_uid}', '{library_uid}', 'RENTED', '{start_date}', '{till_date}')
    """

    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            connection.commit()
            result = True
        except Exception as ex:
            print(ex)
            connection.rollback()
            result = False

    if result:
        result = {
            "reservationUid": uid,
            "status": "RENTED",
            "startDate": start_date,
            "tillDate": till_date,
        }

    return result
