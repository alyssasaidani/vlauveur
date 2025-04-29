from DAO.DAOSession import DAOSession

class TrajetDAO:
    @staticmethod
    def get_all_trajets():
        connexion = DAOSession.get_connexion()
        try:
            curseur = connexion.cursor(dictionary=True)

            sql = """
                SELECT 
                    s_depart.nom AS station_depart,
                    s_arrivee.nom AS station_arrivee,
                    t.km_parcourus,
                    TIMESTAMPDIFF(MINUTE, t.date_depart, t.date_retour) AS duree_minutes
                FROM trajet t
                JOIN station s_depart ON t.station_depart = s_depart.id_station
                JOIN station s_arrivee ON t.station_arrivee = s_arrivee.id_station
            """

            curseur.execute(sql)
            resultats = curseur.fetchall()
            return resultats

        except Exception as e:
            raise Exception(f"Erreur lors de la récupération des trajets : {e}")


    @staticmethod
    def get_filtered_trajets(distance_min, date_min):
        connexion = DAOSession.get_connexion()
        try:
            curseur = connexion.cursor(dictionary=True)
            sql = """
                SELECT 
                    s_depart.nom AS station_depart,
                    s_arrivee.nom AS station_arrivee,
                    t.km_parcourus,
                    TIMESTAMPDIFF(MINUTE, t.date_depart, t.date_retour) AS duree_minutes
                FROM trajet t
                JOIN station s_depart ON t.station_depart = s_depart.id_station
                JOIN station s_arrivee ON t.station_arrivee = s_arrivee.id_station
                WHERE t.km_parcourus >= %s AND t.date_depart >= %s
            """
            curseur.execute(sql, (distance_min, date_min))
            resultats = curseur.fetchall()
            return resultats

        except Exception as e:
            raise Exception(f"Erreur lors du filtrage des trajets : {e}")
