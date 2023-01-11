from abc import ABC, abstractmethod
from datetime import datetime
from calendar import Calendar


class addStrategy(ABC):
    @abstractmethod
    def add(self,start_time:datetime,end_time:datetime,calendar:Calendar):
        pass

