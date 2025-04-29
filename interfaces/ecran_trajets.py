import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from DAO.DAO_trajet import TrajetDAO

class EcranTrajets(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Historique des Trajets - Vlauve")
        self.geometry("800x600")
        self.configure(bg="#e1f5fe")

        # Titre
        titre = tk.Label(self, text="Historique des Trajets 🚲", font=("Helvetica", 18), bg="#e1f5fe")
        titre.pack(pady=10)

        # Tableau Treeview
        self.tree = ttk.Treeview(self, columns=("depart", "arrivee", "distance", "duree"), show="headings")
        self.tree.heading("depart", text="Station Départ")
        self.tree.heading("arrivee", text="Station Arrivée")
        self.tree.heading("distance", text="Distance (km)")
        self.tree.heading("duree", text="Durée (minutes)")
        self.tree.pack(expand=True, fill="both", pady=20)

        # Champs de filtre
        frame_filtre = tk.Frame(self, bg="#e1f5fe")
        frame_filtre.pack(pady=5)

        label_distance = tk.Label(frame_filtre, text="Distance minimum (km):", bg="#e1f5fe")
        label_distance.grid(row=0, column=0, padx=5)
        self.entry_distance = tk.Entry(frame_filtre)
        self.entry_distance.grid(row=0, column=1, padx=5)

        label_date = tk.Label(frame_filtre, text="Date après (AAAA-MM-JJ):", bg="#e1f5fe")
        label_date.grid(row=1, column=0, padx=5)
        self.entry_date = tk.Entry(frame_filtre)
        self.entry_date.grid(row=1, column=1, padx=5)

        # Boutons
        bouton_frame = tk.Frame(self, bg="#e1f5fe")
        bouton_frame.pack(pady=10)

        self.bouton_filtrer = tk.Button(bouton_frame, text="Filtrer", command=self.filtrer_trajets)
        self.bouton_filtrer.grid(row=0, column=0, padx=10)

        self.bouton_exporter = tk.Button(bouton_frame, text="Exporter CSV", command=self.exporter_csv)
        self.bouton_exporter.grid(row=0, column=1, padx=10)

        # Charger les trajets au démarrage
        self.charger_trajets()

    def charger_trajets(self):
        self.tree.delete(*self.tree.get_children())
        trajets = TrajetDAO.get_all_trajets()
        for trajet in trajets:
            self.tree.insert("", "end", values=(
                trajet["station_depart"],
                trajet["station_arrivee"],
                trajet["km_parcourus"],
                trajet["duree_minutes"]
            ))

    def filtrer_trajets(self):
        distance_min = self.entry_distance.get()
        date_min = self.entry_date.get()

        try:
            trajets = TrajetDAO.get_filtered_trajets(distance_min, date_min)
            self.tree.delete(*self.tree.get_children())

            if not trajets:
                messagebox.showinfo("Info", "Aucun trajet trouvé pour ces critères.")
                return

            for trajet in trajets:
                self.tree.insert("", "end", values=(
                    trajet["station_depart"],
                    trajet["station_arrivee"],
                    trajet["km_parcourus"],
                    trajet["duree_minutes"]
                ))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def exporter_csv(self):
        try:
            fichier = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("Fichiers CSV", "*.csv")],
                title="Enregistrer le fichier CSV"
            )
            if not fichier:
                return

            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                # En-têtes
                writer.writerow(["Station Départ", "Station Arrivée", "Distance (km)", "Durée (minutes)"])

                # Lignes
                for ligne in self.tree.get_children():
                    valeurs = self.tree.item(ligne)["values"]
                    writer.writerow(valeurs)

            messagebox.showinfo("Succès", f"Exportation réussie vers :\n{fichier}")

        except Exception as e:
            messagebox.showerror("Erreur", str(e))
