
from app.POO.event import Event


class EventSchool(Event):
    def __init__(self,id_salle:int) -> None:
        super().__init__()
        self.id_salle=id_salle
        self.type="school"

