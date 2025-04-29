CREATE TABLE Reseau (
    id_reseau INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    annee_mise_en_place INT,
    ville_nom VARCHAR(100),
    ville_code_postal VARCHAR(10)
);

CREATE TABLE Station (
    id_station INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    nom VARCHAR(100),
    adresse VARCHAR(255),
    places_total INT,
    places_electriques INT,
    places_non_electriques INT,
    vlauves_electriques_disponibles INT,
    vlauves_non_electriques_disponibles INT,
    id_reseau INT,
    FOREIGN KEY (id_reseau) REFERENCES Reseau(id_reseau)
);

CREATE TABLE Vlauveur (
    id_vlauveur INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    telephone VARCHAR(20),
    adresse_rue VARCHAR(255),
    adresse_numero VARCHAR(10),
    code_postal VARCHAR(10),
    ville VARCHAR(100),
    numero_carte_identite VARCHAR(50),
    montant_garantie DECIMAL(10,2)
);

CREATE TABLE Vlauve (
    id_vlauve INT AUTO_INCREMENT PRIMARY KEY,
    reference_reseau VARCHAR(50) NOT NULL,
    electrique BOOLEAN NOT NULL,
    niveau_batterie INT,
    date_mise_en_circulation DATE,
    total_km_parcourus FLOAT,
    statut ENUM('disponible', 'en_circulation', 'en_reparation', 'en_panne', 'perdu', 'non_disponible') NOT NULL,
    id_station INT,
    FOREIGN KEY (id_station) REFERENCES Station(id_station)
);

CREATE TABLE Trajet (
    id_trajet INT AUTO_INCREMENT PRIMARY KEY,
    id_vlauveur INT,
    id_vlauve INT,
    station_depart INT,
    station_arrivee INT,
    km_parcourus FLOAT,
    date_depart DATE,
    date_retour DATE,
    FOREIGN KEY (id_vlauveur) REFERENCES Vlauveur(id_vlauveur),
    FOREIGN KEY (id_vlauve) REFERENCES Vlauve(id_vlauve),
    FOREIGN KEY (station_depart) REFERENCES Station(id_station),
    FOREIGN KEY (station_arrivee) REFERENCES Station(id_station)
);

CREATE TABLE Facture (
    id_facture INT AUTO_INCREMENT PRIMARY KEY,
    id_vlauveur INT,
    date_facture DATE,
    montant_total DECIMAL,
    FOREIGN KEY (id_vlauveur) REFERENCES Vlauveur(id_vlauveur)
);

CREATE TABLE Paiement (
    id_paiement INT AUTO_INCREMENT PRIMARY KEY,
    id_facture INT,
    date_paiement DATE,
    montant DECIMAL,
    FOREIGN KEY (id_facture) REFERENCES Facture(id_facture)
);

CREATE TABLE Abonnement (
    id_abonnement INT AUTO_INCREMENT PRIMARY KEY,
    id_vlauveur INT,
    type_abonnement ENUM('annuel', 'occasionnel') NOT NULL,
    type_abonnement_annuel ENUM('classique', 'tarif_reduit'),
    date_debut DATE,
    date_fin DATE,
    duree_jours INT,
    FOREIGN KEY (id_vlauveur) REFERENCES Vlauveur(id_vlauveur)
);
