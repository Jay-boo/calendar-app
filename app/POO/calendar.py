
from datetime import datetime
from app.database import Database
from app.POO.event import Event


class Calendar:
    def __init__(self) -> None:
        self.events=[]

    def add_event(self,event:Event):
        event.add_event_to_calendar(self)

    def conflict_time(self,start_time:datetime,end_point:datetime):
        for event in events:
            


    def get_events(self):
        pass

    def remove_event(self,event:Event):
        pass




    #--------------------------------------------
    # update methodes

    def update_time_period_event(self,event:Event,new_start_time:datetime,new_end_time:datetime):
        pass

    def update_title_event(self,event:Event,new_title:str):
        pass

    def update_desc_event(self,event:Event,new_desc:str):
        pass
    

