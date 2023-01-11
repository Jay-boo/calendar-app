from unittest import TestCase 
from datetime import datetime
from POO.event import Event
from POO.eventSchool import EventSchool
from POO.eventLeasure import EventLeasure
from POO.calendar import Calendar



class testCalendar(TestCase):

    def test_calendar_no_conflict__add_event(self):
        event_1=EventSchool("Cours SQL","Apprentissage des methodes SQL et noSQL",datetime(2023,1,13,9),datetime(2023,1,13,12),105)
        event_2=EventLeasure("cinema","Seance Avatar 2",datetime(2023,1,13,14),datetime(2023,1,13,17),105)
        calendar=Calendar()
        self.assertEquals(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEquals(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])

        # print(calendar.get_events()[0])

    def test_calendar_conflict_addOrNothingStartegy_add_event(self):
        pass

    def test_calendar_conflict_priorityStrategy_add_event(self):
        pass



    
        




