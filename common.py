import streamlit as st

title = "Assur'Aimant (a SC™ company)"

def sidebar(logo:bool=True, option:bool=True):
    if logo:
        st.sidebar.image('./Medical_Care_Logo.png')
        st.sidebar.write("## a SC™ company")
        st.sidebar.write("___")
    if option:
        st.sidebar.write("### Options")

def supprimer_derniere_ligne(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    # Vérifier s'il y a des lignes à supprimer
    if len(lignes) > 1:
        if lignes:
            # Supprimer la dernière ligne
            lignes = lignes[:-1]

            # Réécrire le fichier avec le contenu mis à jour
            with open(nom_fichier, 'w') as fichier:
                fichier.writelines(lignes)
