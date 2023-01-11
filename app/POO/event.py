from abc import ABC, abstractmethod
from datetime import datetime,date
from typing import List
from POO.addStrategy import addStrategy
from POO.reminder import Reminder


class Event(ABC):

    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime) -> None:
        assert start_time < end_time
        self.id=0
        self.title=title
        self.created_at=date.today()
        self.updated_at=self.created_at
        self.desc=desc
        self.start_time=start_time
        self.end_time=end_time
        self.type=None
        self.strategy=None
        self.reminders=[]

    def attachReminders(self,reminders:List[Reminder]):
        for reminder in reminders:
            self.reminders.append(reminder)

    def removeReminder(self,reminder:Reminder):
        self.reminders.remove(reminder)



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



        # assert isinstance(self.strategy,addStrategy)
        # add_operation=self.strategy.add(self.start_time,self.end_time,calendar)
        # if  add_operation !=None :
        #     self.start_time,self.end_time=add_operation[0],add_operation[1]
        #     calendar.events.append(self)
    def __str__(self):
        return f'Event(title={self.title},start_time={self.start_time},end_time={self.end_time},created_at={self.created_at},self.updated_at={self.updated_at})'





