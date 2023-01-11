from abc import ABC, abstractmethod
from datetime import datetime,date
from app.POO.addStrategy import addStrategy
from app.POO.event import Event

from app.POO.calendar import Calendar


class Event(ABC):

    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime) -> None:
        assert start_time < end_time
        self.id=0
        self.title=title
        self.created_at=date.today()
        self.updated_at=None
        self.desc=desc
        self.start_time=start_time
        self.end_time=end_time
        self.type=None
        self.strategy=None

    def conflict_with(self,event:Event):
        """
        return True if is in conflict 
        """
        if event.start_time < self.start_time:
            if event.end_time > self.start_time:
                return True
        else:
            if event.start_time < self.end_time:
                return True 
        return False


    def is_in_time_interval(self, t_start:datetime,t_end:datetime):
        if t_start < self.start_time:
            if t_end > self.start_time:
                return True
        else:
            if t_start < self.end_time:
                return True 
        return False

    def setStrategy(self,strategy):
        self.strategy=strategy


    @abstractmethod
    def add_event_to_calendar(self,calendar:Calendar):
        assert isinstance(self.strategy,addStrategy)
        add_operation=self.strategy.add(self.start_time,self.end_time,calendar)
        if  add_operation !=None :
            self.start_time,self.end_time=add_operation[0],add_operation[1]
            calendar.events.append(self)





