class Station:#on cree une class appelee station
    def __init__(self, id, nom, adresse, capacite_elec, capacite_non_elec, reseau_id):# on cree une methode _init_ elle est appelee automatiquement quand on cree une station c comme un constructeur en lui donnant ses premieres valeurs
        self.id = id #ça veut dire qu’on assigne la valeur de la variable id à l’attribut id de l’objet courant (self).
        self.nom = nom
        self.adresse = adresse  # sous forme "GPS / Rue / Numéro"
        self.capacite_elec = capacite_elec
        self.capacite_non_elec = capacite_non_elec
        self.reseau_id = reseau_id
