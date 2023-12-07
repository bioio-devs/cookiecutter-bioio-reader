# Cookiecutter BioIO Reader

[![Build Status](https://github.com/bioio-devs/cookiecutter-bioio-reader/workflows/CI/badge.svg)](https://github.com/bioio-devs/cookiecutter-bioio-reader/actions)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

A cookiecutter template for creating a new BioIO file format reader plugin.

## About

`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a new
[BioIO File Format Reader Plugin](https://github.com/bioio-devs/bioio).
This cookiecutter generates:

-   A directory structure for your project
-   Prebuilt `pyproject.toml` file to help you develop and install your reader
    plugin package
    -   Preconfigured to additionally label your reader plugin package as a
        bioio reader plugin
-   Includes basic examples of modules, tests, etc.
-   Continuous integration
    -   Preconfigured to generate project documentation
    -   Preconfigured to automatically run tests every time you push to GitHub
    -   Preconfigured to help you release your reader plugin package publicly (PyPI)

## Quickstart

To use this template use the following commands.

1. `pip install cookiecutter`
2. `cookiecutter gh:bioio-devs/cookiecutter-bioio-reader`

Once the project is generated, move to the newly created project directory
and follow the instructions in `SETUP.md`.

### Notes

1. Requires `setuptools>=64.0` to install library locally in editable mode
    * Most environment managers pull in the latest `setuptools` automatically when
      creating a new environment anyway.
2. Must initialize the project as a `git` repository prior to installing locally.
    * This is due to the dynamic version management with `setuptools-scm`.
    * After running the cookiecutter, you should push code to a remote host
      (GitHub, GitLab, etc.) or at the very least, run `git init` prior to install.

## Features

-   Uses `pytest` for local testing, simply run `just build` from a terminal.
-   Runs tests on Windows, Mac, and Ubuntu on every commit to `main` and
    every commit to branches with an open `pull request` to `main` using
    GitHub Actions.
-   Releases your Python Package to PyPI when you push to `main` after pushing a new
    git tag with `just tag-for-release` and `just release`.
-   Automatically builds documentation using Sphinx on every push to `main` and deploys
    to GitHub Pages.
-   Includes very minimal example code to get started.

List of available [just](https://github.com/casey/just) commands:
```bash
just
```
```
Available recipes:
    build                    # run lint and then run tests
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    install                  # install with all deps
    lint                     # lint, format, and check all files
    release                  # release a new version
    tag-for-release version  # tag a new version
    test                     # run tests
    update-from-cookiecutter # update this repo using latest cookiecutter-bioio-reader
```