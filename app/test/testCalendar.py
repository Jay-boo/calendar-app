from unittest import TestCase 
from datetime import datetime, timedelta
from POO.event import Event
from POO.eventSchool import EventSchool
from POO.eventLeasure import EventLeasure
from POO.calendar import Calendar


now=datetime.now()

event_1_interval=[now+timedelta(hours=3),now+timedelta(hours=6)]
add_configs={
        'noConflictBefore':[now+timedelta(hours=1),now+timedelta(hours=3)],
        'noConflictBeforeBis':[now+timedelta(hours=1),now+timedelta(hours=2)],
        'noConflictAfter':[now+timedelta(hours=6),now+timedelta(hours=7)],
        'noConflictAfterBis':[now+timedelta(hours=7),now+timedelta(hours=8)],
        'event1StartBeforeEndIn':[now+timedelta(hours=5),now+timedelta(hours=7)],
        'event1StartInEndAfter':[now+timedelta(hours=2),now+timedelta(hours=5)],
        'event1StartInEndIn':[now+timedelta(hours=2),now+timedelta(hours=7)],
        'event1StartBeforeEndAfter':[now+timedelta(hours=4),now+timedelta(hours=5)],
        'event1Isevent2':[now+timedelta(hours=3),now+timedelta(hours=6)]

}

excepted_outputs_allOrNothingStrategy={
        'noConflictBefore':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True},
        'noConflictBeforeBis':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True},
        'noConflictAfter':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True},
        'noConflictAfterBis':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True},
        'event1StartBeforeEndIn':{'len_calendar':1,'contain_event_1':True,'contain_event_2':False},
        'event1StartInEndAfter':{'len_calendar':1,'contain_event_1':True,'contain_event_2':False},
        'event1StartInEndIn':{'len_calendar':1,'contain_event_1':True,'contain_event_2':False},
        'event1StartBeforeEndAfter':{'len_calendar':1,'contain_event_1':True,'contain_event_2':False},
        'event1Isevent2':{'len_calendar':1,'contain_event_1':True,'contain_event_2':False}
        }



excepted_outputs_priorityStrategy={
        'noConflictBefore':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True,'start_time_event_1':event_1_interval[0],'end_time_event_1':event_1_interval[1]},
        'noConflictBeforeBis':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True,'start_time_event_1':event_1_interval[0],'end_time_event_1':event_1_interval[1]},
        'noConflictAfter':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True,'start_time_event_1':event_1_interval[0],'end_time_event_1':event_1_interval[1]},
        'noConflictAfterBis':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True,'start_time_event_1':event_1_interval[0],'end_time_event_1':event_1_interval[1]},
        'event1StartBeforeEndIn':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True ,'start_time_event_1':event_1_interval[0],'end_time_event_1':add_configs['event1StartBeforeEndIn'][0]},
        'event1StartInEndAfter':{'len_calendar':2,'contain_event_1':True,'contain_event_2':True ,'start_time_event_1':add_configs['event1StartInEndAfter'][1],'end_time_event_1':event_1_interval[1]},
        'event1StartInEndIn':{'len_calendar':1,'contain_event_1':False,'contain_event_2':True},
        'event1StartBeforeEndAfter':{'len_calendar':3,'contain_event_1':True,'contain_event_2':True ,'start_time_event_1':event_1_interval[0],'end_time_event_1':add_configs['event1StartBeforeEndAfter'][0]},
        'event1Isevent2':{'len_calendar':1,'contain_event_1':False,'contain_event_2':True}
        }

class testCalendar(TestCase):

    def test_calendar_no_conflict__add_event(self):
        event_1=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                event_1_interval[0],
                event_1_interval[1],
                105
        )

        event_2=EventLeasure("Seance de cinema",
                             "Seance Avatar 2",
                             add_configs['noConflictBefore'][0],
                             add_configs['noConflictBefore'][1],
                             "cinéma"
        )
        calendar=Calendar()
        self.assertEqual(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEqual(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])
        
        calendar.remove_event(event_2)

        event_2=EventLeasure("Seance de cinema",
                             "Seance Avatar 2",
                             add_configs['noConflictBeforeBis'][0],
                             add_configs['noConflictBeforeBis'][1],
                             "cinéma"
        )
        calendar=Calendar()
        self.assertEqual(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEqual(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])

        calendar.remove_event(event_2)

        event_2=EventLeasure("Seance de cinema",
                             "Seance Avatar 2",
                             add_configs['noConflictAfter'][0],
                             add_configs['noConflictAfter'][1],
                             "cinéma"
        )
        calendar=Calendar()
        self.assertEqual(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEqual(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])

        calendar.remove_event(event_2)

        event_2=EventLeasure("Seance de cinema",
                             "Seance Avatar 2",
                             add_configs['noConflictAfterBis'][0],
                             add_configs['noConflictAfterBis'][1],
                             "cinéma"
        )
        calendar=Calendar()
        self.assertEqual(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEqual(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])
        print("end basic test ---------------------")







    def test_calendar_conflict_addOrNothingStartegy_add_event(self):
    
        event_1=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                event_1_interval[0],
                event_1_interval[1],
                105
        )



        for config,event_2_interval in add_configs.items():
            # Event Leasure has a allOrNothingStartegy
            calendar=Calendar()
            calendar.add_event(event_1)
            event_2=EventLeasure(
                    "Seance de cinema",
                    "Seance Avatar 2",
                    event_2_interval[0],
                    event_2_interval[1],
                    "cinéma"
            )
        
            calendar.add_event(event_2)
            self.assertEqual(len(calendar.get_events()),excepted_outputs_allOrNothingStrategy[config]['len_calendar'])
            self.assertEqual(calendar.get_events().__contains__(event_1),excepted_outputs_allOrNothingStrategy[config]['contain_event_1'])
            self.assertEqual(calendar.get_events().__contains__(event_2),excepted_outputs_allOrNothingStrategy[config]['contain_event_2'])





    def test_calendar_conflict_priorityStrategy_add_event(self):
        print("--------------------------------")
        print("TEST PRIORITY STRATEGY-----------------------------")

        for config,event_2_interval in add_configs.items():
            print(f"----------{config}")
            # Event School has a priorityStartegy
            calendar=Calendar()
            event_1=EventSchool(
                    "Cours SQL",
                    "Apprentissage des methodes SQL et noSQL",
                    event_1_interval[0],
                    event_1_interval[1],
                    105
            )
            calendar.add_event(event_1)
            event_2=EventSchool(
                    "Cours ML",
                    "Apprentissage supervisé",
                    event_2_interval[0],
                    event_2_interval[1],
                    105
            )
        
            calendar.add_event(event_2)
            if config=="event1StartInEndAfter":
                print(calendar)
            self.assertEqual(len(calendar.get_events()),excepted_outputs_priorityStrategy[config]['len_calendar'])
            self.assertEqual(calendar.get_events().__contains__(event_1),excepted_outputs_priorityStrategy[config]['contain_event_1'])
            self.assertEqual(calendar.get_events().__contains__(event_2),excepted_outputs_priorityStrategy[config]['contain_event_2'])
            if excepted_outputs_priorityStrategy[config]['contain_event_1']:
                self.assertEqual(excepted_outputs_priorityStrategy[config]["start_time_event_1"],event_1.start_time)
                self.assertEqual(excepted_outputs_priorityStrategy[config]["end_time_event_1"],event_1.end_time)
            print(f"---end-------{config}")
                

