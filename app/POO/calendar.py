from calendar import calendar
from datetime import datetime
from typing import List
from POO.event import Event
from POO.addStrategy import addStrategy
import pytz
class Calendar:
    def __init__(self) -> None:
        self.events=[]

    def add_event(self,event:Event):
        assert event.start_time> datetime.now().replace(tzinfo=pytz.utc)
        assert isinstance(event.strategy,addStrategy)
        add_operation=event.strategy.add(event.start_time,event.end_time,self)
        if  add_operation !=None :
            event.start_time,event.end_time=add_operation[0],add_operation[1]
            self.events.append(event)

            


    def get_events(self)->List[Event]:
        return self.events

    def remove_event(self,event:Event):
        self.events.remove(event)


    def __str__(self) -> str:
        msg=""
        for event in self.get_events():
            msg+=str(event)+"\n"
        return msg




