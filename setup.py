from distutils.core import setup
from is_valid_postgres_column_name import __version__, __author__
import setuptools


def get_long_description():
    with open("README.md", "r", encoding="utf8") as f:
        return f.read()


setup(
    name="is_valid_postgres_column_name",
    python_requires=">=3.0",
    version=__version__,
    license="MIT",
    description="Allows you to check if a given "
    "string can be PostgreSQL column name",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        include=(
            "is_valid_postgres_column_name",
            "is_valid_postgres_column_name.*",
        )
    ),
    package_data={
        "is_valid_postgres_column_name": [
            "py.typed",
            "reserved_keywords/*.txt",
        ],
    },
    platforms="any",
    author=__author__,
    url="https://github.com/tomwojcik/is_valid_postgres_column",
    download_url="https://github.com/tomwojcik/is_valid_postgres_column/"
    f"archive/{__version__}.tar.gz",
    keywords=["psycopg2", "psycopg3", "postgres", "postgresql"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
