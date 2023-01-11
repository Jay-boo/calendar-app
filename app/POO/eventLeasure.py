from datetime import datetime
from app.POO.allOrNothingStrategy import allOrNothingStrategy
from app.POO.event import Event


class EventLeasure(Event):
    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime,activity:int) -> None:
        super().__init__(title,desc,start_time,end_time)
        self.activity=activity
        self.type="leasure"
        self.strategy=allOrNothingStrategy()

    def add_event_to_calendar(self,calendar:Calendar):

        print("adding leasure event to calendar")
        return super().add_event_to_calendar(calendar)
