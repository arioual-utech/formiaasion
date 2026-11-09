# Consignes pour préparer une session (Hive)

Lues par la Queen et les Workers au début de chaque Hive « Session de formation IA ».

## Contexte

Formation de collègues IAAS (95 % dev/ops, GitHub Copilot dans VS Code sous WSL, AlmaLinux 9 ou Ubuntu). Fil rouge : dépôt privé `iaassistant` sur le poste de chaque apprenant. Modèles à suivre : `docs/sessions/0.2-copilot-vscode/` et `docs/sessions/1.1-llm-tokens-couts/`. Point de départ : `_template/`.

## Conventions non négociables

- Une commande par bloc bash, jamais deux dans le même bloc.
- Variantes Ubuntu ET AlmaLinux 9 quand elles diffèrent (ex. pas d'installation de curl sur Alma).
- Jamais le mot « formateur ». Le dépôt fil rouge s'appelle `iaassistant`.
- Pas de « U Tech », pas d'URL interne : le dépôt est public.
- Slides Marp : pas de HTML brut (`html: false`), images en markdown depuis `assets/`, notes de présentation dans chaque slide.
- Chiffres (prix, versions) : source et date de relevé, jamais de mémoire.
- Ne jamais exécuter `git commit` ni `git push`. Ne rien modifier hors `docs/sessions/<dossier de la session>/`.

## Rôles des Workers

**Test Automation Engineer (testeur).** Rejoue chaque commande de la fiche, dans l'ordre, dans un conteneur Docker neuf : `almalinux:9` ET `ubuntu:24.04`. Script passé par stdin (`bash -s < script`), pas de `-v` sur un fichier. Travaille dans le scratchpad, pas dans le dépôt. Rapporte : commande, résultat, écart avec le « Vérifier » de la fiche. Pièges à re-tester : version de Python choisie par uv (`uv python pin`), curl-minimal sous Alma, `uv` introuvable après `deactivate`, `pyproject.toml` manquant avant `uv add`, certificats d'entreprise (`UnknownIssuer`).

**Code Reviewer (relecteur).** Lit fiche, slides, prérequis et bonus. Vérifie : conventions ci-dessus, cohérence fiche / slides / durées du déroulé, front-matter complet, liens relatifs valides, copier-coller (un bloc = une commande), critères de validation mesurables.

**Prompt Engineer (pédagogie).** Critique l'enchaînement : objectif tenable dans la durée du format, un « Vérifier » par étape, table « Si ça bloque », exemples concrets pour des équipes dev/ops.

## Déroulé de la Queen

1. Lire `_template/` et les deux sessions modèles. Résumer en 5 lignes max le plan (objectif, déroulé minuté, brique ajoutée à `iaassistant`, prérequis). Attendre l'accord avant d'écrire.
2. Créer `docs/sessions/<numéro>-<slug>/` : `00-prerequis.md`, `01-fiche-etudiant.md`, `02-slides.md`, `03-pour-aller-plus-loin.md` (et `assets/` si schéma SVG).
3. Faire vérifier à la source (page officielle, avec date) tout prix, version ou fonctionnalité citée.
4. Déléguer avec `send_message`, une consigne complète par Worker, en parallèle.
5. Recouper, corriger soi-même les fichiers, faire re-tester ce qui a échoué. Maximum 2 boucles.
6. Vérifier le rendu des slides : `marp --no-stdin --allow-local-files <fichier> --images png -o <scratchpad>/s.png`. Regarder les slides à tableau ou à schéma.
7. Rapport final court : fichiers créés, résultats Docker (Alma / Ubuntu), points ouverts, commande pour voir les slides : `PORT=8090 marp -s docs/sessions/<dossier>` puis `http://localhost:8090/02-slides.md`.
8. Ne rien publier. Étape suivante, sur demande explicite de l'utilisateur seulement : `python scripts/sync_obsidian.py`, puis commit et push.
