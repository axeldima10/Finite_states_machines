import subprocess
from tkinter import *


#créer la fenêtre 
window = Tk()
window.title("Simulateur d'automtes")
window.geometry("720x480")
window.iconbitmap("image.ico")
window.config(background='#4065A4')
 
def program_main():
    subprocess.Popen(["python", "app.py"])
    window.destroy()

frame= Frame(window, bg='#4065A4')
label_title= Label(frame, text="Bienvenue sur l'application", font=("Arial", 30), bg='#4065A4', fg='white')
label_title.pack()

#ajouter bouton 
btn_main=Button(frame, text="Ouvrir l'application", font=("Arial", 30), bg='white', fg='#4065A4', command=program_main)
btn_main.pack(pady=25, fill=X)

""" #création d'images
width= 300
height= 300
image = PhotoImage( file="image.jpg").zoom(35).subsample(32)

#création d'espace pour dessiner des composants graphiques 
canvas =  Canvas(window, width=width, height=height, bg='#4065A4')
canvas.create_image(width/2, height/2 , image = image)
canvas.pack(expand=YES) """
frame.pack(expand=YES)

#Afficher la fenêtre 
window.mainloop()