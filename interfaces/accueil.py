import tkinter as tk
from tkinter import messagebox



class Accueil(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vlauve")
        self.geometry("400x300")
        self.configure(bg="#90dfe1")

        # Champs de connexion
        self.label_email = tk.Label(self, text="Email :", bg="#90dfe1")
        self.label_email.pack()
        self.entry_email = tk.Entry(self, width=30)
        self.entry_email.pack(pady=5)

        self.label_mdp = tk.Label(self, text="Mot de passe :", bg="#90dfe1")
        self.label_mdp.pack()
        self.entry_mdp = tk.Entry(self, show="*", width=30)
        self.entry_mdp.pack(pady=5)

        self.bouton_connexion = tk.Button(self, text="Connexion", command=self.connexion)
        self.bouton_connexion.pack(pady=10)
        

    def connexion(self):
        email = self.entry_email.get()
        mot_de_passe = self.entry_mdp.get()

        if email and mot_de_passe:
            from interfaces.ecran_stations import EcranStations
            self.withdraw()  # cacher Accueil sans détruire
            app = EcranStations(self) # passer self comme parent
            app.mainloop()
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
