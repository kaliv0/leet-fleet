SHELL := /bin/bash

.PHONY: lint test all

lint:
	ruff format leet
	npx prettier --write "leet/**/*.{ts,js,json,md}"

test:
	@bash ./scripts/test.sh

all: lint test
