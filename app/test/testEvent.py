
from unittest import TestCase 
from datetime import datetime, timedelta
from POO.eventSchool import EventSchool
from POO.eventLeasure import EventLeasure

class TestEvent(TestCase):

    def test_is_in_time_interval(self):
        """
        test_is_in_time_interval test la fonction is_in_time_intervall
        On s 'attend a ce que cette fonction renvoie True des lors que l'event appartient au time_intervalle

        Lorsque notre evenement se temrine à la meme heure que l'intervalle de temps commencve on s'attend a se ce l'on nous retourne False
        Lorsque notre evenement se commence à la meme heure que l'intervalle de temps se termine on s'attend a se ce l'on nous retourne False



        """
        now=datetime.now()
        event=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                now+timedelta(hours=3),
                now+timedelta(hours=6),
                105
        )

        #  l'event est strictment après l'interval:False
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=1),now+timedelta(hours=3)),False
        )
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=1),now+timedelta(hours=2)),False
        )

        #L'event est strictment avant l'interval : False
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=6),now+timedelta(hours=7)),False
        )
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=7),now+timedelta(hours=8)),False
        )

        # L'event commence avant l'interval mais fini dans l'interval : True
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=5),now+timedelta(hours=7)),True 
        )


        # L'event commence durant l'interval mais fini après l'interval : True
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=2),now+timedelta(hours=5)),True 
        )



        # L'event commence et termine au cours de l'interval
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=2),now+timedelta(hours=7)),True 
        )

        #L'event commence avant l'interval et se termine après
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=4),now+timedelta(hours=5)),True 
        )

        #L'event ==interval
        self.assertEqual(
            event.is_in_time_interval(now+timedelta(hours=3),now+timedelta(hours=6)),True 
        )

