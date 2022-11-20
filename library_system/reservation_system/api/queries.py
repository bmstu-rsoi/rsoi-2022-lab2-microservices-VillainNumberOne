from django.db import connection

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
