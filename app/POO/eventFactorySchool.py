from app.POO import eventFactory
from app.POO.event import Event
from app.POO.eventSchool import EventSchool


class EventFactorySchool(eventFactory):
    def __init__(self,id_salle) -> None:
        self.id_salle=id_salle


    def createEvent(self,title:str,desc:str,start_time:datetime,end_time:datetime)-> Event:
        return EventSchool(title,desc,start_time,end_time,self.id_salle:int)

