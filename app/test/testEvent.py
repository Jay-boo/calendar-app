
from unittest import TestCase 
from datetime import datetime
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
        event=EventSchool(
                "Cours SQL",
                "Apprentissage des methodes SQL et noSQL",
                datetime(2023,1,13,9),
                datetime(2023,1,13,12),
                105
        )

        # Le début et la fin de l'evement sont tout les deux en dehors de l'intervalle 
        # avec event_start > intervalle_end   
        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13,14),datetime(2023,1,13,17)),False
        )

        # Le début de l'evement  est dans l'intervalle mais pas la fin²
        # avec intervall_start<event_start < intervalle_end   &intervall_end < event_end 
        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13,11),datetime(2023,1,13,17)),True
        )

        # Inversement
        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13,8),datetime(2023,1,13,11)),True
        )


        # Le début et la fin de l'evement sont tout les deux en dehors de l'intervalle 
        # avec event_start < intervalle_start   & event_end > intervalle_end
        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13, 8),datetime(2023,1,13,17)),True
        )

        # Le début et la fin de l'evement sont tout les deux dans l'intervalle 
        # avec event_start > intervalle_start   & event_end < intervalle_end
        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13, 10),datetime(2023,1,13,11)),True
        )

        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13,8),datetime(2023,1,13,9)),False
        )

        self.assertEqual(
            event.is_in_time_interval(datetime(2023,1,13,12),datetime(2023,1,13,14)),False
        )



