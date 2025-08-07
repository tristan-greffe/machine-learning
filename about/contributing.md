# Contributing

## Submission guidelines

Contributions are always welcome!

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork it! 🤙

2. Create your feature branch: `git checkout -b my-new-feature`

3. Commit your changes: `git commit -m "Add some feature"`

4. Push to the branch: `git push origin my-new-feature`

5. Submit a pull request 👍

## Commit message guidelines

We follow the [Conventional commits specifications](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) which provides a set of rules to make commit messages more readable when looking through the project history. But also, we use the git commit messages to generate the change log.

### Commit message format

The commit message should be structured as follows:

```
<type>: <subject> [optional `breaking`]
```

Where `type` must be one of the following:
* `build`: changes that affect the build system (external dependencies)
* `ci`: changes to our CI configuration files and scripts
* `chore`: changes that affect the project structure
* `docs`: changes that affect the documentation only
* `feat`: a new feature
* `fix`: a bug fix
* `perf`: a code change that improves performance
* `refactor`: a code change that neither fixes a bug nor adds a feature
* `revert`: revert changes
* `style`: changes that do not affect the meaning of the code (lint issues)
* `test`: adding missing tests or correcting existing tests

Use the optional `[ breaking ]` keyword to declare a **BREAKING CHANGE**. 

### Examples

* Commit message with description and breaking change in body
```
feat: allow provided config object to extend other configs [ breaking ]
```

* Commit message with no body
```
docs: correct spelling in the contributing.md file
```

* Commit message for a fix using an issue number.
```
fix: fix minor issue in code (#12)
```