

from app.POO.event import Event


class EventLeasure(Event):
    def __init__(self,activity:int) -> None:
        super().__init__()
        self.activity=activity
        self.type="leasure"
