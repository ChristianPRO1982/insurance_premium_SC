# Insurance Premium Prediction

Ce projet vise à développer une application de prédiction des primes d'assurance basée sur un modèle de machine learning de régression. Le backend est développé en Python, utilisant notamment la bibliothèque scikit-learn, tandis que le frontend est créé avec Streamlit.

## Fichiers du Projet

- **chris.ipynb:** Le notebook Jupyter contenant le code pour l'exploration des données et la création du modèle.

- **common.py:** Fichier contenant des fonctions utilitaires partagées.

- **data_cleaned_cheated.csv:** Données nettoyées avec des valeurs modifiées (triche) pour des démonstrations éducatives.

- **data_cleaned.csv:** Données nettoyées sans triche.

- **data_customer.csv:** Fichier de données contenant les profils des clients.

- **données d'origine.csv:** Fichier de données original.

- **données sans doublon.csv:** Fichier de données sans doublons.

- **favicon.ico:** Icône du site.

- **HomePage.py:** Script principal du frontend Streamlit.

- **Medical_Care_Logo2.png, Medical_Care_Logo3.png, Medical_Care_Logo.png:** Images du logo médical.

- **model.py:** Script pour l'entraînement du modèle.

- **model.sav:** Modèle sauvegardé après l'entraînement.

- **README.md:** Le fichier que vous lisez actuellement, fournissant des informations sur le projet.

- **requirements.txt:** Fichier contenant les dépendances Python nécessaires pour le backend.

- **pages/'A- a- Estimation.py', 'A- b- Créer un nouvel assuré.py', 'B- a- Base de données.py', 'B- b- Analyses.py', 'Z- Une petite histoire.py', 'ZZ- un petit jeu.py':** Scripts du frontend décrivant différentes pages de l'application.

## Installation

1. Clônez le dépôt:

    ```bash
    git clone https://github.com/ChristianPRO1982/insurance_premium_SC.git
    ```

2. Installez les dépendances:

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le backend:

    ```bash
    python model.py
    ```

2. Exécutez le frontend:

    ```bash
    streamlit run HomePage.py
    ```

3. Accédez à l'application dans votre navigateur à l'adresse [http://localhost:8501](http://localhost:8501).

## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez créer une nouvelle branche, effectuer vos modifications et soumettre une pull request.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
