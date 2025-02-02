# Todo List

[![Build Icon]][Build Status]&emsp;[![LICENSE Icon]][LICENSE]

[Build Icon]: https://img.shields.io/github/actions/workflow/status/1git2clone/python-todo-list/pyright.yml?branch=main
[Build Status]: https://github.com/1git2clone/currency-conversion/actions?query=branch%3Amain
[LICENSE Icon]: https://img.shields.io/badge/license-Unlicense-blue.svg
[LICENSE]: LICENSE

A todo list terminal app written in Python which interacts with a PostgreSQL database.

## Table of contents

- [Todo List](#todo-list)
  - [Setting up](#setting-up)
    - [PostgreSQL](#postgresql)
    - [Environment files](#environment-files)
    - [Python and libraries](#python-and-libraries)
      - [Virtual environment](#virtual-environment)
        - [Linux](#linux)
        - [Windows](#windows)
      - [Tooling](#tooling)

## Setting up

### PostgreSQL

Download PostgreSQL with your package manager/installer of choice or build it
from source. You can find additional download instructions on the PostgreSQL
website:

- <https://www.postgresql.org/download/>

### Environment files

After that you need to make a `.env` file in the [root](./) of this project.

> [!NOTE]
> Refer to the [.env-example](./.env-example) file for an example of how the
> `.env` file should look like.

### Python and libraries

If you don't have Python installed, install it from here:

- <https://www.python.org/downloads/>

Additionally, this project uses a [`pyproject.toml`](./pyproject.toml) file and
pip doesn't have support for reading project dependencies from it so you'd
either need a tool like [`poetry`](https://python-poetry.org/) or
[`uv`](https://github.com/astral-sh/uv). This project uses `uv` so make sure to
install it from [here](https://github.com/astral-sh/uv/releases) if you want to
follow along.

> [!NOTE]
> It's not impossible to also use `pip`, you'd just need a `requirements.txt`
> file. This project doesn't have it as it'd duplicate a part of the logic for
> the [`pyproject.toml`](./pyproject.toml) file.

#### Virtual environment

After installing `uv` you need to type out the following commands:

##### Linux

```sh
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

##### Windows

```powershell
uv venv
.venv\Scripts\Activate.ps1
uv pip install -r pyproject.toml
```

#### Tooling

This is more of an editor environment thing, but my recommended extensions to
use to write better to reason with Python code (links are for VS Code, but they
work on most editors) are:

- [Pyright](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)
  (Static type analyzer)

- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
  (Formatter)
