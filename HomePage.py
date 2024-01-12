import common
import streamlit as st

st.set_page_config(page_title=common.title, page_icon="favicon.ico", layout="wide")
common.sidebar(option=False)


st.write(
"""___
## Bienvenue chez Assur'Aimant - Votre Bouclier Financier Compétitif!
Chez Assur'Aimant, nous croyons que la tranquillité d'esprit ne devrait pas être un luxe inaccessible. C'est pourquoi nous nous engageons à vous offrir une protection financière exceptionnelle à des prix qui ne pèsent pas sur votre budget. Nous sommes fiers de présenter une nouvelle ère dans le monde de l'assurance - une ère où la qualité et l'accessibilité se rencontrent harmonieusement.
___
### Pourquoi choisir Assur'Aimant?
""")

col1, col2 = st.columns(2)

col1.write("""
🌟 Prix Compétitifs Imbattables: Notre engagement envers des tarifs compétitifs défie les normes de l'industrie. Chez Assur'Aimant, nous comprenons l'importance de maximiser votre budget sans compromettre la qualité de votre protection.

🤝 Service Personnalisé: Nous ne traitons pas simplement des polices d'assurance; nous construisons des relations. Notre équipe dévouée est là pour vous guider à chaque étape du processus, répondre à vos questions et personnaliser une solution qui répond à vos besoins uniques.

🔒 Protection Complète: Assur'Aimant offre une gamme complète de produits d'assurance pour vous protéger, que ce soit pour votre voiture, votre maison, votre santé ou d'autres besoins spécifiques. Vous pouvez compter sur nous pour être votre bouclier financier à chaque étape de la vie.
""")

col2.write("""
🌐 Innovation Technologique: Nous sommes à la pointe de la technologie pour rendre le processus d'assurance plus simple, plus rapide et plus transparent. Découvrez une nouvelle façon de gérer vos polices avec notre plateforme en ligne intuitive.

✨ Confiance et Intégrité: Chez Assur'Aimant, la confiance et l'intégrité sont les piliers de notre entreprise. Nous sommes fiers de bâtir une relation de confiance avec nos clients en offrant des services honnêtes, transparents et dignes de confiance.

Faites le choix judicieux pour votre avenir financier. Rejoignez la famille Assur'Aimant aujourd'hui et bénéficiez de la protection dont vous avez besoin à un prix qui vous fera sourire. Parce que chez Assur'Aimant, nous aimons vous voir protégé sans vous ruiner.
""")

st.session_state['age'] = 25
st.session_state['height'] = 170
st.session_state['weight'] = 70
st.session_state['sex'] = 0
st.session_state['smoker'] = 0
st.session_state['children'] = 0
st.session_state['region'] = "northeast"
st.session_state['predict'] = 4435.13