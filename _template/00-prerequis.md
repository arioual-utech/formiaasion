---
session: "N"
nom: "Nom de la session"
phase: "Phase X"
format: lab
duree: 60
brique: ""
statut: brouillon
tags: [formation, prerequis]
---
# Prérequis : Nom de la session

> [!info] À faire **avant** la session. Compter 10 minutes. Si un point échoue, prévenir le formateur la veille.

## Sessions à avoir suivies

- [ ] Session X : titre (apporte : ...)
- [ ] Session Y : titre

## Ce que `mon-assistant` doit contenir

État attendu du dépôt en arrivant (la brique de la session précédente est poussée) :

```text
mon-assistant/
└── ...
```

## Vérifier son poste

| Quoi               | Commande               | Résultat attendu |
| ------------------ | ---------------------- | ---------------- |
| Git configuré      | `git config user.name` | ton nom          |
| Version de l'outil | `outil --version`      | `X.Y` ou plus    |
| Accès réseau       | `curl -sI https://...` | `HTTP/2 200`     |

## Accès nécessaires

- [ ] VPN ou réseau de l'entreprise actif
- [ ] Compte / licence : ...
- [ ] Accès au lab Coder : ...

## Notions à connaître

Une ligne par notion, avec un lien. Pas d'explication ici.

- Notion : lien ou fiche de la session X

## En cas de problème

Écrire au formateur avec : la commande lancée et le message d'erreur complet.
