# {{ cookiecutter.project_slug }}

[![Build Status](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/actions)
[![Documentation](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/actions/workflows/docs.yml/badge.svg)](https://{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

This plugin is intended to be used in conjunction with [bioio](https://github.com/bioio-devs/bioio)
---

## Installation

**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}.git`

## Quickstart

```python
from {{ cookiecutter.python_slug }} import Reader 

r = Reader("my-image.ext")
r.dims
```

## Documentation

For full package documentation please visit [{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }}](https://{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }}).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**{{ cookiecutter.license }}**
