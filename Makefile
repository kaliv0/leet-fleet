SHELL := /bin/bash

.PHONY: lint test all

lint:
	ruff format leet
	npx prettier --write "leet/**/*.{ts,js,json,md}"

test:
	@failed=0; \
	while IFS= read -r -d '' f; do \
		if head -n 5 "$$f" | grep -qE '^#\s*@skip:'; then continue; fi; \
		if ! grep -q '__main__' "$$f"; then continue; fi; \
		if ! PYTHONPATH=. python3 "$$f" >/dev/null 2>&1; then \
			echo "FAIL $$f"; \
			failed=1; \
		fi; \
	done < <(find leet -name '*.py' -print0); \
	while IFS= read -r -d '' f; do \
		if head -n 5 "$$f" | grep -qE '^//\s*@skip:'; then continue; fi; \
		out=$$(node "$$f" 2>&1); \
		status=$$?; \
		if [ $$status -ne 0 ] || echo "$$out" | grep -q 'Assertion failed'; then \
			echo "FAIL $$f"; \
			echo "$$out" | grep 'Assertion failed' || true; \
			failed=1; \
		fi; \
	done < <(find leet -name '*.ts' -print0); \
	if [ $$failed -ne 0 ]; then exit 1; fi; \
	echo "All tests passed"

all: lint test
