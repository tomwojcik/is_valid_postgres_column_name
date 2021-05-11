import os

import logging
import time

import pandas as pd

from is_valid_postgres_column_name.constants import (
    SUPPORTED_POSTGRESQL_VERSIONS,
)

logger = logging.getLogger(__name__)


def _gen_file_from_url(version: float) -> None:
    assert version in SUPPORTED_POSTGRESQL_VERSIONS
    url = (
        f"https://www.postgresql.org/docs/{version}/sql-keywords-appendix.html"
    )
    logger.info(f"Fetching table for url {url}")
    df = pd.read_html(url)[1]
    df = df.iloc[:, :2]
    keyword, psql = df.columns
    reserved_keywords_df = df[df.loc[:, psql] == "reserved"]
    lst = sorted(map(str, set(reserved_keywords_df[keyword].tolist())))

    path = os.path.join(
        "is_valid_postgres_column_name", "reserved_keywords", f"{version}.txt"
    )
    with open(path, "w") as f:
        for row in lst:
            f.write(f"{str(row).upper().strip()}\n")
    logger.info("Fetched")


def gen_keywords_files() -> None:
    for version in SUPPORTED_POSTGRESQL_VERSIONS:
        _gen_file_from_url(version)
        time.sleep(1)


if __name__ == "__main__":
    gen_keywords_files()
