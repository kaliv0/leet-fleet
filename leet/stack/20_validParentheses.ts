// 20. Valid Parentheses
function isValid(s: string): boolean {
    if (!s || s.length % 2 !== 0) {
        return false
    }

    const parenMap = {
        "{" : "}",
        "[" : "]",
        "(": ")"
    }

    const stack = []
    for (const ch of s){
        if (ch in parenMap){
            stack.push(ch);
            continue
        }

        if (!stack || parenMap[stack.pop()] !== ch) {
            return false
        }
    }

    return stack.length === 0;
}

const cases: [string, boolean][] =[
    ["()", true],
    ["()[]{}", true],
    ["(]", false],
    ["([])", true],
    ["([)]", false],
    ["((", false],
    ["[", false],
    ["", false]
]

for (const [s, res] of cases){
    console.assert(isValid(s) === res);
}

