[![Test Suite](https://github.com/tomwojcik/is_valid_postgres_column/actions/workflows/test-suite.yml/badge.svg)](https://github.com/tomwojcik/is_valid_postgres_column/actions/workflows/test-suite.yml)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![PyPI version](https://badge.fury.io/py/is-valid-postgres-column-name.svg)](https://badge.fury.io/py/is-valid-postgres-column-name)


I found it weird there's no simple way to check if a given string can be a PostgreSQL column name.
Although, to my understanding, you can escape with quotation marks some names that are otherwise invalid,
I don't think escaping such a thing is a good idea.

This validation is required if your column name can be dynamically generated.

# How to use

```python
>>> from is_valid_postgres_column_name import is_valid_postgres_column_name
>>> is_valid_postgres_column_name("column_A")
True
>>> is_valid_postgres_column_name("1column_A")
False
```

All PostgreSQL versions are supported. The only difference between versions, to my knowledge, are reserved keywords.
```python
>>> is_valid_postgres_column_name("window", version=13)
False
>>> is_valid_postgres_column_name("window", version=7.1)
True
```

# Installation

```shell
$ pip install -U is_valid_postgres_column_name
```

# Requirements

Python 3.0+

# Dependencies

None.

# Contribution

Welcome.

# Alternatives

If you don't want to download additional library for such a simple thing, have a look at `sqlparse` [`keywords.py`](https://github.com/andialbrecht/sqlparse/blob/23d29933ddc4272b495d36e0e32d3eaf0c3ef76d/sqlparse/keywords.py) file.
