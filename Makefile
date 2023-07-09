path := .

.DEFAULT_GOAL := help
MAKEFLAGS 	  += --silent --no-print-directory

RED 	:= \\033[0;31m
GREEN 	:= \\033[1;32m
YELLOW 	:= \\033[1;33m
BLUE 	:= \\033[0;36m
RESET 	:= \\033[0m


# Main
##############################################################################


.PHONY: init
init: create-venv  ## Initialises the project (creates a virtual environment) and gives further instructions
	@echo "$(GREEN)Now you can activate venv with:"
	@echo
	@echo "$(BLUE)    1. source ./.venv/bin/activate"
	@echo
	@echo "$(GREEN)And install requirements:"
	@echo
	@echo "$(BLUE)    2. make install-requirements"
	@echo
	@echo "$(GREEN)And run this project with:"
	@echo
	@echo "$(BLUE)    3. make run$(RESET)"
	@echo


.PHONY: install-requirements
install-requirements:  ## Install all requirements from 'requirements.txt'
	@echo
	@echo "$(GREEN)Applying requirements.txt..."
	@echo "============================$(RESET)"
	@echo
	pip install -r requirements.txt
	@echo


.PHONY: run
run:  ## Launch app (run.py)
	python run.py


.PHONY: create-venv venv env
create-venv:  ## Create virtual enviroment for Python
	@if [ ! -d ".venv/" ]; then \
		virtualenv .venv --prompt Python-TicTacToe 1>/dev/null; \
		echo "$(GREEN)    Virtual env created!$(RESET)\n"; \
	fi


# Alias
venv: create-venv  ## Alias for 'create-venv'
env: create-venv  ## Alias for 'create-venv'


# Lint
##############################################################################


.PHONY: lint-check lint lints check
lint-check: ruff mypy pyright black  ## Complete code base check with linters and formatters


# Alias
lint: lint-check  ## Alias for 'lint-check'
lints: lint-check  ## Alias for 'lint-check'
check: lint-check  ## Alias for 'lint-check'


.PHONY: ruff
ruff:  # Use 'ruff' utilite as linter
	@echo
	@echo "$(BLUE)Applying ruff..."
	@echo "$(GREEN)================$(RESET)"
	@echo
	ruff check $(path) --fix
	@echo

.PHONY: mypy
mypy:  # Use 'mypy' utilite as linter
	@echo
	@echo "$(BLUE)Applying mypy..."
	@echo "$(GREEN)================$(RESET)"
	@echo
	mypy $(path)
	@echo

.PHONY: pyright
pyright:  ## Use 'black' utilite as linter
	@echo
	@echo "$(BLUE)Applying pyright..."
	@echo "$(GREEN)===================$(RESET)"
	@echo
	pyright $(path)
	@echo

.PHONY: black
black:  ## Use 'black' utilite as formatter
	@echo
	@echo "$(BLUE)Applying black..."
	@echo "$(GREEN)=================$(RESET)"
	@echo
	black $(path)
	@echo


# Clean cache
##############################################################################


.PHONY: clean
clean:  ## Clear linter cache (.mypy_cache .ruff_cache)
	@echo "$(RED)Remove:$(RESET) .mypy_cache/"
	@echo "$(RED)Remove:$(RESET) .ruff_cache/"
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache


# Other
##############################################################################


.PHONY: help
help:  ## Show this output, i.e. help to use the commands
	grep -E '^[a-zA-Z_-]+:.*?# .*$$' Makefile | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


info-%:
	@make --dry-run --always-make $* | grep -v "info"


print-%:
	@$(info '$*'='$($*)')


.SILENT:

