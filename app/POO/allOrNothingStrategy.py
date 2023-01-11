from datetime import datetime
from app.POO.addStrategy import addStrategy
from app.POO.calendar import Calendar


class allOrNothingStrategy(addStrategy):

    def add(self,start_time:datetime,end_time:datetime,calendar:Calendar):
        
        for event in calendar.events:
            if event.is_in_time_terminal(start_time,end_time):
                print(f"event not added cause other evenement is scheduled : ${event.title}")
                return None 
        return [start_time,end_time]
    
    


