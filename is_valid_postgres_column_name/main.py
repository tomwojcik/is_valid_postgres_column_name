import os

from typing import Pattern, Set

import functools

__all__ = ["is_valid_postgres_column_name", "is_reserved_postgres_keyword"]

from is_valid_postgres_column_name.constants import (
    DEFAULT_PATTERN,
    SUPPORTED_POSTGRESQL_VERSIONS,
)


@functools.lru_cache(maxsize=3)
def _get_keywords(v: float) -> Set[str]:
    if v not in SUPPORTED_POSTGRESQL_VERSIONS:
        raise ValueError("Unsupported PostgreSQL version")

    this_dir, _ = os.path.split(os.path.abspath(__file__))
    with open(
        os.path.join(this_dir, "reserved_keywords", f"{v}.txt"), "r"
    ) as f:
        lst = f.read().splitlines()
    return set(lst)


def is_reserved_postgres_keyword(
    s: str, version: float = max(SUPPORTED_POSTGRESQL_VERSIONS)
) -> bool:
    keywords = _get_keywords(v=version)
    return s.upper() in keywords


def pattern_matches(s: str, pattern: Pattern = DEFAULT_PATTERN) -> bool:
    """https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-
    SYNTAX-IDENTIFIERS."""
    return bool(pattern.match(s))


def is_valid_postgres_column_name(
    column_name: str,
    version: float = max(SUPPORTED_POSTGRESQL_VERSIONS),
    pattern: Pattern = DEFAULT_PATTERN,
) -> bool:
    if is_reserved_postgres_keyword(column_name, version):
        return False
    elif not 0 < len(column_name) < 63:
        return False
    elif not pattern_matches(column_name, pattern):
        return False
    return True
