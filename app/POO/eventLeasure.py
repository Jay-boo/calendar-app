from datetime import datetime
from POO.allOrNothingStrategy import allOrNothingStrategy
from POO.event import Event
from POO.calendar import Calendar

class EventLeasure(Event):
    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime,activity:str,id:int=None) -> None:
        super().__init__(title,desc,start_time,end_time,id)
        self.property=activity
        self.type="leasure"
        self.strategy=allOrNothingStrategy()

