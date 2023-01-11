
from datetime import datetime , timedelta


class Reminder:

    def __init__(self,time_before_event:timedelta=timedelta(minutes=5)):
        self.time_before_event=time_before_event
