<!-- omit in toc -->
# Contributing to Grafana Calendar Annotator

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Styleguides](#styleguides)

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://github.com/cam-barts/grafana-calendar-annotator).

Before you ask a question, it is best to search for existing [Issues](https://github.com/cam-barts/grafana-calendar-annotator/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/cam-barts/grafana-calendar-annotator/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.


## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://github.com/cam-barts/grafana-calendar-annotator). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/cam-barts/grafana-calendar-annotatorissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to vulns@coder.cam.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/cam-barts/grafana-calendar-annotator/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Grafana Calendar Annotator, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/cam-barts/grafana-calendar-annotator) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/cam-barts/grafana-calendar-annotator/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/cam-barts/grafana-calendar-annotator/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most Grafana Calendar Annotator users. You may also want to point out the other projects that solved it better and which could serve as inspiration.


### Your First Code Contribution

This project expects `poetry` to be installed. See installation instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer).

This project makes heavy use of [pre-commit](https://pre-commit.com/) to enforce style standards for both code and commit messages. After cloning and installing dev dependancies with `poetry install`, the `pre-commit` command should be available. Run `pre-commit install` to ensure all hooks are installed and useful for your environment.

```bash
git clone https://github.com/cam-barts/grafana-calendar-annotator.git # or whatever your fork url is
cd grafana-calendar-annotator
poetry install
pre-commit install
```

A current list of hooks can be found at https://github.com/cam-barts/grafana-calendar-annotator/blob/main/.pre-commit-config.yaml, but at the time of writing these hooks run at commit time:

- [Commitizen](https://pypi.org/project/commitizen/) for standardized commit messages
- [pycln](https://pypi.org/project/pycln/) to clean unused imports
- [isort](https://pypi.org/project/isort/) to keep imports sorted
- [black](https://pypi.org/project/black/) to format code in a standard way
- [bandit](https://pypi.org/project/bandit/) to check for security antipatterns in code
- [pip-audit](https://pypi.org/project/pip-audit/) to ensure dependancies don't introduce vulnerabilities
- [trailing-whitespace](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace) Trims trailing whitespace
- [check-ast](https://github.com/pre-commit/pre-commit-hooks#check-ast) prevents checking in syntax errors
- [check-json](https://github.com/pre-commit/pre-commit-hooks#check-json) ensures json files are valid
- [check-toml](https://github.com/pre-commit/pre-commit-hooks#check-toml) ensures toml files are valid
- [check-yaml](https://github.com/pre-commit/pre-commit-hooks#check-yaml) ensures yaml files are valid


## Styleguides

### Code

As mentioned in the previous section, pre-commit will ensure that everything is stylistically acceptable. After you `git add` changes to the staging area, run `pre-commit run --all-files` to format all code and ensure style guidelines are adhered to.

### Commit Messages

Commit messages are validated using [commitizen](https://pypi.org/project/commitizen/) using conventional commit style. The best way to ensure that the commit matches the expected style is to replace `git commit -m ...` with `cz commit` and follow the prompts in the terminal.

> NOTE: Your commit *will* fail if changes don't pass pre-commit checks. It's recommended to run `pre-commit run --all-files` before `cz commit`

**Example Commit Message**

The following is the output of `cz example`

```txt
fix: correct minor typos in code

see the issue for details on the typos fixed

closes issue #12
```

**Info**

The following is the output of `cz info`

```txt
The commit contains the following structural elements, to communicate
intent to the consumers of your library:

fix: a commit of the type fix patches a bug in your codebase
(this correlates with PATCH in semantic versioning).

feat: a commit of the type feat introduces a new feature to the codebase
(this correlates with MINOR in semantic versioning).

BREAKING CHANGE: a commit that has the text BREAKING CHANGE: at the beginning of
its optional body or footer section introduces a breaking API change
(correlating with MAJOR in semantic versioning).
A BREAKING CHANGE can be part of commits of any type.

Others: commit types other than fix: and feat: are allowed,
like chore:, docs:, style:, refactor:, perf:, test:, and others.

We also recommend improvement for commits that improve a current
implementation without adding a new feature or fixing a bug.

Notice these types are not mandated by the conventional commits specification,
and have no implicit effect in semantic versioning (unless they include a BREAKING CHANGE).

A scope may be provided to a commit’s type, to provide additional contextual
information and is contained within parenthesis, e.g., feat(parser): add ability to parse arrays.

<type>[optional scope]: <description>

[optional body]

[optional footer]
```

<!-- omit in toc -->
## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!