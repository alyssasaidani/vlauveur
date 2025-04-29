import tkinter as tk
from tkinter import messagebox
import datetime

from DAO.DAO_vlauveur import VlauveurDAO
from DAO.DAO_abonnement import AbonnementDAO


class Inscription(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Inscription - Vlauve")
        self.geometry("400x750")
        self.configure(bg="#90dfe1")

        # Titre
        titre = tk.Label(self, text="Créer un compte Vlauve 🚲", font=("Helvetica", 16), bg="#90dfe1")
        titre.pack(pady=10)

        # Champs utilisateur
        self._creer_champ("Prénom :", "prenom")
        self._creer_champ("Nom :", "nom")
        self._creer_champ("Email :", "email")
        self._creer_champ("Mot de passe :", "mot_de_passe", show="*")
        self._creer_champ("Téléphone :", "telephone")
        self._creer_champ("Adresse complète :", "adresse")

        # Type d'abonnement
        self.label_type_abonnement = tk.Label(self, text="Type d'abonnement :", bg="#90dfe1")
        self.label_type_abonnement.pack()

        self.type_abonnement = tk.StringVar()
        self.type_abonnement.set("annuel")

        self.radio_annuel = tk.Radiobutton(self, text="Annuel", variable=self.type_abonnement, value="annuel", command=self.afficher_options_abonnement, bg="#90dfe1")
        self.radio_annuel.pack()

        self.radio_occasionnel = tk.Radiobutton(self, text="Occasionnel", variable=self.type_abonnement, value="occasionnel", command=self.afficher_options_abonnement, bg="#90dfe1")
        self.radio_occasionnel.pack()

        # Sous-options (type annuel ou durée occasionnel)
        self.options_abonnement = tk.Frame(self, bg="#90dfe1")
        self.options_abonnement.pack(pady=5)

        self.sous_option = tk.StringVar()
        self.afficher_options_abonnement()

        # Bouton valider
        self.bouton_valider = tk.Button(self, text="Valider l'inscription", command=self.valider_inscription)
        self.bouton_valider.pack(pady=20)

    def _creer_champ(self, texte, attribut, show=None):
        label = tk.Label(self, text=texte, bg="#90dfe1")
        label.pack()
        entry = tk.Entry(self, width=30, show=show)
        entry.pack(pady=5)
        setattr(self, f"entry_{attribut}", entry)

    def afficher_options_abonnement(self):
        # Nettoyer l'ancienne frame
        for widget in self.options_abonnement.winfo_children():
            widget.destroy()

        if self.type_abonnement.get() == "annuel":
            tk.Label(self.options_abonnement, text="Type d'abonnement annuel :", bg="#90dfe1").pack()
            tk.Radiobutton(self.options_abonnement, text="Classique", variable=self.sous_option, value="classique", bg="#90dfe1").pack()
            tk.Radiobutton(self.options_abonnement, text="Tarif Réduit", variable=self.sous_option, value="tarif_reduit", bg="#90dfe1").pack()
        else:
            tk.Label(self.options_abonnement, text="Durée abonnement :", bg="#90dfe1").pack()
            tk.Radiobutton(self.options_abonnement, text="1 jour", variable=self.sous_option, value="1", bg="#90dfe1").pack()
            tk.Radiobutton(self.options_abonnement, text="7 jours", variable=self.sous_option, value="7", bg="#90dfe1").pack()

    def valider_inscription(self):
        # Récupérer les données
        prenom = self.entry_prenom.get()
        nom = self.entry_nom.get()
        email = self.entry_email.get()
        mot_de_passe = self.entry_mot_de_passe.get()
        telephone = self.entry_telephone.get()
        adresse = self.entry_adresse.get()
        type_abonnement = self.type_abonnement.get()
        sous_type = self.sous_option.get()

        if prenom and nom and email and mot_de_passe and telephone and adresse :
            try:
                # 1. Ajouter le vlauveur
                id_vlauveur = VlauveurDAO.ajouter_vlauveur(
                    prenom=prenom,
                    nom=nom,
                    email=email,
                    mot_de_passe=mot_de_passe,
                    telephone=telephone,
                    adresse=adresse
                )

                # 2. Ajouter son abonnement
                date_debut = datetime.date.today()
                if type_abonnement == "annuel":
                    date_fin = date_debut.replace(year=date_debut.year + 1)
                    duree = 365
                    type_annuel = sous_type
                else:
                    if sous_type == "1":
                        date_fin = date_debut + datetime.timedelta(days=1)
                        duree = 1
                    else:
                        date_fin = date_debut + datetime.timedelta(days=7)
                        duree = 7
                    type_annuel = None  # Aucun type pour un abonnement occasionnel

                AbonnementDAO.ajouter_abonnement(
                    id_vlauveur=id_vlauveur,
                    type_abonnement=type_abonnement,
                    type_abonnement_annuel=type_annuel,
                    date_debut=date_debut,
                    date_fin=date_fin,
                    duree_jours=duree
                )

                messagebox.showinfo("Succès", "Inscription réussie ✅")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {e}")
                print(e)
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = Inscription(root)
    app.mainloop()
