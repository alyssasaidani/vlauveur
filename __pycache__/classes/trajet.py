class Trajet:
    def __init__(self, id, velo_id, utilisateur_id, station_depart_id, station_arrivee_id, km, date_depart, date_retour):
        self.id = id
        self.velo_id = velo_id #Quel vélo a été utilisé
        self.utilisateur_id = utilisateur_id #Qui a fait le trajet
        self.station_depart_id = station_depart_id
        self.station_arrivee_id = station_arrivee_id
        self.km = km
        self.date_depart = date_depart
        self.date_retour = date_retour
