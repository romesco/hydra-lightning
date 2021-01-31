## Unique Aspects

We are striving for this repo to be a close to 'self-maintained' as possible.
A decent amount of the core code (the configuration files themselves) are auto-generated
by a tool called `configen` which we are working on directly within `hydra`. Generally,
users of these configs do not have to understand how to use `configen`. However, if you
plan to contribute, it will be much easier if you have taken a look at
[how `configen` works](https://github.com/facebookresearch/hydra/tree/master/tools/configen) first.

Put simply, think of the directory `/configen` as the source for the core configs. To expand this,
we edit `/configen/conf` and then regenerate. Currently, this is done through `generate_configs.py`,
but this may be updated.

## Setup a Dev Environment

This repo uses a poetry/nox/pre-commit approach. Generally the flow is the following:

```
GitHub Actions ->
   Nox ->
    [Lint] Pre-commit:
       black
       flake8
       reorder-python-imports
    [Test] Pytest
    [Coverage Report]
```

```bash
# Install non-system python (we recommend pyenv).
# For more info on pyenv: https://github.com/pyenv/pyenv
# Feel free to skip this if you already have a conda python installed.


curl https://pyenv.run | bash
# Add commands to terminal startup. For bash:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec $SHELL
pyenv install 3.9.0
pyenv local 3.9.0 # sets this as local python version for directory
pyenv which python # confirm you have the python you expect

# Install poetry and pipx
# For more info on poetry: https://python-poetry.org/docs/#installation
# For more info on pipx: https://github.com/pipxproject/pipx#overview-what-is-pipx

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
python3 -m pip install --user pipx

# Install nox and nox-poetry (pipx is now recommended for installing applications).
# If you don't want pipx installed, you can substitute 'pip install --user'.

pipx install nox
pipx inject nox nox-poetry

# Clone this repo

git clone https://github.com/romesco/hydra-lightning

# Install project with poetry

poetry install

# Install pre-commit hooks

nox -s pre-commit -- install

# See available nox sessions

nox --list-sessions

# Run full test suite

nox

```

## Pull Requests

We're ready for your pull requests! Don't be shy about it. If you are working through
and idea, put it up as soon as you can as a "draft" PR, and we will offer help.

Here's the workflow:

1. Fork the repo and create your feature branch from `main`.
2. If you've added code, add suitable tests.
3. Ensure the test suite and lint pass.

## Issues

Please file issue if you require a new config we have not provided, have an idea for a useful tutorial, or notice a bug.

## License

By contributing to `hydra-lightning`, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.
