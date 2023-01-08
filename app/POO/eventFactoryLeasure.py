from app.POO import eventFactory
from app.POO import Event
from datetime import datetime
from app.POO.eventLeasure import EventLeasure


class eventFactoryLeasure(eventFactory):
    def __init__(self,activity) -> None:
        self.activity=activity


    def createEvent(self,title:str,desc:str,start_time:datetime,end_time:datetime)-> Event:
        return EventLeasure(title:str,desc:str,start_time:datetime,end_time:datetime,self.activity:int)

