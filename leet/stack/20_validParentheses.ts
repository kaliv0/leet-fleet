// 20. Valid Parentheses
function isValid(s: string): boolean {
    if (!s || s.length % 2 !== 0) {
        return false;
    }

    const parenMap = {
        "{": "}",
        "[": "]",
        "(": ")",
    };

    const stack = [];
    for (const ch of s) {
        if (ch in parenMap) {
            stack.push(ch);
            continue;
        }

        if (!stack || parenMap[stack.pop()] !== ch) {
            return false;
        }
    }

    return stack.length === 0;
}

const isValidCases = [
    { s: "()", result: true },
    { s: "()[]{}", result: true },
    { s: "(]", result: false },
    { s: "([])", result: true },
    { s: "([)]", result: false },
    { s: "((", result: false },
    { s: "[", result: false },
    { s: "", result: false },
];

isValidCases.forEach(({ s, result }) => {
    const actual = isValid(s);
    console.assert(actual === result, `${actual} !== ${result}`);
});
