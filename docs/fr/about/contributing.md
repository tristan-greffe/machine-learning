# Contribuer

## Comment contribuer

Toutes les contributions sont les bienvenues !

L'open source est ce qu'il est grâce aux gens qui se prêtent au jeu — toute
contribution est **grandement appréciée**.

Si tu as une idée pour améliorer le projet, fork le dépôt et ouvre une pull
request. Tu peux aussi simplement ouvrir une issue avec le tag
`enhancement`.

1. Fork le dépôt.
2. Crée une branche : `git checkout -b feature/ma-feature`
3. Commit : `git commit -m "feat: ajoute X"`
4. Push : `git push origin feature/ma-feature`
5. Ouvre une pull request.

## Convention de commits

On suit les [Conventional Commits](https://www.conventionalcommits.org/fr/v1.0.0/),
ça garde l'historique lisible et permet de générer un changelog
automatiquement.

### Format

```
<type>: <sujet> [optional `breaking`]
```

`type` doit être l'un de :

| Type      | Quand l'utiliser |
| --------- | --- |
| `build`   | Changements affectant le système de build (dépendances externes) |
| `ci`      | Changements de la configuration CI |
| `chore`   | Changements affectant la structure du projet |
| `docs`    | Changements de documentation uniquement |
| `feat`    | Nouvelle fonctionnalité |
| `fix`     | Correction de bug |
| `perf`    | Amélioration de performance |
| `refactor`| Refactoring (ni feature ni fix) |
| `revert`  | Revert d'un commit |
| `style`   | Mise en forme (lint, espaces…) |
| `test`    | Ajout ou correction de tests |

Le mot-clé optionnel `[ breaking ]` indique un **BREAKING CHANGE**.

### Exemples

```
feat: allow provided config object to extend other configs [ breaking ]
docs: correct spelling in the contributing.md file
fix: fix minor issue in code (#12)
```
