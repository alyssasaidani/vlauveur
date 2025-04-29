class vlauve:
    def __init__(self, reference, type_electrique, statut, date_mise_circulation, km_total, station_id):
        self.reference = reference
        self.type_electrique = type_electrique  # True si électrique, False sinon
        self.statut = statut  # 'disponible', 'en_circulation', 'en_reparation', 'en_panne', 'perdu', 'non_disponible'
        self.date_mise_circulation = date_mise_circulation
        self.km_total = km_total
        self.station_id = station_id #L'identifiant de la station où il est garé (ou None si il est en circulation, par exemple)