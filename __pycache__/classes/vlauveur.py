from DAO.DAOSession import DAOSession

class VlauveurDAO:
    @staticmethod
    def ajouter_vlauveur(prenom, nom, email, mot_de_passe, telephone, adresse):
        connexion = DAOSession.get_connexion()
        try:
            curseur = connexion.cursor()
            sql = """
                INSERT INTO vlauveur (prenom, nom, email, mot_de_passe, telephone, adresse_rue)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            curseur.execute(sql, (prenom, nom, email, mot_de_passe, telephone, adresse))
            connexion.commit()
            return curseur.lastrowid  # Retourne l'ID du vlauveur inséré

        except Exception as e:
            raise Exception(f"Erreur lors de la création du vlauveur : {e}")
