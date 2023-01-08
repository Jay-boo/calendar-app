from asyncio.locks import Event

from click.types import datetime


class Calendar:
    def __init__(self) -> None:
        self.events=[]

    def get_events(self):
        pass

    def remove_event(self,event:Event):
        pass

    def add_event(self,event:Event):
        pass



    #--------------------------------------------
    # update methodes

    def update_time_period_event(self,event:Event,new_start_time:datetime,new_end_time:datetime):
        pass

    def update_title_event(self,event:Event,new_title:str):
        pass

    def update_desc_event(self,event:Event,new_desc:str):
        pass
    

