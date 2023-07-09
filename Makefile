.DEFAULT_GOAL := help
MAKEFLAGS 	  += --silent --no-print-directory


# Main
##############################################################################

.PHONY: start
init: create-venv
	@echo "\\033[0;32mNow you can activate venv with:\n"
	@echo "\\033[0;33m    1. source ./.venv/bin/activate\n"
	@echo "\\033[0;32mAnd install requirements:\n"
	@echo "\\033[0;33m    2. make install-requirements\n"
	@echo "\\033[0;32mAnd run this project with:\n"
	@echo "\\033[0;33m    3. make run\n\\033[0m"

.PHONY: install-requirements
install-requirements:
	pip install -r requirements.txt

.PHONY: create-venv
create-venv:
	@if [ ! -d ".venv/" ]; then \
		virtualenv .venv --prompt Python-TicTacToe 1>/dev/null; \
		echo "\\033[0;32mVirtual env created!\\033[0m"; \
	else \
		echo "\\033[0;33mVirtual env already created!\\033[0m"; \
	fi

.PHONY: venv
venv: create-venv

.PHONY: run
run:
	python run.py


# Lint
##############################################################################

.PHONY: lint lints check
lint:
	@echo lint with ruff

# Alias
lints: lint
check: lint


# Clean cache
##############################################################################

.PHONY: clean
clean:
	@echo rm .mypy-cache and ...


# Other
##############################################################################

.PHONY: help
help:
	@echo help block

info-%:
	@make --dry-run --always-make $* | grep -v "info"

print-%:
	@$(info '$*'='$($*)')


.SILENT:

