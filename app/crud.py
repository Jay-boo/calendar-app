from asyncio import events
from app.POO.calendar import Calendar
from app.POO.event import Event
from app.POO.eventFactory import EventFactory
from app.POO.eventFactoryLeasure import EventFactoryLeasure
from app.POO.eventFactorySchool import EventFactorySchool
from app.POO.eventLeasure import EventLeasure
from app.POO.eventSchool import EventSchool
from database import Database



def get_events_by_type_id(type_id,db:Database):
    schoolFactory=EventFactorySchool()
    leasureFactory=EventFactoryLeasure()
    events_list=[]

    with db.conn as connection:
        
        with connection.cursor() as cursor :
            request=f"SELECT * from event WHERE type_event_id=${type};"
            cursor.execute(request)
            res=cursor.fetchall()


        for event in  res:
            if event[3]==0:
                event=EventSchool(title=,desc=,start_time=,end_time=,salle=)
            else if event[3]==1:
                event=EventLeasure(title=,desc=,start_time=,end_time=,activity=)
            events_list.append(event)
    
    return res

def get_event(db:Database,id_event:int):
    with db.conn as connection:
        with connection.cursor() as cursor :
            request=f"SELECT * from event WHERE id_event=${id_event};"
            cursor.execute(request)
            res=cursor.fetchall()
    return res


def load_calendar(db:Database)-> Calendar:
    calendar=Calendar()
    events=get_events(db)
    calendar.events=events
    return calendar




def add_event(db:Database,factory:EventFactory,title,desc,start_time,end_time):
    event=factory.createEvent(title,desc,start_time,end_time)
    event.add_event_to_calendar()

    with db.conn as connection:
        with connection.cursor() as cursor :
            request=f"INSERT INTO event(id_event,nom,description,type_event)"%(event.id,event.nom,event.desc,event.type)
            cursor.execute(request)
            res=cursor.fetchall()
    return res



