from database import Database


def get_events(db:Database):
    with db.conn as connection:
        with connection.cursor() as cursor :
            request="SELECT * from event"
            cursor.execute(request)
            res=cursor.fetchall()
    return res

def get_event(id_event:int):
    pass

def create_event():
    pass


