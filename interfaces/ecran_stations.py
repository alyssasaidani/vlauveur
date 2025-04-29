import tkinter as tk
from tkinter import messagebox, ttk
from DAO.DAO_station import StationDAO
from DAO.DAO_vlauve import VlauveDAO  # DAO pour gérer les vélos
from interfaces.ecran_trajets import EcranTrajets  # Import du bon écran


class EcranStations(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Stations disponibles - Vlauve")
        self.geometry("800x600")
        self.configure(bg="#90dfe1")

        # Titre
        titre = tk.Label(self, text="Liste des Stations 🚲", font=("Helvetica", 18), bg="#90dfe1")
        titre.pack(pady=10)

        # Tableau Treeview
        colonnes = ("Nom", "Places Totales", "Places Electriques", "Places Non Electriques")
        self.tree = ttk.Treeview(self, columns=colonnes, show="headings")

        for col in colonnes:
            self.tree.heading(col, text=col)

        self.tree.pack(expand=True, fill="both", padx=20, pady=20)

        # Bouton Louer un vélo
        bouton_louer = tk.Button(self, text="Louer un vélo", command=self.louer_velo)
        bouton_louer.pack(pady=10)

        # Ajoute un bouton dans ton interface
        self.bouton_trajets = tk.Button(self, text="Voir mes trajets", command=self.ouvrir_trajets)
        self.bouton_trajets.pack(pady=10)




        # Charger les stations
        self.charger_stations()
    def ouvrir_trajets(self):
       EcranTrajets(self)

    def charger_stations(self):
        self.tree.delete(*self.tree.get_children())
        stations = StationDAO.get_all_stations()
 

        for station in stations:
            self.tree.insert("", tk.END, values=(station['nom'], station['places_total'], station['places_electriques'], station['places_non_electriques']), iid=station['id_station'])

    def louer_velo(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner une station.")
            return

        id_station = int(selection[0])

        # Chercher un vélo disponible
        velo = VlauveDAO.get_velo_disponible_par_station(id_station)

        if velo:
            # Mettre à jour le vélo (en circulation)
            VlauveDAO.louer_velo(velo['id_vlauve'])
            messagebox.showinfo("Succès", f"Vélo {velo['reference_reseau']} loué avec succès 🚲 !")
        else:
            messagebox.showerror("Erreur", "Aucun vélo disponible dans cette station.")
