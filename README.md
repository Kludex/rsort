<h1 align="center">
    <strong>rsort</strong>
</h1>
<p align="center">
    <a href="https://github.com/Kludex/rsort" target="_blank">
        <img src="https://img.shields.io/github/last-commit/Kludex/rsort" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/Kludex/rsort/Test">
        <img src="https://img.shields.io/codecov/c/github/Kludex/rsort">
    <br />
    <a href="https://pypi.org/project/rsort" target="_blank">
        <img src="https://img.shields.io/pypi/v/rsort" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/rsort">
    <img src="https://img.shields.io/github/license/Kludex/rsort">
</p>

Sort Python requirements with ease! :tada:

Currently supporting `requirements.txt` and `pyproject.toml` for poetry only.

## Installation

``` bash
pip install rsort
```

## Usage

``` bash
❯ rsort --help
Usage: rsort [OPTIONS] COMMAND [ARGS]...

  Sort requirements with ease!

Options:
  --files TEXT  Requirements file to be sorted.
  --check       Only check if needs to be sorted.  [default: False]
  --diff        Only changes to be made.  [default: False]
  --version     Show rsort version.
  --help        Show this message and exit.
```

# TODO

- [ ] Add tests

## License

This project is licensed under the terms of the MIT license.
