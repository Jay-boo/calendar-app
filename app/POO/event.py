from abc import ABC, abstractmethod
from datetime import datetime,date


class Event(ABC):
    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime) -> None:
        self.id=0
        self.title=title
        self.created_at=date.today()
        self.updated_at=None
        self.desc=desc
        self.start_time=start_time
        self.end_time=end_time
        self.type=None


    def change_time_period(start_time:datetime,end_time:datetime):
        pass


