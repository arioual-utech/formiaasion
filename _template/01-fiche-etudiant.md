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
| **Prérequis** | [[00-prerequis]] |
| **Brique ajoutée à `mon-assistant`** | `chemin/de/la/brique` |

## Objectif

À la fin de la session, tu sais : (une phrase, un verbe d'action).

## Déroulé

| Durée       | Étape                           |
| ----------- | ------------------------------- |
| 5 min       | Rappel de la session précédente |
| 10 min      | Démo par le formateur           |
| 35 à 40 min | TP (ci-dessous)                 |
| 5 min       | Validation                      |

## Pas à pas

### Étape 1 : titre de l'étape

Ce qu'on fait, en une phrase.

```bash
commande à copier
```

**Vérifier** : ce qu'on doit voir (sortie, fichier créé, comportement).

### Étape 2 : titre de l'étape

...

> [!tip] Astuce
> Un raccourci ou un piège évité.

## Validation

Montrer au formateur (ou cocher) :

- [ ] Critère observable 1 (ex. `commande` affiche ...)
- [ ] Critère observable 2
- [ ] La brique est poussée dans ton dépôt

## Pousser la brique

```bash
cd ~/mon-assistant
git add .
git commit -m "feat: <brique de la session>"
git push
```

## Si ça bloque

| Symptôme | Cause probable | Solution |
|---|---|---|
| Message d'erreur exact | ... | ... |

## À retenir

- 2 ou 3 points, pas plus.

## Pour aller plus loin

Exercice optionnel : [[03-pour-aller-plus-loin]]
