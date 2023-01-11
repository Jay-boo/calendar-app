from datetime import datetime
from POO.calendar import Calendar
from POO.priorityStrategy import priorityStrategy
from POO.event import Event


class EventSchool(Event):
    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime,id_salle:int) -> None:
        super().__init__(title,desc,start_time,end_time)
        self.property=id_salle
        self.type="school"
        self.strategy= priorityStrategy()

