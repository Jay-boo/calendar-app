from datetime import datetime
from app.POO.calendar import Calendar
from app.POO.event import Event


class EventSchool(Event):
    def __init__(self,title:str,desc:str,start_time:datetime,end_time:datetime,id_salle:int) -> None:
        super().__init__(title,desc,start_time,end_time)
        self.id_salle=id_salle
        self.type="school"
        self.strategy=

    def add_event_to_calendar(self,calendar:Calendar):
        # Si le creneau est libre rien de spécial, si ca ne l'est pas les évent scolaire garde 
        # la priorité sur les events sportif
        print("adding School event to calendar")

        return super().add_event_to_calendar(calendar)

