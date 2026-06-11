# Contributing

## Submission guidelines

Contributions are always welcome!

Contributions are what make the open-source community such an amazing place
to learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

If you have a suggestion that would make this better, please fork the repo
and create a pull request. You can also simply open an issue with the tag
`enhancement`.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "feat: add some feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a pull request.

## Commit message guidelines

We follow the [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/)
specification, which keeps the history readable and lets us generate the
changelog automatically.

### Format

```
<type>: <subject> [optional `breaking`]
```

`type` must be one of the following:

| Type      | When to use |
| --------- | --- |
| `build`   | Changes affecting the build system (external dependencies) |
| `ci`      | Changes to the CI configuration |
| `chore`   | Changes affecting the project structure |
| `docs`    | Documentation-only changes |
| `feat`    | A new feature |
| `fix`     | A bug fix |
| `perf`    | A performance improvement |
| `refactor`| Code change that neither fixes a bug nor adds a feature |
| `revert`  | Revert a previous commit |
| `style`   | Formatting (lint, whitespace) |
| `test`    | Adding or fixing tests |

The optional `[ breaking ]` keyword declares a **BREAKING CHANGE**.

### Examples

```
feat: allow provided config object to extend other configs [ breaking ]
docs: correct spelling in the contributing.md file
fix: fix minor issue in code (#12)
```
