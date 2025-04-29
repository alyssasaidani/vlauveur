from DAO.DAOSession import DAOSession

class VlauveDAO:
    @staticmethod
    def mettre_vlauve_en_circulation(id_vlauve):
        connexion = DAOSession.get_connexion()
        try:
            curseur = connexion.cursor()
            sql = "UPDATE vlauve SET statut = 'en_circulation' WHERE id_vlauve = %s"
            curseur.execute(sql, (id_vlauve,))
            connexion.commit()

        except Exception as e:
            raise Exception(f"Erreur lors de la mise en circulation du vélo : {e}")
from DAO.DAOSession import DAOSession

class VlauveDAO:
    @staticmethod
    def get_velo_disponible_par_station(id_station):
        connexion = DAOSession.get_connexion()
        curseur = connexion.cursor(dictionary=True)
        sql = """
            SELECT * FROM vlauve
            WHERE id_station = %s
            AND statut = 'disponible'
            LIMIT 1
        """
        curseur.execute(sql, (id_station,))
        return curseur.fetchone()

    @staticmethod
    def louer_velo(id_vlauve):
        connexion = DAOSession.get_connexion()
        curseur = connexion.cursor()
        sql = """
            UPDATE vlauve
            SET statut = 'en_circulation'
            WHERE id_vlauve = %s
        """
        curseur.execute(sql, (id_vlauve,))
        connexion.commit()
