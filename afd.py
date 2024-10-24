import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

def generer_graphe():
    # Récupération des informations fournies par l'utilisateur
    transitions = entree_transitions.get().split(',')
    alphabets = set()
    etats = set()
    for transition in transitions:
        etat1, alphabet, etat2 = transition
        alphabets.add(alphabet)
        etats.add(etat1)
        etats.add(etat2)

    # Création du graphe
    afd = nx.DiGraph()

    # Ajout des nœuds
    for etat in etats:
        afd.add_node(etat)

    # Définition de l'état initial
    etat_initial = entree_initial_state.get()
    afd.add_node(etat_initial, initial=True)

    # Définition des états finaux
    etats_finaux = entree_final_states.get().split(',')
    for etat in etats_finaux:
        afd.add_node(etat, final=True)

    # Ajout des transitions
    for transition in transitions:
        etat1, alphabet, etat2 = transition
        afd.add_edge(etat1, etat2, label=alphabet)

    # Récupération des états initiaux et finaux
    etats_initiaux = [etat for etat, attrs in afd.nodes(data=True) if attrs.get('initial')]
    etats_finaux = [etat for etat, attrs in afd.nodes(data=True) if attrs.get('final')]

    # Affichage du graphe
    pos = nx.spring_layout(afd)  # Layout pour l'affichage
    nx.draw_networkx(afd, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_nodes(afd, pos, nodelist=etats_initiaux, node_color='lightgreen', node_size=500)
    nx.draw_networkx_nodes(afd, pos, nodelist=etats_finaux, node_color='lightpink', node_size=500)
    nx.draw_networkx_edges(afd, pos, edge_color='black', arrows=True)

    # Étiquetage des transitions
    edge_labels = {(u, v): d['label'] for u, v, d in afd.edges(data=True)}
    nx.draw_networkx_edge_labels(afd, pos, edge_labels=edge_labels)

    # Affichage du graphe dans une fenêtre Tkinter
    plt.title("Automate Fini Déterministe (AFD)")
    plt.axis('off')
    plt.show()

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("AFD avec Tkinter")

# Création des widgets de saisie
label_transitions = tk.Label(fenetre, text="Transitions (sous la forme 'étatAlphabetétat', séparées par des virgules):")
label_transitions.pack()
entree_transitions = tk.Entry(fenetre)
entree_transitions.pack()

label_initial_state = tk.Label(fenetre, text="État initial:")
label_initial_state.pack()
entree_initial_state = tk.Entry(fenetre)
entree_initial_state.pack()

label_final_states = tk.Label(fenetre, text="États finaux (séparés par des virgules):")
label_final_states.pack()
entree_final_states = tk.Entry(fenetre)
entree_final_states.pack()

# Bouton pour générer le graphe
bouton_generer = tk.Button(fenetre, text="Générer le graphe", command=generer_graphe)
bouton_generer.pack()

# Démarrage de la boucle Tkinter
fenetre.mainloop()
