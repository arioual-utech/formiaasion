---
session: "N"
nom: "Nom de la session"
phase: "Phase X"
format: lab
duree: 60
brique: ""
statut: brouillon
tags: [formation, fiche-etudiant]
---
# Nom de la session

| | |
|---|---|
| **Format** | Lab · 60 min |
| **Phase** | Phase X |
| **Prérequis** | [Prérequis](00-prerequis.md) |
| **Brique ajoutée à `iaassistant`** | `chemin/de/la/brique` |

## Objectif

À la fin de la session, tu sais : (une phrase, un verbe d'action).

## Déroulé

| Durée       | Étape                           |
| ----------- | ------------------------------- |
| 5 min       | Rappel de la session précédente |
| 10 min      | Démo                            |
| 35 à 40 min | TP (ci-dessous)                 |
| 5 min       | Validation                      |

## Pas à pas

Les commandes sont à lancer **une par une**, en vérifiant le résultat de chacune avant de passer à la suivante.

### Étape 1 : titre de l'étape

Ce qu'on fait, en une phrase.

```bash
commande à copier
```

**Vérifier** : ce qu'on doit voir (sortie, fichier créé, comportement).

### Étape 2 : titre de l'étape

...

!!! tip "Astuce"
    Un raccourci ou un piège évité.

## Validation

Coche chaque ligne :

- [ ] Critère observable 1 (ex. `commande` affiche ...)
- [ ] Critère observable 2
- [ ] La brique est poussée dans ton dépôt

## Pousser la brique

```bash
cd ~/projets/iaassistant
```

```bash
git add .
```

```bash
git commit -m "feat: <brique de la session>"
```

```bash
git push
```

## Si ça bloque

| Symptôme | Cause probable | Solution |
|---|---|---|
| Message d'erreur exact | ... | ... |

## À retenir

- 2 ou 3 points, pas plus.

## Pour aller plus loin

Exercice optionnel : [Pour aller plus loin](03-pour-aller-plus-loin.md)
