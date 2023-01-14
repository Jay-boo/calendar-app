from datetime import datetime
from POO.addStrategy import addStrategy
from POO.calendar import Calendar


class allOrNothingStrategy(addStrategy):

    def add(self,start_time:datetime,end_time:datetime,calendar:Calendar):
        
        for event in calendar.get_events():
            if event.is_in_time_interval(start_time,end_time):
                print(f"event not added cause other evenement is scheduled : {event.title}")
                return None 
        print("event added using addOrNothingStrategy")
        return [start_time,end_time]
    
    


