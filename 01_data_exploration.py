# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:42:01 2026

@author: AUGUSTIN KOUATCHOUA
"""


# NOTE : les expressions pandas seules des sections exploratoires
# peuvent ne pas s’afficher lors de l’exécution du fichier entier.
# Pour voir leur résultat, exécuter la ligne dans la console ou utiliser print().

# ==================================================================
# 1. IMPORTATION ET CHARGEMENT DES DONNÉES
# ==================================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\Users\AUGUSTIN KOUATCHOUA\OneDrive\Bureau\projets SQL\credit-risk-analytics-pipeline\data\application_train.csv")


# ==================================================================
# 2. EXPLORATION DU DATASET
# ==================================================================

#Nombre total de demandes de crédit

print("le nombre total de demandes de crédit est ",len(df))

#Le nombre total de variables et leurs noms

print("le nombre total de variables est ",df.shape[1])
print("les noms des différentes variables sont ",df.columns)

#les 10 premières demandes de crédit

print("les 10 premières demandes de crédit sont ",df.head(10))



# ==================================================================
# 3. SÉLECTION ET FILTRAGE DES DONNÉES
# ==================================================================

##selectionner des colonnes avec pandas

#selectionner la colonne AMT_CREDIT

df["AMT_CREDIT"]

#selectionner plusieurs colonnes SK_ID_CURR, AMT_CREDIT et TARGET

df[["SK_ID_CURR", "AMT_CREDIT", "TARGET"]]

#Afficher uniquement les 10 premières lignes des colonnes SK_ID_CURR, AMT_CREDIT, AMT_INCOME_TOTAL et TARGET'

df[["SK_ID_CURR", "AMT_CREDIT","AMT_INCOME_TOTAL","TARGET"]].head(10)



##Filtrer les demandes de crédit

#Afficher toutes les demandes de crédit dont le montant AMT_CREDIT est supérieur à 1 000 000

df[df["AMT_CREDIT"]> 1000000]

#Afficher les demandes de crédit dont le revenu AMT_INCOME_TOTAL est inférieur à 100 000

df[df["AMT_INCOME_TOTAL"]< 100000]

#Affiche uniquement les demandes pour lesquelles qui ont des difficultés de remboursement

df[df["TARGET"]==1]

#Afficher uniquement les colonnes SK_ID_CURR, AMT_CREDIT et TARGET pour les demandes dont le montant du crédit dépasse 500 000


df[df["AMT_CREDIT"] > 500000][["SK_ID_CURR", "AMT_CREDIT", "TARGET"]]

##Combiner plusieurs conditions (AND / OR)

#Afficher les demandes de crédit dont le montant AMT_CREDIT est supérieur à 1 000 000 ET dont le revenu AMT_INCOME_TOTAL est inférieur à 200 000

df[(df["AMT_CREDIT"]> 1000000) & (df["AMT_INCOME_TOTAL"]< 200000)]

#Afficher les demandes dont le montant du crédit est inférieur à 100 000 OU supérieur à 1 500 000.

df[(df["AMT_CREDIT"]< 100000) | (df["AMT_CREDIT"]> 1500000)]

#Afficher les demandes avec TARGET = 1 ET un revenu inférieur à 150 000.

df[(df["AMT_INCOME_TOTAL"]< 150000) & (df["TARGET"]==1)]

#Affiche uniquement les colonnes SK_ID_CURR, AMT_CREDIT, AMT_INCOME_TOTAL et TARGET pour les demandes dont
# Le crédit dépasse 500 000.
# Le revenu est inférieur à 200 000.
# TARGET = 1

df[(df["AMT_CREDIT"] > 500000) & (df["AMT_INCOME_TOTAL"]< 200000) & (df["TARGET"]==1)][["SK_ID_CURR", "AMT_CREDIT","AMT_INCOME_TOTAL", "TARGET"]]

##Quel est le revenu moyen des emprunteurs présentant des difficultés de remboursement

df[df["TARGET"]==1]["AMT_INCOME_TOTAL"].mean()


# ==================================================================
# 4. AGRÉGATIONS ET GROUPBY
# ==================================================================

##GROUP BY avec pandas

#Calculer le revenu moyen pour chaque valeur de TARGET

df.groupby("TARGET")["AMT_INCOME_TOTAL"].mean()

#Calculer le montant total des crédits pour chaque valeur de TARGET

df.groupby("TARGET")["AMT_CREDIT"].sum()

#le nombre de demandes de crédit pour chaque valeur de TARGET

df.groupby("TARGET")["TARGET"].size()

#Pour chaque valeur de TARGET, calculer le revenu moyen et le revenu maximum

df.groupby("TARGET")["AMT_INCOME_TOTAL"].agg(["mean", "max"])

#Pour chaque valeur de TARGET, calculer le montant minimum, moyen et maximum des crédits

df.groupby("TARGET")["AMT_CREDIT"].agg(["min","mean","max"])

#Pour chaque valeur de TARGET, calcule le montant total et le montant moyen des annuités

df.groupby("TARGET")["AMT_ANNUITY"].agg(["sum","mean"])

#Calculer le revenu moyen pour chaque combinaison de TARGET et CODE_GENDER

df.groupby(["TARGET","CODE_GENDER"])["AMT_INCOME_TOTAL"].mean()

#Calculer le nombre de demandes de crédit pour chaque combinaison de TARGET et CODE_GENDER

df.groupby(["TARGET","CODE_GENDER"])["AMT_CREDIT"].size()

#Pour chaque combinaison de TARGET et CODE_GENDER, calculer le montant minimum, moyen et maximum des crédits

df.groupby(["TARGET","CODE_GENDER"])["AMT_CREDIT"].agg(["min","mean","max"])

#Pour chaque valeur de TARGET, calculer sur une même ligne :
#Le montant moyen des crédits
#Le revenu total 
#Le montant maximum des annuités

df.groupby("TARGET").agg({"AMT_CREDIT":"mean","AMT_INCOME_TOTAL":"sum","AMT_ANNUITY":"max"})



# ==================================================================
# 5. TRI ET ANALYSE DES CATÉGORIES
# ==================================================================

#Les 10 demandes de crédit les p^lus élevées

df.sort_values("AMT_CREDIT", ascending=False).head(10)

#les 5 demandes ayant les revenus déclarés les plus faibles

df.sort_values("AMT_INCOME_TOTAL").head(5)

#les colonnes SK_ID_CURR, AMT_CREDIT et TARGET pour les 10 demandes de crédit les plus élevées

df[["SK_ID_CURR","AMT_CREDIT","TARGET"]].sort_values("AMT_CREDIT", ascending = False).head(10)


#Pour TARGET = 1, affiche les 10 montants de crédit les plus élevés

df[df["TARGET"]==1].sort_values("AMT_CREDIT", ascending = False).head(10)

#les différentes catégories présentes dans NAME_INCOME_TYPE (type de revenu)

df["NAME_INCOME_TYPE"].unique()

#Le nombre de catégories différentes dans NAME_EDUCATION_TYPE

df["NAME_EDUCATION_TYPE"].nunique()

#Le nombre de demandes pour chaque catégorie de NAME_FAMILY_STATUS

df["NAME_FAMILY_STATUS"].value_counts()

#Le nombre de valeurs de CODE_GENDER et le nombre de demandes correspondant à chaque valeur

df["CODE_GENDER"].nunique()
df["CODE_GENDER"].value_counts()


# ==================================================================
# 6. STATISTIQUES DESCRIPTIVES
# ==================================================================

#statistiques descriptives de AMT_INCOME_TOTAL

df["AMT_INCOME_TOTAL"].describe()

#montant médian des crédits (AMT_CREDIT)

df["AMT_CREDIT"].median()

#l'écart-type des revenus (AMT_INCOME_TOTAL)

df["AMT_INCOME_TOTAL"].std()

#Pour chaque valeur de TARGET, calcul de la moyenne, la médiane et l'écart-type des montants de crédit

df.groupby("TARGET")["AMT_CREDIT"].mean()
df[df["TARGET"]==0]["AMT_CREDIT"].median()
df[df["TARGET"]==1]["AMT_CREDIT"].median()
df[df["TARGET"]==0]["AMT_CREDIT"].std()
df[df["TARGET"]==1]["AMT_CREDIT"].std()


# ==================================================================
# 7. VALEURS MANQUANTES ET DOUBLONS
# ==================================================================

#Nombre de valeurs manquantes contient la colonne AMT_INCOME_TOTAL et AMT_ANNUITY

df["AMT_INCOME_TOTAL"].isnull().sum()
df["AMT_ANNUITY"].isnull().sum()

#le nombre de valeurs manquantes pour chaque colonne du dataset

df.isnull().sum()

#Les 10 colonnes atant le plus de valeurs manquantes

df.isnull().sum().sort_values(ascending= False).head(10)

#pourcentage de valeurs manquantes dans AMT_ANNUITY et OCCUPATION_TYPE

(df["AMT_ANNUITY"].isnull().sum()/len(df))* 100
(df["OCCUPATION_TYPE"].isnull().sum()/len(df))* 100

#pourcentage de valeurs manquantes pour toutes les colonnes du dataset

(df.isnull().sum()/len(df))* 100

#les 10 colonnes ayant le pourcentage de valeurs manquantes le plus élevé, en arrondissant les résultats à deux décimales.

(round((df.isnull().sum()/len(df))* 100,2)).sort_values(ascending = False).head(10)

#Nombre de lignes entièrement identiques du dataset

df.duplicated().sum()

#Nombre de lignes entièrement identiques dans SK_ID_CURR

df["SK_ID_CURR"].duplicated().sum()

#lignes considérées comme des doublons exacts
df[df.duplicated()]

#Affichage de toutes les lignes dont le SK_ID_CURR apparaît plusieurs fois, y compris la première occurrence

df[df.duplicated(subset=["SK_ID_CURR"], keep=False)]


# ==================================================================
# 8. NETTOYAGE ET CRÉATION DE VARIABLES
# ==================================================================

#copie du dataset df

df_clean=df.copy()

#Suppression des lignes entièrement identiques de df_clean

df_clean = df_clean.drop_duplicates().copy()

#Doublons restants dans df_clean

print("Doublons restants :", df_clean.duplicated().sum())

#Le nombre de lignes avant et après le nettoyage

print("Lignes avant nettoyage :", len(df))
print("Lignes après nettoyage :", len(df_clean))

#Nombre de demandes présentent un montant de crédit (AMT_CREDIT) inférieur ou égal à zéro

(df["AMT_CREDIT"]<=0).sum()


#Afficher les demandes dont le crédit est inférieur ou égal à zéro ET le revenu est inférieur ou égal à zéro.

df[(df["AMT_CREDIT"]<=0) & (df["AMT_INCOME_TOTAL"]<=0)][["SK_ID_CURR", "AMT_CREDIT", "AMT_INCOME_TOTAL"]]

#Création d'une nouvelle colonne AMT_ANNUITY_CLEAN contenant les valeurs de AMT_ANNUITY, avec les valeurs manquantes remplacées par la médiane

df_clean["AMT_ANNUITY_CLEAN"] = df_clean["AMT_ANNUITY"].fillna(df_clean["AMT_ANNUITY"].median())

#Nombre de valeurs manquantes dans AMT_ANNUITY_CLEAN

df_clean["AMT_ANNUITY_CLEAN"].isnull().sum()

#Comparer la moyenne de AMT_ANNUITY avec celle de AMT_ANNUITY_CLEAN

df_clean["AMT_ANNUITY_CLEAN"].mean()-df_clean["AMT_ANNUITY"].mean()

#Nombre de demandes présentent un revenu AMT_INCOME_TOTAL inférieur ou égal à zéro

(df_clean["AMT_INCOME_TOTAL"]<=0).sum()

#Création d'une colonne CREDIT_INCOME_RATIO dans df_clean, en calculant le ratio uniquement pour les revenus strictement positifs. Pour les autres lignes, conserve une valeur manquante

df_clean.loc[df_clean["AMT_INCOME_TOTAL"]>0, "CREDIT_INCOME_RATIO"] = (df_clean["AMT_CREDIT"] / df_clean["AMT_INCOME_TOTAL"])

#Afficher les 10 demandes ayant le ratio crédit/revenu le plus élevé, avec les colonnes SK_ID_CURR, AMT_CREDIT, AMT_INCOME_TOTAL et CREDIT_INCOME_RATIO

df_clean[["SK_ID_CURR", "AMT_CREDIT", "AMT_INCOME_TOTAL", "CREDIT_INCOME_RATIO"]].sort_values("CREDIT_INCOME_RATIO", ascending=False).head(10)


# ==================================================================
# 9. ANALYSE DU RISQUE ET KPI
# ==================================================================

#Calcul du pourcentage de demandes avec TARGET = 1 pour chaque catégorie de NAME_INCOME_TYPE

df.groupby("NAME_INCOME_TYPE")["TARGET"].mean() * 100

#Pour chaque catégorie de NAME_FAMILY_STATUS, afficher dans un même tableau :
#- Le nombre de demandes, nommé nombre_demandes.
#- Le taux de difficulté de remboursement en pourcentage, nommé taux_difficulte

kpi_famille = df_clean.groupby("NAME_FAMILY_STATUS").agg(
    nombre_demandes=("TARGET", "size"),
    taux_difficulte=("TARGET", "mean")
)
kpi_famille["taux_difficulte"] = kpi_famille["taux_difficulte"] * 100
print(kpi_famille)

#Création une colonne RISK_CATEGORY dans df_clean à partir de CREDIT_INCOME_RATIO, avec les catégories Faible, Modéré et Élevé selon les seuils du tableau. Les ratios manquants doivent rester non classés

df_clean["RISK_CATEGORY"] = df_clean["CREDIT_INCOME_RATIO"].apply(
    lambda x: None if pd.isna(x)
    else "Élevé" if x > 4
    else "Modéré" if x >= 2
    else "Faible"
)

#Nombre de demandes dans chaque catégorie de risque

print(df_clean["RISK_CATEGORY"].value_counts(dropna=False))

#Pour chaque catégorie de risque, calcule :
#- Le nombre de demandes.
#- Le montant moyen des crédits (AMT_CREDIT).
#- Le taux de difficulté de remboursement (TARGET) en pourcentage

resultat = df_clean.groupby("RISK_CATEGORY").agg(nombre_demandes=("TARGET", "size"), credit_moyen=("AMT_CREDIT", "mean"), taux_difficulte=("TARGET", "mean"))
resultat["taux_difficulte"] = resultat["taux_difficulte"] * 100


# ==================================================================
# 10. VISUALISATIONS
# ==================================================================

#Création d'un graphique en barres montrant le taux de difficulté de remboursement (%) pour chaque catégorie RISK_CATEGORY

resultat["taux_difficulte"].plot(kind="bar")
plt.ylabel("Taux de difficulté (%)")
plt.title("Taux de difficulté par catégorie")
plt.show()

#Création d'un graphique en barres représentant le montant moyen des crédits (credit_moyen) pour chaque catégorie RISK_CATEGORY

resultat["credit_moyen"].plot(kind="bar", color = "orange")
plt.ylabel("Crédit moyen")
plt.title("Crédit moyen par catégorie")
plt.show()

#Création d'un histogramme de la colonne AMT_CREDIT avec :
#- 40 intervalles (bins=40).
#- Une couleur bleue.
#- Le titre « Distribution des montants de crédit ».
#- L'axe horizontal nommé « Montant du crédit ».
#- L'axe vertical nommé « Nombre de demandes ».

df_clean["AMT_CREDIT"].plot(kind="hist", bins = 40, color = "blue")
plt.title("Distribution des montants de crédit")
plt.ylabel("Nombre de demandes")
plt.xlabel("Montant du crédit")
plt.show()


#comparaison de la distribution des montants de crédit entre deux groupes (target = 0 et Target = 1)
#Target = 0


df_clean[df_clean["TARGET"]==0]["AMT_CREDIT"].plot(kind="hist", bins = 40, color = "red")
plt.title("Distribution des montants de crédit")
plt.ylabel("Nombre de demandes")
plt.xlabel("Montant du crédit")
plt.show()

#target = 1

df_clean[df_clean["TARGET"]==1]["AMT_CREDIT"].plot(kind="hist", bins = 40, color = "purple")
plt.title("Distribution des montants de crédit")
plt.ylabel("Nombre de demandes")
plt.xlabel("Montant du crédit")
plt.show()


#Création d'un nuage de points pour analyser la relation entre :
#- Axe X : AMT_INCOME_TOTAL (revenu total).
#- Axe Y : AMT_ANNUITY (annuité du crédit).

df_clean.plot(kind="scatter",x="AMT_INCOME_TOTAL",y="AMT_ANNUITY")
plt.xlabel("somme des revenus")
plt.ylabel("annuité de crédit")
plt.title("Analyse de la relation entre les revenus et les annuités de crédit")
plt.show()


# ==================================================================
# 11. CORRÉLATION
# ==================================================================

#Calcul de la corrélation entre AMT_INCOME_TOTAL et AMT_ANNUITY

print("Corrélation revenus / annuités :", df_clean["AMT_INCOME_TOTAL"].corr(df_clean["AMT_ANNUITY"]))


# ==================================================================
# 12. EXPORT ET CONTRÔLE FINAL
# ==================================================================

# Enregistrer les KPI dans le dossier outputs du projet.
# Le dossier est créé s'il n'existe pas.
dossier_sortie = r"C:\Users\AUGUSTIN KOUATCHOUA\OneDrive\Bureau\projets SQL\credit-risk-analytics-pipeline\outputs"
os.makedirs(dossier_sortie, exist_ok=True)
chemin_csv = os.path.join(dossier_sortie, "credit_risk_kpi.csv")

# reset_index() conserve le nom de la catégorie dans le CSV.
resultat.reset_index().to_csv(chemin_csv, index=False)
print("Fichier exporté :", chemin_csv)

# Relire le même fichier pour contrôler le résultat.
df_kpi = pd.read_csv(chemin_csv)
print("Aperçu des KPI :")
print(df_kpi.head(5))
print("Dimensions :", df_kpi.shape)
print("Valeurs manquantes :")
print(df_kpi.isnull().sum())
print("Catégories triées par taux de difficulté :")
print(df_kpi.sort_values("taux_difficulte", ascending=False))
