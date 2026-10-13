# Formation IA

Parcours de sessions courtes (15, 30 ou 60 minutes) pour utiliser l'IA au quotidien, avec un projet fil rouge construit session après session.

Le site est publié avec GitHub Pages. Il est protégé par un mot de passe : le contenu des pages est chiffré dans le HTML publié.

## Structure

| Dossier | Contenu |
|---|---|
| `docs/` | Contenu du site (mkdocs) |
| `docs/sessions/` | Une session par dossier. **Chiffré dans git** (git-crypt) |
| `_template/` | Modèle d'une session : prérequis, fiche étudiant, slides, exercice bonus |
| `theme/sakura.css` | Thème des slides (Marp) |

## Écrire une session

1. Copier `_template/` vers `docs/sessions/NN-nom-court/` et supprimer les fichiers inutiles pour le format (newsletter, concept ou lab).
2. Écrire les fichiers.
3. Prévisualiser les slides : extension VS Code « Marp for VS Code » (le thème est déclaré dans `.vscode/settings.json`).
4. Prévisualiser le site : `SITE_PASSWORD=essai mkdocs serve` dans un environnement virtuel Python avec `mkdocs`, `mkdocs-material` et `mkdocs-encryptcontent-plugin`.

## Chiffrement

- **Dans git** : `git-crypt` chiffre `docs/sessions/`. Sans la clé, les fichiers sont illisibles (les noms de fichiers et les messages de commit restent visibles).
- **Sur le site** : `mkdocs-encryptcontent-plugin` chiffre chaque page avec le mot de passe du site.
- **Secrets de CI** : `GIT_CRYPT_KEY` (clé git-crypt encodée en base64) et `SITE_PASSWORD`. Aucun secret n'est stocké dans le dépôt.

## Cloner et déverrouiller

```bash
git clone https://github.com/arioual-utech/formiaasion.git
cd formiaasion
git-crypt unlock /chemin/vers/la/cle
```
