### Hexlet tests and linter status:
[![Actions Status](https://github.com/KAnanev/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/KAnanev/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c670260520a7f208a8fb/maintainability)](https://codeclimate.com/github/KAnanev/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c670260520a7f208a8fb/test_coverage)](https://codeclimate.com/github/KAnanev/python-project-lvl2/test_coverage)
[![Python application](https://github.com/KAnanev/python-project-lvl2/actions/workflows/python-app.yml/badge.svg)](https://github.com/KAnanev/python-project-lvl2/actions/workflows/python-app.yml)

Description:

Difference calculator - a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com/. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility features:

- Support for different input formats: yaml, json
- Report generation in the form of plain text, stylish and json

Usage example:
```python
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```


How to install:
- clone repository
- [install poetry](https://python-poetry.org/docs/#installation)
- use `make test`
- use `make build`
- ` pip install dist/hexlet-code-0.1.0.tar.gz`

How to use:
- `gendiff -f[optional] <file_path> <file_path>`
- for more `gendiff -h or --help`

Use an application to find out the difference in two flat json files, format = string:
[![asciicast](https://asciinema.org/a/VuezFHLKBTmlFxF00Ycnp9FXd.svg)](https://asciinema.org/a/VuezFHLKBTmlFxF00Ycnp9FXd)

Use an application to find out the difference in two nested json files, format = string:
[![asciicast](https://asciinema.org/a/gZck67D38JYkqUg7q4OTLlTK0.svg)](https://asciinema.org/a/gZck67D38JYkqUg7q4OTLlTK0)

Use an application to find out the difference in two nested json files, format = plain:
[![asciicast](https://asciinema.org/a/QT9ncyyKEi0LcncpCfv69X74Y.svg)](https://asciinema.org/a/QT9ncyyKEi0LcncpCfv69X74Y)

Use an application to find out the difference in two nested json files, format = json:
[![asciicast](https://asciinema.org/a/IODph4mMBfiiTA9MsUfpSbWX6.svg)](https://asciinema.org/a/IODph4mMBfiiTA9MsUfpSbWX6)