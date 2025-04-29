from DAO.DAOSession import DAOSession

class StationDAO:
    @staticmethod
    def get_all_stations():
        connexion = DAOSession.get_connexion()
        curseur = connexion.cursor(dictionary=True)
        curseur.execute("SELECT * FROM station")
        stations = curseur.fetchall()
        return stations
