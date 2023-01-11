from datetime import datetime
from app.POO.eventLeasure import EventLeasure
from app.POO.eventSchool import EventSchool
from app.POO.addStrategy import addStrategy
from app.POO.calendar import Calendar

class priorityStrategy(addStrategy):

    def add(self,start_time:datetime,end_time:datetime,calendar:Calendar):
        for event in calendar.events:
            if event.is_in_time_terminal(start_time,end_time):

                if(event.start_time<start_time and event.end_time > end_time):
                    #On coupe l'event en 2
                    event.end_time =start_time
                    if event.type=="school":
                        new_event=EventSchool(event.title,event.desc,end_time,event.end_time,event.id_salle)

                    else:
                        new_event=EventLeasure(event.title,event.desc,end_time,event.end_time,event.activity)
                    calendar.add_event(new_event)
                    #Normallement y'aura pas de conflict


                elif event.start_time<start_time and event.end_time < end_time: 
                    event.end_time = start_time

                elif event.start_time> start_time and event.end_time <end_time:
                    calendar.remove_event(event)

                elif event.start_time> start_time and event.end_time >end_time:
                    event.start_time=end_time

        return [start_time,end_time]
        
    
    


