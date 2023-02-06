from POO.event import Event
from POO.eventLeasure import EventLeasure
from POO.eventSchool import EventSchool



def transfrom_with_strat(evn:Event,type,property):
        if type.lower() == "leasure":
            return EventLeasure(
            title=evn.title,
            desc=evn.desc,
            start_time=evn.start_time,
            end_time=evn.end_time,
            activity=property
            )
        elif type.lower() == "school":
            return EventSchool(
            title=evn.title,
            desc=evn.desc,
            start_time=evn.start_time,
            end_time=evn.end_time,
            id_salle=property
            )
        else:
            return False