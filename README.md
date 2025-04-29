# Vlauve - Gestion de location de vélos

**Vlauve** est une application Python conçue pour gérer un service de location de vélos électriques et classiques.  
Elle permet aux abonnés de louer des vélos, de consulter l'historique de leurs trajets et de générer des factures mensuelles.

---

## Fonctionnalités principales

- **Connexion utilisateur** : Interface simple pour accéder à l'application.
- **Affichage des stations** :
  - Liste complète des stations disponibles avec places totales, électriques et non électriques.
  - Louer un vélo en fonction de la disponibilité.
- **Historique des trajets** :
  - Affichage des trajets effectués (station de départ, arrivée, distance parcourue, durée).
  - Filtrage des trajets par distance minimum et date.
  - Export de l'historique sous format CSV.
- **Facturation** :
  - Génération automatique d'une facture mensuelle pour chaque abonné basée sur ses trajets.
- **Base de données MySQL** :
  - Toutes les données (stations, vélos, trajets, utilisateurs) sont stockées de manière sécurisée.

---

## Technologies utilisées

- **Python 3.13**
- **Tkinter** pour l'interface graphique (GUI)
- **MySQL** pour la base de données
- **SQL** pour la gestion des requêtes
- **Pandas** (optionnel pour exporter en CSV)

---

## Organisation du projet

```
/DAO
    DAO_station.py
    DAO_vlauve.py
    DAO_trajet.py
    ...
/interfaces
    accueil.py
    ecran_stations.py
    ecran_trajets.py
main.py
scriptSQL.sql
```

---

## Comment démarrer ?

1. Cloner le projet.
2. Importer le fichier `scriptSQL.sql` dans votre serveur MySQL pour créer la base de données.
3. Adapter la connexion MySQL dans `DAOSession.py`.
4. Lancer `main.py` pour démarrer l'application.
