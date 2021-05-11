import re

SUPPORTED_POSTGRESQL_VERSIONS = [
    7.1,
    7.2,
    7.3,
    7.4,
    8.0,
    8.1,
    8.2,
    8.3,
    8.4,
    9.0,
    9.1,
    9.2,
    9.3,
    9.4,
    9.5,
    9.6,
    10,
    11,
    12,
    13,
]

DEFAULT_PATTERN = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
