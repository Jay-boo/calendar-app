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
        self.assertEqual(len(calendar.get_events()), 0)
        calendar.add_event(event_1)
        self.assertEqual(len(calendar.get_events()), 1)
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()), 2)
        self.assertEqual(event_1,calendar.get_events()[0])
        self.assertEqual(event_2,calendar.get_events()[1])

        # print(calendar.get_events()[0])

    def test_calendar_conflict_addOrNothingStartegy_add_event(self):
        event_1=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )
        # Event Leasure has a allOrNothingStartegy
        calendar=Calendar()
        calendar.add_event(event_1)

        #---------------------
        #Cas 1
        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,8),
                datetime(2023,1,13,13),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),1)#L'event2 ne doit pas avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),False)

        #---------------------
        #Cas 2
        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,10),
                datetime(2023,1,13,13),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),1)#L'event2 ne doit pas avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),False)

        #---------------------
        #Cas 3
        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,8),
                datetime(2023,1,13,11),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),1)#L'event2 ne doit pas avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),False)

        #---------------------
        #Cas 4
        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,10),
                datetime(2023,1,13,11),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),1)#L'event2 ne doit pas avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),False)

        #---------------------
        #Cas 5
        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,7),
                datetime(2023,1,13,9),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),2)#L'event2 doit avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),True)

        event_2=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,12),
                datetime(2023,1,13,14),
                105
        )
        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),3)#L'event2 doit avoir ete ajouté
        self.assertEqual(calendar.get_events().__contains__(event_2),True)






    def test_calendar_conflict_priorityStrategy_add_event(self):
        event_1=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )
        # Event School has a allOrNothingStartegy
        calendar=Calendar()
        calendar.add_event(event_1)

        #---------------------
        #Cas 1
        print("----------------priority case 1")
        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,8),
                datetime(2023,1,13,13),
                105
        )

        
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),1)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 n'existe plus
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),False)

        calendar.remove_event(event_2)

        #---------------------
        #Cas 2
        print("----------------priority case 2")
        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,10),
                datetime(2023,1,13,13),
                105
        )

        calendar.add_event((event_1))
        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),2)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 soit desormais un evenement allant de 9h a 10h
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),True)
        self.assertEqual(event_2.start_time,datetime(2023,1,13,10))
        self.assertEqual(event_2.end_time,datetime(2023,1,13,13))
        self.assertEqual(event_1.start_time,datetime(2023,1,13,9))
        self.assertEqual(event_1.end_time,datetime(2023,1,13,10))



        #---------------------
        #Cas 3
        print("----------------priority case 3")
        event_1=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )
        calendar=Calendar()
        calendar.add_event(event_1)
        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,8),
                datetime(2023,1,13,11),
                105
        )

        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),2)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 soit desormais un evenement allant de 9h a 10h
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),True)
        self.assertEqual(event_2.start_time,datetime(2023,1,13,8))
        self.assertEqual(event_2.end_time,datetime(2023,1,13,11))
        self.assertEqual(event_1.start_time,datetime(2023,1,13,11))
        self.assertEqual(event_1.end_time,datetime(2023,1,13,12))

        #---------------------
        #Cas 4
        print("----------------priority case 4")
        event_1=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )
        calendar=Calendar()
        calendar.add_event(event_1)
        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,10),
                datetime(2023,1,13,11),
                105
        )

        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),3)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 soit desormais un evenement allant de 9h a 10h
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),True)
        self.assertEqual(event_2.start_time,datetime(2023,1,13,10))
        self.assertEqual(event_2.end_time,datetime(2023,1,13,11))
        self.assertEqual(event_1.start_time,datetime(2023,1,13,9))
        self.assertEqual(event_1.end_time,datetime(2023,1,13,10))

        #---------------------
        #Cas 5
        print("----------------priority case 5")
        event_1=EventLeasure(
                "cinema",
                "Seance Avatar 2",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )
        calendar=Calendar()
        calendar.add_event(event_1)
        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,7),
                datetime(2023,1,13,9),
                105
        )

        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),2)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 soit desormais un evenement allant de 9h a 10h
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),True)
        self.assertEqual(event_2.start_time,datetime(2023,1,13,7))
        self.assertEqual(event_2.end_time,datetime(2023,1,13,9))
        self.assertEqual(event_1.start_time,datetime(2023,1,13,9))
        self.assertEqual(event_1.end_time,datetime(2023,1,13,12))

        event_2=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,12),
                datetime(2023,1,13,14),
                105
        )

        calendar.add_event(event_2)
        self.assertEqual(len(calendar.get_events()),3)
        # L'event 2 doit etre ajouter de tel sorte que l'evenement 1 soit desormais un evenement allant de 9h a 10h
        self.assertEqual(calendar.get_events().__contains__(event_2),True)
        self.assertEqual(calendar.get_events().__contains__(event_1),True)
        self.assertEqual(event_2.start_time,datetime(2023,1,13,12))
        self.assertEqual(event_2.end_time,datetime(2023,1,13,14))
        self.assertEqual(event_1.start_time,datetime(2023,1,13,9))
        self.assertEqual(event_1.end_time,datetime(2023,1,13,12))

    



    
        




