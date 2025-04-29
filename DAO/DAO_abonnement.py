from DAO.DAOSession import DAOSession



class AbonnementDAO:
    @staticmethod
    def ajouter_abonnement(id_vlauveur, type_abonnement, type_abonnement_annuel, date_debut, date_fin, duree_jours):
        connexion = DAOSession.get_connexion()
        try:
            curseur = connexion.cursor()
            sql = """
                INSERT INTO abonnement (id_vlauveur, type_abonnement, type_abonnement_annuel, date_debut, date_fin, duree_jours)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            curseur.execute(sql, (
                id_vlauveur,
                type_abonnement,
                type_abonnement_annuel,
                date_debut,
                date_fin,
                duree_jours
            ))
            connexion.commit()

        except Exception as e:
            raise Exception(f"Erreur lors de la création de l'abonnement : {e}")

