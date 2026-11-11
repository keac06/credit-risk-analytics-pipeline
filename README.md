# Credit Risk Analytics — Pipeline local Python

## Présentation

Projet de portfolio d'analyse du risque de crédit réalisé en **Python, pandas et Matplotlib**, à partir du jeu de données **Home Credit Default Risk** disponible sur Kaggle.

L'objectif est de préparer les données de demandes de crédit, d'explorer les facteurs associés aux difficultés de remboursement et de produire des indicateurs (KPI) par catégorie de ratio crédit/revenu.

Ce projet est un **pipeline analytique local**. Il ne s'agit ni d'un modèle de prédiction bancaire ni d'un pipeline cloud distribué.

## Architecture

```text
credit-risk-analytics-pipeline/
├── data/
│   └── application_train.csv       # À télécharger séparément
├── scripts/
│   └── credit_risk_analysis.py
├── outputs/
│   └── credit_risk_kpi.csv         # Généré par le script
├── requirements.txt
├── .gitignore
└── README.md
```

**Flux :** fichier CSV → lecture pandas → exploration → nettoyage → variables → KPI → graphiques → export CSV → contrôle de l'export.

## Source des données

Jeu de données : [Home Credit Default Risk sur Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data).

Télécharger `application_train.csv` et le placer dans le dossier `data/`. Le fichier source n'est pas inclus dans ce dépôt.

## Prérequis

- Python 3
- pandas
- Matplotlib
- Spyder ou un autre environnement Python

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Exécution

1. Placer `application_train.csv` dans `data/`.
2. Ouvrir `scripts/credit_risk_analysis.py` dans Spyder.
3. Exécuter le fichier entier.
4. Consulter les résultats dans la console et les graphiques.
5. Vérifier le fichier `outputs/credit_risk_kpi.csv`.

Le script utilise des chemins calculés à partir de son emplacement : il n'est pas nécessaire de modifier un chemin Windows personnel.

## Étapes de l'analyse

1. Importation et chargement des données
2. Exploration du dataset
3. Sélection et filtrage
4. Agrégations et `groupby`
5. Tri et analyse des catégories
6. Statistiques descriptives
7. Valeurs manquantes et doublons
8. Nettoyage et création de variables
9. Analyse du risque et KPI
10. Visualisations
11. Corrélation
12. Export et contrôle final

Les lignes exploratoires écrites sous forme d'expressions pandas seules ne s'affichent pas nécessairement lors de l'exécution du fichier entier dans Spyder ; les principaux résultats finaux sont affichés avec `print()`.

## Indicateurs produits

Le fichier `credit_risk_kpi.csv` contient :

| Colonne | Description |
|---|---|
| `RISK_CATEGORY` | Catégorie construite à partir du ratio crédit/revenu |
| `nombre_demandes` | Nombre de demandes dans la catégorie |
| `credit_moyen` | Montant moyen des crédits |
| `taux_difficulte` | Pourcentage de demandes avec `TARGET = 1` |

Catégories de ratio crédit/revenu :

- **Faible** : ratio inférieur à 2
- **Modéré** : ratio entre 2 inclus et 4 inclus
- **Élevé** : ratio supérieur à 4
- **Non classé** : ratio manquant (exclu du `groupby` par défaut)

Le ratio est calculé uniquement lorsque le revenu est strictement positif.

## Limites

- Les catégories « Faible », « Modéré » et « Élevé » correspondent à des **seuils analytiques choisis pour l'exercice** : elles ne constituent pas un score de risque validé.
- `TARGET = 1` désigne la difficulté de remboursement selon la définition du jeu de données, pas une probabilité prédite.
- Les valeurs manquantes ne sont pas toutes imputées : une nouvelle colonne `AMT_ANNUITY_CLEAN` remplace uniquement les annuités manquantes par la médiane.
- Le script génère des graphiques à l'écran, mais ne les enregistre pas automatiquement.
- L'exécution complète doit être validée localement avec le CSV source.

## Technologies

Python · pandas · Matplotlib · CSV · Spyder
