import mysql.connector

class DAOSession:
    __connexion = None

    @staticmethod
    def get_connexion():
        if DAOSession.__connexion is None:
            DAOSession.__connexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vlauve2"
            )
        return DAOSession.__connexion

    @staticmethod
    def close():
        if DAOSession.__connexion is not None:
            DAOSession.__connexion.close()
            DAOSession.__connexion = None
