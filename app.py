import tkinter as tk
import subprocess
from tkinter import *

# Création de la fenêtre principale
root = tk.Tk()
window=root
window.geometry("720x480")
window.iconbitmap("image.jpg")
window.config(background='#41B77F')

frame1= Frame(window, bg='#41B77F')
frame2= Frame(window, bg='#41B77F')
# Définition de la fonction pour lancer le premier programme
def program_1():
    subprocess.Popen(["python", "simulateur_AFD.py"])

# Création des deux boutons
label_title= Label(frame1, text="Bienvenue sur mon simulateur d'automate", font=("Arial", 24), bg='#41B77F', fg='white')
label_subtitle= Label(frame2, text="Quel type d'automate souhaiteriez-vous simuler ? ", font=("Arial", 18), bg='#41B77F', fg='white')
button_1 = tk.Button(frame2, text="Automate fini déterministe", font=("Arial", 12), bg='white', fg='#4065A4',command=program_1)
button_2 = tk.Button(frame2, text="Automate non fini déterministe",font=("Arial", 12), bg='white', fg='#4065A4')
""" message_1 = tk.Label(frame, height=3, font=12, text="Automate fini déterliniste")
message_2 = tk.Label(frame, height=3, font=12, text="Automate fini non déterministe")
message_3 = tk.Label(frame, height=3, text="Vous pouvez aussi simuler un automate fini déterministe ici sur SIMULATEUR_AFN,\ncependant ce simulateur n'est pas très performant pour certains AFD") """

# Placement des boutons dans la fenêtre
""" message_1.pack()
message_2.pack() """
label_title.pack()
label_subtitle.pack()
button_1.pack()
button_2.pack()
#message_3.pack()

frame1.pack(expand=YES)
frame2.pack(expand=YES)

# Affichage de la fenêtre
root.mainloop()
