#!/usr/bin/env bash
set -uo pipefail

failed=0

fail() {
    echo "FAIL $1"
    echo "$2"
    failed=1
}

while IFS= read -r -d '' f; do
    # Skip files marked with @skip: in the first 5 lines
    if head -n 5 "$f" | grep -qE '^(#|//)\s*@skip:'; then
        continue
    fi

    case "$f" in
        *.py)
            grep -q '__main__' "$f" || continue
            out=$(PYTHONPATH=. python3 "$f" 2>&1) || fail "$f" "$out" ;;
        *.ts)
            out=$(node "$f" 2>&1)
            if [ $? -ne 0 ] || grep -q 'Assertion failed' <<< "$out"; then
                fail "$f" "$out"
            fi ;;
    esac
done < <(find leet \( -name '*.py' -o -name '*.ts' \) -print0)

if [ "$failed" -ne 0 ]; then
    exit 1
fi

echo "All tests passed"
