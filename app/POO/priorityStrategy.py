from datetime import datetime
from POO.addStrategy import addStrategy
from POO.calendar import Calendar
from copy import copy

class priorityStrategy(addStrategy):

    def add(self,start_time:datetime,end_time:datetime,calendar:Calendar):
        """
        Retourne les start_time et end_time effectif de l'event. 
        Il est possible que l'event se retrouve découper commme deux evenements. 
        """
        for event in calendar.get_events():
            if event.is_in_time_interval(start_time,end_time):

                if(event.start_time<start_time and event.end_time > end_time):
                    print("event couper en 2")
                    #On coupe l'event en 2
                    # event_bis=event
                    event_bis=copy(event)
                    start_time_bis=end_time
                    end_time_bis=event.end_time
                    event.end_time =start_time
                    event_bis.start_time=start_time_bis
                    event_bis.end_time=end_time_bis
                    calendar.add_event(event_bis)
                    
                    



                elif event.start_time<start_time and event.end_time <= end_time: 
                    event.end_time = start_time

                elif event.start_time>= start_time and event.end_time <=end_time:
                    calendar.remove_event(event)

                elif event.start_time>=start_time and event.end_time >end_time:
                    event.start_time=end_time
        print("event added using priorityStartegy")
        return [start_time,end_time]
        
    
    


