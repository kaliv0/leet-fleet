// 119. Pascal's Triangle II

function getRow(rowIndex: number): number[] {
    let currRow = [1];
    for (let i = 1; i <= rowIndex; i++) {
        let nextRow = [1];
        for (let j = 1; j < i; j++) {
            nextRow.push(currRow[j - 1] + currRow[j]);
        }
        nextRow.push(1);
        currRow = nextRow;
    }
    return currRow;
}

const getRowCases = [
    { rowIndex: 3, result: [1, 3, 3, 1] },
    { rowIndex: 0, result: [1] },
    { rowIndex: 1, result: [1, 1] },
];

getRowCases.forEach(({ rowIndex, result }) => {
    const actual = getRow(rowIndex);
    console.assert(
        JSON.stringify(actual) === JSON.stringify(result),
        `${JSON.stringify(actual)} !== ${JSON.stringify(result)}`,
    );
});
