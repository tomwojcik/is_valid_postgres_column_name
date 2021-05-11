import pytest

from is_valid_postgres_column_name import (
    is_reserved_postgres_keyword,
    is_valid_postgres_column_name,
)
from is_valid_postgres_column_name.constants import (
    SUPPORTED_POSTGRESQL_VERSIONS,
)
from is_valid_postgres_column_name.main import _get_keywords, pattern_matches


@pytest.fixture(autouse=True)
def clear_lru_cache():
    _get_keywords.cache_clear()
    yield
    _get_keywords.cache_clear()


@pytest.mark.parametrize(
    "column_name, is_valid",
    [
        # reserved
        ("do", False),
        ("DO", False),
        # length
        ("", False),
        ("a" * 62, True),
        ("a" * 63, False),
    ],
)
def test_is_valid_column_name(column_name, is_valid):
    assert is_valid_postgres_column_name(column_name) is is_valid


@pytest.mark.parametrize(
    "column_name, is_valid",
    [("asd", True), ("$asd", False), ("*asd", False), ("1asd", False)],
)
def test_pattern_passes(column_name, is_valid):
    assert pattern_matches(column_name) is is_valid
    assert is_valid_postgres_column_name(column_name) is is_valid


@pytest.mark.parametrize(
    "column_name, is_reserved",
    [("do", True), ("DO", True), ("kitty", False), ("TheBeatles", False)],
)
def test_is_reserved_keyword(column_name, is_reserved):
    assert is_reserved_postgres_keyword(column_name) is is_reserved


@pytest.mark.parametrize("version", [1, 2, 3, 4, 5])
def test_invalid_postgres_version_in_main_func(version):
    with pytest.raises(ValueError):
        is_valid_postgres_column_name(column_name="anything", version=version)


@pytest.mark.parametrize("version", [1, 2, 3, 4, 5])
def test_invalid_postgres_version_is_reserved_func(version):
    with pytest.raises(ValueError):
        _get_keywords(version)


def test_keywords_cache():
    min_version = min(SUPPORTED_POSTGRESQL_VERSIONS)
    max_version = max(SUPPORTED_POSTGRESQL_VERSIONS)

    _get_keywords(v=min_version)
    assert _get_keywords.cache_info().hits == 0
    assert _get_keywords.cache_info().misses == 1

    _get_keywords(v=min_version)
    assert _get_keywords.cache_info().hits == 1
    assert _get_keywords.cache_info().misses == 1

    _get_keywords(v=max_version)
    assert _get_keywords.cache_info().hits == 1
    assert _get_keywords.cache_info().misses == 2

    _get_keywords(v=max_version)
    assert _get_keywords.cache_info().hits == 2
    assert _get_keywords.cache_info().misses == 2
