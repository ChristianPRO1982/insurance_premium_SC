import common
import streamlit as st

title = "Une petite histoire"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)

st.write(
"""
### You
Donne moi une petite histoire drôle sur le machin learning...

### ChatGPT
Bien sûr, voici une petite histoire drôle sur le machine learning :

Un jour, un algorithme de machine learning est entré dans un bar. Le barman, intrigué, lui demande : "Hey, pourquoi es-tu ici ?"

L'algorithme répond : "Eh bien, j'ai entendu dire que tu avais un ensemble de données intéressant et que tu avais besoin de quelques prédictions."

Le barman, surpris, demande : "Comment peux-tu faire des prédictions dans un bar ?"

L'algorithme sourit et dit : "Je vais vous le prouver ! Regardez, en fonction des boissons commandées par vos clients, je peux prédire le type de musique qu'ils vont aimer."

Le barman, amusé, dit : "D'accord, montre-moi."

L'algorithme commence : "Si quelqu'un commande un martini, il va aimer la musique classique. Si c'est une bière, il préfère le rock. Pour un verre de vin, c'est du jazz."

Le barman, sceptique, sert un verre de vin à un client et attend la prédiction.

L'algorithme, confiant, déclare : "Ce client va adorer du jazz !"

Le client, après avoir pris une gorgée, dit : "En fait, j'aime le hip-hop."

L'algorithme, embarrassé, s'excuse : "Désolé, je suppose que j'ai besoin de plus de données pour améliorer ma prédiction. Mais au moins, je ne suis pas aussi mauvais que l'algorithme voisin qui essayait de prédire les préférences de danse en fonction des boissons."

Le barman sourit et dit : "Eh bien, c'est ça, l'apprentissage automatique. Toujours en train d'apprendre, même s'il y a parfois quelques fausses notes !"
"""
)