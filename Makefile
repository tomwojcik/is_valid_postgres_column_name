.PHONY: run_hooks test docs minor

run_hooks:
	pre-commit run --all-files --show-diff-on-failure

gen_files:
	python gen_keywords_files.py

deps:
	pip-compile

test:
	pytest --cov=is_valid_postgres_column_name --cov-report term-missing tests.py --verbose

docs:
	cd docs && make html

minor:
	bump2version patch
