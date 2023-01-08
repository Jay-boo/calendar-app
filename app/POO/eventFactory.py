from abc import ABC, abstractmethod
from datetime import datetime

class EventFactory(ABC):

    @abstractmethod
    def createEvent(self,title:str,desc:str,start_time:datetime,end_time:datetime):
        pass
